"""植物生物信息学查询工具。

通过 Ensembl REST API 查询植物基因数据（零配置、免密钥）。
支持常见模式植物物种：拟南芥、水稻、玉米、小麦、大豆等。
参考：https://rest.ensembl.org/documentation/info/lookup_symbol
"""
from __future__ import annotations

from bio_mcp.core.ensembl import EnsemblClient

_client: EnsemblClient | None = None

# 常见植物物种的 Ensembl 名称映射
PLANT_SPECIES = {
    "arabidopsis": "arabidopsis_thaliana",
    "拟南芥": "arabidopsis_thaliana",
    "rice": "oryza_sativa",
    "水稻": "oryza_sativa",
    "maize": "zea_mays",
    "玉米": "zea_mays",
    "wheat": "triticum_aestivum",
    "小麦": "triticum_aestivum",
    "soybean": "glycine_max",
    "大豆": "glycine_max",
    "tomato": "solanum_lycopersicum",
    "番茄": "solanum_lycopersicum",
    "grape": "vitis_vinifera",
    "葡萄": "vitis_vinifera",
    "barley": "hordeum_vulgare",
    "大麦": "hordeum_vulgare",
    "sorghum": "sorghum_bicolor",
    "高粱": "sorghum_bicolor",
    "potato": "solanum_tuberosum",
    "马铃薯": "solanum_tuberosum",
    "cotton": "gossypium_hirsutum",
    "棉花": "gossypium_hirsutum",
}


def _get_client() -> EnsemblClient:
    global _client
    if _client is None:
        _client = EnsemblClient()
    return _client


def _resolve_species(species: str) -> str:
    """将常见名称解析为 Ensembl 物种名。"""
    key = species.strip().lower()
    if key in PLANT_SPECIES:
        return PLANT_SPECIES[key]
    # 若已传入下划线形式（如 arabidopsis_thaliana）则直接使用
    if "_" in key:
        return key
    # 否则回退到拟南芥
    return "arabidopsis_thaliana"


def register(server):
    """注册植物工具到MCP服务器"""

    @server.tool("plant_gene_lookup", description="Look up plant gene information via Ensembl Plants. Input: gene symbol (e.g. AT1G01010, AGL1), plant species (e.g. arabidopsis/rice/maize/wheat/soybean). Output: gene ID, description, biotype, genomic location. 植物基因查询：通过 Ensembl Plants 查询植物基因信息（拟南芥/水稻/玉米/小麦/大豆等）。")
    def plant_gene_lookup_tool(symbol: str, species: str = "arabidopsis_thaliana") -> str:
        """Look up a plant gene by symbol."""
        client = _get_client()
        resolved = _resolve_species(species)
        try:
            gene = client.gene_by_symbol(symbol, resolved)
        except Exception as e:
            return f"植物基因查询失败: {str(e)}"
        if not gene.get("gene_id"):
            return (
                f"未找到 {symbol} 在 {resolved} 中的基因信息。\n"
                "请确认基因符号正确，或尝试其他物种（如 arabidopsis/rice/maize）。"
            )
        return f"""植物基因信息: {symbol} ({resolved})

- Ensembl基因ID: {gene.get('gene_id')}
- 基因符号: {gene.get('symbol')}
- 描述: {gene.get('description')}
- 生物型: {gene.get('biotype')}
- 位置: chr{gene.get('chr')}:{gene.get('start')}-{gene.get('end')} ({gene.get('strand')}链)
- 组装版本: {gene.get('assembly')}"""

    @server.tool("plant_species_list", description="List supported plant species for BioMCP plant gene lookup. Input: none. Output: common plant species names mapped to Ensembl species IDs. 列出支持的植物物种及其对应 Ensembl 物种名。")
    def plant_species_list_tool() -> str:
        """List supported plant species."""
        lines = []
        seen = set()
        for common, ensembl in PLANT_SPECIES.items():
            if ensembl in seen:
                continue
            seen.add(ensembl)
            lines.append(f"- {common}: {ensembl}")
        return "支持的植物物种 / Supported plant species:\n\n" + "\n".join(lines)