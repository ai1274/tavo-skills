---
name: tavo-studio
description: "实现和验证 Tavo TPG v2、TavoJS、主题、高级渲染与 WebView；核查包结构、PNG、导入/导出和目标宿主兼容。架构与命令从目标工程当前 owner 取得。"
---

# Tavo 工程实现与验证

先区分代码/包/导入/宿主四类结果。读目标最近规则、合同、真实入口、相关测试和当前包定义，再从[工程索引](references/engineering-index.md)选一行参考。不要默认加载其他分支或旧仓库规则。

新建、修改或修复插件时，默认按[插件优化流程](references/plugin-performance.md)完善本次涉及的功能并检查运行链路。补齐可证实的功能缺口，优化可复现的性能瓶颈，分别执行功能回归和性能复测。

实现或修复 App 右侧边栏 → WebView → 插件内技能应用时，读[侧栏技能应用与自动配置](references/sidebar-skill-application.md)，复用目标工程的注册、配置和执行实现。

1. **定位执行面。** 插件 `entry.js`/scoped `tavo`、主题脚本、消息/高级渲染脚本、EJS、原生 in-chat Tool Calling、外部 MCP 各有独立边界。按目标上下文核对同名 API、生命周期、权限和数据可见性。不要从跨层同名推断能力。
2. **约束最小变更。** 复用当前源码 owner、入口和测试 seam。行为缺陷先建立能命中问题的回归，纯样式或文档改动做定向检查。按下文核对新 TPG 的必填内容，通过项目 builder 生成包，不直接改 `dist`、生成 panel 或归档。人工源文件是不是生成物由目标合同/builder 决定。
3. **算真实最低版本。** 根据实际使用能力的 `since` 与版本门禁，取所需最低版本的最大值作为 `minAppVersion`，再与项目的支持范围核对。1.10.0 提供基础 `list`/`when`。1.11.0 增加 `header`、`placeholder`、textarea 行数和列表默认记录的 `$t`。核查 `header.when` 的作用范围仅限标题，并分别处理列表空数组与重置默认值。1.12.0 的只读快照记录了 `tavo.decision.evaluate` 与插件自定义事件的声明。使用这两项时，先核验目标宿主的版本支持情况，再声明 `minAppVersion`。[1.11.0 表单差异](../tavo-1-0-beta-skill/references/38-tavo-1110-mcp-evidence.md) · [1.12.0 声明变化](../tavo-1-0-beta-skill/references/39-tavo-1120-mcp-evidence.md) · [官方插件开发](https://docs.tavoai.dev/cn/guides/plugin-development/)。
4. **验证到用户要求的层。** 语法/schema → 聚焦测试 → 目标 package/builder → [产物核验](references/artifact-validation-playbook.md) → 经授权的目标宿主/数据 readback。前一层不替代后一层。

## 新建或补全 TPG 项目

- **平台必填：** 新包在根目录放 `manifest.json`，写 `specVersion: 2`、稳定小写 `id`、单行 `name`（1–64 个可见字符）、SemVer `version`、单行字面 `author`（1–32 个可见字符）、`description` 和 `localization.defaultLocale`。新建插件按用户或项目约定填写作者，已有插件保留原署名。声明输入动作、右侧边栏动作或最后一条消息动作时，`entry` 指向包内实际脚本，并核对动作 ID 与 handler 一致；其他引用也须打进包，用正斜杠相对路径。
- **面向用户的必交内容：** `description` 首段直接说明插件做什么，兼顾列表展示的纯文本前 120 个字符；后接「使用指南」，写明实际前提、Tavo 内入口、核心操作步骤及适用的限制或风险。用 Markdown，不靠原始 HTML；`description` 上限为 10,000 个可见字符且 UTF-8 不超过 64 KiB。用 `$t` 时核对当前及默认语言能解析到完整文案并将所用 catalog 随包交付，不能只写 README。已有面板或设置页可给必要提示，不为此另建页面。
- **按能力填写。** 按实际使用的功能核定 `minAppVersion` 和权限。封面按项目需要提供。[官方根字段与文本限制](https://docs.tavoai.dev/cn/guides/plugin-development/)

## 插件版本与更新日志

- 每次交付插件更新时，以此前交付版本和最终保留的插件改动为基准，按项目版本策略更新一次。项目无规则时，兼容修复、性能或交互完善升 patch，新增兼容功能升 minor，不兼容变更升 major。新插件初始化版本和首版日志。复测和重复打包沿用本次候选版本。只读检查或插件内容无净变化时沿用原版本。
- 更新版本的真实维护位置，并同步项目实际使用的 `manifest.json`、包配置或 builder 引用。更新本版 `releaseNotes`，按最终改动写清新增、完善、修复或可证实的性能收益。使用 `$t` 时同步对应语言目录。维护已有 `CHANGELOG` 或版本记录，只在其中保留历史。插件 ID 与按能力核定的 `minAppVersion` 各自维护。
- 从版本和日志更新后的源码走项目 builder，读取生成包内的 `version` 和解析后的 `releaseNotes`，确认与实际改动和维护源一致。交付写明旧版、新版及验证结果。

## 面板与主题美化

- 沿用项目已有组件和样式变量；先让标题、核心操作和结果一眼可辨，再处理装饰。保持间距、字级和强调色一致；图标按钮有可访问名称，保留焦点可见，状态不只靠颜色区分。涉及异步操作时给必要的加载、空态和失败反馈，避免重复提交。
- 插件面板样式限定在自己的根容器；主题只用官方公开选择器，不尝试用主题 CSS 修改插件 iframe 或原生控件。消息 iframe 的正文和思考区分别在 `.tavo-message-content`、`.tavo-message-reasoning` 下设置样式。主题包用根目录 `custom.css` / `custom.js`，不要把源码内联进 `theme.json`。[官方主题开发](https://docs.tavoai.dev/cn/guides/theme-development/)
- `/chat` 面板避开顶部导航和底部安全区；保留聊天输入时用 `bottomInput`，否则用 `bottomSafe`，两者不叠加。悬浮入口须支持触摸和鼠标拖动，区分点击与拖动，并提供位置恢复。检查窄屏、长文案、目标亮暗配色、滚动、键盘弹出与关闭操作；只有目标 Tavo WebView 实测才能证明宿主渲染通过。

## 开发时用 MCP 验证

用户提供 Tavo MCP 地址时，使用该地址进行真实验证，首选直连 HTTP JSON-RPC。按[直连运行手册](../tavo-1-0-beta-skill/references/11-mcp-runtime.md#插件开发校验)核对同会话版本和实际工具 schema，校验本次更新的 manifest、源码或实际打包输入。对功能、渲染、桥接和存储，使用该实例实际支持且已获授权的工具，核对目标插件版本、操作结果或回读数据。连接失败、缺少地址、工具或授权时，继续本地验证并说明哪项真实行为仍待测。分别报告清单与审计、宿主运行及本地模拟结果。

MCP 发现或校验之外的操作仍按 [MCP 分支](../tavo-1-0-beta-skill/SKILL.md)核对权限。角色卡写作主任务交给[角色卡分支](../tavo-character-card/SKILL.md)；项目结构不明时读[工程定位](../tavo-memory-steward-clean-workflow/references/project-architecture.md)。
