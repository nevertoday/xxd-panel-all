import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import brief_intake as bi

STUB = '''
def validate(text, subjects=None):
    out = ["第 2 段不是 references/shell.md 的原文 → 运行 scripts/finalize.py 自动补外壳"]
    if "编号" in text:
        out.append("文字段有编号或图号却没写每张另起")
    return out

def warnings(text):
    return []
'''


class BriefIntakeTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "dna/scripts").mkdir(parents=True)
        (self.tmp / "dna/scripts/validate_dna.py").write_text(STUB, encoding="utf-8")

    def run_cli(self, body, *extra):
        brief = self.tmp / "brief.md"
        brief.write_text(body, encoding="utf-8")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = bi.main([str(brief), "--dna", str(self.tmp / "dna"), *extra])
        return rc, buf.getvalue()

    def test_old_shell_is_a_note_not_a_failure(self):
        rc, out = self.run_cli(bi.DNA_OPENING + "，不多不少。\n\n正文。")
        self.assertEqual(rc, 0)
        self.assertIn("NOTE", out)
        self.assertNotIn("FAIL", out)

    def test_failures_are_advisory_unless_strict(self):
        body = "# Original XXD Panel 355 style brief\n\n" + bi.DNA_OPENING + "。\n\n编号写在角落。"
        rc, out = self.run_cli(body)
        self.assertEqual(rc, 0)
        self.assertIn("FAIL 文字段有编号", out)
        rc, _ = self.run_cli(body, "--strict")
        self.assertEqual(rc, 1)

    def test_other_formats_are_skipped(self):
        rc, out = self.run_cli("请基于我上传的每一张摄影作品，分别制作一张海报。")
        self.assertEqual(rc, 0)
        self.assertIn("SKIP", out)


if __name__ == "__main__":
    unittest.main()
