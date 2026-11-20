# Plugins And TPG

This reference covers current Tavo plugin packaging, runtime entry points, Hooks, settings, TTS, and validation boundaries.

## Evidence Snapshot

- Official pages: `https://docs.tavoai.dev/cn/guides/plugins/`, `https://docs.tavoai.dev/cn/guides/plugin-development/`, and the tutorial `https://docs.tavoai.dev/cn/guides/plugin-development-guide/`.
- `official-current`: 14-page Chinese corpus under `references/official-current/`, refreshed `2026-09-23` from `llms-full.txt`. Start there for Manifest v2, `lastMessageActions`, chat-page insets, and `fileProcessors`. The plugin-development-guide page is an MCP+Agent first-plugin tutorial, not this repository's Memory Steward workflow. The 2026-09-23 plugin-development page no longer declares a shared 55-second `generation:prepare` host budget.
- `mcp-runtime`: Tavo `1.6.0` read-only snapshot in `$tavo-1-0-beta-skill` `references/35-tavo-160-mcp-evidence.md`. The plugin capability table remains `references/33-tavo-132-plugin-compatibility.md` because `tavo://docs/plugins/compatibility` is byte-identical to the 1.3.2 body.
- `prior-version/live-verified`: retained 0.92 atomic summary `assets/evidence/0.92.0/20260717-live-matrix.json`. Entry-only, legacy, dual-entry precedence, config reads, input Hooks, generation prepare/success, structured input send, positive package variants, update preservation, and Backup B restoration have bounded 0.92 proof. Notification, generation-source, and TTS cases remain mixed.

Plugins are `.tpg` zip packages available since v0.91.0. Use a plugin when behavior should be reusable across characters or chats; use ordinary character/message TavoJS when behavior belongs to one card.

