#!/usr/bin/env python3
"""Build the General README soldier roster: one 16:9 sample per Soldier.

Reads each sibling `xxd-panel-NNN/assets/examples/sample-05.png` (the first
left–right sample), writes JPEG thumbs into `assets/roster/`, and replaces the
marked roster block in the five General READMEs. No network, no image models.

  python3 scripts/soldier_roster.py --root ..
  python3 scripts/soldier_roster.py --root .. --skip-thumbs
"""
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from PIL import Image

START, END = "<!-- xxd-soldier-roster:start -->", "<!-- xxd-soldier-roster:end -->"
THUMB_WIDTH = 800
THUMB_QUALITY = 80
GITHUB = "https://github.com/nevertoday/xxd-panel-{nnn}"
TITLE_RE = re.compile(r"^#\s+(?:🦁\s*)?XXD Panel (\d{3})\s*[｜|]\s*(.+)$", re.M)
HEADING_RE = re.compile(r"^## .+$", re.M)

README_FILES = (
    "README.md",
    "README.en.md",
    "README.ja.md",
    "README.ko.md",
    "README.ar.md",
)
LEGACY_HEADINGS = {
    "README.md": "## 新增士兵",
    "README.en.md": "## New Soldiers",
    "README.ja.md": "## 新しい兵士",
    "README.ko.md": "## 새로운 병사",
    "README.ar.md": "## الجنود الجدد",
}
COPY = {
    "README.md": (
        "全部士兵 · 16:9 左右双联样张",
        "每张是对应士兵的一张 16:9 左右对照样张（左为现实摄影，右为本编号转绘）。点击图片进入该士兵的 GitHub 仓库。",
    ),
    "README.en.md": (
        "All Soldiers · 16:9 left–right samples",
        "Each tile is one 16:9 left–right sample from that Soldier (reality left, this Panel's design right). Click the image to open the Soldier's GitHub repository.",
    ),
    "README.ja.md": (
        "全部の兵士 · 16:9 左右対照サンプル",
        "各タイルは、その兵士の 16:9 左右対照サンプル 1 枚です（左が現実写真、右が当該番号の転訳）。画像をクリックすると、その兵士の GitHub リポジトリが開きます。",
    ),
    "README.ko.md": (
        "전체 병사 · 16:9 좌우 대조 샘플",
        "각 칸은 해당 병사의 16:9 좌우 대조 샘플 한 장입니다(왼쪽 실제 사진, 오른쪽 해당 번호의 전역). 이미지를 클릭하면 그 병사의 GitHub 저장소로 이동합니다.",
    ),
    "README.ar.md": (
        "جميع الجنود · عينات أفقية 16:9",
        "كل مربع عينة أفقية 16:9 واحدة من ذلك الجندي (الواقع يسارًا، وتصميم هذا الرقم يمينًا). انقر الصورة لفتح مستودع GitHub الخاص بالجندي.",
    ),
}


def discover_panels(root: Path) -> list[int]:
    found = []
    for path in sorted(root.glob("xxd-panel-[0-9][0-9][0-9]")):
        if not path.is_dir():
            continue
        n = int(path.name.split("-")[-1])
        if (path / "SKILL.md").is_file():
            found.append(n)
    return found


def soldier_title(panel_dir: Path, readme_name: str, nnn: int) -> str:
    path = panel_dir / readme_name
    text = path.read_text(encoding="utf-8") if path.is_file() else ""
    match = TITLE_RE.search(text)
    if match:
        return match.group(2).strip()
    return f"XXD Panel {nnn:03d}"


def sample_path(panel_dir: Path) -> Path:
    examples = panel_dir / "assets" / "examples"
    for name in ("sample-05.png", "sample-05.jpg", "sample-01.png", "sample-01.jpg"):
        candidate = examples / name
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f"no horizontal sample in {examples}")


def write_thumb(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        rgb = im.convert("RGB")
        width, height = rgb.size
        if width != THUMB_WIDTH:
            height = max(1, round(height * THUMB_WIDTH / width))
            rgb = rgb.resize((THUMB_WIDTH, height), Image.Resampling.LANCZOS)
        rgb.save(dest, format="JPEG", quality=THUMB_QUALITY, optimize=True)


def cell(nnn: int, title: str) -> str:
    repo = GITHUB.format(nnn=f"{nnn:03d}")
    src = f"./assets/roster/{nnn:03d}.jpg"
    alt = html.escape(f"XXD Panel {nnn:03d} · {title}")
    return (
        f'<td width="50%" valign="top">\n'
        f'<a href="{repo}"><img src="{src}" alt="{alt}" width="100%"></a>\n'
        f'<p align="center"><a href="{repo}"><strong>{nnn:03d}</strong> · {html.escape(title)}</a></p>\n'
        f"</td>"
    )


def render_table(panels: list[int], titles: dict[int, str]) -> str:
    rows = []
    for i in range(0, len(panels), 2):
        left = cell(panels[i], titles[panels[i]])
        if i + 1 < len(panels):
            right = cell(panels[i + 1], titles[panels[i + 1]])
            rows.append(f"  <tr>\n    {left}\n    {right}\n  </tr>")
        else:
            rows.append(f"  <tr>\n    {left}\n  </tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def render_block(readme_name: str, panels: list[int], titles: dict[int, str]) -> str:
    heading, intro = COPY[readme_name]
    table = render_table(panels, titles)
    return f"{START}\n\n## {heading}\n\n{intro}\n\n{table}\n\n{END}"


def replace_block(text: str, readme_name: str, block: str) -> str:
    if START in text and END in text:
        first, last = text.index(START), text.index(END) + len(END)
        return text[:first] + block + text[last:]
    legacy = LEGACY_HEADINGS[readme_name]
    start = text.find(legacy)
    if start < 0:
        raise RuntimeError(f"{readme_name}: missing roster heading {legacy!r}")
    following = HEADING_RE.search(text, start + len(legacy))
    if not following:
        raise RuntimeError(f"{readme_name}: missing heading after roster")
    return text[:start] + block + "\n\n" + text[following.start():]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--skip-thumbs", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    general = root / "xxd-panel-all"
    if not (general / "README.md").is_file():
        parser.error(f"General README not found under {general}")
    panels = discover_panels(root)
    if not panels:
        parser.error("no soldier repositories found")
    thumbs = general / "assets" / "roster"
    missing = []
    for n in panels:
        panel_dir = root / f"xxd-panel-{n:03d}"
        try:
            src = sample_path(panel_dir)
        except FileNotFoundError:
            missing.append(n)
            continue
        dest = thumbs / f"{n:03d}.jpg"
        if not args.skip_thumbs:
            write_thumb(src, dest)
        elif not dest.is_file():
            missing.append(n)
    if missing:
        raise SystemExit(f"missing samples for panels: {missing}")
    for name in README_FILES:
        titles = {
            n: soldier_title(root / f"xxd-panel-{n:03d}", name, n) for n in panels
        }
        path = general / name
        old = path.read_text(encoding="utf-8")
        new = replace_block(old, name, render_block(name, panels, titles))
        if new != old:
            path.write_text(new, encoding="utf-8")
            print(f"updated {name}")
        else:
            print(f"unchanged {name}")
    print(f"roster {len(panels)} soldiers; thumbs in {thumbs}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
