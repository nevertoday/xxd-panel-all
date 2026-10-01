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

# Panel 245 uses its own eight photographs so it does not repeat 230–244.
PORTRAIT_POOL_FROM_245: dict[str, tuple[str, ...]] = {
    "still-life": ("photo-1556910103-1c02745aae4d",),
    "companion": ("photo-1548767797-d8c844163c4c",),
    "bird": ("photo-1548550023-2bdb3c5beed7",),
    "figure": ("photo-1502823403499-6ccfcf4fb453",),
}
LANDSCAPE_POOL_FROM_245: dict[str, tuple[str, ...]] = {
    "landscape": ("photo-1510414842594-a61c69b5ae57",),
    "architecture": ("photo-1518005020951-eccb494ad742",),
    "animal": ("photo-1518717758536-85ae29035b6d",),
    "plant": ("photo-1520763185298-1b434c919102",),
}

# Panel 244 uses its own eight photographs so it does not repeat 230–243.
PORTRAIT_POOL_FROM_244: dict[str, tuple[str, ...]] = {
    "still-life": ("photo-1524995997946-a1c2e315a42f",),
    "companion": ("photo-1558788353-f76d92427f16",),
    "bird": ("photo-1620694563886-c3a80ec55f41",),
    "figure": ("photo-1513956589380-bad6acb9b9d4",),
}
LANDSCAPE_POOL_FROM_244: dict[str, tuple[str, ...]] = {
    "landscape": ("photo-1532274402911-5a369e4c4bb5",),
    "architecture": ("photo-1479839672679-a46483c0e7c8",),
    "animal": ("photo-1450778869180-41d0601e046e",),
    "plant": ("photo-1441974231531-c6227db76b6e",),
}

# Panels 230–243 use these pools so that run of 14 soldiers does not share a
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


