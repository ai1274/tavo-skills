# Validation Checklist

Use the checks that match the requested package. Mark unsupported host behavior as `unknown`.

## Structure

- [ ] Every JSON file parses with the standard JSON parser.
- [ ] The card has a supported `spec` / `spec_version` pair for the requested compatibility target. The retained CCv2 checker is not a CCv3 validator; exercise CCv3 with matching structure checks or the authorized target importer.
- [ ] `data` is an object; `data.extensions` is an object; `tags` and `alternate_greetings` are arrays.
- [ ] `data.name` and `data.first_mes` are non-empty.
- [ ] Embedded `character_book.entries` is an array; IDs are unique; required fields have expected types.
- [ ] `regex_scripts` is an array when present; each rule has a name, pattern, replacement, and deliberate enabled/placement/timing values.
- [ ] Existing extension fields and unknown source fields were preserved unless the user explicitly requested removal.

## Content

- [ ] Durable identity and behavior facts are in description/personality/scenario, not only creator notes.
- [ ] `first_mes` demonstrates the intended voice without speaking for `{{user}}`.
- [ ] Dialogue examples use `<START>` and consistent `{{char}}` / `{{user}}` markers.
- [ ] Each worldbook `content` stands alone and does not rely on its title or keyword list.
- [ ] Constant entries are genuinely global; triggered entries have useful keys and no accidental broad matches.
- [ ] User-private facts, inactive route data, and secret character information do not leak into unrelated branches.
- [ ] Constraints do not contradict the character contract or require impossible simultaneous outputs.
- [ ] The package does not add a future timeline or force a relationship outcome without the user's request.

## Regex and rendering

- [ ] The card's output protocol names every tag a regex expects.
- [ ] All tags are paired and the multiline pattern handles the declared content shape.
- [ ] Special rules precede generic fallback rules.
- [ ] Capture-group references match the pattern's groups; full-match placeholders are used only where the target supports them.
- [ ] Display-only, prompt-only, receive, and edit-time rules are separated intentionally.
- [ ] Replacement HTML is balanced and CSS selectors are scoped to the generated markup.
- [ ] Empty, malformed, already-rendered, and multiline inputs have a defined result.
- [ ] Event handlers, remote URLs, script-like content, and clipboard behavior are explicit side effects, not accidental output.

## Delivery

- [ ] The final response names all changed artifacts and their relationship.
- [ ] Commands include working directory and exit code.
- [ ] Import, live rendering, persistence, PNG extraction, and mobile behavior are only called verified when actually tested on the target host.
- [ ] Remaining assumptions, compatibility gaps, and rollback/repair steps are stated.
