#!/usr/bin/env python3
"""Selection tests for Unsplash documentation-sample sources. No network."""
import unittest

import unsplash_sample_sources as unsplash


class SelectTests(unittest.TestCase):
    def test_eight_distinct_ids_and_orientations(self):
        rows = unsplash.select(226)
        self.assertEqual([row["sample"] for row in rows], list(range(5, 13)))
        self.assertEqual(len({row["id"] for row in rows}), 8)
        self.assertEqual([row["orientation"] for row in rows[:4]], ["portrait"] * 4)
        self.assertEqual([row["orientation"] for row in rows[4:]], ["landscape"] * 4)
        self.assertEqual([row["size"] for row in rows[:4]], ["1536x864"] * 4)
        self.assertEqual([row["size"] for row in rows[4:]], ["1152x1536"] * 4)
        self.assertEqual(
            [row["category"] for row in rows[:4]],
            list(unsplash.PORTRAIT_CATEGORIES),
        )
        self.assertEqual(
            [row["category"] for row in rows[4:]],
            list(unsplash.LANDSCAPE_CATEGORIES),
        )

    def test_rotation_differs_by_panel(self):
        a = tuple(row["id"] for row in unsplash.select(226))
        b = tuple(row["id"] for row in unsplash.select(227))
        self.assertNotEqual(a, b)

    def test_landscape_and_portrait_pools_do_not_overlap(self):
        land = {photo for photos in unsplash.LANDSCAPE_POOL.values() for photo in photos}
        port = {photo for photos in unsplash.PORTRAIT_POOL.values() for photo in photos}
        self.assertFalse(land & port)


if __name__ == "__main__":
    unittest.main()
