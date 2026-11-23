# 技术文档与证据

[Tavo 官方文档](https://docs.tavoai.dev/cn/)提供平台声明。具体安装版本的 MCP 工具和 schema 以同一会话的授权发现为准。宿主行为需要在目标版本测试并读回。

## 2026-11-23 技术文档核对

核对[官网 Markdown 导出](https://docs.tavoai.dev/llms-full.txt)的 18 篇中文技术文档。相较 2026-11-20，TavoJS API、插件开发、主题开发、主题开发指南共 4 篇更新，14 篇不变；未发现新增中文指南。2026-11-20 已新增决策开发指南。

- 插件调用若在切换聊天时被 `chat_runtime_not_ready` 拒绝，应等新聊天的 `chat:opened`，核对目标再发起，不会自动重试。
- 新制主题的 `custom.css`、`custom.js` 放在 `.thm` 根目录，与 `theme.json` 同级。主题 CSS 的公开选择器有宿主作用域，不覆盖原生界面或插件 iframe；消息 iframe 内的正文、思考区使用各自容器。

这些是官网声明，不等同于旧版兼容或目标 WebView 实测。MCP 侧的变更独立记录在[1.12.0 摘要](../../tavo-1-0-beta-skill/references/39-tavo-1120-mcp-evidence.md)。

## 官网章节

- [advanced-rendering](https://docs.tavoai.dev/cn/guides/advanced-rendering/)
- [decision-api](https://docs.tavoai.dev/cn/guides/decision-api/)
- [ejs-template](https://docs.tavoai.dev/cn/guides/ejs-template/)
- [javascript-api](https://docs.tavoai.dev/cn/guides/javascript-api/)
- [long-memory](https://docs.tavoai.dev/cn/guides/long-memory/)
- [lore-book](https://docs.tavoai.dev/cn/guides/lore-book/)
- [mcp-server](https://docs.tavoai.dev/cn/guides/mcp-server/)
- [plugin-development](https://docs.tavoai.dev/cn/guides/plugin-development/)
- [plugin-development-guide](https://docs.tavoai.dev/cn/guides/plugin-development-guide/)
- [plugins](https://docs.tavoai.dev/cn/guides/plugins/)
- [preset](https://docs.tavoai.dev/cn/guides/preset/)
- [regular](https://docs.tavoai.dev/cn/guides/regular/)
- [supported-macros](https://docs.tavoai.dev/cn/guides/supported-macros/)
- [theme](https://docs.tavoai.dev/cn/guides/theme/)
- [theme-development](https://docs.tavoai.dev/cn/guides/theme-development/)
- [theme-development-guide](https://docs.tavoai.dev/cn/guides/theme-development-guide/)
- [tool-calling](https://docs.tavoai.dev/cn/guides/tool-calling/)
- [vector-memory](https://docs.tavoai.dev/cn/guides/vector-memory/)

## 本地资料

公开发行包含原创说明、实验摘要、脚本、模板和合成测试数据。官网镜像、完整 MCP 捕获与本地工程地图由维护者保存在本地。公开发行中的历史摘要可能记录这些本地文件的文件名、来源和校验值。可从授权的 Tavo 实例重新采集所需的最小证据。

已有独立获取的规范化官方 Markdown 时，可用平台技能下的 `scripts/search_official_docs.py --corpus <目录> <关键词>` 离线检索。脚本要求每个文件保留官方来源、同步日期、证据级别、证据边界四行元数据。公开版默认依靠上表及平台技能的官方 URL 索引。

原始文档与第三方名称的权利归各自权利人所有。仓库的 MIT 许可证覆盖本仓库有权许可的材料。
