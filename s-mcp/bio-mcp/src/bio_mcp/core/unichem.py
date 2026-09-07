"""UniChem 客户端：化合物标识符映射服务。

UniChem是EBI的化学结构标识符映射服务，连接多个化学数据库。
API：https://www.ebi.ac.uk/unichem/rest/，免鉴权。
参考：https://chembl.gitbook.io/unichem/api

说明：UniChem 现行可靠的公开端点是按 InChIKey 查询，返回该化合物
在多个化学数据库（ChEMBL/PubChem/DrugBank/ChEBI 等）中的标识符映射。
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.http import BioHTTP

BASE = "https://www.ebi.ac.uk/unichem/rest"


class UniChemClient:
    def __init__(self) -> None:
        self._http = BioHTTP(base_url=BASE, timeout=30.0)

    def lookup_inchikey(self, inchikey: str) -> dict[str, Any]:
        """按 InChIKey 查询化合物在多个数据库中的标识符映射。

        inchikey：InChI Key（标准化化学标识符）
        返回示例：[{"src_id": "1", "src_compound_id": "CHEMBL25"}, ...]
        """
        try:
            resp = self._http.get(f"inchikey/{inchikey}")
            if resp.status_code != 200:
                return {
                    "inchikey": inchikey,
                    "mappings": [],
                    "status": resp.status_code,
                    "error": f"HTTP {resp.status_code}",
                }
            data = resp.json()
            # 正常返回 JSON 数组；未找到时返回 {"error": "..."} 字典
            if isinstance(data, dict):
                return {
                    "inchikey": inchikey,
                    "mappings": [],
                    "error": data.get("error", "未找到该 InChIKey"),
                }
            return {"inchikey": inchikey, "mappings": data, "status": 200}
        except Exception as e:
            return {"inchikey": inchikey, "mappings": [], "error": str(e)}

    def close(self) -> None:
        self._http.close()