For new TPGs use `specVersion: 2` and check [the current plugin chapter](https://docs.tavoai.dev/cn/guides/plugin-development/) for root entry and localization. Omitted or `specVersion: 1` is compatibility only, without spec-2 package i18n. The target project owns its source paths and packaging; the 0.92 behavior below is historical.

## Current Package Shape

Use this layout for new plugins:

```text
my-plugin/
  manifest.json
  entry.js
  locales/en.json
  locales/zh-CN.json
  ui/panel.html
  cover.png
```

- `manifest.json` is the package manifest and must be at the plugin root.
- `entry` is the current main JavaScript entry, normally root `entry.js`.
- `entry` is required when `contributes.inputActions`, `contributes.sidebar`, or `contributes.lastMessageActions` is declared. It is also valid for a hook-only plugin with no UI contribution.
- A fragment/settings-only plugin may omit `entry` when it executes no plugin-level JavaScript.
- Legacy `scripts.actions` remains a platform compatibility alias. If both are present, current official and MCP docs declare that `entry` wins. Do not use `scripts.actions` for Memory Steward.
- `.tpg` is zip-based. The current MCP runtime doc also declares `.zip` accepted for development/import flows.

The official page says the manifest must be at package root. The current MCP runtime additionally declares a wrapper-folder import rule: a root manifest wins; otherwise exactly one nested manifest candidate is accepted and its parent becomes the plugin root; multiple nested candidates are rejected as ambiguous. The 0.92 phone matrix roundtripped a root `.tpg`, one-wrapper archive, and development `.zip`. Multiple-manifest ambiguity remains offline-validator/runtime-contract evidence rather than a live install claim.

## Manifest And Path Rules

Required root fields for Manifest v2:

- `id`: stable lowercased plugin id using letters/digits and `.`, `_`, or `-` separators.
- `name`: display string or exact `{ "$t": "key" }`.
- `version`: valid SemVer such as `1.0.0`.
- `specVersion`: `2` for new plugins.
- `author`: required non-localized 1–32 grapheme single line.
- `description`: required; may be localized Markdown.
- `localization`: required `defaultLocale`; optional `resources` maps hyphenated locale tags to package-relative UTF-8 JSON catalogs.

Common optional fields:

- `entry`: package-relative entry script.
- `cover`, `releaseNotes`.
- `minAppVersion`: optional valid SemVer for v2, compared before install. Set it to the highest `since` among used capabilities with `affectsMinimum=true` from `$tavo-1-0-beta-skill` `references/33-tavo-132-plugin-compatibility.md`. Do not default it to the current Tavo version.
- `permissions`: declarative capability names such as `input`, `message`, `generate`, `variable`, `file`, `network`, and `tts`.
- `contributes`: settings, input actions, sidebar actions, last-message actions, and HTML fragments.

Omitted or explicit `specVersion: 1` remains a platform compatibility path: `version`/`minAppVersion` stay non-empty strings and the minimum-app gate is not applied. Do not use that path for new TPG development.

Resource paths are virtual paths relative to the selected plugin root:

- use `/` on every platform;
- reject absolute paths, Windows backslashes, URLs, and `..` traversal;
- require the declared `entry` and fragment sources to exist and decode correctly;
- do not assume files outside the selected plugin root are installed;
- do not assume symlinks that resolve outside the package are safe.

Absolute paths, traversal, backslashes, missing entry files, external symlinks, and multiple-manifest ambiguity all belong in the negative fixture set. Only the first three plus missing entry are stated by current official prose; wrapper ambiguity and zip-entry safety are `mcp-runtime`; external-symlink behavior remains `needs-live-verify`.

## Entry Runtime And Config

Plugin code should use the unqualified lexical `tavo` binding in `entry`, `/chat` fragments, and `/messages` fragments. Do not use `window.tavo` or `globalThis.tavo` as the plugin-scoped contract.

`tavo.plugin.config` is synchronous and read-only:

```js
const enabled = tavo.plugin.config.get('enabled')
const config = tavo.plugin.config.all()
```

- `get(key)` returns the saved value, falling back to the schema `default`; it returns `null` when neither exists.
- `all()` returns a shallow copy of effective values, including defaults and user overrides.
- Mutating the returned object does not save or change plugin configuration.
- The API does not expose the raw schema and has no runtime write method; users edit values through Tavo's plugin settings page.
- The binding is scoped to the current plugin and is available in entry/action/fragment contexts.

The 0.92 config fixture live-verified default merging, a saved override, effective `all()` values, and non-persistence after mutating the returned copy. This does not add a runtime write API; settings still persist through Tavo's settings/MCP configuration surface.

## Contributions

Current contribution types:

- `contributes.inputActions`: native actions in the input `+` menu (`since` 0.91.0).
- `contributes.sidebar`: native actions grouped in the right sidebar (`since` 0.91.0).
- `contributes.lastMessageActions`: action-bar actions on the absolute last stable chat message (`since` 1.3.0). Advanced Rendering only. Handler receives `{ chatId, messageId, role }` and never message text; `tavo.message.current()` is `null` in that entry handler.
- `contributes.htmlFragments`: local UTF-8 HTML mounted in chat/message locations (`since` 0.91.0).
- `contributes.settings.schema`: a flat settings form with `switch`, `select`, `slider`, `text`, `textarea`, `info`, `divider`, and `break` elements.

Documented fragment mounts include `/chat`, `/chat/head/start`, `/chat/head/end`, `/chat/body/start`, `/chat/body/end`, `/messages/start`, `/messages/end`, and role/position filters for message mounts.

Use `tavo.plugin.onInputAction(id, handler)`, `onSidebarAction(id, handler)`, and `onLastMessageAction(id, handler)` for new actions. Lower-level `plugin.on('inputActions:<id>'|'sidebar:<id>'|'lastMessageActions:<id>', handler)` forms remain supported. IDs must match the manifest exactly.

Chat-page `/chat` fragments and chat-page entry/action code may use `--tavo-inset-*` CSS variables and `tavo.ui.getInsets()` / `onInsetsChanged`. `/messages` fragments do not. See `references/official-current/plugin-development.md`. `tavo.message.variant` is plugin/TavoJS runtime (`since` 1.3.0), not MCP or native model Tool Calling.

## Chat And Message Notification Hooks

An installed plugin `entry` can register current-chat notifications with `tavo.plugin.on(type, handler)`:

- `chat:opened`, `chat:closed`, `chat:updated`;
- `chat:changed` is a compatibility alias for `chat:updated`, and handlers receive `event.type === 'chat:updated'`;
- `message:added`, `message:updated`, `message:deleted`;
- `message:changed` fires after the specific message event.

Current contract details:

- events contain `type`, `pluginId`, ISO `at`, and the relevant `chatId` plus lightweight `chat`/`message` data;
- `message:added` is for a persistent message, not loading, transient draft, or streaming-token intermediate state;
- a failing handler does not block other plugin handlers or chat operation;
- events are not queued while the runtime is unloaded; a late registration receives one catch-up `chat:opened` when a chat is already open.

The 0.92 F05 case is `mixed`: observed chat-open field shape, specific message event before `message:changed`, one persistent assistant add after streaming, and handler isolation all passed. A controlled chat update did not deliver `chat:updated` to a `chat:changed` compatibility handler. Do not claim the alias or the whole notification family as reliable on this build.

## Input Send Hooks

Only plugin `entry` scripts register `input:beforeSend` and `input:afterSend`. Declare `permissions: ["input"]` as author intent.

`input:beforeSend` intercepts all three documented sources:

- native send button/return key (`source: ui`);
- `tavo.input.send()` (`source: tavojs`);
- MCP `tavo_input_send` (`source: mcp`).

The handler runs before macros and slash-command parsing. `type`, `pluginId`, `chatId`, `source`, and `at` are read-only; `text` is the only mutable field and must remain a string. Return values are ignored; cancellation must call `event.cancel(reason?)`.

Handlers run serially in stable plugin/registration order with a five-second limit. A throw, timeout, or non-string draft rolls back only that handler and fails open. Explicit cancellation stops later handlers, retains the latest committed text and attachments, and does not add another toast. `input:afterSend` is a non-blocking notification after accepted/trimmed input and does not wait for generation.

The Hooks require the current chat Advanced Rendering WebView runtime. If unavailable, current runtime docs say they are bypassed without queueing or blocking the send. The 0.92 matrix observed all three sources, committed rewrite, explicit cancellation with input retained, handler-local fail-open for throw/non-string/timeout, and `afterSend` acceptance timing. Attachment preservation was not exposed and is not a passed assertion.

## Generation Lifecycle Hooks

Only installed plugin `entry` scripts can register these Hooks; HTML fragments and pure character/message TavoJS cannot. Declare `permissions: ["generate"]`.

- `generation:prepare`: serial interceptor before request construction. Mutable `event.text` is only the latest user text for the transient model request; it may be empty and does not alter the saved user message.
- `generation:success`: serial interceptor after generation/extensions and before character-message save. Mutable final text must remain non-empty; empty output is discarded.
- `generation:error`: non-blocking terminal notification with sanitized `error.code` and `error.message` only.
- `generation:cancelled`: non-blocking terminal notification with boolean `partial`; `true` saves the partial character message then emits `message:added`, while `false` saves no message.

Supported `source` values are `reply`, `groupReply`, `continuation`, `othersContinuation`, and `regeneration`. Image, speech, summary, independent, and pure TavoJS/JSAPI generation paths are excluded by current docs.

The 2026-09-23 official page says prepare handlers run in registration order with no host timeout, while each success handler still waits at most five seconds. Older runtime evidence recorded a five-second limit for both. Throws, timeouts, invalid text, and empty success text fail open for that handler only. They cannot cancel generation. The 0.92 provider-fixture matrix live-verified transient prepare rewrite without changing the saved user message, steady multi-plugin order, success-before-save mutation, fail-open empty/throw/timeout, sanitized errors, partial/empty cancellation persistence, and one terminal event. Source behavior is `mixed`: reply, regeneration, and continuation were observed, while the controlled `othersContinuation` path emitted neither the Hook nor a persisted message; auxiliary-path exclusion stayed blocked.

## Plugin TTS

Plugin runtime exposes `tavo.tts.play(text, options)` and `tavo.tts.stop()`:

- declare `permissions: ["tts"]`;
- plugin code must explicitly pass exactly one character or persona id/object in `voice`;
- `queue` and `applyPlaybackRules` default to `false`;
- `stop()` stops the current chat's shared TTS queue, including UI, ordinary TavoJS, and other-plugin work.

The API shape is `official-current`/`mcp-runtime`. With a deterministic OpenAI-compatible provider and a working character binding, one character call and two queued calls were accepted and produced speech requests; missing voice and dual character+persona selection were rejected. Persona acceptance was not retested with a working binding. Speaker correctness, audio quality, and audible queue clearing require human listening and must not be marked passed from UI or gateway state alone.

## Advanced Rendering Boundary

- Plugin entry/actions/fragments require the current chat Advanced Rendering WebView runtime.
- Installed fragment code is separate from the JavaScript mode for character cards/model-output bubbles; that mode does not disable enabled plugin code.
- `/messages` fragments have current-message context; entry, native actions, sidebar actions, and `/chat` fragments do not.
- Current MCP docs describe `permissions` as author-intent declarations, not enforced runtime gates. That is a runtime-doc contract, not permission-bypass approval.

## Prior-Version Live Evidence

Retained Tavo `0.91.0` artifacts prove the older package/install/action/fragment route and are useful regression controls:

- `artifacts/tavo-validation/20260710-plugin-package-install/`
- `artifacts/tavo-validation/20260710-plugin-ui-action/`
- `artifacts/tavo-validation/20260710-203300-semantic-model-kpi-v23/model-calls/plugin-action-panel/`
- `artifacts/tavo-validation/20260711-020000-cross-feature-matrix-v11-partial-34-35/model-calls/plugin-tavojs-lorebook/`

They do not substitute for the retained 0.92 evidence. Use `assets/evidence/0.92.0/20260717-live-matrix.json` only for version-scoped entry/config/Hook/TTS/package/update/backup claims, and keep every mixed or manual boundary in that asset.

## 0.92 Live Findings And Remaining Queue

The 2026-07-17 run completed the core F01-F11 matrix, positive root/wrapper/zip imports, same-id update preservation, and a native Backup B uninstall/restore roundtrip. Use only atomic assertions from the retained summary; F05, F09, and F11 remain mixed.

Remaining discriminating work:

1. retest `chat:changed` alias delivery without conflating runtime reload/catch-up;
2. isolate `othersContinuation` and the declared auxiliary-path exclusions;
3. test persona TTS with a working binding and perform human listening for identity, quality, and queue stop;
4. keep ambiguous/missing/backslash/symlink negative packages offline unless a separately authorized live rejection test is necessary;
5. rerun current gate and exact user-state restoration after future app/runtime changes.

## Validation Tooling

- `scripts/test_validate_tpg_package.py` runs the offline 0.92 package/fixture compatibility matrix for entry, legacy fallback, dual-entry precedence, hook-only packages, wrapper roots, ambiguity, unsafe paths, missing files, and external symlinks.
- `scripts/tavo_generation_hook_fixture.py` is a deterministic LAN OpenAI-compatible endpoint for JSON, SSE, slow-stream, HTTP 500, and malformed-protocol generation cases. It allowlists clients and writes redacted mode-0600 captures under a mode-0700 directory.
- `scripts/test_tavo_generation_hook_fixture.py` verifies that fixture's auth, allowlist, JSON/SSE/fault modes, secret-file handling, and nested credential redaction offline.
