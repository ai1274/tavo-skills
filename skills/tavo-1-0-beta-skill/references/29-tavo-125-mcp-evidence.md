# Tavo MCP 1.2.5 Read-Only Evidence

> 公开发行收录说明与摘要。完整官网镜像及现场捕获保存在本地，来源与复核方法见[技术文档与证据](../../tavo-skill/references/public-release-sources.md)。

整理日期：`2026-08-23`（Asia/Shanghai）  
证据级别：`mcp-runtime`  
范围：direct HTTP JSON-RPC 只读发现、内部 docs/capabilities、工具清单和 `tavo_status`；不包含写入、当前聊天或完整运行时 payload。

## Snapshot

- Server: `tavo` / `Tavo` / `1.2.5`。
- Negotiated protocol: `2025-06-18`。
- Inventory: 96 tools, 20 resources, 8 resource templates, 0 prompts。
- Read successfully: `initialize`、`tools/list`、`resources/list`、`resources/templates/list`、`prompts/list`、7 个 `tavo://docs/*`、`tavo://capabilities` 和只读 `tavo_status`。
- Deliberately not read: `tavo://runtime`、`tavo://current-chat`，避免把当前会话或私有上下文写入项目。

## Incremental Findings

- `tavo_app_version` 与 `tavo_app_version_number` 在当前工具清单中可见。
- `tavo_input_send` 在输入被正常聊天流接受时返回，不等待模型或生图完成。
- 文件列表使用不透明 cursor 分页，并返回路径、名称、大小、MIME 类型和修改时间等元数据。
- 写安全以同一次 `tools/list` 的 descriptor 为准：按工具实际暴露的 `dryRun`、`clientRequestId` 等控制执行；不要把旧版本 `expectedRevision` 推断到所有当前工具。
- 开发构建可见 debug 资源和控制工具，但这些不是 release build 的生产 API。
- TavoJS 聊天切换未准备好时返回 `error.code=conflict`、`error.details.reason=chat_runtime_not_ready`、`error.details.retryable=true`；请求不执行且不会自动重试。

## Resource Hashes

Hashes identify the retrieved text used for this snapshot; they do not prove runtime reliability.

| URI | Characters | SHA-256 |
| --- | ---: | --- |
| `tavo://docs/overview` | 2178 | `735cb2eb4c5b7eba66823c9bd405c114267ae68188d15ed6e8f8c5d841fed87e` |
| `tavo://docs/tools` | 7492 | `ac0f024cc086ba98fffb4466cc841fd4af77b719141be8c784e41afe9d9a4c73` |
| `tavo://docs/write-safety` | 2276 | `b196051edcd3c377a8aef657d7d1d8a1df473d77aa791ab34624578530074c3b` |
| `tavo://docs/macros` | 4998 | `4e77bc6e5255de7c9acc1756d38b0d64909cd470e216127f5f9fa8682fa2fda4` |
| `tavo://docs/tavojs` | 11074 | `07400372d331bba75ccf9b793fab6810fd9680ca6c09d74f5b6517e10cfa40e0` |
| `tavo://docs/tool-calling` | 15904 | `ce137222af7d8510c29b8c43be4bfa031e4c5803b62ca5d6849acc9bb9866fcb` |
| `tavo://docs/plugins` | 36932 | `4abb976ac964871e0b48afe428b16f485a221b683a488b9b882a59d41765fef9` |

## Boundaries

No MCP write, generation, TTS playback, plugin install/enable/configuration, debug control, or current-chat read was executed. The snapshot proves only the listed transport/discovery/readability facts. Persistence, provider behavior, UI behavior, costs, performance, and installation state remain `unknown`.
