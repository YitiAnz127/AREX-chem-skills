---
name: bio-release
description: Release checklist for BioMCP — version bump, honest doc sync, offline tests, clean commit, push, GitHub release. Use before every release to keep numbers consistent and authorship clean.
---

# BioMCP Release Checklist / 发布清单

Use this checklist before tagging any release. 每次发布前按此清单执行。

## Prerequisites 前置检查

1. **Run the offline unit tests** 运行离线单元测试:
   ```bash
   python3 -m pytest tests/ -q
   ```
   All tests must pass. 全部必须通过。The tool-count test (`test_create_server_registers_all_tools`) enforces the exact expected set — update `EXPECTED_TOOLS` when tools change.

2. **Verify actual tool / database counts** 核实真实工具/数据库数量:
   ```bash
   python3 -c "import sys; sys.path.insert(0,'src'); import asyncio; from bio_mcp.server import create_server; print(len(asyncio.run(create_server().list_tools())))"
   ls src/bio_mcp/core/*.py | grep -v __ | grep -vE 'http|cache' | wc -l
   ```
   The numbers must match what README, pyproject.toml, and server.py DESCRIPTION claim. 数字必须与 README / pyproject.toml / server.py 一致。

## Steps 步骤

3. **Bump version** 升版本: edit `src/bio_mcp/__init__.py` and `pyproject.toml`.
4. **Sync docs honestly** 诚实同步文档:
   - README badges, feature counts, tool tables, architecture diagram, project structure.
   - CHANGELOG new entry with correct counts.
   - Verification status: mark new tools as best-effort unless individually e2e validated. 新工具除非逐一端到端验证过，否则标记为 best-effort。
5. **Check for leaks** 检查泄露:
   ```bash
   grep -rn --exclude-dir=.git -E '~$|/root|token|password|api[_-]?key' src/ README.md pyproject.toml
   ```
   No local paths, no tokens, no credentials in the repo. 仓库中不得出现本地路径/凭证。
6. **Commit with clean authorship** 提交（作者必须干净）:
   ```bash
   git add -A
   git commit -m "release vX.Y.Z: <summary>"
   ```
   Ensure `git config user.name` / `user.email` are set to the account owner (`qgeng1465 <qgeng1465@users.noreply.github.com>`). Never add Co-Authored-By or AI tool names. 提交作者只能是项目账号，不得出现任何 AI 工具名。
7. **Push** 推送 (use proxy when needed 需要时代理):
   ```bash
   git push origin main
   ```
   If network needs a proxy: `git -c http.proxy=http://127.0.0.1:7890 push origin main`.
8. **Create GitHub release** 创建 release:
   ```bash
   gh release create vX.Y.Z --title "vX.Y.Z" --notes "$(sed -n '1,80p' CHANGELOG.md | head -40)"
   ```
   Attach a source tarball if desired. 可选附带源码包。

## Honesty rules 诚实规则

- Never claim a tool is "end-to-end verified" unless it was actually tested against the real API during development. 未实际测试过的工具不得声称已端到端验证。
- Report reachability honestly via `db_health_check`; note that connectivity reflects the current network, not permanent availability. 连通性如实报告。
- The README's "honest note" section must reflect current verification status. README 的诚实声明必须反映当前验证状态。
