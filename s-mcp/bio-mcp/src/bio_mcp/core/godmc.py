"""GoDMC mQTL 客户端：全基因组 SNP×CpG 甲基化数量性状位点元分析。

GoDMC（Genetics of DNA Methylation Consortium, MRC IEU）对 28 个队列做了
SNP×CpG mQTL 元分析，提供遗传变异与 DNA 甲基化之间的关联，免鉴权。
API：REST http://api.godmc.org.uk/v0.1/
注意：端点使用 http（非 https），部分网络环境可能不可达。

能力：
  - assoc_by_rsid：按 rsID 查询该 SNP 的 mQTL 关联（→ CpG 位点）
  - assoc_by_cpg：按 CpG 位点查询其 mQTL 关联（→ SNP）
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.http import BioHTTP

BASE = "http://api.godmc.org.uk/v0.1"


class GoDMCClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=40.0)

    def assoc_by_rsid(self, rsid: str) -> dict[str, Any]:
        """按 rsID 查询该 SNP 的 mQTL 关联（返回关联的 CpG 位点）。"""
        try:
            resp = self._http.get(f"assoc_meta/rsid/{rsid}")
            return {"rsid": rsid, "data": resp.json()}
        except Exception as e:  # noqa: BLE001
            return {"rsid": rsid, "error": str(e)}

    def assoc_by_cpg(self, cpg: str) -> dict[str, Any]:
        """按 CpG 位点查询其 mQTL 关联（返回关联的 SNP）。"""
        try:
            resp = self._http.get(f"assoc_meta/cpg/{cpg}")
            return {"cpg": cpg, "data": resp.json()}
        except Exception as e:  # noqa: BLE001
            return {"cpg": cpg, "error": str(e)}
