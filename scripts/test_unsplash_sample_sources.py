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

    def test_panels_230_through_243_do_not_share_sources(self):
        seen = {}
        for panel in range(230, 244):
            rows = unsplash.select(panel)
            self.assertEqual(len({row["id"] for row in rows}), 8)
            for row in rows:
                self.assertNotIn(row["id"], seen, row["id"])
                seen[row["id"]] = (panel, row["sample"])
        self.assertEqual(len(seen), 14 * 8)
        legacy = {
            row["id"]
            for panel in range(1, 230)
            for row in unsplash.select(panel)
        }
        # One flower id remains in the historical docs pool. Every other new id is new.
        overlap = set(seen) & legacy
        self.assertEqual(overlap, {"photo-1490750967868-88aa4486c946"})

    def test_rotation_differs_by_panel(self):
        a = tuple(row["id"] for row in unsplash.select(226))
        b = tuple(row["id"] for row in unsplash.select(227))
        self.assertNotEqual(a, b)

    def test_landscape_and_portrait_pools_do_not_overlap(self):
        land = {photo for photos in unsplash.LANDSCAPE_POOL.values() for photo in photos}
        port = {photo for photos in unsplash.PORTRAIT_POOL.values() for photo in photos}
        self.assertFalse(land & port)

    def test_tb20_twenty_distinct_landscape_slots(self):
        rows = unsplash.select_tb20(226)
        self.assertEqual([row["sample"] for row in rows], list(range(1, 21)))
        self.assertEqual(len({row["id"] for row in rows}), 20)
        self.assertEqual([row["orientation"] for row in rows], ["landscape"] * 20)
        self.assertEqual([row["size"] for row in rows], ["1152x1536"] * 20)
        self.assertEqual(
            [row["category"] for row in rows],
            list(unsplash.TB20_CATEGORIES),
        )

    def test_tb20_rotation_differs_by_panel(self):
        a = tuple(row["id"] for row in unsplash.select_tb20(226))
        b = tuple(row["id"] for row in unsplash.select_tb20(227))
        self.assertNotEqual(a, b)

    def test_tb20_pool_ids_are_unique(self):
        photos = [photo for photos in unsplash.TB20_POOL.values() for photo in photos]
        self.assertEqual(len(photos), len(set(photos)))
        self.assertEqual(tuple(unsplash.TB20_POOL), unsplash.TB20_CATEGORIES)


if __name__ == "__main__":
    unittest.main()