# Panels 246–267 each take a different index, so this batch of 22 does not share a photograph.
TB20_POOL_FROM_246: dict[str, tuple[str, ...]] = {
    "mountain": (
        "photo-1604223190546-a43e4c7f29d7",
        "photo-1612441804231-77a36b284856",
        "photo-1611080402167-ed75bae6df32",
        "photo-1610552050890-fe99536c2615",
        "photo-1552152370-fb05b25ff17d",
        "photo-1466854076813-4aa9ac0fc347",
        "photo-1612539473441-dfc1cefd5e1e",
        "photo-1495710388177-22c73fa5f84e",
        "photo-1604428803896-c1e5151d4128",
        "photo-1612676239016-41e2c92b8e06",
        "photo-1584148721201-b6432e0d5106",
        "photo-1508108712903-49b7ef9b1df8",
        "photo-1500964757637-c85e8a162699",
        "photo-1620414476107-2188707d780b",
        "photo-1530631045516-a797dbaabd14",
        "photo-1625647891375-91463187659f",
        "photo-1643984009272-3879e788dcf1",
        "photo-1608820980073-0a946a135983",
        "photo-1569951707784-04494c5ed864",
        "photo-1615213780624-97494a577778",
        "photo-1699786023101-2181d624d234",
        "photo-1622717125780-f4950b116473",
    ),
    "lake": (
        "photo-1583244685026-d8519b5e3d21",
        "photo-1533757879476-8f4a3cb1ae4b",
        "photo-1620065263283-f084beb12754",
        "photo-1611012341156-f7f8e6a2c7e2",
        "photo-1571161535093-e7642c4bd0c8",
        "photo-1719340198760-434a1763b3ac",
        "photo-1571564756948-51c10b7f058e",
        "photo-1603137884437-f31086c73ec4",
        "photo-1554290999-9052c2d5e559",
        "photo-1600185947787-ad08e1b51430",
        "photo-1615393915491-2b7cb33b2678",
        "photo-1534517612812-ab773a8ac477",
        "photo-1559080463-5c7eb3a52de1",
        "photo-1594757402095-996109616b0b",
        "photo-1559155800-8871d78bb4e7",
        "photo-1562375121-ea1bc3e8fc10",
        "photo-1570106178002-deb401f6e4fc",
        "photo-1545943368-83f7ff6affa0",
        "photo-1605409027404-0213e0c7182e",
        "photo-1628844349504-be690076fe6b",
        "photo-1602562069169-922dae85b518",
        "photo-1660601634773-ec3018945bc3",
    ),
    "coast": (
        "photo-1707007730851-c53cc2879f00",
        "photo-1669529101039-6886cececeb7",
        "photo-1717177724724-075c564922b0",
        "photo-1601056646282-c43ba699f1d5",
        "photo-1708225355078-0810dc3ae2e4",
        "photo-1684864854127-cf1443eb4bf0",
        "photo-1672595075859-8a27da421ea0",
        "photo-1620564713851-828f981480bb",
        "photo-1546479006-84e752f06b5d",
        "photo-1651935123016-19e832b85264",
        "photo-1695453461885-bcecb1c64320",
        "photo-1620564713749-8f99f07de1c4",
        "photo-1731512390796-d1369b558f93",
        "photo-1704268391361-1b2eedf8a955",
        "photo-1614677826714-e01cf01d3e80",
        "photo-1622485613935-1f6ce7aae665",
        "photo-1645974459771-855ac128b89f",
        "photo-1626239217523-8e1913b7b833",
        "photo-1629669858710-9d35c9d5b0af",
        "photo-1674884135998-e1fa74a7e566",
        "photo-1613325447561-da08e93a4b5a",
        "photo-1672141443193-86bdbdd7f2ed",
    ),
    "forest": (
        "photo-1592859600972-1b0834d83747",
        "photo-1758438919146-f3f59a6d2544",
        "photo-1624818145490-b385d0593e5d",
        "photo-1621769507764-a9b056cf2d8a",
        "photo-1544039161-b0c20826c6f6",
        "photo-1604342767712-f7448911dc51",
        "photo-1592859600977-378df7f369e3",
        "photo-1597201423947-3e0028337902",
        "photo-1592222761725-8c9dd3ded974",
        "photo-1650464179774-caf42373dc17",
        "photo-1700656106838-5a7d917d2678",
        "photo-1643769624791-d89829a580b4",
        "photo-1656716000034-01cb4972af83",
        "photo-1476560123413-698b683da026",
        "photo-1685330187195-1bae2038f3c4",
        "photo-1632307941173-5d541ea1d940",
        "photo-1759188534271-be7832eff679",
        "photo-1761461922930-9afd5bf09593",
        "photo-1556047573-ef501e2a3325",
        "photo-1759672220260-ce22c7b9e1ca",
        "photo-1752230446597-a5b08f8647e4",
        "photo-1670770157766-ed95c968a268",
    ),
    "field": (
        "photo-1518717202715-9fa9d099f58a",
        "photo-1580738204555-8686f3a2db43",
        "photo-1647879826700-cfc5fd9d9a31",
        "photo-1598871955824-3db4b5f9494d",
        "photo-1711397651462-3b2a22f5cfc8",
        "photo-1695129852126-1a3a7124a48e",
        "photo-1560211653-55f9fb833a8e",
        "photo-1498408040764-ab6eb772a145",
        "photo-1560559383-338dc7faf062",
        "photo-1622300650085-75a45d99a256",
        "photo-1682268980601-aac652831c9a",
        "photo-1620735157125-4612c2e3eba4",
        "photo-1717446585456-15dcbb9f039c",
        "photo-1688068705061-0305b5828e58",
        "photo-1622977266039-dbb162254c12",
        "photo-1596438820487-d54464e763d7",
        "photo-1666545743813-e692fb2b2430",
        "photo-1596987851982-3b90e09ab4ac",
        "photo-1562329203-835f220ab4d6",
        "photo-1676154417247-08646c2067a5",
        "photo-1595598239736-223ad4fe7da5",
        "photo-1599739336568-b42af4996938",
    ),
    "desert": (
        "photo-1621795307430-3ff25aa08945",
        "photo-1617374128851-c84e37dc9f37",
        "photo-1638024510305-c36fcc0bf3b1",
        "photo-1548272475-4a32d90e4f91",
        "photo-1587760376595-24f1d2483018",
        "photo-1611522135886-a632d94ff6ae",
        "photo-1679978677453-9452668cb867",
        "photo-1666837147745-1c9dea9908a4",
        "photo-1520440718111-45fe694b330a",
        "photo-1509228105826-2d09109f16bc",
        "photo-1541832039-cab7e4310f28",
        "photo-1635407343367-c580bc91dc9d",
        "photo-1619408507579-368cba59746f",
        "photo-1715297923840-44ed5c4c2cc6",
        "photo-1637935142056-03d421b2b13c",
        "photo-1558709995-98a2f442ecca",
        "photo-1639402479478-f5e7881c0ccc",
        "photo-1583307266943-e0055bb40037",
        "photo-1688345917203-310bf5e3c8e0",
        "photo-1652670098484-ed324ee57158",
        "photo-1618768638775-4e4b35be986e",
        "photo-1706804010975-0dfc65e791ff",
    ),
    "snow": (
        "photo-1483921020237-2ff51e8e4b22",
        "photo-1476108621677-3c620901b5e7",
        "photo-1465220183275-1faa863377e3",
        "photo-1483664852095-d6cc6870702d",
        "photo-1623057896740-99f8c2f090fc",
        "photo-1523720131524-71ae6dbed986",
        "photo-1614093643263-7ebf3d099724",
        "photo-1612099452850-ed8efe7d58ff",
        "photo-1485439439964-39b6b5d20d7e",
        "photo-1635420280816-c0dc0ee8a7a7",
        "photo-1484603738253-e5b73679e8cb",
        "photo-1577457943926-11193adc0563",
        "photo-1513843000111-3eb82159a25c",
        "photo-1672452352689-05e8ae81935b",
        "photo-1674725404942-ee3782b8131b",
        "photo-1614630669107-f48325791b57",
        "photo-1613358024823-357ede526cc3",
        "photo-1515885267349-1fcef6e00fd1",
        "photo-1621409498706-50b236377558",
        "photo-1639929684703-7c1ef85af732",
        "photo-1629153990811-1120a18966ce",
        "photo-1621290102989-e9865bef2dcf",
    ),
    "waterfall": (
        "photo-1476610182048-b716b8518aae",
        "photo-1568323003715-8c0254336dfa",
        "photo-1621959721891-d297dfd9d6ee",
        "photo-1597099911706-1f7c9ba6839b",
        "photo-1575580280904-905f466584e0",
        "photo-1564258443-0c2e108f445a",
        "photo-1608462884409-20ad7c86b55f",
        "photo-1705956659280-bb5e61e5a0c7",
        "photo-1656288227038-28aaa4f6b8ad",
        "photo-1705956659508-b3a899873d13",
        "photo-1550500880-d31e0e9eeb83",
        "photo-1658662882873-df79fb55df4c",
        "photo-1661527530814-d6ff4bc69b56",
        "photo-1681855862273-63a703c61a11",
        "photo-1681855862489-dcba6fc6933c",
        "photo-1654077842967-1af3695ba1b6",
        "photo-1681855862309-c994725a5997",
        "photo-1696692775926-1adde921e33c",
        "photo-1650525686127-8c69a6cd00d9",
        "photo-1627897073764-a8ad3367f50b",
        "photo-1681855862163-bffb7c3eab13",
        "photo-1681855862736-219f60468f23",
    ),
    "architecture": (
        "photo-1531591022136-eb8b0da1e6d0",
        "photo-1483366774565-c783b9f70e2c",
        "photo-1546414701-81cc6963c67f",
        "photo-1467154243382-ebe2c7d14fef",
        "photo-1613484259733-383234e8e8af",
        "photo-1453586857165-eb78d44460ca",
        "photo-1589360810891-0935e508429a",
        "photo-1616418534243-ab757ff8ce3a",
        "photo-1576831356777-59f382e176b4",
        "photo-1576831371356-d6e9411ae501",
        "photo-1557053819-aa6046add523",
        "photo-1739125714645-96ecb3274ad6",
        "photo-1538534658409-30f2502cb010",
        "photo-1587410198315-1f277736e66d",
        "photo-1510554318937-cd0860bf68c2",
        "photo-1684315010367-82ec64e218d1",
        "photo-1712806383411-a4edbec75b17",
        "photo-1613651613954-519ca9c8a650",
        "photo-1712105052319-c900e970467a",
        "photo-1563341432-f006cb3c426a",
        "photo-1710701427282-68f4799118c1",
        "photo-1712806375405-c666c772ea75",
    ),
    "city": (
        "photo-1496588152823-86ff7695e68f",
        "photo-1575380591643-b2c92368dc6d",
        "photo-1499092346589-b9b6be3e94b2",
        "photo-1518235506717-e1ed3306a89b",
        "photo-1758967905380-f62a8c8fd373",
        "photo-1571951103752-53c15cad28e5",
        "photo-1550763347-0736ab2976ea",
        "photo-1664353655151-9d94a9170eb0",
        "photo-1547841243-eacb14453cd9",
        "photo-1618861138969-0d7a9d315b1f",
        "photo-1616864202566-fbc4c67e2174",
        "photo-1502921982-f2471545c93b",
        "photo-1625726411847-8cbb60cc71e6",
        "photo-1611728337177-89dfbbdc7a3a",
        "photo-1609970105047-d0cbe314122d",
        "photo-1557211300-9991249b466a",
        "photo-1606787110443-7d8ebf733ac9",
        "photo-1583759311999-c8821f61e5b0",
        "photo-1672279410716-c676739163e9",
        "photo-1709014488957-bd321385b8a1",
        "photo-1600712365047-26f7a4f04d44",
        "photo-1609945648638-cefddce6e6d8",
    ),
    "street": (
        "photo-1634123431577-d448e438edb4",
        "photo-1620004071518-52531ff9162c",
        "photo-1726688203462-927759764ed6",
        "photo-1492724282899-01d3e50e6862",
        "photo-1587227172142-a0b19efd6f91",
        "photo-1625556841726-ee3959350033",
        "photo-1610818647551-866cce9f06d5",
        "photo-1565642899687-1c332fb7dc65",
        "photo-1634478137488-8499c2d88447",
        "photo-1651332609816-1a253a45565a",
        "photo-1587829366508-3f479565f300",
        "photo-1722516242850-ff7672b36c10",
        "photo-1709054622660-562a14bcfd76",
        "photo-1712419020105-2e75a1fc3bd3",
        "photo-1609069258650-fd58e4c7b278",
        "photo-1531398745307-6ad63a8b5284",
        "photo-1440330033336-7dcff4630cef",
        "photo-1652174834052-119f4d8f8448",
        "photo-1586812416094-a79ae86d22f5",
        "photo-1515963665762-77ef90e624fa",
        "photo-1518005068251-37900150dfca",
        "photo-1637138769122-6ad2ffb766dd",
    ),
    "interior": (
        "photo-1618221999490-9418f64786aa",
        "photo-1694032007593-8ead82259b11",
        "photo-1625163865002-c3563a586b95",
        "photo-1689263131882-a5470cc879a3",
        "photo-1689263131868-8a6ddf0ccc32",
        "photo-1509647924673-bbb53e22eeb8",
        "photo-1512324725833-abbc95d06090",
        "photo-1704040686413-2c607dbd2f06",
        "photo-1704040686510-b747ff423ebb",
        "photo-1704040686428-7534b262d0d8",
        "photo-1628624997995-0f1fd6f29dce",
        "photo-1704040686370-52238a5dab05",
        "photo-1611596189148-a74728c484ca",
        "photo-1704040686481-f7837b3da1ba",
        "photo-1669387448840-610c588f003d",
        "photo-1667828291018-89512ce6b71a",
        "photo-1631048649038-e31d38df5a25",
        "photo-1678762200388-51e11225d4de",
        "photo-1645241910657-15bc4c16e0f2",
        "photo-1689263131929-82d8f6431323",
        "photo-1677100091536-4a311441afb5",
        "photo-1703867110051-a0eb1e77b967",
    ),
    "cafe": (
        "photo-1729394405518-eaf2a0203aa7",
        "photo-1709548145082-04d0cde481d4",
        "photo-1726873800099-53f5496281e0",
        "photo-1544031064-9de80864ade5",
        "photo-1685602729695-0664ea4e5c06",
        "photo-1689037676470-b72230d5236e",
        "photo-1690999934686-85806c270eb7",
        "photo-1712730642507-d4ad0904e997",
        "photo-1624583338957-4d155ca886dc",
        "photo-1655182413225-695cc7ed0411",
        "photo-1621343607959-5d11ff0f1e39",
        "photo-1648808694138-6706c5efc80a",
        "photo-1729394404917-21d9e73e5454",
        "photo-1633073490205-27c0ad419a84",
        "photo-1655182404825-d088887fa132",
        "photo-1611653683051-17e3b2d6e8ea",
        "photo-1655182418176-57d7fa51afa9",
        "photo-1516197370049-569c4eaba1d6",
        "photo-1655182407177-b0e046ba511e",
        "photo-1628613550014-d89ec27d7667",
        "photo-1729394405014-0a6bd5c63c59",
        "photo-1682778418768-16081e4470a1",
    ),
    "food": (
        "photo-1705948730553-3ea0c89ae6fb",
        "photo-1547573854-74d2a71d0826",
        "photo-1577303935007-0d306ee638cf",
        "photo-1571987530791-58e3e7744d99",
        "photo-1591632288574-a387f820a1ca",
        "photo-1624726175512-19b9baf9fbd1",
        "photo-1630527152680-500b5453fb04",
        "photo-1604491928425-86c35b1d1649",
        "photo-1580687833156-23f5b8247f4d",
        "photo-1687039588464-09f1b52208c7",
        "photo-1620171449638-8154348fda11",
        "photo-1669472546359-418a98630699",
        "photo-1551807306-4bcd16b92a41",
        "photo-1554579306-94e345617dbc",
        "photo-1576402187878-974f70c890a5",
        "photo-1705948731485-6e4c6c180d0d",
        "photo-1618666185561-baed3459ff18",
        "photo-1758705206993-f141bbe56193",
        "photo-1605883705077-8d3d3cebe78c",
        "photo-1614548539644-ef528186523a",
        "photo-1684160244466-b89ef03b7638",
        "photo-1528738064262-9f834cbdfda1",
    ),
    "market": (
        "photo-1590437084089-9f5ae1500176",
        "photo-1570365473297-4a454f76ff0e",
        "photo-1628532431030-3b6d433ed166",
        "photo-1614020124467-cd66081a993d",
        "photo-1662714194223-7afefe9417a3",
        "photo-1498579397066-22750a3cb424",
        "photo-1606230749281-a3305ca0feac",
        "photo-1552912470-ee2e96439539",
        "photo-1584208632661-f8db31bb6489",
        "photo-1768162126091-3190821908dd",
        "photo-1679060689538-602a9fd156fe",
        "photo-1665525928021-c2a7ff9393e0",
        "photo-1633412954701-a4f29ee0c154",
        "photo-1662899311670-7e6bbe986166",
        "photo-1557844352-761f2565b576",
        "photo-1615406837056-34d12bc66120",
        "photo-1487646709898-58d3c6e8d886",
        "photo-1695654397565-b904c10fe594",
        "photo-1557779182-f4d9682636b5",
        "photo-1510382844537-64b45768cacf",
        "photo-1610269118340-f89055c4a658",
        "photo-1588005011879-5b79164c0cbc",
    ),
    "animal": (
        "photo-1705560823716-1c380fd74e7e",
        "photo-1452001603782-7d4e7d931173",
        "photo-1487213802982-74d73802997c",
        "photo-1421986717928-4dffe1c3e4e0",
        "photo-1726335849487-fd5d3b63b87c",
        "photo-1701430916245-c126556b6da0",
        "photo-1599456671475-da8c5b91e52c",
        "photo-1757858849087-7095a55a0550",
        "photo-1678048632134-79d0c6ebbd53",
        "photo-1678048632153-d961f9c37a48",
        "photo-1678048632168-39fdc9f781a9",
        "photo-1678048632412-f18bbbd3662a",
        "photo-1678048632070-b65d83de6e5f",
        "photo-1726336252228-cafc9cfe92e6",
        "photo-1763582301441-a8d94c1bd15f",
        "photo-1651707265633-6043d4606339",
        "photo-1678048632050-2e3a3ee69ab0",
        "photo-1563644786008-051ff259517c",
        "photo-1615148109219-6af9bff46b80",
        "photo-1723698894461-46081a11bdf3",
        "photo-1636704169578-c4c3d9a90b0c",
        "photo-1593923428221-c59c39b35581",
    ),
    "bird": (
        "photo-1572065134352-af1a6aa45e7f",
        "photo-1682229908322-a292d71b070b",
        "photo-1666467160097-4435e8aed6cf",
        "photo-1694687049544-4ca6510b38aa",
        "photo-1520087976699-624d8c6c00cd",
        "photo-1662097482573-4824afef5921",
        "photo-1601326105941-a29e58047392",
        "photo-1697622263716-8c80a97bcfad",
        "photo-1743179302955-3bc0b64bd7dc",
        "photo-1655459267355-41a489ef189e",
        "photo-1624143771210-b4dd90772343",
        "photo-1607029710852-eebf0224c1b2",
        "photo-1710172636336-f9a1f83e2fd0",
        "photo-1624133310859-348852f33103",
        "photo-1715593412047-74823f84b31a",
        "photo-1716335523442-b917069b42ea",
        "photo-1700604728952-9a7f27268b37",
        "photo-1688346900853-c98b6ad43604",
        "photo-1498822249651-e2e45dfbdfe8",
        "photo-1700937615172-9f8d24e83d81",
        "photo-1783023857276-0cb38f93aaaa",
        "photo-1700937621663-4a5657919a90",
    ),
    "plant": (
        "photo-1519073213287-1dda8e41e6cf",
        "photo-1599424055697-e474bf6f8300",
        "photo-1723049055982-4d76bf16a353",
        "photo-1607709399003-ac6b6549e24a",
        "photo-1695390477342-4e8598a99855",
        "photo-1679248857495-c23afe8c476c",
        "photo-1638314150896-f08292da57cd",
        "photo-1708515806001-135149942d59",
        "photo-1749700153821-da4068b731ce",
        "photo-1723887525851-f78bd537741d",
        "photo-1724502637623-a6e24298d02b",
        "photo-1632814777559-3e8916b62142",
        "photo-1733271389299-38199fa0ddd7",
        "photo-1596734759518-cbd47987c241",
        "photo-1790273435508-1e4036cd0b9f",
        "photo-1682844617654-b669fa6d9a8b",
        "photo-1696632080376-702b09104b27",
        "photo-1682844617873-f23863a32aeb",
        "photo-1663000487745-3cf42ca4bec7",
        "photo-1680119287071-21e9eb25b087",
        "photo-1641392214399-1600f825eaac",
        "photo-1704089787943-0137b479ec14",
    ),
    "boat": (
        "photo-1646518341211-6f98f8e45c8e",
        "photo-1711483668304-90fac5c665cb",
        "photo-1623000435964-d6be14403668",
        "photo-1722203229062-ee4e8110c80c",
        "photo-1682989411453-2d4a89f9074f",
        "photo-1653940509310-e07dcedb1933",
        "photo-1659320933767-fd2f38406b26",
        "photo-1723672661163-9bf4327c6779",
        "photo-1707749221092-12dbdbc9d327",
        "photo-1786101652439-1418b7e1ae78",
        "photo-1660029755634-c38991500f14",
        "photo-1786684937736-bad87772517b",
        "photo-1697826416330-0241d6ff333f",
        "photo-1685375866113-d0971993a7fc",
        "photo-1596227457352-adf126374d6a",
        "photo-1686078737991-eb4be8c0f09c",
        "photo-1612899359429-5b1f7039074a",
        "photo-1781866075927-798a0971deb2",
        "photo-1689080855243-704688a10705",
        "photo-1766300991420-0c970d85c5cf",
        "photo-1635883069995-62b9d2147a72",
        "photo-1780224785745-cf23be44a3d7",
    ),
    "night": (
        "photo-1444703686981-a3abbc4d4fe3",
        "photo-1528353518104-dbd48bee7bc4",
        "photo-1677145316529-a6e02cc8c504",
        "photo-1719859061194-04c67413a472",
        "photo-1475274047050-1d0c0975c63e",
        "photo-1444080748397-f442aa95c3e5",
        "photo-1595520519880-a86c48ea536c",
        "photo-1465101162946-4377e57745c3",
        "photo-1508402476522-c77c2fa4479d",
        "photo-1467810160588-c86c0deb5d16",
        "photo-1484950763426-56b5bf172dbb",
        "photo-1491466424936-e304919aada7",
        "photo-1482385916434-814664df9c5b",
        "photo-1497157813429-d722e7526625",
        "photo-1531177071211-ed1b7991958b",
        "photo-1476504825079-f50520ac761d",
        "photo-1614279629245-d7a138f035f0",
        "photo-1534796636912-3b95b3ab5986",
        "photo-1501418611786-e29f9929fe03",
        "photo-1450849608880-6f787542c88a",
        "photo-1528818955841-a7f1425131b5",
        "photo-1498611291069-aa296192f1e4",
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
    if panel >= 245:
        portrait_pool, landscape_pool = PORTRAIT_POOL_FROM_245, LANDSCAPE_POOL_FROM_245
    elif panel >= 244:
        portrait_pool, landscape_pool = PORTRAIT_POOL_FROM_244, LANDSCAPE_POOL_FROM_244
    elif panel >= 230:
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
    pool = TB20_POOL_FROM_246 if panel >= 246 else TB20_POOL
    if tuple(pool) != TB20_CATEGORIES:
        raise RuntimeError("TB20 pool keys must match TB20_CATEGORIES order")
    rows = []
    used: set[str] = set()
    for index, (sample, category) in enumerate(zip(TB20_SLOTS, TB20_CATEGORIES)):
        chosen = _pick(pool[category], panel, index, used)
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
