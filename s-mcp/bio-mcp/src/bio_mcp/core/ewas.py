"""EWAS Atlas 客户端：全基因组表观遗传关联研究知识库。

EWAS Atlas（国家基因组科学数据中心 NGDC, CNCB）收录全基因组 EWAS 研究，
提供 CpG 位点与性状/疾病/暴露的关联、相关基因与转录本、PMID 溯源，免鉴权。
API：REST https://ngdc.cncb.ac.cn/ewas/rest

能力：
  - probe_lookup：按 CpG 位点查询其关联（性状/研究/PMID）与相关基因
  - gene_lookup：按基因符号查询关联的 CpG 探针与关联列表
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.http import BioHTTP

BASE = "https://ngdc.cncb.ac.cn/ewas/rest"


class EWASClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=40.0)

    def probe_lookup(self, probe_id: str) -> dict[str, Any]:
        """按 CpG 位点查询其 EWAS 关联。"""
        try:
            resp = self._http.get("probe", params={"probeId": probe_id})
            return {"probe_id": probe_id, "data": resp.json()}
        except Exception as e:  # noqa: BLE001
            return {"probe_id": probe_id, "error": str(e)}

    def gene_lookup(self, gene_symbol: str) -> dict[str, Any]:
        """按基因符号查询关联的 CpG 探针与关联。"""
        try:
            resp = self._http.get("gene", params={"geneSymbol": gene_symbol})
            return {"gene_symbol": gene_symbol, "data": resp.json()}
        except Exception as e:  # noqa: BLE001
            return {"gene_symbol": gene_symbol, "error": str(e)}
