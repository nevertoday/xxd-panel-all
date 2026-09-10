#!/usr/bin/env python3
"""Smoke tests for soldier_runtime overlay filtering and contamination checks."""
from pathlib import Path
import tempfile
import unittest

import soldier_runtime as sr


class OverlayTests(unittest.TestCase):
    def test_junk_bullets_dropped(self):
        text = """---
name: xxd-panel-001
description: "x"
---
## Acceptance gate

Inspect every final PNG at full size and thumbnail size. Accept only when:

- it is a fresh result from the correct current source or theme;
- `top-bottom` reads as two primary horizontal parts, leaving their exact proportions to the image model;

When a result fails, retry only the failed source-brief or runtime requirement.
"""
        self.assertEqual(sr.extract_style_overlay(text), '')

    def test_style_paragraph_kept(self):
        text = """## Output and acceptance

Recompose the core subject into a small circular souvenir stamp. Avoid smooth vectors.

Write final PNGs directly inside one fresh task directory.
"""
        self.assertIn('circular souvenir stamp', sr.extract_style_overlay(text))

    def test_overlay_markdown_merges(self):
        extracted = 'Keep the stamp English headline.\n\n- it is a fresh result'
        out = sr.overlay_markdown(180, extracted)
        self.assertIn('prohibits left-right layout', out)
        self.assertIn('Keep the stamp English headline.', out)
        self.assertNotIn('- it is a fresh result', out)


class ContaminationTests(unittest.TestCase):
    def test_canonical_imagegen_ok_for_panel_100(self):
        path = sr.CANON / sr.IMAGEGEN_NAME
        self.assertEqual(sr.check_contamination(path, 100), [])

    def test_canonical_compose_ok_for_panel_001(self):
        path = sr.CANON / sr.COMPOSE_NAME
        self.assertEqual(sr.check_contamination(path, 1), [])

    def test_flags_panel_number_in_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / sr.IMAGEGEN_NAME
            p.write_text('MAX_RESPONSE_BYTES = 105 * 1024 * 1024\n')
            fails = sr.check_contamination(p, 105)
            self.assertTrue(any('contamination' in f or '100 MiB' in f for f in fails))


if __name__ == '__main__':
    unittest.main()
