---
name: tavo
description: "Tavo 全局统一入口。用于 Tavo 平台能力、TavoJS、MCP、TPG v2、插件与 WebView、主题、角色卡 / 世界书 / 预设 / 正则，以及 Memory Center、记忆管家、Tavo 项目架构和工程工具。非 Tavo 通用工作不触发。"
---

# Tavo

按**要交付什么**选择主分支，不按出现了哪些名词叠加技能。从本文件位置直接打开对应的全局 `SKILL.md`，只读当前问题需要的参考。无需让用户手动选专项、无需重新调用技能。显式指定其他技能或路径时尊重其选择；项目内同名技能不是下表的全局文件，但所在项目的规则、合同、测试和 builder 仍约束项目工作。

| 用户要交付什么 | 读取主分支 |
| --- | --- |
| 解释平台能力、配置、接口区别，或编写独立预设 / 世界书 / 正则 / EJS 内容 | [平台文档与内容编写](../tavo-skill/SKILL.md) |
| 连接或诊断 MCP、查看 MCP 的工具/资源/schema、比较指定 MCP 版本，或经 MCP 执行被授权的操作 | [MCP 与版本证据](../tavo-1-0-beta-skill/SKILL.md) |
| 新建、修改、调试、构建 TPG / TavoJS / 主题 / WebView；核验包结构、PNG 封装或导入链路 | [工程实现与验证](../tavo-studio/SKILL.md) |
| 编写或审查角色卡套件，连同配套世界书、角色输出约束或卡内正则 | [角色卡设计](../tavo-character-card/SKILL.md) |
| 方案已定，交付物是 owner 定位、修改路径锁定或最小回归计划 | [主线最小开发](../tavo-mainline-minimal-development/SKILL.md) |
| 交付物是仓库架构/维护边界、任务合同、Writer 集成、验收或归档判断 | [项目架构与工作流](../tavo-memory-steward-clean-workflow/SKILL.md) |
| Router、Registry、项目资源校验、Project Map、RAG、Graphify、Hook 或发布脚本本身需要操作/排障 | [项目工具链](../tavo-project-tooling/SKILL.md) |

**消歧：**“TPG 的 `minAppVersion` 怎么定”是平台问答；“改这个 TPG 并打包”是工程；“连接服务器看看该字段是否暴露”是 MCP。只列已定方案的修改/回归路径走主线，梳理各工程职责走架构。卡自带世界书/正则仍走角色卡；单独写世界书走平台。源码修复不会因为要跑测试就切到工具链。确有第二交付或只有另一分支能完成的交接，到那个阶段再读另一分支，例如做卡后才通过 MCP 核对导入 schema，不因此执行导入。

**查官方技术文档：**先按交付物选分支；已知页面就直接读。接口名、配置项或术语涉及多页、章节不明时，使用[官方 URL 索引](../tavo-skill/references/01-official-url-map.md#search-the-official-snapshots-offline)。检索结果用于定位原文，不改变分支、证据级别或操作授权。

只有用户要用 Tavo 或任务确实依赖 Tavo 时才应用：仅处在 Tavo 目录、提到产品名称、翻译一段日志，或普通 CSS/JSON 问题，不自动进入整套流程。项目对象不清时先由当前目录和最近规则定位；不同 owner 会改变结果且无法消歧时才问。

声明、schema、离线测试、宿主行为分别取证。分析、构建与宿主操作权限分开；未经授权不安装、不写用户数据、不调用 provider、不发布。不要输出或保存凭据。
