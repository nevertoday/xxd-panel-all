#!/usr/bin/env python3
"""Fetch Unsplash photographs for Soldier documentation samples and TB20 series.

Default sample scheme for the xxd-panel family. Rotates by Panel number so two
Soldiers do not share the same eight photos. Never uses the shared 陈翔海报 queue.

Slots 05–08 are 16:9 left–right. The photograph occupies the left half (~8:9),
so sources are native portrait photographs. Slots 09–12 are 3:4 top–bottom.
The photograph occupies the top half (~3:2), so sources are native landscape photographs.

`--series tb20` fetches twenty landscape photographs for independent 3:4
top-bottom canvases. The photograph occupies the top half (~3:2).

  python3 scripts/unsplash_sample_sources.py --root .. --panel 226
  python3 scripts/unsplash_sample_sources.py --root .. --panel 226 --series tb20
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

# Photo-half geometry, not full-canvas orientation:
# 16:9 left-right → left half is ~8:9 → portrait sources.
# 3:4 top-bottom → top half is ~3:2 → landscape sources.
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

# Panels 230 and later use these pools so a run of 14 soldiers does not share a
# documentation photograph. Each tuple is length 14 and the ids are disjoint.
# Do not prepend or reorder them: select() rotates with (panel + slot) % len.
PORTRAIT_POOL_FROM_230: dict[str, tuple[str, ...]] = {
    "still-life": (
        "photo-1511920170033-f8396924c348",
        "photo-1514432324607-a09d9b4aefdd",
        "photo-1544947950-fa07a98d237f",
        "photo-1565958011703-44f9829ba187",
        "photo-1488477181946-6428a0291777",
        "photo-1551024601-bec78aea704b",
        "photo-1482049016688-2d3e1b311543",
        "photo-1506084868230-bb9d95c24759",
        "photo-1497935586351-b67a49e012bf",
        "photo-1447933601403-0c6688de566e",
        "photo-1459755486867-b55449bb39ff",
        "photo-1517685352821-92cf88aee5a5",
        "photo-1512820790803-83ca734da794",
        "photo-1495446815901-a7297e633e8d",
    ),
    "companion": (
        "photo-1574158622682-e40e69881006",
        "photo-1495360010541-f48722b34f7d",
        "photo-1517849845537-4d257902454a",
        "photo-1537151608828-ea2b11777ee8",
        "photo-1573865526739-10659fec78a5",
        "photo-1552053831-71594a27632d",
        "photo-1530281700549-e82e7bf110d6",
        "photo-1583512603805-3cc6b41f3edb",
        "photo-1517423440428-a5a00ad493e8",
        "photo-1537151625747-768eb6cf92b2",
        "photo-1583337130417-3346a1be7dee",
        "photo-1560807707-8cc77767d783",
        "photo-1596854407944-bf87f6fdd49e",
        "photo-1568572933382-74d440642117",
    ),
    "bird": (
        "photo-1555169062-013468b47731",
        "photo-1452570053594-1b985d6ea890",
        "photo-1611689342806-0863700ce1e4",
        "photo-1591608971362-f08b2a75731a",
        "photo-1574068468668-a05a11f871da",
        "photo-1612024782955-49fae79e42bb",
        "photo-1486365227551-f3f90034a57c",
        "photo-1520808663317-647b476a81b9",
        "photo-1516467508483-a7212febe31a",
        "photo-1560813962-ff3d8fcf59ba",
        "photo-1579373903781-fd5c0c30c4cd",
        "photo-1549608276-5786777e6587",
        "photo-1480044965905-02098d419e96",
        "photo-1591195853828-11db59a44f6b",
    ),
    "figure": (
        "photo-1534528741775-53994a69daeb",
        "photo-1531123897727-8f129e1688ce",
        "photo-1531746020798-e6953c6e8e04",
        "photo-1548142813-c348350df52b",
        "photo-1517841905240-472988babdf9",
        "photo-1521119989659-a83eee488004",
        "photo-1544005313-94ddf0286df2",
        "photo-1552058544-f2b08422138a",
        "photo-1580489944761-15a19d654956",
        "photo-1519345182560-3f2917c472ef",
        "photo-1599566150163-29194dcaad36",
        "photo-1544723795-3fb6469f5b39",
        "photo-1524502397800-2eeaad7c3fe5",
        "photo-1525134479668-1bee5c7c6845",
    ),
}
LANDSCAPE_POOL_FROM_230: dict[str, tuple[str, ...]] = {
    "landscape": (
        "photo-1469474968028-56623f02e42e",
        "photo-1511593358241-7eea1f3c84e5",
        "photo-1500534623283-312aade485b7",
        "photo-1486870591958-9b9d0d1dda99",
        "photo-1474044159687-1ee9f3a51722",
        "photo-1432405972618-c60b0225b8f9",
        "photo-1549880338-65ddcdfd017b",
        "photo-1551632811-561732d1e306",
        "photo-1526772662000-3f88f10405ff",
        "photo-1465101046530-73398c7f28ca",
        "photo-1527489377706-5bf97e608852",
        "photo-1494548162494-384bba4ab999",
        "photo-1500530855697-b586d89ba3ee",
        "photo-1466781783364-36c955e42a7f",
    ),
    "architecture": (
        "photo-1511818966892-d7d671e672a2",
        "photo-1448630360428-65456885c650",
        "photo-1503387762-592deb58ef4e",
        "photo-1460317442991-0ec209397118",
        "photo-1523482580672-f109ba8cb9be",
        "photo-1512453979798-5ea266f8880c",
        "photo-1542314831-068cd1dbfeeb",
        "photo-1496564203457-11bb12075d90",
        "photo-1486406146926-c627a92ad1ab",
        "photo-1464146072230-91cabc968266",
        "photo-1497366216548-37526070297c",
        "photo-1497366811353-6870744d04b2",
        "photo-1497366754035-f200968a6e72",
        "photo-1481627834876-b7833e8f5570",
    ),
    "animal": (
        "photo-1437622368342-7a3d73a34c8f",
        "photo-1474511320723-9a56873867b5",
        "photo-1564349683136-77e08dba1ef7",
        "photo-1425082661705-1834bfd09dca",
        "photo-1551717743-49959800b1f6",
        "photo-1504006833117-8886a355efbf",
        "photo-1535591273668-578e31182c4f",
        "photo-1511044568932-338cba0ad803",
        "photo-1519052537078-e6302a4968d4",
        "photo-1587300003388-59208cc962cb",
        "photo-1561037404-61cd46aa615b",
        "photo-1543466835-00a7907e9de1",
        "photo-1583511655857-d19b40a7a54e",
        "photo-1548199973-03cce0bbc87b",
    ),
    "plant": (
        "photo-1462275646964-a0e3386b89fa",
        "photo-1463936575829-25148e1db1b8",
        "photo-1470058869958-2a77ade41c02",
        "photo-1459411552884-841db9b3cc2a",
        "photo-1496062031456-07b8f162a322",
        "photo-1526047932273-341f2a7631f9",
        "photo-1518531933037-91b2f5f229cc",
        "photo-1509423350716-97f9360b4e09",
        "photo-1464226184884-fa280b87c399",
        "photo-1516594798947-e65505dbb29d",
        "photo-1490818387583-1baba5e638af",
        "photo-1471193945509-9ad0617afabf",
        "photo-1490750967868-88aa4486c946",
        "photo-1455659817273-f96807779a8a",
    ),
}

LR_SLOTS = (5, 6, 7, 8)
TB_SLOTS = (9, 10, 11, 12)
SIZES = {n: ("1536x864" if n <= 8 else "1152x1536") for n in (*LR_SLOTS, *TB_SLOTS)}
CROP = {
    "portrait": "auto=format&fit=crop&w=1500&h=1688&q=80",
    "landscape": "auto=format&fit=crop&w=2000&h=1333&q=80",
}

# Twenty independent 3:4 top-bottom sources. Photo half is ~3:2, so native
# landscape photographs. Same rotation-by-panel rule as the eight-slot docs.
TB20_SIZE = "1152x1536"
TB20_SLOTS = tuple(range(1, 21))
TB20_CATEGORIES = (
    "mountain",
    "lake",
    "coast",
    "forest",
    "field",
    "desert",
    "snow",
    "waterfall",
    "architecture",
    "city",
    "street",
    "interior",
    "cafe",
    "food",
    "market",
    "animal",
    "bird",
    "plant",
    "boat",
    "night",
)
TB20_POOL: dict[str, tuple[str, ...]] = {
    "mountain": (
        "photo-1501785888041-af3ef285b470",
        "photo-1464822759023-fed622ff2c3b",
        "photo-1506905925346-21bda4d32df4",
        "photo-1482192505345-5655af888cc4",
        "photo-1519904981063-b0cf448d479e",
    ),
    "lake": (
        "photo-1439066615861-d1af74d74000",
        "photo-1476514525535-07fb3b4ae5f1",
        "photo-1506744038136-46273834b3fb",
        "photo-1470770841072-f978cf4d019e",
        "photo-1506260408121-e353d10b87c7",
    ),
    "coast": (
        "photo-1507525428034-b723cf961d3e",
        "photo-1505142468610-359e7d316be0",
        "photo-1473116763249-2faaef81ccda",
        "photo-1500375592092-40eb2168fd21",
        "photo-1471922694854-ff1b63b20054",
    ),
    "forest": (
        "photo-1441974231531-c6227db76b6e",
        "photo-1448375240586-882707db888b",
        "photo-1511497584788-876760111969",
        "photo-1447752875215-b2761acb3c5d",
        "photo-1418065460487-3e41a6c84dc5",
    ),
    "field": (
        "photo-1500382017468-9049fed747ef",
        "photo-1470071459604-3b5ec3a7fe05",
        "photo-1472214103451-9374bd1c798e",
        "photo-1426604966848-d7adac402bff",
        "photo-1444858291040-58f756a3bdd6",
    ),
    "desert": (
        "photo-1509316785289-025f5b846b35",
        "photo-1473580044384-7ba9967e16a0",
        "photo-1500534314209-a25ddb2bd429",
        "photo-1469854523086-cc02fe5d8800",
        "photo-1682687220742-aba13b6e50ba",
    ),
    "snow": (
        "photo-1418985991508-e47386d96a71",
        "photo-1457269449834-928af64c684d",
        "photo-1483728642387-6c3bdd6c93e5",
        "photo-1517299321609-52687d1bc55a",
        "photo-1604537529428-15bcbeecfe4d",
    ),
    "waterfall": (
        "photo-1433086966358-54859d0ed716",
        "photo-1518182170546-07661fd94144",
        "photo-1490730141103-6cac27aaab94",
        "photo-1475924156734-496f6cac6ec1",
        "photo-1502082553048-f009c37129b9",
    ),
    "architecture": (
        "photo-1493976040374-85c8e12f0c0e",
        "photo-1486325212027-8081e485255e",
        "photo-1487956382158-bb926046304a",
        "photo-1528164344705-47542687000d",
        "photo-1490806843957-31f4c9a91c65",
    ),
    "city": (
        "photo-1449824913935-59a10b8d2000",
        "photo-1480714378408-67cf0d13bc1b",
        "photo-1477959858617-67f85cf4f1df",
        "photo-1444723121867-7a241cacace9",
        "photo-1540959733332-eab4deabeeaf",
    ),
    "street": (
        "photo-1523906834658-6e24ef2386f9",
        "photo-1524413840807-0c3cb6fa808d",
        "photo-1478436127897-769e1b3f0f36",
        "photo-1542051841857-5f90071e7989",
        "photo-1524850011238-e3d235c7d4c9",
    ),
    "interior": (
        "photo-1517248135467-4c7edcad34c4",
        "photo-1554995207-c18c203602cb",
        "photo-1502672260266-1c1ef2d93688",
        "photo-1618221195710-dd6b41faaea6",
        "photo-1600210492486-724fe5c67fb0",
    ),
    "cafe": (
        "photo-1495474472287-4d71bcdd2085",
        "photo-1509042239860-f550ce710b93",
        "photo-1554118811-1e0d58224f24",
        "photo-1521017432531-fbd92d768814",
        "photo-1498804103079-a6351b050096",
    ),
    "food": (
        "photo-1504674900247-0877df9cc836",
        "photo-1414235077428-338989a2e8c0",
        "photo-1473093295043-cdd812d0e601",
        "photo-1569718212165-3a8278d5f624",
        "photo-1565299624946-b28f40a0ae38",
    ),
    "market": (
        "photo-1488459716781-31db52582fe9",
        "photo-1542838132-92c53300491e",
        "photo-1533900298318-6b8da08a523e",
        "photo-1540189549336-e6e99c3679fe",
        "photo-1512621776951-a57141f2eefd",
    ),
    "animal": (
        "photo-1553284965-83fd3e82fa5a",
        "photo-1456926631375-92c8ce872def",
        "photo-1500595046743-cd271d694d30",
        "photo-1546182990-dffeafbe841d",
        "photo-1484406566174-9da000fda645",
    ),
    "bird": (
        "photo-1444464666168-49d633b86797",
        "photo-1552728089-57bdde30beb3",
        "photo-1522926193341-e9ffd686c60f",
        "photo-1497206365907-f5e630693df0",
        "photo-1514888286974-6c03e2ca1dba",
    ),
    "plant": (
        "photo-1490750967868-88aa4486c946",
        "photo-1455659817273-f96807779a8a",
        "photo-1416879595882-3373a0480b5b",
        "photo-1501004318641-b39e6451bec6",
        "photo-1485955900006-10f4d324d411",
    ),
    "boat": (
        "photo-1544551763-46a013bb70d5",
        "photo-1468413253725-0d5181091126",
        "photo-1559827260-dc66d52bef19",
        "photo-1530053969600-caed2596d242",
        "photo-1540206395-68808572332f",
    ),
    "night": (
        "photo-1419242902214-272b3f66ee7a",
        "photo-1464802686167-b939a6910659",
        "photo-1534274988757-a28bf1a57c17",
        "photo-1519681393784-d120267933ba",
        "photo-1514565131-fce0801e5785",
    ),
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
    if panel >= 230:
        portrait_pool, landscape_pool = PORTRAIT_POOL_FROM_230, LANDSCAPE_POOL_FROM_230
    else:
        portrait_pool, landscape_pool = PORTRAIT_POOL, LANDSCAPE_POOL
    groups = (
        ("portrait", LR_SLOTS, PORTRAIT_CATEGORIES, portrait_pool),
        ("landscape", TB_SLOTS, LANDSCAPE_CATEGORIES, landscape_pool),
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


def select_tb20(panel: int) -> list[dict]:
    if tuple(TB20_POOL) != TB20_CATEGORIES:
        raise RuntimeError("TB20_POOL keys must match TB20_CATEGORIES order")
    rows = []
    used: set[str] = set()
    for index, (sample, category) in enumerate(zip(TB20_SLOTS, TB20_CATEGORIES)):
        chosen = _pick(TB20_POOL[category], panel, index, used)
        used.add(chosen)
        rows.append(
            {
                "sample": sample,
                "category": category,
                "orientation": "landscape",
                "id": chosen,
                "size": TB20_SIZE,
                "url": f"https://images.unsplash.com/{chosen}?{CROP['landscape']}",
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


def cache_path(root: Path, photo_id: str) -> Path:
    return root / "tmp" / "imagegen" / "unsplash-cache" / f"{photo_id}.jpg"


def download_cached(root: Path, url: str, photo_id: str) -> Path:
    dest = cache_path(root, photo_id)
    if dest.is_file() and dest.stat().st_size >= 20000:
        return dest
    download(url, dest)
    return dest


def _write_index(index: Path, written: list[dict]) -> Path:
    index.parent.mkdir(parents=True, exist_ok=True)
    index.write_text(json.dumps(written, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return index


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
        cached = download_cached(root, row["url"], row["id"])
        dest.write_bytes(cached.read_bytes())
        record = dict(row)
        record["file"] = str(dest)
        written.append(record)
        print(
            f"{panel}/{row['sample']:02d} {row['orientation']} {row['category']} "
            f"{row['id']} {dest.stat().st_size}"
        )
    return _write_index(out_dir.parent / "unsplash-sources.json", written)


def fetch_tb20_panel(root: Path, panel: int) -> Path:
    rows = select_tb20(panel)
    out_dir = root / "tmp" / "imagegen" / f"{panel}" / "sources-tb20"
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for row in rows:
        name = f"{row['sample']:02d}-landscape-{row['category']}.jpg"
        dest = out_dir / name
        path_text = str(dest)
        if any(marker in path_text for marker in FORBIDDEN_MARKERS):
            raise RuntimeError(f"refusing forbidden sample source path: {dest}")
        cached = download_cached(root, row["url"], row["id"])
        dest.write_bytes(cached.read_bytes())
        record = dict(row)
        record["file"] = str(dest)
        written.append(record)
        print(
            f"{panel}/tb20-{row['sample']:02d} landscape {row['category']} "
            f"{row['id']} {dest.stat().st_size}"
        )
    return _write_index(out_dir.parent / "unsplash-tb20-sources.json", written)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--panel", type=int, action="append", required=True)
    parser.add_argument("--series", choices=("docs8", "tb20"), default="docs8")
    args = parser.parse_args()
    root = args.root.resolve()
    fetch = fetch_tb20_panel if args.series == "tb20" else fetch_panel
    for panel in args.panel:
        fetch(root, panel)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, urllib.error.URLError, OSError) as exc:
        print(f"unsplash_sample_sources: {exc}", file=sys.stderr)
        raise SystemExit(1)
