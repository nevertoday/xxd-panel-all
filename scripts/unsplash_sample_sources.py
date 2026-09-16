#!/usr/bin/env python3
"""Fetch eight distinct Unsplash photographs for Soldier documentation samples.

Default sample scheme for the xxd-panel family. Rotates by Panel number so two
Soldiers do not share the same eight photos. Never uses the shared 陈翔海报 queue.

Slots 05–08 are 16:9 left–right, so sources are native landscape photographs.
Slots 09–12 are 3:4 top–bottom, so sources are native portrait photographs.

  python3 scripts/unsplash_sample_sources.py --root .. --panel 226
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

USER_AGENT = "xxd-panel-sample-sources/1"
FORBIDDEN_MARKERS = ("陈翔海报", "tmp/imagegen/170")

# 16:9 left-right uses wide scenes. 3:4 top-bottom uses tall subjects.
LANDSCAPE_CATEGORIES = ("landscape", "architecture", "animal", "plant")
PORTRAIT_CATEGORIES = ("still-life", "companion", "bird", "figure")

LANDSCAPE_POOL: dict[str, tuple[str, ...]] = {
    "landscape": (
        "photo-1501785888041-af3ef285b470",
        "photo-1464822759023-fed622ff2c3b",
        "photo-1472214103451-9374bd1c798e",
        "photo-1426604966848-d7adac402bff",
        "photo-1507525428034-b723cf961d3e",
        "photo-1506905925346-21bda4d32df4",
        "photo-1470071459604-3b5ec3a7fe05",
        "photo-1439066615861-d1af74d74000",
        "photo-1519681393784-d120267933ba",
        "photo-1476514525535-07fb3b4ae5f1",
    ),
    "architecture": (
        "photo-1493976040374-85c8e12f0c0e",
        "photo-1449824913935-59a10b8d2000",
        "photo-1517248135467-4c7edcad34c4",
    ),
    "animal": (
        "photo-1444464666168-49d633b86797",
        "photo-1553284965-83fd3e82fa5a",
        "photo-1456926631375-92c8ce872def",
        "photo-1500595046743-cd271d694d30",
        "photo-1514888286974-6c03e2ca1dba",
    ),
    "plant": (
        "photo-1490750967868-88aa4486c946",
        "photo-1500382017468-9049fed747ef",
        "photo-1441974231531-c6227db76b6e",
        "photo-1448375240586-882707db888b",
        "photo-1511497584788-876760111969",
    ),
}

PORTRAIT_POOL: dict[str, tuple[str, ...]] = {
    "still-life": (
        "photo-1544787219-7f47ccb76574",
        "photo-1516035069371-29a1b244cc32",
    ),
    "companion": (
        "photo-1543852786-1cf6624b9987",
    ),
    "bird": (
        "photo-1552728089-57bdde30beb3",
    ),
    "figure": (
        "photo-1494790108377-be9c29b29330",
        "photo-1506794778202-cad84cf45f1d",
        "photo-1507003211169-0a1dd7228f2d",
        "photo-1524504388940-b1c1722653e1",
        "photo-1529626455594-4ff0802cfb7e",
        "photo-1539571696357-5a69c17a67c6",
        "photo-1488426862026-3ee34a7d66df",
        "photo-1500648767791-00dcc994a43e",
    ),
}

LANDSCAPE_SLOTS = (5, 6, 7, 8)
PORTRAIT_SLOTS = (9, 10, 11, 12)
SIZES = {n: ("1536x864" if n <= 8 else "1152x1536") for n in (*LANDSCAPE_SLOTS, *PORTRAIT_SLOTS)}
CROP = {
    "landscape": "auto=format&fit=crop&w=2000&h=1125&q=80",
    "portrait": "auto=format&fit=crop&w=1500&h=2000&q=80",
}


def _pick(photos: tuple[str, ...], panel: int, salt: int, used: set[str]) -> str:
    for offset in range(len(photos)):
        photo_id = photos[(panel + salt + offset) % len(photos)]
        if photo_id not in used:
            return photo_id
    raise RuntimeError(f"no unused Unsplash id in pool of {len(photos)}")


def select(panel: int) -> list[dict]:
    rows = []
    used: set[str] = set()
    groups = (
        ("landscape", LANDSCAPE_SLOTS, LANDSCAPE_CATEGORIES, LANDSCAPE_POOL),
        ("portrait", PORTRAIT_SLOTS, PORTRAIT_CATEGORIES, PORTRAIT_POOL),
    )
    for orientation, slots, categories, pool in groups:
        for index, (sample, category) in enumerate(zip(slots, categories)):
            chosen = _pick(pool[category], panel, index, used)
            used.add(chosen)
            rows.append(
                {
                    "sample": sample,
                    "category": category,
                    "orientation": orientation,
                    "id": chosen,
                    "size": SIZES[sample],
                    "url": f"https://images.unsplash.com/{chosen}?{CROP[orientation]}",
                }
            )
    return rows


def download(url: str, dest: Path) -> None:
    req = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, "Accept": "image/*"}
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
        ctype = resp.headers.get("Content-Type", "")
    if len(data) < 20000 or data[:3] not in (b"\xff\xd8\xff", b"\x89PN"):
        raise RuntimeError(f"not an image ({len(data)} bytes, {ctype}): {url}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)


def fetch_panel(root: Path, panel: int) -> Path:
    rows = select(panel)
    out_dir = root / "tmp" / "imagegen" / f"{panel}" / "sources"
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for row in rows:
        name = f"{row['sample']:02d}-{row['orientation']}-{row['category']}.jpg"
        dest = out_dir / name
        path_text = str(dest)
        if any(marker in path_text for marker in FORBIDDEN_MARKERS):
            raise RuntimeError(f"refusing forbidden sample source path: {dest}")
        download(row["url"], dest)
        record = dict(row)
        record["file"] = str(dest)
        written.append(record)
        print(
            f"{panel}/{row['sample']:02d} {row['orientation']} {row['category']} "
            f"{row['id']} {dest.stat().st_size}"
        )
    index = out_dir.parent / "unsplash-sources.json"
    index.write_text(json.dumps(written, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return index


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--panel", type=int, action="append", required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    for panel in args.panel:
        fetch_panel(root, panel)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, urllib.error.URLError, OSError) as exc:
        print(f"unsplash_sample_sources: {exc}", file=sys.stderr)
        raise SystemExit(1)
