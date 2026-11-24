# Tavo Skills

面向 Tavo 创作者与插件开发者的八个 Agent Skills。可以通过 `tavo` 查平台文档、制作角色卡与世界书、开发插件和主题，或连接 MCP 核对当前宿主支持的功能。Codex 还可以按交付物直接选择主线最小开发、项目架构与工作流或项目工具链。

技能安装在 Codex 或 Claude Code 中。需要验证插件在 Tavo 中的实际表现时，再使用目标 Tavo App。

## 快速开始

1. 克隆仓库，或在 GitHub 的 **Code → Download ZIP** 下载 `main` 并解压。
2. 将 `skills/` 下的八个子目录复制到客户端的技能目录，保持八个目录同级。已有同名目录时先比较本地改动。
3. 在客户端打开新会话。在已有项目中使用时，说明项目位置、交付物和目标 Tavo 版本。

| 客户端 | 用户级技能目录 | 调用方式 |
| --- | --- | --- |
| Codex | `~/.agents/skills/` | 直接描述任务，或输入 `$tavo` 让它选择分支 |
| Claude Code | `~/.claude/skills/` | 输入 `/tavo` |

本次更新从 `main` 安装。首次发布的安装包见 [v1.0.0](https://github.com/ai1274/tavo-skills/releases/tag/v1.0.0)。

### 可以这样用

- 补全这个 TPG v2 的清单和随包使用指南。用已授权的 MCP 校验 manifest、审计源码并复验，再用项目的 builder 打包。
- 调整这个插件的聊天面板，让窄屏上也能看清主操作，并检查输入框、安全区和键盘弹出时的布局。
- `$tavo` 在当前历史记录插件增加按发言方筛选。新建和维护插件时，默认检查相关运行路径，按实测证据优化并复测。[插件性能实测流程](skills/tavo-studio/references/plugin-performance.md)
- 为这个角色制作 CCv3 卡片和配套世界书，检查触发范围，并核对封装到 PNG 的数据。

## 技能一览

| 技能 | 交付物 |
| --- | --- |
| [tavo](skills/tavo/SKILL.md) | 统一入口，按任务加载专项技能 |
| [tavo-skill](skills/tavo-skill/SKILL.md) | 平台文档、预设、世界书、正则和 EJS |
| [tavo-1-0-beta-skill](skills/tavo-1-0-beta-skill/SKILL.md) | MCP 连接、实时 schema 和版本证据。目录名保留用于兼容 |
| [tavo-studio](skills/tavo-studio/SKILL.md) | TPG v2、TavoJS、主题、WebView、打包和 PNG 验证 |
| [tavo-character-card](skills/tavo-character-card/SKILL.md) | 角色卡及配套世界书、正则和输出约束 |
| [tavo-mainline-minimal-development](skills/tavo-mainline-minimal-development/SKILL.md) | 定位维护入口、最小修改和回归范围 |
| [tavo-memory-steward-clean-workflow](skills/tavo-memory-steward-clean-workflow/SKILL.md) | 项目职责、功能合同、实施和验收 |
| [tavo-project-tooling](skills/tavo-project-tooling/SKILL.md) | 技能路由、注册、索引与项目工具链 |

## 用 MCP 边改边验

在 Tavo 设置中启用 MCP Server，并使用该实例提供的地址。首选直连 HTTP JSON-RPC，同机示例为 `http://127.0.0.1:7347/mcp`。需要认证时，仅在当次运行中向授权的地址提供 Bearer 凭据。

插件开发时先发现目标版本、工具和兼容性声明，再用 `tavo_plugin_validate_manifest` 校验清单，用 `tavo_plugin_audit` 审计相关源码和语言资源。按诊断修正并复验后，运行项目 builder。真机验收还需在目标 App 检查导入、交互和实际渲染。[MCP 运行手册](skills/tavo-1-0-beta-skill/references/11-mcp-runtime.md)

新建 TPG v2 时按工程技能补齐清单、简介和随包使用指南。涉及面板或主题时，核对样式作用域、交互状态、窄屏布局和宿主安全区。[工程开发规则](skills/tavo-studio/SKILL.md)

2026 年 11 月 23 日的公开复核覆盖 Tavo MCP 1.12.0，并验证了合成插件的清单校验与源码审计。官网更新涉及 TavoJS 的聊天切换、插件开发，以及 `.thm` 主题包和样式作用域。[MCP 证据](skills/tavo-1-0-beta-skill/references/39-tavo-1120-mcp-evidence.md) · [官网来源与更新](skills/tavo-skill/references/public-release-sources.md)

## 离线验证

运行脚本时，使用 Python 3.11+ 和 Node.js 20+。以下命令在仓库根目录运行，无需连接 Tavo。设备验证另需 Android ADB 和经授权的 Tavo MCP。

```text
python -B skills/tavo-1-0-beta-skill/scripts/test_validate_tpg_package.py
python -B skills/tavo-1-0-beta-skill/scripts/test_dump_mcp_surface.py
python -B skills/tavo-skill/scripts/test_search_official_docs.py
node --check skills/tavo-studio/scripts/png-card-lib.mjs
```

文档搜索的语料相关测试默认跳过。获取语料后，将其目录设为 `TAVO_DOCS_CORPUS`，再运行文档搜索测试。[离线语料说明](skills/tavo-skill/references/public-release-sources.md#本地资料)

## 许可证与来源

仓库中可许可的技能说明、工具、模板和合成测试数据采用 [MIT 许可证](LICENSE)。第三方材料的权利归各自权利人所有。公开版提供官网链接、去敏实验摘要和获取离线语料的方法。[技术文档与证据](skills/tavo-skill/references/public-release-sources.md)
