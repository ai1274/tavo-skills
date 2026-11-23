---
name: tavo-skill
description: "回答 Tavo 能力、配置、TavoJS/主题/Tool Calling 边界，或设计独立预设、世界书、正则和 EJS。查看 MCP 实时 schema、制作角色卡套件或实现插件另有专项。"
---

# Tavo 平台文档与内容编写

先辨别用户需要的是**官方声明**、**目标版本实际暴露的 schema**、**宿主行为**，还是**创作建议**。用[全局来源说明](references/00-source-of-truth.md)区分证据。问“最新”时查官网/发行渠道或本次授权连接，说明证据覆盖；不要把离线快照当成实时版本或可靠性测试。

已知页面直接打开官方链接。找不到章节时使用[官方 URL 索引](references/01-official-url-map.md)，已有本地语料时可按[离线检索说明](references/01-official-url-map.md#search-the-official-snapshots-offline)定位原文。

| 主题 | 直接读所需页面 |
| --- | --- |
| 预设、世界书、正则 | [预设](https://docs.tavoai.dev/cn/guides/preset/)、[世界书](https://docs.tavoai.dev/cn/guides/lore-book/)、[正则](https://docs.tavoai.dev/cn/guides/regular/)。分别核对注入位置、扫描/触发和显示/发送时机，不用其它宿主的字段猜 Tavo。 |
| 宏、EJS | [宏](https://docs.tavoai.dev/cn/guides/supported-macros/)、[EJS](https://docs.tavoai.dev/cn/guides/ejs-template/)；只在相应提示字段上下文下讨论执行和回退。 |
| TavoJS、主题、高级渲染 | [TavoJS](https://docs.tavoai.dev/cn/guides/javascript-api/)、[主题开发](https://docs.tavoai.dev/cn/guides/theme-development/)、[高级渲染](https://docs.tavoai.dev/cn/guides/advanced-rendering/)。`tavo.theme.on`/`.emit` 在主题上下文。`.thm` 根目录使用 `custom.css`、`custom.js`；MCP/API 的 `customCss`、`customJs` 是源码字符串，不能直接当作包格式。兼容旧格式时查目标宿主。 |
| 决策 API、插件自定义事件 | `tavo.decision.evaluate` 属于角色脚本和插件的 TavoJS API。高级渲染下的插件自定义事件仅在当前聊天、同一插件的 `entry` 与 `/chat` 片段间作用。[决策开发指南](https://docs.tavoai.dev/cn/guides/decision-api/) · [插件开发](https://docs.tavoai.dev/cn/guides/plugin-development/) |
| 长记忆、向量 | [长记忆](https://docs.tavoai.dev/cn/guides/long-memory/)、[向量管理](https://docs.tavoai.dev/cn/guides/vector-memory/)。`tavo.memory.getShortTermLength()` 是全局历史消息数量上限，`0` 不限制；不等于实际上下文、轮数或 token。1.12.0 的 MCP schema 仍将 `vectorized` 世界书激活类型标为尚不生效。 |
| TPG、原生 Tool Calling、外部 MCP | [插件开发](https://docs.tavoai.dev/cn/guides/plugin-development/)、[原生 Tool Calling](https://docs.tavoai.dev/cn/guides/tool-calling/)、[MCP Server](https://docs.tavoai.dev/cn/guides/mcp-server/)。不要把原生模型工具、插件动作与外部工具混作一个目录。 |
| 角色/聊天/媒体、提供方设置、其他功能 | 查[官方 URL 与全局资料索引](references/01-official-url-map.md)的对应官方页；旧 UI/历史实测只能作为待复核线索。 |

编写时先定消费端、作用域、数据形状与可见效果。独立世界书检查正/负触发、扫描范围和定位；正则拿真实格式的合成样本测空值、多行、规则顺序与显示/发送差异；预设/EJS 核查注入顺序、变量缺失和错误回退。局部测试只证明对应断言，不证明真实导入或模型遵从。

仅遇到真实连接/schema 才打开 [MCP 分支](../tavo-1-0-beta-skill/SKILL.md)；角色卡套件走[角色卡](../tavo-character-card/SKILL.md)，可运行插件/主题/WebView 则走[工程分支](../tavo-studio/SKILL.md)。
