# Tavo MCP 1.2.9 Read-Only Evidence

> 公开发行收录说明与摘要。完整官网镜像及现场捕获保存在本地，来源与复核方法见[技术文档与证据](../../tavo-skill/references/public-release-sources.md)。

整理日期：`2026-09-02`（Asia/Shanghai）  
证据级别：`mcp-runtime`  
范围：direct HTTP JSON-RPC 只读发现、内部 docs/capabilities、工具与资源清单、版本状态和插件元数据；不包含写入、生成、TTS、调试控制或当前聊天正文。

## Snapshot

- Server: `tavo` / `Tavo` / `1.2.9`。
- Negotiated protocol: `2025-06-18`。
- Inventory: 96 tools, 20 resources, 8 resource templates, 0 prompts。
- `tavo_status`: 29 characters, 45 lorebooks, 29 regexes, 11 presets, 1 persona。
- Installed plugin metadata: `com.tavo.memory-steward` `1.17.110`, enabled; features `inputActions`, `sidebar`, `htmlFragments`, `settings`。

## Resource hashes

Hashes identify retrieved UTF-8 text; they do not prove runtime reliability.

| URI | Characters | SHA-256 |
| --- | ---: | --- |
| `tavo://capabilities` | 6618 | `d3def258b9c7f44f9944439e923dfbb44ad9d6a11dac1cd684a8876a6a112b60` |
| `tavo://docs/overview` | 2178 | `735cb2eb4c5b7eba66823c9bd405c114267ae68188d15ed6e8f8c5d841fed87e` |
| `tavo://docs/tools` | 7278 | `765d7eb28d632590f0960cc8bfb7eafb3b746cd8767d46a93b7941c7e135ff2f` |
| `tavo://docs/write-safety` | 2276 | `b196051edcd3c377a8aef657d7d1d8a1df473d77aa791ab34624578530074c3b` |
| `tavo://docs/macros` | 4998 | `4e77bc6e5255de7c9acc1756d38b0d64909cd470e216127f5f9fa8682fa2fda4` |
| `tavo://docs/tavojs` | 11078 | `098cc236187c1f52593db2d60fc952a9e4e19db62085f16eac83fcffa2abf85a` |
| `tavo://docs/tool-calling` | 16146 | `eb4dc11da32cf8b97cf739dca128417679134f66265e23d691e1889882597638` |
| `tavo://docs/plugins` | 37795 | `6eee09261069f391100f33542bb8cdeb1e57498f1620772a5b5fefd0efa2ef34` |

## Boundaries

No MCP write, generation, TTS, plugin install/enable/configuration, debug control, or current-chat read was executed. This snapshot proves transport, identity, discovery inventory, resource readability, and one read-only status call only. Persistence, provider behavior, UI behavior, costs, performance, import, and semantic reliability remain `unknown`.
