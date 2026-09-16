#!/usr/bin/env python3
"""Fetch eight distinct Unsplash photographs for Soldier documentation samples.

Default sample scheme for the xxd-panel family. Rotates by Panel number so two
Soldiers do not share the same eight photos. Never uses the shared 陈翔海报 queue.

  python3 scripts/unsplash_sample_sources.py --root .. --panel 224
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

# Eight subject slots. Each category has multiple verified Unsplash photo IDs.
# Order is sample-05..08 (16:9 left-right) then sample-09..12 (3:4 top-bottom).
CATEGORIES = (
    "still-life",
    "mammal",
    "architecture",
    "bird",
    "plant",
    "companion",
    "food",
    "landscape",
)

POOL: dict[str, tuple[str, ...]] = {
    "still-life": (
        "photo-1544787219-7f47ccb76574",
        "photo-1494976388531-d1058494cdd8",
        "photo-1546069901-ba9599a7e63c",
    ),
    "mammal": (
        "photo-1553284965-83fd3e82fa5a",
        "photo-1456926631375-92c8ce872def",
        "photo-1518837695005-2083093ee35b",
    ),
    "architecture": (
        "photo-1528164344705-47542687000d",
        "photo-1545569341-9eb8b30979d9",
        "photo-1493976040374-85c8e12f0c0e",
    ),
    "bird": (
        "photo-1444464666168-49d633b86797",
        "photo-1552728089-57bdde30beb3",
    ),
    "plant": (
        "photo-1490750967868-88aa4486c946",
        "photo-1500382017468-9049fed747ef",
        "photo-1441974231531-c6227db76b6e",
    ),
    "companion": (
        "photo-1514888286974-6c03e2ca1dba",
        "photo-1456926631375-92c8ce872def",
    ),
    "food": (
        "photo-1569718212165-3a8278d5f624",
        "photo-1504674900247-0877df9cc836",
        "photo-1414235077428-338989a2e8c0",
    ),
    "landscape": (
        "photo-1501785888041-af3ef285b470",
        "photo-1464822759023-fed622ff2c3b",
        "photo-1472214103451-9374bd1c798e",
        "photo-1426604966848-d7adac402bff",
        "photo-1500530855697-b586d89ba3ee",
        "photo-1439066615861-d1af74d74000",
        "photo-1559827260-dc66d52bef19",
    ),
}

SLOTS = tuple(range(5, 13))
SIZES = {n: ("1536x864" if n <= 8 else "1152x1536") for n in SLOTS}


def select(panel: int) -> list[dict]:
    rows = []
    used = set()
    for index, category in enumerate(CATEGORIES):
        photos = POOL[category]
        chosen = None
        for offset in range(len(photos)):
            photo_id = photos[(panel + index + offset) % len(photos)]
            if photo_id not in used:
                chosen = photo_id
                break
        if chosen is None:
            raise RuntimeError(f"no unused Unsplash id for {category}")
        used.add(chosen)
        sample = SLOTS[index]
        rows.append(
            {
                "sample": sample,
                "category": category,
                "id": chosen,
                "size": SIZES[sample],
                "url": f"https://images.unsplash.com/{chosen}?auto=format&fit=crop&w=2000&q=80",
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
        name = f"{row['sample']:02d}-{row['category']}.jpg"
        dest = out_dir / name
        path_text = str(dest)
        if any(marker in path_text for marker in FORBIDDEN_MARKERS):
            raise RuntimeError(f"refusing forbidden sample source path: {dest}")
        download(row["url"], dest)
        record = dict(row)
        record["file"] = str(dest)
        written.append(record)
        print(f"{panel}/{row['sample']:02d} {row['category']} {row['id']} {dest.stat().st_size}")
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
