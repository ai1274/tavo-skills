# Tavo MCP 1.2.8 Read-Only Evidence

> 公开发行收录说明与摘要。完整官网镜像及现场捕获保存在本地，来源与复核方法见[技术文档与证据](../../tavo-skill/references/public-release-sources.md)。

整理日期：`2026-08-28`（Asia/Shanghai）  
证据级别：`mcp-runtime`  
范围：direct HTTP JSON-RPC 只读发现、内部 docs、工具清单、资源清单、版本状态和已安装插件元数据；不包含写入、生成、TTS、调试控制或当前聊天正文。

## Snapshot

- Server: `tavo` / `Tavo` / `1.2.8`。
- Negotiated protocol: `2025-03-26`。
- Inventory: 96 tools, 20 resources, 8 resource templates, 0 prompts。
- Read successfully: `initialize`、`tools/list`、`resources/list`、`resources/templates/list`、`prompts/list`、7 个 `tavo://docs/*` 和只读 `tavo_status`。
- `tavo_status` asset counts: 27 characters, 41 lorebooks, 26 regexes, 10 presets, 1 persona。
- Installed plugin metadata: `com.tavo.memory-steward` version `1.17.54`, enabled; features `inputActions`, `sidebar`, `htmlFragments`, `settings`。

## Resource hashes

Hashes identify the retrieved UTF-8 text used for this snapshot; they do not prove runtime reliability.

| URI | Characters | SHA-256 |
| --- | ---: | --- |
| `tavo://docs/overview` | 2178 | `735cb2eb4c5b7eba66823c9bd405c114267ae68188d15ed6e8f8c5d841fed87e` |
| `tavo://docs/tools` | 7278 | `765d7eb28d632590f0960cc8bfb7eafb3b746cd8767d46a93b7941c7e135ff2f` |
| `tavo://docs/write-safety` | 2276 | `b196051edcd3c377a8aef657d7d1d8a1df473d77aa791ab34624578530074c3b` |
| `tavo://docs/macros` | 4998 | `4e77bc6e5255de7c9acc1756d38b0d64909cd470e216127f5f9fa8682fa2fda4` |
| `tavo://docs/tavojs` | 11078 | `098cc236187c1f52593db2d60fc952a9e4e19db62085f16eac83fcffa2abf85a` |
| `tavo://docs/plugins` | 37186 | `28de28fcdd3d37ce1c87caf9a6f090b11e7bf9da3e1dbf9d0be68aaf546849f9` |
| `tavo://docs/tool-calling` | 16146 | `eb4dc11da32cf8b97cf739dca128417679134f66265e23d691e1889882597638` |

## Boundaries

No MCP write, plugin install/enable/configuration, generation, TTS playback, debug control, or live release operation was executed. This snapshot proves transport/discovery/readability and returned metadata only. Persistence, provider behavior, UI behavior, costs, performance, and live installation remain `unknown`. The prior `1.2.5` snapshot remains versioned historical evidence.
