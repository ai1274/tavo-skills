# Card Package Schema

This is the interchange shape, not the external MCP schema or proof of an importer. [TavoJS declarations](https://docs.tavoai.dev/cn/guides/javascript-api/) describe CCv2/CCv3, raw data and SillyTavern wrappers; do not silently move native `placements` or other MCP-only keys into a card extension.

## Character card envelope

Prefer this envelope for new cards:

```json
{
  "spec": "chara_card_v3",
  "spec_version": "3.0",
  "data": {
    "name": "",
    "description": "",
    "personality": "",
    "scenario": "",
    "first_mes": "",
    "mes_example": "",
    "creator_notes": "",
    "system_prompt": "",
    "post_history_instructions": "",
    "alternate_greetings": [],
    "tags": [],
    "creator": "",
    "character_version": "",
    "extensions": {}
  }
}
```

Keep `data.extensions` as an object even when empty. `alternate_greetings` and `tags` are arrays. Use `chara_card_v2` / `2.0` only for a stated compatibility target.

## Embedded worldbook

An embedded book lives at `data.character_book` and uses an `entries` array. A practical entry contains:

```json
{
  "id": 0,
  "name": "Entry name",
  "comment": "Human-facing memo",
  "keys": ["trigger"],
  "content": "A complete statement that stands alone.",
  "enabled": true,
  "constant": false,
  "insertion_order": 100,
  "position": "after_char",
  "extensions": {}
}
```

Do not assume `name`, `comment`, or `keys` are injected into the prompt. Put all model-facing meaning in `content`. When editing an existing card, retain extension fields even if the local template omits them.

## Regex entries

The common card-attached shape is `data.extensions.regex_scripts`, an array of entries such as:

```json
{
  "id": "stable-id",
  "scriptName": "field-render",
  "findRegex": "<field>([^<]+)</field>",
  "replaceString": "<span class=\"field\">$1</span>",
  "trimStrings": [],
  "placement": [2],
  "disabled": false,
  "markdownOnly": true,
  "promptOnly": false,
  "runOnEdit": false,
  "substituteRegex": 0,
  "minDepth": null,
  "maxDepth": null
}
```

Field names and runtime support are host/version dependent. Preserve unknown fields from an existing artifact and label import/runtime claims as unverified until the target Tavo channel confirms them. A regex entry is a transform contract, not permission to execute arbitrary code.

## Standalone worldbook conversion

Standalone SillyTavern-style worldbooks may use an `entries` object keyed by UID, while embedded cards use an array. Do not copy one shape into the other by hand when the repository provides `worldbook_to_character_book.mjs`; inspect the converter's input/output and use it for conversion.
