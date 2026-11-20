# Source Of Truth

> 公开发行收录说明与摘要。完整官网镜像及现场捕获保存在本地，来源与复核方法见[技术文档与证据](../../tavo-skill/references/public-release-sources.md)。

This file defines how the Tavo skill decides what is current, what is inferred, and what is historical.

## Current Official Documentation Baseline

Official technical chapters: the 17-page official technical corpus verified on 2026-11-18 (five updated, twelve byte-identical). See [global sync manifest（来源说明）](../../tavo-skill/references/public-release-sources.md#本地资料).

### Historical Public Crawl

- `official-current`: complete public crawl fetched on 2026-08-09 from `https://docs.tavoai.dev/cn/`: 84/84 pages, 0 errors, 0 unfetched URLs, `complete=true`, `missing_text_count=0`.
- The crawl now includes the public Tool Calling page and is later than the connected 1.0 runtime evidence. It is declaration evidence only; no non-Markdown official snapshot is committed. Reproduce with `scripts/fetch_official_docs.py` and record the normalized manifest/counts in task evidence.
- A local TLS check reported a missing Authority Key Identifier; the crawl used a process-local unverified TLS context after the default fail-closed attempt. This is not certificate-chain verification or runtime reliability proof.

## Latest Captured MCP Snapshot

Tavo `1.11.0` / build `1110` on 2026-11-18: `112/21/8/0` tools/resources/templates/prompts and 19 public reads. Discovery and declarations only. See [1.11.0 evidence](38-tavo-1110-mcp-evidence.md).

## Historical 1.10.0 MCP Snapshot

- `mcp-runtime`: `references/37-tavo-1100-mcp-evidence.md` and `assets/evidence/1.10.0/20261114-readonly-snapshot.json` record 2026-11-14 Tavo `1.10.0` / build `1100`, protocol `2025-06-18`, inventory `112/21/8/0`, five discovery calls, all 20 selected reads and status passing.
- The matching public-resources and tools files retain 19 public texts and all 112 descriptors. Against complete 1.9.0 evidence, there are no added/removed tools: theme create/update schemas add nullable cover, and asset rename/delete descriptions account for cover references. Four public documents and the chat-theme schema changed; 14 public texts and 108 descriptors match.
- Compatibility adds settings `when` and `list` since `1.10.0`. Set `minAppVersion` from the capabilities actually used. Read-only declarations do not establish write, vector/embedding, UI, persistence or model behavior.

## Historical 1.9.0 MCP Snapshot

- `mcp-runtime`: `references/36-tavo-190-mcp-evidence.md` and `assets/evidence/1.9.0/20261107-readonly-snapshot.json` record 2026-11-07 Tavo `1.9.0` / build `1090`, requested and negotiated protocol `2025-06-18`, 112 tools, 21 resources, 8 templates, 0 prompts, all 20 selected document/schema/runtime reads, and a successful read-only status call.
- Portable `20261107-public-resources.json` retains only 19 public capability/docs/schema texts; `20261107-tools.json` retains the 112 current descriptors. Runtime/current-chat bodies and status user counts are not distributed. Four public docs and the chat-theme schema changed against 1.6.0 hashes. Old raw tool descriptors are absent, so added/removed tools and tool-schema changes remain `unknown`.
- Discovery and document readability do not prove runtime behavior. The plugin compatibility body remains byte-identical; keep its 1.3.2 filenames and versioned behavior limits.

## Historical 1.6.0 MCP Snapshot

- `mcp-runtime`: the 2026-09-23 read-only snapshot in `references/35-tavo-160-mcp-evidence.md` and `assets/evidence/1.6.0/20260923-readonly-snapshot.json` records Tavo `1.6.0` (build `1060`), negotiated MCP protocol `2025-06-18`, 112 tools, 21 resources, 8 templates, 0 prompts, changed runtime docs, one changed chat-theme schema description, plugin metadata, and a successful read-only `tavo_status`. The operator connection banner and `initialize` agreed on `1.6.0`.
- Relative to 1.5.0, the measured surface adds 16 import/export and theme-asset tools. `tavo://docs/macros` and `tavo://docs/plugins/compatibility` stay byte-identical. The other measured docs and `tavo://schemas/chat-theme` changed. Official `llms-full.txt` also changed: 799449 bytes, SHA-256 `4280908bd10786f8df556ec120df67f6639178de9377ec80ea42b17ac55288c5`.
- The 1.5.0 snapshot remains versioned evidence in `references/34-tavo-150-mcp-evidence.md` / `assets/evidence/1.5.0/20260915-readonly-snapshot.json`. It was byte-identical to the 2026-09-11 1.3.2 declared surface except for runtime identity and status counts.
- The 1.3.2 snapshot remains versioned evidence in `references/32-tavo-132-mcp-evidence.md` / `assets/evidence/1.3.2/20260911-readonly-snapshot.json`. Because the compatibility body is still unchanged, its files keep their 1.3.2 names: `references/33-tavo-132-plugin-compatibility.md` and `assets/evidence/1.3.2/20260911-plugins-compatibility.json`.
- The 1.2.9, 1.2.8, and 1.2.5 snapshots remain versioned historical evidence in `references/31-tavo-129-mcp-evidence.md` / `assets/evidence/1.2.9/20260902-readonly-snapshot.json`, `references/30-tavo-128-mcp-evidence.md` / `assets/evidence/1.2.8/20260828-readonly-snapshot.json`, and `references/29-tavo-125-mcp-evidence.md` / `assets/evidence/1.2.5/20260823-readonly-snapshot.json`.

## Historical 1.2.5 Evidence Baseline

- `official-current`: the 2026-08-09 public crawl above is supplemented by the 2026-08-23 TavoJS and Plugin Development page increment recorded in the project official mirror. The 2026-07-26 83-page files remain a historical comparison baseline only.
- `mcp-runtime`: the 2026-08-23 read-only snapshot in `references/29-tavo-125-mcp-evidence.md` and `assets/evidence/1.2.5/20260823-readonly-snapshot.json` records Tavo `1.2.5`, negotiated MCP protocol `2025-06-18`, 96 tools, 20 resources, 8 templates, 0 prompts, seven selected docs reads, capabilities read, and a successful read-only `tavo_status`.
- `release-announcement`: the user-provided Tavo 1.1 announcement declares the 1.1 feature, resource-management, performance, fix, experience, and iOS-release changes listed in `references/02-capabilities-overview.md`. It remains versioned first-party release-note evidence, not current 1.2.5 schema or reliability proof.
- `release-announcement`: the Tavo 1.0 notice announces native tool calling, plugin center, UI/performance work, `memory.append`, and fixes. It selects test targets but does not define schemas, defaults, or reliability.
- `prior-version/mcp-runtime`: the redacted 1.1 strict gate in `assets/evidence/1.1.0/20260812-gate.json`. It records Tavo `1.1.0`, negotiated MCP protocol `2025-06-18`, 95 tools, 20 resources, 8 templates, 0 prompts, all 19 selected capability/runtime/docs/schema reads, and a successful read-only `tavo_status`.
- `prior-version/live-verified`: the 1.0 discovery gate and incremental Agent Loop/MCP summary in `assets/evidence/1.0.0/`. They remain usable only for explicitly versioned compatibility claims and unchanged axes; they are not current 1.1 behavior proof.
- `prior-version`: the 0.93 broad zero-real matrix, `assets/evidence/0.92.0/20260717-live-matrix.json`, and retained 0.91 artifacts remain version-scoped controls.

The 1.0 Agent Loop run used a real provider through a credential-redacting gateway. That proves only the exact model-visible schemas, tool choices, loop transitions, and app effects captured per case; it does not turn unrelated features into real-provider or semantic passes. The prior 0.93 run used a deterministic provider with no upstream or real credentials and remains bounded to its recorded request-assembly/UI/persistence axes.

The retained official crawl has no dedicated release-notes page and does not describe the 1.0 Agent Loop. Treat the MCP `serverInfo.version` and Android package version as runtime version evidence; do not infer a complete changelog from documentation diffs or promote every announcement bullet without a matching runtime/live test.

## Source And Behavior Order

For **declared capabilities and field shapes**:

1. `official-current`: the latest crawl of `https://docs.tavoai.dev/cn/` produced by `scripts/fetch_official_docs.py`.
2. `release-announcement`: current release bullets only for identifying likely deltas.
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
- "Tavo 1.1 官方公告提到，但本轮尚未复验运行时语义..." or "1.0 更新公告提到，但文档尚未给出契约..." for `release-announcement`;
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
python3 scripts/compare_mcp_surfaces.py <previous-mcp-surface.json> <current-mcp-surface.json>
```

The historical complete official-doc crawl is the 2026-08-09 public crawl recorded in task evidence; the 2026-08-23 two-page increment is retained in the project Markdown mirror. The 2026-07-26, 2026-07-16, and 2026-07-10 snapshots are retained as versioned comparison baselines. Refresh the live site and MCP surface before treating this draft as current after future product updates.

`scripts/fetch_official_docs.py` is fail-closed by default: incomplete crawl, fetch errors, or unfetched discovered URLs should return nonzero unless `--allow-partial` is explicitly passed.
