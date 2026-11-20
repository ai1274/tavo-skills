# Tavo MCP 1.3.2 Read-Only Evidence

> 公开发行收录说明与摘要。完整官网镜像及现场捕获保存在本地，来源与复核方法见[技术文档与证据](../../tavo-skill/references/public-release-sources.md)。

整理日期：`2026-09-11`（Asia/Shanghai）  
证据级别：`mcp-runtime`  
范围：direct HTTP JSON-RPC 只读发现、内部 docs/capabilities、工具与资源清单、版本状态和插件元数据；不包含写入、生成、TTS、调试控制或当前聊天正文。

连接文案标注 `Tavo MCP Server: 1.3.1`；同一次 `initialize` 与只读 `tavo_app_version` 返回 `1.3.2` / `1032`。本快照以协商后的 `serverInfo.version=1.3.2` 作为运行时版本。

## Snapshot

- Server: `tavo` / `Tavo` / `1.3.2`。
- Negotiated protocol: `2025-06-18`。
- Inventory: 96 tools, 21 resources, 8 resource templates, 0 prompts。
- `tavo_status`: 29 characters, 53 lorebooks, 29 regexes, 11 presets, 1 persona。
- Installed plugin metadata: `com.tavo.memory-steward` `1.17.163`, enabled; features `inputActions`, `sidebar`, `htmlFragments`。

## Resource hashes

Hashes identify retrieved UTF-8 text; they do not prove runtime reliability.

| URI | Characters | SHA-256 |
| --- | ---: | --- |
| `tavo://capabilities` | 6661 | `23abd34367e1f07d802d0828d5e9d8b72362390684eb672bfd73797b7e7531fb` |
| `tavo://docs/overview` | 2178 | `735cb2eb4c5b7eba66823c9bd405c114267ae68188d15ed6e8f8c5d841fed87e` |
| `tavo://docs/tools` | 10126 | `d05213c4bb513d52b4c5b83746238a43b1d662d09a34382cf0799ca1df26e688` |
| `tavo://docs/write-safety` | 2276 | `b196051edcd3c377a8aef657d7d1d8a1df473d77aa791ab34624578530074c3b` |
| `tavo://docs/macros` | 4998 | `4e77bc6e5255de7c9acc1756d38b0d64909cd470e216127f5f9fa8682fa2fda4` |
| `tavo://docs/tavojs` | 15327 | `583decb6bc253b6484a78b8f682a034f1a5d021dbc54c91fffde935de024e7ed` |
| `tavo://docs/plugins` | 46295 | `20711aee6c855537eb1c90b41fea433ce55a94e1ed4461a38f1b38363dcd7665` |
| `tavo://docs/plugins/compatibility` | 2351 | `4f802fab4142c743e913f06a49fb2fc20eaca1b339cbe6b50f790776d10606b7` |

Readable table: `references/33-tavo-132-plugin-compatibility.md`. Exact UTF-8 body: `assets/evidence/1.3.2/20260911-plugins-compatibility.json`.
| `tavo://docs/tool-calling` | 21346 | `c8ec634d3b0e77e0a14f516be426efcd8127accb3e32f199684ef624b17b7494` |

## Boundaries

No MCP write, generation, TTS, plugin install/enable/configuration, debug control, or current-chat read was executed. This snapshot proves transport, identity, discovery inventory, resource readability, one read-only status call, one read-only app-version call, and one read-only plugin metadata get only. Persistence, provider behavior, UI behavior, costs, performance, import, and semantic reliability remain `unknown`.
