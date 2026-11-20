# Tavo 1.10.0 MCP Evidence

> 公开发行收录说明与摘要。完整官网镜像及现场捕获保存在本地，来源与复核方法见[技术文档与证据](../../tavo-skill/references/public-release-sources.md)。

## Read-only snapshot

On 2026-11-14, strict discovery and read-only app-version calls identified Tavo `1.10.0` / build `1100`. Requested and negotiated MCP protocol were `2025-06-18`. All five discovery calls, all 20 selected capability/runtime/docs/schema reads, and `tavo_status` passed. Inventory: 112 tools, 21 resources, 8 templates, 0 prompts.

Portable evidence under `assets/evidence/1.10.0/`:

- `20261114-readonly-snapshot.json`: redacted identity, gate, current resource/template descriptors, public hashes, and bounded comparison.
- `20261114-public-resources.json`: exact text map of nine public capability/document resources and ten schemas.
- `20261114-tools.json`: all 112 tool descriptors, including descriptions and input schemas.

Private runtime/current-chat bodies, status counts, credentials and endpoint identity are excluded. Success flags retain the private reads' outcome only.

## Measured delta against 1.9.0

The retained `assets/evidence/1.9.0/20261107-tools.json` and `20261107-public-resources.json` provide complete descriptor and 19-public-text baselines. No tool names were added or removed; 108 descriptors are identical.

- `tavo_theme_create` adds `theme.cover` and `tavo_theme_update` adds `patch.cover`: HTTP(S) URL or `theme/assets/<name>` reference; string or `null`, where null clears the cover.
- `tavo_theme_assets_rename` now describes updating matching `background.image` and `cover` references; `tavo_theme_assets_delete` describes clearing both references. Both leave `customCss` unchanged. These two description changes do not change their input schemas.
- Four public documents changed: `overview`, `tavojs`, `plugins`, and `plugins/compatibility`. The overview change names “Tavo MCP Server”. Only `chat-theme` changed among the ten schema texts, adding the same `cover` field. Fourteen public texts are identical and the retained 19 URI set has no additions or removals.
- Full resource-list/template descriptor deltas remain unknown because the 1.9.0 portable baseline retains counts and public text, not complete discovery descriptors. This does not limit the exact tool-descriptor or public-text comparison above.

## New declared contracts

These are `mcp-runtime` declarations, not execution proof or a complete release changelog:

- Plugin compatibility adds `contributes.settings.schema.when` and `contributes.settings.schema.list`, each `since: 1.10.0`, `manifestDetectable: true`, `affectsMinimum: true`. Set `minAppVersion` to the maximum `since` of capabilities actually used and affecting the minimum. Do not default it to the current app version. The old `references/33-tavo-132-plugin-compatibility.md` table remains historical; use the current public resource for new settings capabilities.
- `when` conditions use earlier fields in the settings schema and are reevaluated as the form changes. Hidden fields retain stored values but supply no value to other visibility expressions while hidden. Object-list settings declare `items`, optional `fixed`, `min`, `max`, and `sortable`; config replacement supplies the whole ordered array, including `[]` when constraints permit. These declarations do not establish successful validation, installation, editing or persistence in this run.
- `contributes.visible` declares defaults per input/sidebar/last-message/chat/messages display position; user choices override defaults. Hidden chat/message positions prevent their fragments and JavaScript from mounting, while entry/lifecycle/hooks remain active.
- `generation:prepare` declares synchronous `event.addContext({ text, role?, position? })` for a separate request block without changing saved chat messages. It documents relative markers and `atDepth`, argument validation, and rollback of context additions with a failed handler's text edits. Check method presence for older hosts; do not infer a `since` absent from compatibility metadata.
- TavoJS declares `tavo.embedding.generate()` and chat/global `tavo.vector` collections, text/vector upserts and searches, listing, rebuild and deletion. Preserve `embeddingSpaceId` with vectors: a different space is incompatible even at equal dimensions. Rebuild persists completed batches and deletions before an error; search can be incomplete while rebuilding. The chat `_memories` collection is shared with long-term memory, so edits/deletes affect recall. These foreground script/plugin declarations add no matching external MCP tools.

## Official source and proof boundary

The 2026-11-14 official `llms-full.txt` export is 917431 bytes, SHA-256 `cef96e5dd15a0302dd510bf572b8ea92a3d8ff6ccbac8f245d36efe20e6ac789`. `$tavo-skill` routes 17 selected Chinese technical pages and retains targeted provenance in `assets/official-docs/targeted-sync-20261114.json`. Official declarations and MCP declarations are separate evidence layers.

This snapshot proves identity, protocol, discovery, public readability and a read-only status call. It does not prove Android/ADB readiness, writes, plugin installation, UI, generation, embedding requests, vector storage/search/rebuild, persistence, import/export, provider reliability, playback or native model-tool execution. No app-data write or behavior experiment was performed by this refresh. The 1.9.0 and earlier references retain their original dates and limits.
