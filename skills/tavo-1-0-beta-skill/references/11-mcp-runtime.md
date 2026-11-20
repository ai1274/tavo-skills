# Tavo MCP 直连运行手册

入口：[官网 MCP Server](https://docs.tavoai.dev/cn/guides/mcp-server/)；留存的本机样本：[1.11.0](38-tavo-1110-mcp-evidence.md)。本手册是公开发现路径，不执行 `tavo_status`、用户数据读取或写入来证明连接。

1. 向已授权 endpoint `POST` JSON-RPC。设置 `Content-Type: application/json` 与 `Accept: application/json, text/event-stream`；需要认证时仅向该 endpoint 发送 `Authorization: Bearer <token>`，不要把值放在 URL、CLI 参数、输出或持久配置。不要自动跨源跟重定向。
2. `initialize` 提交支持的 `protocolVersion`（1.11.0 证据为 `2025-06-18`）、`capabilities`、`clientInfo`。解析匹配请求 ID 的 JSON-RPC 响应；SSE 要取 `data` 中对应的响应而非把流当普通 JSON。记录实际协商值、`serverInfo` 和返回的 `Mcp-Session-Id`（若有），不回显会话/授权值。
3. 后续 HTTP 请求带 `MCP-Protocol-Version`（协商值）并延用 session header（若有）。先发 `notifications/initialized`，通知无 `id`，不以空的成功响应体为错误。再按需使用 `tools/list`、`resources/list`、`resources/templates/list` 或 `prompts/list`；跟随 `nextCursor` 直至所需列表完整。连接失败先区分 HTTP、JSON-RPC、session 与业务工具错误。
4. `resources/read` 只读任务限定的 URI。比如 `tavo://capabilities`、`tavo://docs/plugins/compatibility` 或任务对应 `tavo://schemas/*`，先确认目标服务器列出或声明该项。默认不读当前用户内容、私有运行元数据或状态探针。调用 App 工具必须经 `tools/call`，不要把工具名发作 RPC 方法；留意工具结果 `isError`。
5. 只保存去敏的版本、计数、资源标识和必要公开 schema。单独记录无法完成的层。工具和资源列表不是宿主写入/渲染/持久化证明，也不是原生聊天工具目录。

旧 `scripts/tavo_mcp_client.py`、`scripts/dump_mcp_surface.py` 保留在[维护索引](01-official-url-map.md#retained-utilities-maintenance-index)中；这些工具的旧调用模式/严格采集不等于上述会话流程或公开最小发现，不要用严格采集代替只读公开清单。若只有“版本或兼容”问题，优先直接查该版本的公开声明。
