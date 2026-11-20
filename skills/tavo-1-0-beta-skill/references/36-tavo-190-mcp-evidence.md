# Tavo 1.9.0 MCP Evidence

> 公开发行收录说明与摘要。完整官网镜像及现场捕获保存在本地，来源与复核方法见[技术文档与证据](../../tavo-skill/references/public-release-sources.md)。

Historical snapshot and complete comparison baseline. The subsequent 1.10.0 evidence is in `references/37-tavo-1100-mcp-evidence.md`; all original 1.9.0 dates and measured limits below remain unchanged.

## Read-only Snapshot

On 2026-11-07, fresh strict discovery identified Tavo `1.9.0`; read-only app-version calls returned `1.9.0` and build `1090`. Requested and negotiated MCP protocol were `2025-06-18`. All five top-level discovery calls, all 20 selected capability/runtime/docs/schema reads, and `tavo_status` succeeded. Inventory: 112 tools, 21 resources, 8 resource templates, 0 prompts.

Portable evidence:

- `assets/evidence/1.9.0/20261107-readonly-snapshot.json`: redacted identity, inventory, public hashes and bounded comparison.
- `assets/evidence/1.9.0/20261107-public-resources.json`: exact URI-to-text map of nine public capability/document resources and ten schemas.
- `assets/evidence/1.9.0/20261107-tools.json`: complete 112 descriptors with `name`, `description`, and `inputSchema`. Use these for this version's declared MCP inputs; refresh before future live operations.

No raw dump, runtime/current-chat body, status user count, private chat identifier, credential or private endpoint is distributed. Public document examples and tool schemas describe contracts, not user state.

## Measured Delta Against 1.6.0

Public text hashes changed for `tavo://docs/macros`, `tavo://docs/tavojs`, `tavo://docs/tool-calling`, and `tavo://docs/tools`; only `tavo://schemas/chat-theme` changed among the ten schema hashes. Other public resource/schema hashes match 1.6.0. The plugin compatibility hash remains `4f802fab4142c743e913f06a49fb2fc20eaca1b339cbe6b50f790776d10606b7`, matching 1.3.2; retain the 1.3.2 compatibility filenames and prior behavior limits.

The 1.6.0 raw tool descriptors are absent. Both snapshots count 112 tools, but added/removed names and changed tool schemas/descriptions remain `unknown`; equal counts do not prove an unchanged interface. The retained 1.6.0 summary is historical evidence, not a reconstructed descriptor baseline.

## Current Documented Contracts

These are `mcp-runtime` declarations observed in the retained public texts, not newly executed behavior or a complete release changelog:

- Macros distinguish `{{charScenario}}` from `{{scenario}}`: the latter uses the conversation override and falls back to the character scenario. Reusable names use `{{char}}` / `{{user}}`; preserve deliberate world proper nouns.
- MCP generation accepts `options.timeout` in milliseconds; omitted or zero means no limit. `tavo_generate` requires a positive explicit `chatId` and non-empty prompt and is non-streaming. Acceptance is separate from downstream completion for `tavo_input_send`.
- TavoJS `tavo.message.variant` manages non-current alternatives on a stable message floor. That namespace is foreground TavoJS/plugin-only; no matching MCP or native model-facing variant tools are declared.
- Native `tavo_web_search` requires a configured complete Web Search API and native transport. `tavo_web_fetch` is separately exposed; it does not execute JavaScript, render dynamic pages, or extract PDF/binary content. These native model tools must not be inferred from the external MCP inventory.
- Theme action buttons and joined button groups have separate CSS selectors: `.tavo-action-bar-button` and `.tavo-action-bar-button-group`. The chat-theme schema is available in the public map; inspect its exact current fields rather than inferring them from old examples.

The public official export was refreshed on 2026-11-07: 863586 bytes, SHA-256 `e93093136e1845e3a6cf30fda59a1bc7bd899134b19d0302bb3d4a2fedde6cc4`. Current topic bodies and sync metadata live in the project `docs/Tavo官方技术文档/` mirror. Official docs and MCP declarations remain distinct evidence sources.

## Proof Boundary

This snapshot proves identity, transport, discovery inventory, public hashes, document/schema readability and a read-only status call. It does not prove Android/ADB readiness, UI, message variants, macros in a real prompt, file import/export, writes, persistence, generation, provider compatibility, playback or web semantics. No app data write, plugin installation, model call or UI experiment was performed by this refresh. Older live evidence remains version-scoped; new behavior needs its own authorized execution and readback.
