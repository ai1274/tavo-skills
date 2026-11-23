# Source Of Truth

> 公开发行收录说明与摘要。完整官网镜像及现场捕获保存在本地，来源与复核方法见[技术文档与证据](public-release-sources.md)。

This file defines how the Tavo skill decides what is current, what is inferred, and what is historical.

## Current Official Documentation Baseline

- `official-current`: the 2026-11-23 [official documentation check](public-release-sources.md#2026-11-23-技术文档核对) compared 18 Chinese technical chapters; four changed and 14 remained unchanged since 2026-11-20. The public repository links to the original pages instead of bundling the snapshots. This targeted comparison does not establish host compatibility.
- Historical 2026-11-07 export: 863586 bytes, SHA-256 `e93093136e1845e3a6cf30fda59a1bc7bd899134b19d0302bb3d4a2fedde6cc4`; its 16-page sync changed six bodies and retained ten versus 2026-10-03.
- The retained 2026-09-23 public-index check listed 84 `/cn` links with the old `/cn/guides/chat/import-export/` URL absent. The 2026-11-07 and 2026-11-14 targeted full-export checks did not repeat a full-site crawl or recheck that link count. Content synchronization is not runtime reliability proof.

## Retained 0.92 Evidence Baseline

- `prior-version`: complete 83-page crawl fetched on 2026-07-16, stored in `assets/official-docs/text-20260716/`, `assets/official-docs/official_manifest-20260716.json`, and `assets/official-docs/url_map-20260716.json`. It is a 0.92-era comparison baseline, not the current official snapshot.
- `prior-version/mcp-runtime`: redacted Tavo `0.92.0` surface stored in `assets/schemas/mcp-surface-0.92.0-20260716.json` with compact index `assets/schemas/mcp-surface-index-0.92.0-20260716.json`.
- `prior-version/live-verified`: the 2026-07-16 ADB/MCP readiness gate plus the redacted 2026-07-17 atomic matrix in `assets/evidence/0.92.0/20260717-live-matrix.json`. The matrix promotes only its named 0.92 assertions: eight core cases passed; F05 notifications, F09 generation sources, and F11 TTS remain mixed. Package/update/Backup B roundtrips and bounded theme, voice-rule, ASR/TTS/image, and NovelAI UI/integration results are recorded separately. Prior 0.91 artifacts remain version-scoped controls.

For MCP schemas and inventory, start with the [1.12.0 MCP public summary](../../tavo-1-0-beta-skill/references/39-tavo-1120-mcp-evidence.md). Do not promote dated observations to live evidence.

The user-provided Tavo 1.1 official announcement is `release-announcement` evidence for the declared update list summarized in `references/02-capabilities-overview.md`. It is `official-only`: it does not replace current MCP descriptors or prove UI, write, persistence, performance, fix, Android, or iOS behavior.

The retained site crawl had no dedicated release-notes page. Verify the relevant store or distribution separately: the [US Apple lookup](https://itunes.apple.com/lookup?id=6744438897&country=us) reported `1.10.0` on 2026-11-18 (released 2026-11-14), while the local MCP capture dated 2026-11-18 recorded `1.11.0` / build `1110`. Neither proves a global latest release. Documentation diffs are not a complete release changelog.

## Source And Behavior Order

For **declared capabilities and field shapes**:

1. `official-current`: the relevant [official source page](01-official-url-map.md), or the optional local technical corpus for its selected 18 chapters.
2. `release-announcement`: versioned official release bullets used to identify likely deltas and tests.
3. `mcp-runtime`: live tools, resources, schemas, runtime docs, and read-only app state from the connected phone.
4. `historical`: older Tavo-family skills, old probe logs, and old generated guides.

For **whether a feature actually works and is reliable**, use `live-verified` evidence from the current app version. Positive and negative Android/MCP experiments both count. A reproducible live regression outranks a general official support statement for the narrower runtime-behavior claim.

When a current official page and the current MCP runtime document the same new contract, label it `official-current` or `mcp-runtime` until the exact Android effect is executed and read back. Two declarations do not equal a live test.

## Conflict Policy

- When official docs and old skills conflict, use official docs as the current claim and move the old claim to `references/historical/deprecated-claims.md`.
- When official docs are vague but MCP runtime exposes a concrete schema/tool, describe the MCP evidence and mark the result `mcp-runtime`.
- When docs and MCP both leave a behavior ambiguous, design an Android experiment in `references/12-validation-matrix.md` before answering as fact.
- When official docs or MCP expose a feature but current live tests fail, say that the feature is declared but currently unreliable. Preserve both sides and use a `mixed` or `blocked` verdict; do not let documentation overwrite the regression.
- When live positive and live negative results conflict, scope each configuration, app/runtime state, and date. The aggregate reliability verdict remains `mixed` until a discriminating retest resolves it.
- When answering creative quality questions, separate product guarantees from authoring guidance. Use `creative-guidance` for craft advice.
- Use `historical-derived` for non-conflicting material from old skills that improves workflow but still needs current Tavo validation before becoming a product fact.

## Old Skill Quarantine

Old Tavo skills are valuable as search material, not as truth. They may provide:

- candidate workflows to retest;
- script ideas and stable SillyTavern-format utilities;
- known traps, removed APIs, and stale mental models;
- examples of card/worldbook/prompt structure that still need current validation.

They must not provide:

- current API signatures without MCP or official-doc confirmation;
- current app UI paths without Android confirmation;
- current plugin or TavoJS behavior without retesting;
- claims about write permission, persistence, or import success without a current evidence path.

## Evidence In Answers

For non-trivial capability answers, state the evidence tier briefly:

- "官方文档当前写到..." for `official-current`;
- "MCP 当前暴露..." for `mcp-runtime`;
- "真机本轮验证..." for `live-verified`;
- "旧 skill 的创作经验可借用，但尚未当作当前产品事实..." for `historical-derived`;
- "旧 skill 里有这个说法，但尚未重验..." for `historical`;
- "旧 skill 里的这个说法现在按废弃处理..." for `deprecated`.

## Refresh Commands

```bash
python3 scripts/fetch_official_docs.py --output /tmp/tavo-official-docs-current
python3 scripts/normalize_official_docs.py
python3 scripts/dump_mcp_surface.py --strict --output /tmp/tavo-mcp-surface-current
```

The complete official-doc text under `assets/official-docs/text-20260716/` is retained 0.92-era evidence. The 2026-07-10 snapshot is the 0.91-era comparison baseline. Use the current corpus and version evidence linked above instead.

`scripts/fetch_official_docs.py` is fail-closed by default: incomplete crawl, fetch errors, or unfetched discovered URLs should return nonzero unless `--allow-partial` is explicitly passed.
