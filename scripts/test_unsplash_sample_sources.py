#!/usr/bin/env python3
"""Selection tests for Unsplash documentation-sample sources. No network."""
import unittest

import unsplash_sample_sources as unsplash


class SelectTests(unittest.TestCase):
    def test_eight_distinct_ids_and_categories(self):
        rows = unsplash.select(224)
        self.assertEqual([row["sample"] for row in rows], list(range(5, 13)))
        self.assertEqual(len({row["id"] for row in rows}), 8)
        self.assertEqual([row["category"] for row in rows], list(unsplash.CATEGORIES))
        self.assertEqual([row["size"] for row in rows[:4]], ["1536x864"] * 4)
        self.assertEqual([row["size"] for row in rows[4:]], ["1152x1536"] * 4)

    def test_rotation_differs_by_panel(self):
        a = tuple(row["id"] for row in unsplash.select(224))
        b = tuple(row["id"] for row in unsplash.select(225))
        self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()
