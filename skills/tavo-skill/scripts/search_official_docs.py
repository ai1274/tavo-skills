#!/usr/bin/env python3
"""Search the locally installed Tavo official Markdown by section."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit


CORPUS = Path(__file__).resolve().parents[1] / "references" / "official-current"
TOKEN = re.compile(r"(?P<han>[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]+)|[a-z0-9_$]+(?:[./:-][a-z0-9_$]+)*")
HEADING = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.+?)(?:[ \t]+#+)?[ \t]*$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


@dataclass
class Section:
    path: Path
    source: str
    synced: str
    headings: tuple[str, ...]
    start: int
    lines: list[str]


def lexemes(text):
    return [m.group() for m in TOKEN.finditer(text.casefold())]


def search_terms(text):
    for m in TOKEN.finditer(text.casefold()):
        word = m.group()
        if m.lastgroup == "han" and len(word) > 1:
            yield from (word[i:i + 2] for i in range(len(word) - 1))
        else:
            yield word


def read_sections(corpus):
    corpus = corpus.resolve(strict=True)
    sections = []
    for path in sorted(corpus.glob("*.md")):
        if path.resolve().parent != corpus:
            raise ValueError(f"snapshot resolves outside the corpus: {path.name}")
        lines = path.read_text(encoding="utf-8-sig").splitlines()
        prefixes = ("官方来源：", "同步日期：", "证据级别：official-current", "证据边界：")
        if len(lines) < 5 or lines[2] != prefixes[2] or not all(line.startswith(prefix) for line, prefix in zip(lines, prefixes)):
            raise ValueError(f"missing official-current provenance: {path.name}")
        source = lines[0].removeprefix(prefixes[0]).strip()
        synced = lines[1].removeprefix(prefixes[1]).strip()
        url = urlsplit(source)
        if url.scheme != "https" or url.netloc != "docs.tavoai.dev" or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", synced):
            raise ValueError(f"invalid snapshot source or date: {path.name}")

        # shortcut: only ATX headings and fenced code; extend if official exports change format.
        starts, hierarchy, fence = [], [], ""
        for index, line in enumerate(lines[4:], 4):
            marker = FENCE.match(line)
            if fence:
                if marker and marker[1].startswith(fence) and not marker[2].strip():
                    fence = ""
                continue
            if marker:
                fence = marker[1]
                continue
            heading = HEADING.match(line)
            if heading:
                level, title = len(heading[1]), re.sub(r"\s+\[#[^\]]+\]$", "", heading[2])
                while hierarchy and hierarchy[-1][0] >= level:
                    hierarchy.pop()
                hierarchy.append((level, title))
                starts.append((index, tuple(name for _, name in hierarchy)))
        first_heading = starts[0][0] if starts else len(lines)
        if any(line.strip() for line in lines[4:first_heading]):
            starts.insert(0, (4, (path.stem,)))
        for (start, headings), (end, _) in zip(starts, starts[1:] + [(len(lines), ())]):
            while end > start + 1 and not lines[end - 1].strip():
                end -= 1
            sections.append(Section(path, source, synced, headings, start + 1, lines[start:end]))
    if not sections:
        raise ValueError("no sections in the official-current corpus")
    return sections


def find_sections(sections, query, limit):
    query = " ".join(query.casefold().split())
    words = lexemes(query)
    if not words:
        return []
    identifiers = {word for word in words if word.isascii()}
    han_words = set(words) - identifiers
    wanted = set(search_terms(query))
    han_terms = wanted - identifiers
    rows = []
    df = Counter()
    for section in sections:
        body = "\n".join(section.lines).casefold()
        freqs = Counter(search_terms(body))
        df.update(freqs.keys() & wanted)
        rows.append((section, body, freqs, sum(freqs.values())))
    mean = sum(row[-1] for row in rows) / len(rows) or 1
    idf = {word: math.log1p((len(rows) - count + 0.5) / (count + 0.5)) for word, count in df.items()}

    ranked = []
    for section, body, freqs, length in rows:
        if not identifiers <= freqs.keys():
            continue
        title = section.headings[-1].casefold()
        literal_han = {word for word in han_words if word in body}
        hits = freqs.keys() & wanted
        # Avoid weak Chinese results from one incidental bigram in a longer query.
        if literal_han != han_words:
            needed = max(min(2, len(han_terms)), (len(han_terms) + 1) // 2)
            if len(hits & han_terms) < needed:
                continue
        phrase = query in " ".join(body.split())
        title_hits = hits & set(search_terms(title))
        norm = 1.2 * (0.25 + 0.75 * length / mean)
        bm25 = sum(idf[word] * freqs[word] * 2.2 / (freqs[word] + norm) for word in sorted(hits))
        title_bonus = 0.75 * sum(idf[word] for word in sorted(title_hits))
        rank = (lexemes(title) == words, query in title, phrase, len(literal_han), bm25 + title_bonus)
        match = "exact" if phrase else "keywords" if literal_han == han_words else "partial"
        ranked.append((rank, section, match))
    ranked.sort(key=lambda row: row[0], reverse=True)
    return [(section, match) for _, section, match in ranked[:limit]]


def result(section, match, query):
    phrase = " ".join(query.casefold().split())
    words = set(lexemes(query))
    wanted = set(search_terms(query))

    def line_score(item):
        index, line = item
        text = line.casefold()
        terms = set(lexemes(text))
        literals = {word for word in words if word in terms or (not word.isascii() and word in text)}
        return phrase in " ".join(text.split()), len(literals), len(wanted & set(search_terms(text))), index != 0

    offset, line = max(enumerate(section.lines), key=line_score)
    line = " ".join(line.split())
    if len(line) > 220:
        anchor = line.casefold().find(phrase)
        if anchor < 0:
            anchor = min((i for word in words | wanted if (i := line.casefold().find(word)) >= 0), default=0)
        start = max(0, anchor - 55)
        line = ("…" if start else "") + line[start:start + 218] + ("…" if start + 218 < len(line) else "")
    return {
        "path": str(section.path), "startLine": section.start,
        "endLine": section.start + len(section.lines) - 1, "headings": section.headings,
        "snippetLine": section.start + offset, "snippet": line, "match": match,
        "source": section.source, "synced": section.synced,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="short keywords or an exact API/field name")
    parser.add_argument("--corpus", type=Path, default=CORPUS, help="local official Markdown corpus")
    parser.add_argument("--limit", type=int, default=3, metavar="N", help="1–10 results (default 3)")
    args = parser.parse_args()
    if not (1 <= args.limit <= 10 and len(args.query) <= 300 and lexemes(args.query)):
        parser.error("query must contain searchable text (max 300 characters); limit must be 1–10")
    try:
        sections = read_sections(args.corpus)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"cannot read Tavo official snapshots: {exc}\n")
    results = [result(section, match, args.query) for section, match in find_sections(sections, args.query, args.limit)]
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps({"evidenceTier": "official-current", "results": results}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
