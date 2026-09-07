"""Expression Atlas 客户端：EBI基因表达数据库查询。

Expression Atlas是EBI的基因表达知识库，包含不同条件和组织中的基因表达数据。
API：https://www.ebi.ac.uk/gxa/json/，免鉴权。
参考：https://www.ebi.ac.uk/gxa/help.html

诚实说明：
- 公开 REST 目前只有实验级端点可用：
  - GET /json/experiments          实验列表
  - GET /json/experiments/{acc}    单个实验（含 profile 行）
  旧的单基因表达端点（json/baseline/expression/{gene} 等）已下线（404）。
  因此本客户端对"按基因"的查询采用客户端过滤实验列表的方式，
  返回与该基因相关的实验（供进一步查看表达），而非数值化的基因表达量。
"""
from __future__ import annotations

import time
from typing import Any

from bio_mcp.core.http import BioHTTP

BASE = "https://www.ebi.ac.uk/gxa"

# 实验列表缓存（公开列表约数千个实验，避免每次搜索都全量下载）
_CACHE: list[dict[str, Any]] | None = None
_CACHE_TIME = 0.0
_CACHE_TTL_SECONDS = 3600.0


def _reset_cache() -> None:
    """重置模块级缓存（测试用）。"""
    global _CACHE, _CACHE_TIME
    _CACHE = None
    _CACHE_TIME = 0.0


class ExpressionAtlasClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=30.0)

    def _experiment_list(self) -> list[dict[str, Any]]:
        """获取并缓存全部实验列表（公开端点 /json/experiments）。"""
        global _CACHE, _CACHE_TIME
        now = time.monotonic()
        if _CACHE is not None and (now - _CACHE_TIME) < _CACHE_TTL_SECONDS:
            return _CACHE
        resp = self._http.get("json/experiments")
        data = resp.json() if resp.status_code == 200 else {}
        experiments = data.get("experiments", []) if isinstance(data, dict) else []
        if isinstance(experiments, list):
            _CACHE = experiments
            _CACHE_TIME = now
            return experiments
        return []

    def _keyword_match(self, record: dict[str, Any], keyword: str) -> bool:
        """在实验记录里做大小写不敏感的关键词匹配。"""
        kw = keyword.lower()
        fields = [
            record.get("experimentDescription", ""),
            record.get("species", ""),
            record.get("experimentAccession", ""),
            record.get("experimentType", ""),
        ]
        return any(kw in str(f).lower() for f in fields)

    def experiment_search(self, term: str, limit: int = 10) -> dict[str, Any]:
        """按关键词搜索表达实验（客户端过滤全部实验列表）。

        term：搜索关键词（cancer、tissue等）
        """
        try:
            all_experiments = self._experiment_list()
            hits = [
                e for e in all_experiments
                if self._keyword_match(e, term)
            ]
            return {
                "search_term": term,
                "total_matches": len(hits),
                "experiments": hits[:limit],
                "status": 200,
            }
        except Exception as e:
            return {"search_term": term, "total_matches": 0, "experiments": [], "error": str(e)}

    def gene_expression(self, gene_id: str, species: str = "homo sapiens", limit: int = 10) -> dict[str, Any]:
        """按基因查找相关表达实验（诚实版）。

        gene_id：基因ID或符号（ENSG00000141510/TP53）
        species：物种（homo sapiens）

        注意：公开 REST 已不提供单基因数值化表达量端点；
        本方法返回在实验描述/物种中匹配到该基因的实验列表，
        供用户在 Expression Atlas 中进一步查看表达情况。
        """
        try:
            all_experiments = self._experiment_list()
            sp = species.lower()
            hits = [
                e for e in all_experiments
                if self._keyword_match(e, gene_id)
                and (sp in str(e.get("species", "")).lower() or sp in str(e.get("kingdom", "")).lower())
            ]
            return {
                "gene_id": gene_id,
                "species": species,
                "total_matches": len(hits),
                "experiments": hits[:limit],
                "status": 200,
                "note": "公开 REST 无单基因数值表达量端点；以下为匹配该基因的表达实验，表达值请打开实验查看。",
            }
        except Exception as e:
            return {"gene_id": gene_id, "species": species, "total_matches": 0, "experiments": [], "error": str(e)}

    def close(self) -> None:
        self._http.close()
