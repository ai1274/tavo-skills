#!/usr/bin/env python3
"""Offline ranking and source-location regressions for the global Tavo skill."""

import os
import tempfile
import unittest
from pathlib import Path

from search_official_docs import CORPUS as DEFAULT_CORPUS, find_sections, read_sections, result


CORPUS = Path(os.environ.get("TAVO_DOCS_CORPUS", str(DEFAULT_CORPUS))).resolve()

CASES = (
    ("记忆", "javascript-api", "🧠 记忆"),
    ("世界书", "lore-book", "📖 世界书"),
    ("minAppVersion", "plugin-development", "版本与 App 兼容性"),
    ("textarea minLines", "plugin-development", "设置 Schema"),
    ("tavo.memory.getShortTermLength()", "javascript-api", "获取短记忆长度"),
    ("短记忆长度", "javascript-api", "获取短记忆长度"),
    ("字段 隐藏 保留", "plugin-development", "条件显示"),
    ("自动提取 10条", "long-memory", "手动提取与10条后自动提取的区别"),
    ("世界书 编写", "lore-book", "世界书的构成与编写指南"),
    ("HTML 语言 完整重渲染", "plugin-development", "插件 HTML 与 JavaScript 国际化"),
    ("resources/templates/list initialize", "mcp-server", "连接后如何使用"),
    ("哪些脚本可以注册生成生命周期", "plugin-development", "生成生命周期 Hooks"),
    ("可见行数上下限", "plugin-development", "设置 Schema"),
    ("渲染键盘避让", "plugin-development", "布局边界与键盘避让"),
)
NEGATIVES = ("量子烤鸭", "textarea 火星烹饪许可证", "tavo.memory.getShortTermLengthTypo()", "!? ")
HEADER = (
    "官方来源：https://docs.tavoai.dev/cn/guides/sample/\n"
    "同步日期：2026-11-18\n证据级别：official-current\n证据边界：测试夹具\n\n"
)


class SearchOfficialDocsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sections = read_sections(CORPUS) if CORPUS.is_dir() else None

    def require_corpus(self):
        if self.sections is None:
            self.skipTest("set TAVO_DOCS_CORPUS to run corpus-dependent tests")

    def test_expected_section_in_top_three(self):
        self.require_corpus()
        for query, page, heading in CASES:
            with self.subTest(query=query):
                hits = find_sections(self.sections, query, 3)
                self.assertTrue(any(s.path.stem == page and heading in s.headings[-1] for s, _ in hits))

    def test_no_match_for_unrelated_or_misspelled_queries(self):
        self.require_corpus()
        for query in NEGATIVES:
            with self.subTest(query=query):
                self.assertEqual(find_sections(self.sections, query, 3), [])

    def test_exact_api_and_snippet_point_to_original_lines(self):
        self.require_corpus()
        query = "tavo.memory.getShortTermLength()"
        section, match = find_sections(self.sections, query, 1)[0]
        row = result(section, match, query)
        path = Path(row["path"])
        original = path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(path.parent, CORPUS)
        self.assertEqual(row["match"], "exact")
        self.assertIn("获取短记忆长度", original[row["startLine"] - 1])
        self.assertIn(query, original[row["snippetLine"] - 1])
        self.assertLessEqual(row["startLine"], row["snippetLine"])
        self.assertLessEqual(row["snippetLine"], row["endLine"])
        self.assertEqual(original[0], "官方来源：" + row["source"])
        self.assertEqual(original[1], "同步日期：" + row["synced"])

    def test_fenced_headings_stay_in_the_containing_section(self):
        text = HEADER + "# 样例 [#样例]\n\n## 用法\n````sh\n```\n# 示例命令\n````\n\n## 后续\n尾声\n"
        with tempfile.TemporaryDirectory() as scratch:
            corpus = Path(scratch)
            (corpus / "sample.md").write_text(text, encoding="utf-8")
            sections = read_sections(corpus)
            self.assertEqual([s.headings for s in sections], [("样例",), ("样例", "用法"), ("样例", "后续")])
            hit, _ = find_sections(sections, "示例命令", 1)[0]
            self.assertEqual(hit.start, 8)

    def test_missing_provenance_fails_closed(self):
        with tempfile.TemporaryDirectory() as scratch:
            corpus = Path(scratch)
            (corpus / "stray.md").write_text("# 不是官方快照\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing official-current provenance"):
                read_sections(corpus)


if __name__ == "__main__":
    unittest.main()
