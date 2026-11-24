> Authority: Skill workflow reference
>
> This playbook owns validation procedure for artifacts produced through `$tavo-studio`. It does not establish Tavo platform capability. Current project contracts, source/tests, current engineering snapshots, discovered schemas, importer/builder behavior, and fresh live evidence remain stronger owners.

# Tavo Artifact Validation Playbook

## Start With The Claim

Write the requested observable output and the strongest claim the artifact must support:

```text
Artifact type:
Source owner:
Target importer/runtime:
Requested observable output:
Capability claims:
Generated owner:
Round-trip path:
Live handoff:
Rollback/cleanup:
```

Choose validation layers that can falsify those claims. An attractive or importable artifact is not automatically semantically correct or runtime-effective.

## Common Validation Layers

| Layer | Examples | Failure meaning |
|---|---|---|
| Syntax/parse | JSON parse, JS syntax, YAML/frontmatter | artifact cannot be consumed reliably |
| Structure/schema | manifest fields, card spec, worldbook entries, export shape | importer/tool contract mismatch |
| Semantic | IDs, relationships, placements, timing, labels, references | parses but means the wrong thing |
| Tool/builder | package, validate, convert, embed, extract | manual structure differs from owner tool |
| Round trip | import/export, embed/extract, package/readback | information lost, normalized, or rejected |
| Repository | tests, build, equality/hash, final gate | integration or generated-boundary defect |
| Live | exact version, module observation, rollback, cleanup | real environment behavior remains unproved |

## Plugin `.tpg`

```text
contract/source
→ focused tests
→ update version and release-note sources for each plugin update
→ repository release gate
→ builder-generated .tpg
→ structure/manifest inspection
→ compatibility-copy equality/hash
→ explicitly authorized live install/readback/module proof
```

Check:

- manifest identity, version, entry/actions/hooks/settings fields match current owner;
- for a plugin update, read back the packaged version and resolved `releaseNotes`. Match them to the updated sources and the retained plugin changes;
- for a new user-facing plugin or a metadata change, read the packaged manifest and any referenced locale files: verify the intended author and that the description includes the actual entry point, operating steps and relevant caveats; do not count a repository-only README;
- archive structure comes from the builder;
- generated package is not edited afterward;
- install payload uses discovered current schema;
- exact live version is reread before module claims;
- rollback and cleanup identify run-owned state.

旧全局 TPG 校验器只作局部检查：平台版不校验新版表单，版本分支版类型清单没有 `list` 或 `header`。用当前项目测试、builder 及兼容声明核对，不为通过旧校验而删合法字段，也不将通过当成完整兼容性证明。

## Project-specific build boundaries

Use the current target's documented source/build boundary. For example, `Memory Center` has its own builder (not the former Memory Steward generation chain), and Conversation Display's hand-maintained footer is not its generated panel. Check [the local architecture map](../../tavo-memory-steward-clean-workflow/references/project-architecture.md) only to locate the current owner. Test byte equality only where the owner actually declares compatibility copies; do not create mirrors just for validation.

## Character Card JSON

Check:

- JSON parse and current card spec/version fields;
- required identity/content fields and intended extensions;
- placeholders, inconsistent names, unsupported assumptions, and sensitive data;
- importer or round-trip behavior when available;
- semantic quality separately from schema validity.

Use [the card package schema](../../tavo-character-card/references/card-package-schema.md) for CCv3 and use `assets/templates/character-card.v2.minimal.json` or `.full.json` only for CCv2. Parse the extracted PNG payload, verify its actual envelope and fields, and compare meaningful data rather than relying on the package name.

## PNG Character Card

Use:

```text
scripts/embed_st_card_png.mjs
scripts/extract_st_card_png.mjs
scripts/png-card-lib.mjs
```

Check:

- source PNG validity;
- serialized card payload before embedding;
- `chara`/`ccv3` chunk presence as required by the selected format;
- extracted payload parse and semantic equality after embedding;
- no claim that arbitrary custom chunks become Tavo regex, preset, plugin, or worldbook resources.

## Worldbook / Lorebook

Check:

- JSON parse, entry identity, keys, enabled state, position/order/depth fields under the target schema;
- stable references and no duplicate/colliding IDs;
- content semantics, trigger coverage, and unintended broad activation;
- conversion output if `scripts/worldbook_to_character_book.mjs` is used;
- import/export normalization and live activation only when the environment is authorized.

## Preset / EJS / Macros / Regex

Check each layer independently:

1. outer object/export schema;
2. EJS syntax and supported helper scope;
3. macro names, expansion order, and state context;
4. regex pattern, flags/placement/timing fields, replacement shape;
5. rendered text/HTML;
6. DOMPurify/WebView/sandbox effects;
7. persistence or action behavior only through the owning API/live evidence.

Remember: EJS renders before macros; regex transformation is not JavaScript execution; HTML display is not persistence proof.

## Evidence Report

```text
Verified:
- <claim> — <owner/evidence>

Inference:
- <claim> — derived from <verified evidence>; invalidated by <counterevidence>

Unknown:
- <claim> — missing <schema/importer/live observation>

Commands and exits:
- <command> — exit <code> — <summary>

Generated/round-trip delta:
- <artifact/hash/normalization>

Live/cleanup:
- <not entered or bounded evidence>
```

Keep evidence bounded and sanitized. Do not retain credentials, private transcripts, complete model responses, or full sensitive payloads.
