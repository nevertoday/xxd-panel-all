#!/usr/bin/env python3
"""Tests for build_soldier_readme: sample grouping, idempotence, ads, Arabic RTL and profile checks."""
import json
import shutil
import struct
import tempfile
import unittest
import zlib
from pathlib import Path

import build_soldier_readme as b

EXAMPLE = json.loads((Path(__file__).resolve().parents[2] / 'xxd-panel-001/references/readme-profile.json').read_text()) \
    if (Path(__file__).resolve().parents[2] / 'xxd-panel-001/references/readme-profile.json').is_file() else None


def png(path: Path, w: int, h: int) -> None:
    ihdr = struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0)
    chunk = struct.pack('>I', len(ihdr)) + b'IHDR' + ihdr + struct.pack('>I', zlib.crc32(b'IHDR' + ihdr))
    path.write_bytes(b'\x89PNG\r\n\x1a\n' + chunk)


def profile(nnn: int) -> dict:
    lang = {'name': 'Name', 'tagline': 'Tagline.', 'look': 'Look.', 'traits': ['a', 'b', 'c'],
            'good': ['g1', 'g2'], 'poor': ['p1', 'p2']}
    return {'skill_description': f'XXD Panel {nnn:03d}｜Name: ' + 'x' * 200 + f' xxd-panel-{nnn:03d}.',
            'short_description': '名：说明', **{k: dict(lang) for k in b.FILES}}


class RenderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.d = self.tmp / 'xxd-panel-007'
        ex = self.d / 'assets' / 'examples'
        ex.mkdir(parents=True)
        (self.d / 'references' / 'original-prompt').mkdir(parents=True)
        png(ex / 'sample-01.png', 1152, 1536)
        png(ex / 'sample-02.png', 1536, 864)
        for lang, name in b.FILES.items():
            (self.d / name).write_text(
                '<img src="./assets/examples/sample-01.png" alt="x"><br><sub>01 · Cat</sub>\n'
                f'## {b.T[lang]["license"]}\n\nLicense text.\n')

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_groups_captions_and_idempotence(self):
        p = profile(7)
        for lang, name in b.FILES.items():
            old = (self.d / name).read_text()
            new = b.render(self.d, lang, p, old)
            self.assertIn('<sub>01 · Cat</sub>', new)
            self.assertIn('sample-02.png', new)
            self.assertTrue(new.rstrip().endswith('</div>') if lang == 'ar' else new.rstrip().endswith('License text.'))
            self.assertEqual(b.render(self.d, lang, p, new), new)
            ads = (b.ADS / name).read_text().strip()
            self.assertIn(ads, new)
            self.assertLess(new.index(ads), new.index('## ' + b.T[lang]['license']))

    def test_validate(self):
        self.assertEqual(b.validate(profile(7), 7), [])
        bad = profile(7)
        bad['en']['look'] = 'The REALITY VIEW stays | here'
        errs = b.validate(bad, 7)
        self.assertTrue(any('jargon' in e for e in errs) and any('"|"' in e for e in errs))

    @unittest.skipIf(EXAMPLE is None, 'family checkout without xxd-panel-001')
    def test_reference_example_valid(self):
        self.assertEqual(b.validate(EXAMPLE, 1), [])


if __name__ == '__main__':
    unittest.main()
