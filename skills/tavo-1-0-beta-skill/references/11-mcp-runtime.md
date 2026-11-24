# Tavo MCP 直连运行手册

本手册覆盖公开发现和插件开发校验。连接验证使用公开版本、工具和资源。[官网 MCP Server](https://docs.tavoai.dev/cn/guides/mcp-server/) · [1.12.0 只读发现](39-tavo-1120-mcp-evidence.md)

1. 从 Tavo 的 MCP 设置复制当前服务器地址，用直连 HTTP `POST` 发送 JSON-RPC。同机地址形如 `http://127.0.0.1:<port>/mcp`，端口以客户端显示为准。设置 `Content-Type: application/json` 与 `Accept: application/json, text/event-stream`。需要认证时，可在进程环境 `TAVO_MCP_AUTH` 注入完整的 `Bearer <token>`，仅发送给获授权的服务器。不要把凭据写入 URL、命令行参数、日志或持久配置，也不要跟随重定向。
2. `initialize` 提交支持的 `protocolVersion`（1.12.0 实测协商为 `2025-06-18`）、`capabilities`、`clientInfo`。解析匹配请求 ID 的 JSON-RPC 响应。SSE 响应取对应事件的 `data`。记录实际协商值和 `serverInfo`，有 `Mcp-Session-Id` 时仅在当次会话中复用。
3. 后续 HTTP 请求带 `MCP-Protocol-Version`（协商值）并延用 session header（若有）。先发 `notifications/initialized`，通知无 `id`，不以空的成功响应体为错误。再按需使用 `tools/list`、`resources/list`、`resources/templates/list` 或 `prompts/list`；跟随 `nextCursor` 直至所需列表完整。连接失败先区分 HTTP、JSON-RPC、session 与业务工具错误。
4. `resources/read` 只读任务限定的 URI。比如 `tavo://capabilities`、`tavo://docs/plugins/compatibility` 或任务对应 `tavo://schemas/*`，先确认目标服务器列出或声明该项。默认不读当前用户内容、私有运行元数据或状态探针。调用 App 工具必须经 `tools/call`，不要把工具名发作 RPC 方法；留意工具结果 `isError`。
5. 只保存去敏的版本、计数、资源标识和必要公开 schema。单独记录无法完成的层。工具和资源列表不是宿主写入/渲染/持久化证明，也不是原生聊天工具目录。

旧 `scripts/tavo_mcp_client.py`、`scripts/dump_mcp_surface.py` 保留在[维护索引](01-official-url-map.md#retained-utilities-maintenance-index)中；这些工具的旧调用模式/严格采集不等于上述会话流程或公开最小发现，不要用严格采集代替只读公开清单。若只有“版本或兼容”问题，优先直接查该版本的公开声明。

## 插件开发校验

真实验证直连用户为当前任务提供的 Tavo MCP 地址。没有地址时记录待测条件。凭据仅随请求发往授权地址。

1. 在同一会话读取版本、`tavo://docs/plugins/compatibility` 和所需工具的 `inputSchema`。目标版本或工具不可用时，继续项目本地验证并记录哪项检查缺少证据。
2. 改动清单时调用 `tavo_plugin_validate_manifest`，按当前 schema 传入 `{ "manifest": ... }`。读取工具结果中的业务状态和字段诊断。该检查能推导清单声明的最低版本，TavoJS 和 HTML 实际使用的能力仍须分别核对。
3. 改动源码、资源或本地化目录时调用 `tavo_plugin_audit`。根据当前 schema 二选一传入经授权且服务端可读的 `sourcePath`，或传不含凭据及用户数据的 `files`。修正诊断后重新校验或审计，再运行项目已有的构建和产物检查。

清单校验和源码审计可以在无安装的开发循环中执行。安装、启用以及目标宿主测试需遵守当前任务授权。[工程验证](../../tavo-studio/SKILL.md)
