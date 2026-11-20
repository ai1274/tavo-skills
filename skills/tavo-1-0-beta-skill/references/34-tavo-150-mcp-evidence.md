# Tavo MCP 1.5.0 Read-Only Evidence

> 公开发行收录说明与摘要。完整官网镜像及现场捕获保存在本地，来源与复核方法见[技术文档与证据](../../tavo-skill/references/public-release-sources.md)。

整理日期：`2026-09-15`（Asia/Shanghai）  
证据级别：`mcp-runtime`  
范围：direct HTTP JSON-RPC 只读发现、内部 docs/capabilities、全部 schemas、工具与资源清单、版本状态和插件元数据；不包含写入、生成、TTS、调试控制或当前聊天正文。

连接文案与本轮 `initialize` 一致标注 `1.5.0`；只读 `tavo_app_version` 返回 `1.5.0`，`tavo_app_version_number` 返回 `1050`。本快照以协商后的 `serverInfo.version=1.5.0` 作为运行时版本。

## Snapshot

- Server: `tavo` / `Tavo` / `1.5.0`。
- Negotiated protocol: `2025-06-18`。
- Inventory: 96 tools, 21 resources, 8 resource templates, 0 prompts。
- `tavo_status`: 29 characters, 50 lorebooks, 29 regexes, 11 presets, 1 persona。
- Installed plugin metadata: `com.tavo.memory-steward` `1.17.182`, enabled; features `inputActions`, `sidebar`, `htmlFragments`。

## 相对 1.3.2 的变化

- 版本：`1.3.2`（`1032`）到 `1.5.0`（`1050`）；连接文案不再与协商版本不一致。
- Inventory 完全不变：96 tools、21 resources（3 static + 8 docs + 10 schemas）、8 resource templates、0 prompts。
- `tavo://capabilities`、全部 8 个 `tavo://docs/*` 与全部 10 个 `tavo://schemas/*` 正文与 2026-09-11 1.3.2 快照逐字节一致；8 个 docs 资源的 SHA-256 逐一相同。
- 因此相对 1.3.2，本轮**没有新增或删除工具、资源、模板、schema 或文档声明**；差异仅在版本身份和 `tavo_status` 资产计数。
- 官方站点本轮无需重刷：`https://docs.tavoai.dev/llms-full.txt` HTTP 200，760701 字节，SHA-256 `4fbe514dd02467ac446776bad72f6459a37f23abc276cd5b28c802acf2861806`，与 2026-09-11 镜像同源字节一致。

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
| `tavo://docs/tool-calling` | 21346 | `c8ec634d3b0e77e0a14f516be426efcd8127accb3e32f199684ef624b17b7494` |

可读兼容表：`references/33-tavo-132-plugin-compatibility.md`；原文：`assets/evidence/1.3.2/20260911-plugins-compatibility.json`。该表正文在 1.5.0 未变，因此仍按 1.3.2 快照命名，不重命名文件。

## Schema hashes

本快照首次记录 schema 正文哈希，便于后续版本判定 schema 是否真的变化。

| URI | Characters | SHA-256 |
| --- | ---: | --- |
| `tavo://schemas/character` | 1284 | `6f36a87c8a11bae1ff0908b6334a9793323e1d98b2e289b91b7472f43f8c8216` |
| `tavo://schemas/lorebook` | 1151 | `eb782105fa50e33f50122a9a4ac1cf57eda38567291960afcc589534260de603` |
| `tavo://schemas/lorebook-entry` | 3009 | `3f26d642dd09f361afd6663ec51d73d67ce394583622ab0cd88686c992efd062` |
| `tavo://schemas/regex` | 495 | `f2428002410d6a2a78794a5162164cd732cca1bf30628933caed1bae9fe293c6` |
| `tavo://schemas/regex-entry` | 686 | `8b8c093ebb1128210235d8d9ef292a2e5dbffa9b3022be5442d1e8118240b25e` |
| `tavo://schemas/preset` | 605 | `b22d7722fdd67b0be1a0ddccb41d60eab24511b79574be4ec6236ab0be94e5bd` |
| `tavo://schemas/persona` | 576 | `f7382c8ca0574a1291dcc0596e70173b71598d5cbbd9bb70bf875fac20e2682c` |
| `tavo://schemas/chat` | 1459 | `fcef6da17958f6b6cd21ce31c4491639d584e7325e68add53073d930f6d208d0` |
| `tavo://schemas/chat-theme` | 16245 | `3a9ad03fbaa38e21a20db31c32aab58af7f1366653d38b0a784960b81be76f1f` |
| `tavo://schemas/message` | 765 | `d21737835999dc27f27e95da2206630186933c419fff568d1c403dad7c447baf` |

顶层 required 保持：character `name/description/first_mes`、lorebook `name/entries`、regex `name/entries`、regex-entry `identifier/name/findRegex/replaceString`、preset `name`、persona `name`、chat `characterIds`、chat-theme `name`、message `content`；lorebook-entry 仍无顶层 required。

## Boundaries

No MCP write, generation, TTS, plugin install/enable/configuration, debug control, or current-chat read was executed. This snapshot proves transport, identity, discovery inventory, complete resource and schema readability, one read-only status call, one read-only plugin metadata read, one read-only app-version call, and one read-only app-version-number call only. Persistence, provider behavior, UI behavior, costs, performance, import, and semantic reliability remain `unknown`.

A 1.3.2-to-1.5.0 identity change with byte-identical declared surface is evidence that the runtime contract did not change on the axes measured here. It is not evidence that intermediate 1.3.x/1.4.x behavior gaps do not exist on axes this snapshot does not measure.
