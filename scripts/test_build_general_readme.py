#!/usr/bin/env python3
"""Tests for build_general_readme: kept sections survive a rerun and the roster folds every style."""
import unittest
from pathlib import Path

import build_general_readme as g

ROOT = Path(__file__).resolve().parents[2]


@unittest.skipUnless(len(g.soldiers(ROOT)) > 3, 'family checkout without Soldier profiles')
class GeneralTests(unittest.TestCase):
    def test_idempotent_and_keeps_ads_and_license(self):
        entries = g.soldiers(ROOT)
        for lang, name in g.sb.FILES.items():
            old = (g.ALL / name).read_text()
            new = g.render(lang, entries, old)
            self.assertEqual(g.render(lang, entries, new), new)
            ads, lic = g.kept_sections(old, lang)
            self.assertIn(ads, new)
            self.assertLess(new.index(g.ADS_END), new.index(lic.splitlines()[0]))
            self.assertEqual(new.count('<img src="./assets/roster/'), len(entries) + 3)


if __name__ == '__main__':
    unittest.main()
