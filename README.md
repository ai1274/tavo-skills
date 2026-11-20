# Tavo Skills

面向 Tavo 内容创作者和工程维护者的八个 Agent Skills。包含技术参考、Python／Node.js 工具、模板、schema 和合成测试数据。

## 安装

下载 Release ZIP 并解压。把其中 `skills/` 下的八个同级目录复制到客户端的用户级技能目录，保留同级布局。目录中已有同名技能时，先比较再替换。

| 客户端 | 默认用户技能目录 |
| --- | --- |
| Codex | `~/.agents/skills/` |
| Claude Code | `~/.claude/skills/` |

在 Codex 选择 `$tavo`，或在 Claude Code 运行 `/tavo`。按任务读取相应分支。

## 技能

- [tavo](skills/tavo/SKILL.md) — 统一入口与任务路由
- [tavo-skill](skills/tavo-skill/SKILL.md) — 平台能力、技术文档和内容编写
- [tavo-1-0-beta-skill](skills/tavo-1-0-beta-skill/SKILL.md) — MCP 发现、版本证据和验证脚本
- [tavo-studio](skills/tavo-studio/SKILL.md) — TPG、TavoJS、主题、WebView、PNG 工具
- [tavo-character-card](skills/tavo-character-card/SKILL.md) — 角色卡、世界书和正则套件
- [tavo-mainline-minimal-development](skills/tavo-mainline-minimal-development/SKILL.md) — 维护位置与最小改动计划
- [tavo-memory-steward-clean-workflow](skills/tavo-memory-steward-clean-workflow/SKILL.md) — 项目架构、职责与验收
- [tavo-project-tooling](skills/tavo-project-tooling/SKILL.md) — 路由、注册、索引和发布工具

## 离线验证

在仓库根目录运行下列命令。工具使用 Python 3.11+ 和 Node.js 20+，设备测试另需配置 Android ADB 及经授权的 Tavo MCP。查看工具的 `--help` 及相应技能文档获取输入说明。

```text
python -B skills/tavo-1-0-beta-skill/scripts/test_validate_tpg_package.py
python -B skills/tavo-1-0-beta-skill/scripts/test_dump_mcp_surface.py
python -B skills/tavo-skill/scripts/test_search_official_docs.py
node --check skills/tavo-studio/scripts/png-card-lib.mjs
```

公开技术链接、离线语料获取与 MCP 证据说明见[技术文档与证据](skills/tavo-skill/references/public-release-sources.md)；授权条款见 [MIT 许可证](LICENSE)。
