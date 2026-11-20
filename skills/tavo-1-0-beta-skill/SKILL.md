---
name: tavo-1-0-beta-skill
description: "连接、诊断或比较 Tavo 外部 MCP；查看工具、资源、模板、schema、权限与版本证据。历史 ID 不代表默认产品版本；不把原生聊天 Tool Calling 当作 MCP。"
---

# Tavo MCP 与版本证据

`$tavo-1-0-beta-skill` 仅是兼容 ID。离线需要字段或版本范围时，先读[最近留存的 1.11.0 只读发现](references/38-tavo-1110-mcp-evidence.md)或目标版本的[历史索引](references/01-official-url-map.md#retained-reference-inventory)；缺少离线证据就标未知，不自动连接 MCP。查询当前连接时以**同一会话**发现为准。

1. **确认授权和范围。** 注入用户授权的 endpoint/凭据，不写文件、命令示例或日志，不将 Authorization 发送给官网或被重定向的服务。只查版本/Schema 时不读聊天、文件、provider 或 `runtime`/`status` 数据。
2. **按当前传输协商。** 直连 HTTP JSON-RPC 按[运行手册](references/11-mcp-runtime.md)完成 `initialize` → `notifications/initialized`，复用协商版本和返回的 session header（若有）。解析 JSON 或 SSE，再分页列出任务需要的工具/资源。无连接或无权限时直接报告，不从旧文档补造结果。
3. **匹配 schema 后才操作。** 用 `tools/call` 的 `params.name` / `arguments`；按同会话 `inputSchema` 识别字段和 side effect。写入、触发生成、安装、全局设置和读取敏感业务数据各自需要授权；有 dry-run、版本修订和幂等能力时按当前工具合同使用。超时后先确认状态，不盲重试。删除/修改前准备回滚，执行后定向读回。
4. **只报告已见证据。** 协商成功、描述符可见、预演、实际写入/读回、真实 UI/模型效果分别记录。将旧版本实验和全渠道发行版本与本机 `serverInfo.version` / app build 分开。

平台声明看[官网 MCP 页](https://docs.tavoai.dev/cn/guides/mcp-server/)；原生聊天工具看[原生 Tool Calling](https://docs.tavoai.dev/cn/guides/tool-calling/)。两者工具目录不互换。
