# MCP Runtime

This reference covers direct HTTP JSON-RPC operation against Tavo's built-in MCP server. It documents Tavo's own MCP surface only; project-specific MCP client/plugin logic does not belong in this Skill.

## Official Page And Security

- `https://docs.tavoai.dev/cn/guides/mcp-server/`
- The server exists since v0.91.0, is disabled by default, and uses a bearer token plus an app-selected access scope.
- Never store or print the bearer token. Saved dumps must redact authorization values and scrub sensitive URL data.
- Common official failure classes are `401` bad/missing token, `403` insufficient scope, `404/405` wrong URL or method, and timeout/reachability failures.

For the current official MCP Server chapter, use [the official mirror](https://docs.tavoai.dev/cn/guides/mcp-server/). Native in-chat Tool Calling is a separate surface from external MCP `tools/list`.

Preferred access for this workflow is direct HTTP JSON-RPC. Invoke app tools through `tools/call`; do not treat tool names as top-level JSON-RPC methods.

For authorized public discovery use [the current connection procedure](../../tavo-1-0-beta-skill/references/11-mcp-runtime.md) and [the retained 1.11.0 evidence](../../tavo-1-0-beta-skill/references/38-tavo-1110-mcp-evidence.md). The rest of this document describes legacy compatibility and phone validation, not required discovery.

The Tavo 1.1 official announcement declares theme CRUD/realtime refresh, external-file import/file listing, broader chat fields, web search, and native Tool behavior. This is `release-announcement` only; do not infer MCP parameter shapes or successful writes from the announcement.

## Retained 0.92 Gate (Historical)

`prior-version/live-verified` on 2026-07-16:

- server identity: Tavo `0.92.0`;
- 70 tools, 18 resources, 7 resource templates, 0 prompts;
- `initialize`, `tools/list`, `resources/list`, `resources/templates/list`, and `prompts/list` all returned without failure;
- all 17 discovered high-value docs/schema resources read successfully;
- current runtime resource reported the protected existing chat with 3 messages and blank input;
- the operator gate also called `tools/call -> tavo_status` successfully;
- ADB gate confirmed an authorized Android 16 device, model `24129PN74C`, package `app.bitbear.tav`, versionName `0.92.0`, versionCode `920`, and a running process. Reusable Skill evidence does not retain the device serial or private chat identity.

Durable redacted evidence:

- `assets/schemas/mcp-surface-0.92.0-20260716.json`
- `assets/schemas/mcp-surface-index-0.92.0-20260716.json`
- `assets/evidence/0.92.0/20260716-gate.json`

This historical gate proves reachability, identity, discovery, document readability, one harmless tool call, and ADB readiness only for its recorded Tavo 0.92 epoch. It does not prove later host behavior or any new plugin, TTS, input, generation, theme, backup, ASR, or UI semantics.

## Protocol Version Distinction

The retained 0.92 `tavo://capabilities` resource declares MCP protocol `2025-06-18`. Both the retained surface dump in `assets/schemas/mcp-surface-0.92.0-20260716.json` and the strict gate in `assets/evidence/0.92.0/20260716-gate.json` requested and negotiated `2025-06-18`. Record both the request and actual response for each artifact:

- use the runtime-declared `2025-06-18` as the default protocol request for refreshed clients;
- record the actual `initialize.result.protocolVersion` returned by the server;
- never rewrite a negotiated value to match the requested value.

A request/response difference is evidence, not by itself a failure. A strict gate fails only when required calls/resources fail or the negotiated protocol is unusable for the tested client.

## Legacy Strict Phone Readiness Contract

This optional legacy workflow includes `tavo_status` and non-public runtime reads. It must not be used for public inventory or to infer authorization. When the strict phone workflow itself is explicitly in scope, its dump must fail unless all of these pass:

1. `initialize`;
2. `tools/list`;
3. `resources/list`;
4. `resources/templates/list`;
5. `prompts/list`;
6. every dynamically discovered docs/schema/capabilities/runtime resource read;
7. one `tools/call` of `tavo_status`.

The dump must save `serverInfo`, requested and negotiated protocol versions, counts, failed top-level calls, failed resource reads, and document read status. Do not downgrade a missing prompts call or failed dynamic document to a warning in strict mode.

`scripts/test_dump_mcp_surface.py` is the offline regression test for this strict contract: prompts/list, every resource read, and `tavo_status` are required, and requested/negotiated protocol plus status success must appear in the summary.

## 0.92 Runtime Boundary (Historical)

In the retained 0.92 surface, available MCP groups covered status, characters, lorebooks, regexes, presets, personas, chats, messages, input, and plugins. Variables/files were declared planned; memory/generation/image generation were deferred; diagnostics were partial. This is not the currently connected host inventory.

The retained 0.92 surface had no ASR/STT/speech-recognition/transcription/microphone tool, resource, resource template, or schema. Report this as “not exposed through the retained 0.92 MCP surface,” not “the app has no ASR” or a current 1.0 claim.

The retained 0.92 `tavo://docs/plugins` and `tavo://docs/tavojs` exposed plugin contracts including root `entry`, legacy alias precedence, hook-only entry, config reads, chat/message notifications, input interception, generation lifecycle Hooks, TTS, and structured `tavo.input.send()` results. Those are prior-version `mcp-runtime` evidence; schema/document visibility is not current Android semantic proof.

## Runtime Principles

- Reread connectivity, version, endpoint, and token state for every live run.
- Prefer read/list before write and dry-run before actual write where exposed.
- Treat runtime docs as point-in-time evidence for the connected app version.
- Preserve stable IDs/revisions and read back every actual write.
- Keep visual, persistence, audio, import, and semantic proof separate.
- Restore the exact user chat/input/API/theme/voice/plugin state after isolated writes.

## Evidence Layout

Use a unique case directory:

```text
artifacts/tavo-validation/YYYYMMDD-<case>/
  run-manifest.json
  device.txt
  package.txt
  mcp_surface.json
  mcp-requests-redacted.jsonl
  mcp-responses-redacted.jsonl
  ui-before.xml
  ui-after.xml
  screen-before.png
  screen-after.png
  readback.json
  restoration.json
  notes.md
```

Record app/device version, current chat, tool names, retained test object IDs, restore actions, and final evidence tier. Keep bearer tokens, API keys, backup contents, and unredacted provider bodies out of the Skill and repository.
