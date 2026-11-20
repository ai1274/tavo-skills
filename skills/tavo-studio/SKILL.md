---
name: tavo-studio
description: "实现和验证 Tavo TPG v2、TavoJS、主题、高级渲染与 WebView；核查包结构、PNG、导入/导出和目标宿主兼容。架构与命令从目标工程当前 owner 取得。"
---

# Tavo 工程实现与验证

先区分代码/包/导入/宿主四类结果。读目标最近规则、合同、真实入口、相关测试和当前包定义，再从[工程索引](references/engineering-index.md)选一行参考。不要默认加载其他分支或旧仓库规则。

1. **定位执行面。** 插件 `entry.js`/scoped `tavo`、主题脚本、消息/高级渲染脚本、EJS、原生 in-chat Tool Calling、外部 MCP 各有独立边界。按目标上下文核对同名 API、生命周期、权限和数据可见性。不要从跨层同名推断能力。
2. **约束最小变更。** 先写能命中问题的回归；复用当前源码 owner、入口和测试 seam。新 TPG 按当前 `specVersion: 2` 文档和目标 manifest；通过该项目 builder 生成包，不直接改 `dist`、生成 panel 或归档。人工源文件是不是生成物由目标合同/builder 决定。
3. **算真实最低版本。** 从插件实际用到的 capability `since`/版本门禁取最大值，与目标支持范围核对：1.10.0 的基础 `list`/`when` 和 1.11.0 的 `header`、`placeholder`、textarea 行数、列表默认记录的 `$t` 不同。不要因本机是 1.11.0 无差别抬高 `minAppVersion`。核查 `header.when` 只隐藏标题，列表空数组与重置默认值分别处理。来源见[1.11.0 声明差异](../tavo-1-0-beta-skill/references/38-tavo-1110-mcp-evidence.md)与[官方插件开发](https://docs.tavoai.dev/cn/guides/plugin-development/)。
4. **把简介和使用指南写进插件。** 新建 TPG 默认在 `manifest.json` 使用字面作者 `Mariage d’amour`（保留 `’`）；用户指定作者优先，不擅自改署已有插件。`description` 首段写清用途与能力，后接「使用指南」：写明实际前提、Tavo 内入口、完成核心任务的步骤，以及适用的限制或风险。使用 `$t` 时把完整文案写入当前维护的语言资源并随包交付；不能只写项目 README。有需要就在已有面板或设置页给简短提示，不为此另建页面。
5. **验证到用户要求的层。** 语法/schema → 聚焦测试 → 目标 package/builder → [产物核验](references/artifact-validation-playbook.md) → 经授权的目标宿主/数据 readback。前一层不替代后一层。UI 变更测窄屏、交互、可读性和失败状态；不因浏览器能渲染就称宿主 WebView 通过。

若任务需要真实 MCP schema 或操作，才读 [MCP 分支](../tavo-1-0-beta-skill/SKILL.md)；角色卡写作主任务交给[角色卡分支](../tavo-character-card/SKILL.md)。项目结构不明时读[本地结构速查](../tavo-memory-steward-clean-workflow/references/project-architecture.md)。不拿本地构建、历史实测或平台声明冒充真实运行结果。
