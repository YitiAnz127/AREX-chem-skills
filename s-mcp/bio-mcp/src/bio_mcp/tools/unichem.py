"""UniChem 化合物标识符映射工具。

UniChem是EBI的化学结构标识符映射服务，连接多个化学数据库。
工具：
  - unichem_mapping: 按 InChIKey 查询化合物跨数据库标识符映射
  - unichem_structure: 按 InChIKey 查询化合物跨库引用详情
"""
from __future__ import annotations

from typing import Any

from bio_mcp.core.unichem import UniChemClient

_client: UniChemClient | None = None


def _get_client() -> UniChemClient:
    global _client
    if _client is None:
        _client = UniChemClient()
    return _client


def register(server: Any) -> None:
    @server.tool(
        name="unichem_mapping",
        description=(
            "Query compound identifier mapping across databases by InChIKey. "
            "按 InChI Key 查询化合物在多个数据库（ChEMBL/PubChem/DrugBank/ChEBI 等）"
            "中的标识符映射：输入标准化化学标识符 InChI Key，返回该化合物在"
            "各化学数据库中的对应 ID，用于跨数据库化合物查询与整合。"
        ),
    )
    def unichem_mapping_tool(
        inchikey: str
    ) -> str:
        """查询化合物跨库标识符映射。

        Args:
            inchikey: InChI Key（标准化化学标识符）
        """
        client = _get_client()
        result = client.lookup_inchikey(inchikey)
        return _format_mapping_result(result)

    @server.tool(
        name="unichem_structure",
        description=(
            "Look up compound cross-references by InChI Key via UniChem. "
            "按 InChI Key 查询化合物的跨库引用详情：返回该化合物在 UniChem "
            "登记的化学数据库及对应标识符（来源/ID 列表），用于结构与标识符验证。"
        ),
    )
    def unichem_structure_tool(
        inchikey: str
    ) -> str:
        """查询化合物跨库引用详情。

        Args:
            inchikey: InChI Key（标准化化学标识符）
        """
        client = _get_client()
        result = client.lookup_inchikey(inchikey)
        return _format_structure_result(result)


def _format_mapping_result(result: dict) -> str:
    """格式化映射查询结果。"""
    if "error" in result:
        return f"UniChem 映射查询未找到/错误: {result['error']}"

    inchikey = result.get("inchikey", "")
    mappings = result.get("mappings", [])

    if not mappings:
        return f"未找到 InChIKey「{inchikey}」的跨库映射信息。"

    lines = [
        f"# UniChem 标识符映射",
        f"",
        f"- **InChI Key**: {inchikey}",
        f"- **映射数量 / Mappings**: {len(mappings)}",
        f"",
    ]

    # src_id 与来源名称的常见对应（UniChem source 编号）
    src_names = {
        "1": "ChEMBL", "2": "DrugBank", "3": "PDB", "4": "PubChem",
        "5": "KEGG", "6": "ChemSpider", "7": "ChEBI", "8": "BindingDB",
        "9": "DrugCentral", "10": "SureChEMBL", "11": "GSRS",
        "15": "CompoundID", "17": "Nikkaji", "20": "FoodB",
        "22": "LIPID MAPS", "23": "MolPort",
    }

    for m in mappings[:20]:
        src = str(m.get("src_id", "?"))
        name = src_names.get(src, f"source-{src}")
        cid = m.get("src_compound_id", "N/A")
        lines.append(f"- **{name}** (src {src}): `{cid}`")

    if len(mappings) > 20:
        lines.append(f"- ...（共 {len(mappings)} 条映射）")

    lines.append("")
    lines.append("来源：UniChem（EBI 化学结构映射服务）。")
    return "\n".join(lines)


def _format_structure_result(result: dict) -> str:
    """格式化结构/跨库引用查询结果。"""
    if "error" in result:
        return f"UniChem 查询未找到/错误: {result['error']}"

    inchikey = result.get("inchikey", "")
    mappings = result.get("mappings", [])

    if not mappings:
        return f"未找到 InChIKey「{inchikey}」的跨库引用信息。"

    lines = [
        f"# UniChem 化合物跨库引用",
        f"",
        f"- **InChI Key**: {inchikey}",
        f"- **引用数据库数 / Databases**: {len(mappings)}",
        f"",
    ]

    for m in mappings[:20]:
        lines.append(
            f"- src_id={m.get('src_id', '?')} → `{m.get('src_compound_id', 'N/A')}`"
        )

    if len(mappings) > 20:
        lines.append(f"- ...（共 {len(mappings)} 条引用）")

    lines.append("")
    lines.append("来源：UniChem（EBI 化学结构映射服务）。")
    return "\n".join(lines)
