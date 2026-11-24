# Tavo 工程按需索引

选任务所需行；平台字段从 [官方技术文档来源](../../tavo-skill/references/00-source-of-truth.md) 取得，特定连接的 schema 以同会话发现为准，项目实现、命令和生成边界以当前 owner 为准。

| 子任务 | 最小参考 |
| --- | --- |
| TPG v2 manifest、entry、贡献项、配置、打包 | [插件开发](https://docs.tavoai.dev/cn/guides/plugin-development/) / [开发指南](https://docs.tavoai.dev/cn/guides/plugin-development-guide/)；从[留存的 1.11.0 兼容证据](../../tavo-1-0-beta-skill/references/38-tavo-1110-mcp-evidence.md)查表单差异；需要目标版本时重新查兼容资源。 |
| App 右侧边栏、WebView 内应用技能 | [侧栏技能应用与自动配置](sidebar-skill-application.md)，沿目标项目的注册、配置与执行链核验。 |
| TavoJS 入口、变量、generation hooks | [TavoJS](https://docs.tavoai.dev/cn/guides/javascript-api/)，查具体上下文和写入/恢复边界。 |
| 主题脚本 / 高级渲染 / WebView | [主题开发](https://docs.tavoai.dev/cn/guides/theme-development/)、[主题开发指南](https://docs.tavoai.dev/cn/guides/theme-development-guide/)或[高级渲染](https://docs.tavoai.dev/cn/guides/advanced-rendering/)；针对声明的宿主/UI 容器验证。 |
| 新建或维护插件时的自动性能检查，或专项性能诊断 | [插件性能实测流程](plugin-performance.md)，按本次涉及的运行链路定位和复测。 |
| EJS、宏、正则 | [EJS](https://docs.tavoai.dev/cn/guides/ejs-template/)、[宏](https://docs.tavoai.dev/cn/guides/supported-macros/)、[正则](https://docs.tavoai.dev/cn/guides/regular/)；按实际执行层验证。 |
| 包结构、产物导入/导出、卡 PNG | [产物核验](artifact-validation-playbook.md)，PNG 补读 [封装工具](png-embedding.md)。 |
| 确认仓库或工程 owner | [本地项目结构](../../tavo-memory-steward-clean-workflow/references/project-architecture.md)，以目标项目合同和实际命令为准。 |

[旧工程快照来源及完整性](official-sources.md) 仅供版本对照，不是当前 API、项目 owner 或默认依赖。
