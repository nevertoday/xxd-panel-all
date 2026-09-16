"""Regression checks for the read-only sample inventory."""
import tempfile
import unittest
from pathlib import Path

from audit_sample_queue import audit


class GalleryAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.panel = self.root / 'xxd-panel-159'
        (self.panel / 'assets/examples').mkdir(parents=True)
        (self.panel / 'assets/examples/sample-05.png').write_bytes(b'test fixture')
        self.link = '![sample](assets/examples/sample-05.png)'

    def check_readme(self, content):
        (self.panel / 'README.md').write_text(content)
        return audit(self.root, 159, 159)['errors']

    def test_valid_gallery(self):
        self.assertEqual([], self.check_readme('<div>Title</div>\n' + self.link))

    def test_misplaced_gallery(self):
        errors = self.check_readme('<div>\n' + self.link + '\n</div>')
        self.assertTrue(any('misplaced' in error for error in errors))

    def test_stale_claim(self):
        errors = self.check_readme('未生成示例图片\n' + self.link)
        self.assertTrue(any('stale' in error for error in errors))

    def test_missing_image(self):
        errors = self.check_readme(self.link.replace('05.png', '06.png'))
        self.assertTrue(any('missing gallery image' in error for error in errors))

    def test_unlinked_inventory_is_not_generation_failure(self):
        self.assertEqual([], self.check_readme('No gallery yet.'))

    def test_forbidden_shared_queue(self):
        brief_dir = self.panel / 'references/original-prompt'
        brief_dir.mkdir(parents=True)
        (brief_dir / 'zh-CN.md').write_text('brief')
        queue = self.root / 'tmp/imagegen/159'
        queue.mkdir(parents=True)
        (queue / 'manifest.json').write_text(
            '[{"sample":5,"image":"/Users/admin/Downloads/陈翔海报2026-08-26/a.jpg",'
            '"size":"1536x864","prompt":"brief\\n\\noverlay"}]'
        )
        errors = audit(self.root, 159, 159)['errors']
        self.assertTrue(any('forbidden shared sample queue' in error for error in errors))


if __name__ == '__main__':
    unittest.main()
