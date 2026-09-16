#!/usr/bin/env python3
"""Prepare eight-slot sample queues from Unsplash sources.

Does not call an image model. Downloads Unsplash photographs unless
tmp/imagegen/NNN/unsplash-sources.json already exists.

  python3 scripts/prepare_sample_queues.py --root .. --start 224 --end 224
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import unsplash_sample_sources as unsplash

LR = (
    "本次交付变量：只使用附件 Image 1 作为本张独立作品的原始参考图，不引用任何其他照片、之前结果或其他编号风格。"
    "生成一张完整 PNG 画布。本次明确覆盖原文竖版上下布局：16:9 横版，目标尺寸1536×864像素，"
    "严格左右50:50两个全高区域，左侧保留原始图像、右侧按上述原文审美设计；原文的上半部分均映射左侧、"
    "下半部分映射右侧。分界线必须在画布正中间。文字模式prompt，目标语种en-US：仅从当前源图提炼极少量简短英文文案，"
    "遵守原文图文位置、尺度与审美原则；不添加固定标题或无根据编号。禁止第三条带、额外标题栏、底栏、内嵌面板或多图网格。"
)
TB = (
    "本次交付变量：只使用附件 Image 1 作为本张独立作品的原始参考图，不引用任何其他照片、之前结果或其他编号风格。"
    "生成一张完整 PNG 画布。3:4竖版，目标尺寸1152×1536像素，严格上下50:50两个全宽区域，上侧保留原始图像，"
    "下侧按上述原文审美设计，分界线必须在画布正中间。文字模式prompt，目标语种en-US：仅从当前源图提炼极少量简短英文文案，"
    "遵守原文图文位置、尺度与审美原则；不添加固定标题或无根据编号。禁止第三条带、额外标题栏、底栏、内嵌面板或多图网格。"
)


def delivery_for(size: str) -> str:
    return LR if size == "1536x864" else TB


def load_sources(root: Path, panel: int) -> list[dict]:
    index = root / "tmp" / "imagegen" / f"{panel}" / "unsplash-sources.json"
    if not index.is_file():
        unsplash.fetch_panel(root, panel)
    rows = json.loads(index.read_text(encoding="utf-8"))
    for row in rows:
        path = Path(row["file"])
        if not path.is_file():
            raise SystemExit(f"{panel}: missing Unsplash file {path}")
        text = str(path)
        if any(marker in text for marker in unsplash.FORBIDDEN_MARKERS):
            raise SystemExit(f"{panel}: forbidden sample source {path}")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    for number in range(args.start, args.end + 1):
        panel = root / f"xxd-panel-{number:03d}"
        if not panel.is_dir():
            continue
        brief = (panel / "references/original-prompt/zh-CN.md").read_text(encoding="utf-8").strip()
        rows = []
        for source in load_sources(root, number):
            rows.append(
                {
                    "sample": source["sample"],
                    "image": source["file"],
                    "size": source["size"],
                    "prompt": brief + "\n\n" + delivery_for(source["size"]),
                }
            )
        out = root / "tmp" / "imagegen" / f"{number}" / "manifest.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{number}: queued {len(rows)} Unsplash slots")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
