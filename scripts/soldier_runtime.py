#!/usr/bin/env python3
"""Copy and verify the family Soldier runtime contract.

No network, model calls, or advertising edits.

  python3 scripts/soldier_runtime.py apply --root ..
  python3 scripts/soldier_runtime.py apply --root .. --panel 1 --panel 108
  python3 scripts/soldier_runtime.py check --root ..
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALL = HERE.parent
REFS = ALL / 'references'
CANON = HERE / 'canonical'

RUNTIME_NAME = 'soldier-runtime.md'
ADAPTER_ZH = 'soldier-adapter.zh-CN.md'
ADAPTER_EN = 'soldier-adapter.en.md'
SAMPLE_NAME = 'sample-workflow.md'
COMPOSE_NAME = 'compose_panel.py'
IMAGEGEN_NAME = 'configured_imagegen.py'

GENERIC_ACCEPT_PREFIXES = (
    'Inspect every result at full',
    'Inspect every final PNG',
    'Write final PNGs directly',
    'Write every selected final PNG',
    'Write every final PNG',
    'Check this Panel against the complete canonical source',
    'When a result fails',
    'These overlay rules add',
    'Accept only when',
)

OVERLAYS = {
    4: """Panel 004 may start from a theme, place, street, address, coordinates, or a reference image. Treat explicit factual material as the reality anchor. When a real place is named and current facts matter, verify them through an available browsing/research route before prompting; do not invent location features. The source brief still controls all visual decisions.""",
    104: """The complete canvas has exactly two primary parts in comparison modes, or one designed field in `design-only` and wallpaper modes. The TRANSFORMED DESIGN must not contain another photograph, another reality view, an embedded poster, an internal upper/lower comparison, or a second copy of the source. Reject any result that becomes an upper/middle/lower three-part structure or a nested split inside the design region.""",
    106: """The 2–4 visual anchors named by the source brief belong inside one unified transformed composition. They are not separate panels, cards, tiles, or collage cells.""",
    107: """The transformed region must contain one grammatically ordered rebus sentence: printed text fragments and source-derived image words alternate along a clear reading path; each pictured word occupies the missing word's position and is essential to reconstructing the sentence. A replaced word never appears again as printed text. Reject a complete printed sentence with decorative pictures, loose illustrations beside copy, sticker walls, card lists, regular grids, or disconnected collages. Text-free delivery destroys that sentence; use it only when the user explicitly accepts that the result will no longer be an image-word rebus.""",
    113: """Check the shell-module construction explicitly: no more than 200 equal or nearly equal square or near-square fragments, a clear geometric grid with chipped edges, matte natural layers and a dense core dissolving into missing or floating modules. Keep the source brief’s 30%–45% subject scale in the designed region and abundant intentional whitespace. Extract bright, fresh source-derived colours rather than copying muddy tones. Do not accept an ordinary mosaic, game pixels, smooth solid blocks, plastic tiles, strong pearlescence or a fully retained photographic scene as this style.""",
    154: """Check deliberate pixel clusters, visibly stepped contours, the restricted source-derived palette, and a small stamp-like anchor. Do not accept a mosaic-filter photograph as pixel art. If deterministic resizing is needed, preserve hard edges in the design with nearest-neighbor resampling; keep photographic resampling separate. This Panel's `scripts/compose_panel.py` may use NEAREST for the design region; do not replace it with the family LANCZOS helper.""",
    159: """Build imagery from characters, dots and low-resolution raster units, not continuous blocks. Preserve ordered density hierarchy and an integrated experimental bitmap title with sparse supporting copy. Use black/white/grey with 1–3 source-derived accents, a small subject and vast whitespace. Avoid uncontrolled glitch, full-scene tracing and ordinary pasted-on titles. If text-free delivery conflicts with character-built imagery, explain the conflict and resolve it before spending an image call; never silently replace the defining visual language.""",
    180: """The source explicitly prohibits left-right layout and Chinese captions: preserve these defaults. An explicit current request for left-right mode overrides only the layout prohibition; explicitly requested text or locale overrides only the corresponding text restriction. State these overrides in the delivery preamble and retain every other source instruction. For default prompt text, preserve the source brief’s English headline below the stamp and smaller keywords beneath it. Use English unless the current user explicitly overrides the language.""",
    196: """This source brief specifically requires human figures. If the source photograph has no person, resolve suitability before generation; do not invent a person or silently generalise the aesthetic to objects.""",
    197: """This source brief specifically requires human figures. If the source photograph has no person, resolve suitability before generation; do not invent a person or silently generalise the aesthetic to objects.""",
}

SKILL_BODY = """\
# XXD Panel {nnn}

Create finished PNG artwork from the current user-supplied photograph or image directory. Read `references/original-prompt/zh-CN.md` completely immediately before every generation. That Chinese source brief is the sole creative and aesthetic authority; never summarise, translate, blend, or replace it with this file, a README, a sample, or another Panel.

Read `references/soldier-runtime.md` completely immediately before building every generation request. It is the sole family runtime contract for parameters, preference reuse, directory batches, preflight, prompt assembly, bitmap execution, output isolation, and acceptance. This Skill must not write a second art direction or a second runtime.
{overlay}
Write every selected final PNG directly inside one fresh task directory under `~/Desktop/xxd/xxd-panel-{nnn}/` (or the explicit `--out` root). Use collision-safe filenames; do not create source, mode, or size subdirectories and do not generate an automatic contact sheet.

## References

- `references/soldier-runtime.md` — family runtime contract used at generation time
- `references/original-prompt/zh-CN.md` — canonical source brief used at runtime
- `references/original-prompt/README.md` — translation index and authority note
- `references/runtime-preferences.md` — safe delivery-preference reuse
- `references/sample-workflow.md` — sample-artwork maintenance only; never a runtime prerequisite
- `references/xxd-panel-{nnn}-prompt.zh-CN.md` and `.en.md` — delivery adapter notes matching the family runtime blocks
"""


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def soldier_dirs(root: Path, panels: list[int] | None) -> list[Path]:
    if panels:
        dirs = [root / f'xxd-panel-{n:03d}' for n in panels]
        missing = [str(p) for p in dirs if not p.is_dir()]
        if missing:
            raise SystemExit('missing Soldier directories:\n' + '\n'.join(missing))
        return dirs
    return sorted(root.glob('xxd-panel-[0-9][0-9][0-9]'))


def panel_number(directory: Path) -> int:
    m = re.fullmatch(r'xxd-panel-(\d{3})', directory.name)
    if not m:
        raise ValueError(directory)
    return int(m.group(1))


def parse_description(skill_text: str) -> str:
    m = re.search(r'^description:\s*("(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|.+)$', skill_text, re.M)
    if not m:
        raise ValueError('SKILL.md missing description')
    raw = m.group(1).strip()
    if raw.startswith('"') and raw.endswith('"'):
        return json.loads(raw)
    if raw.startswith("'") and raw.endswith("'"):
        return raw[1:-1].replace("''", "'")
    return raw


def is_junk_overlay(para: str) -> bool:
    p = para.strip()
    if not p:
        return True
    if p.startswith('- ') or p.startswith('-\t'):
        return True
    if any(p.startswith(prefix) for prefix in GENERIC_ACCEPT_PREFIXES):
        return True
    if p.startswith('For linked wallpapers'):
        return True
    if 'leaving their exact proportions to the image model' in p:
        return True
    if p.startswith('Use names such as `source-'):
        return True
    return False


def split_paras(block: str) -> list[str]:
    return [p.strip() for p in re.split(r'\n\s*\n', block) if p.strip()]


def extract_style_overlay(skill_text: str) -> str:
    blocks: list[str] = []
    overlay = re.search(
        r'## Panel-specific overlay\n+(.*?)(?:\n## |\Z)', skill_text, re.S)
    if overlay:
        blocks.extend(split_paras(overlay.group(1)))
    for head in (
        r'## Output and acceptance',
        r'## Acceptance gate',
        r'## Acceptance and output',
        r'## Acceptance and delivery',
    ):
        m = re.search(head + r'\n+', skill_text)
        if not m:
            continue
        rest = skill_text[m.end():]
        nxt = re.search(r'\n## ', rest)
        blocks.extend(split_paras(rest[: nxt.start() if nxt else len(rest)]))
        break
    keep = []
    seen = set()
    for para in blocks:
        if is_junk_overlay(para):
            continue
        key = re.sub(r'\s+', ' ', para)
        if key in seen:
            continue
        seen.add(key)
        keep.append(para)
    return '\n\n'.join(keep).strip()


def overlay_markdown(nnn: int, extracted: str) -> str:
    parts: list[str] = []
    hardcoded = OVERLAYS.get(nnn, '').strip()
    if hardcoded:
        parts.append(hardcoded)
    for para in split_paras(extracted):
        if is_junk_overlay(para):
            continue
        compact = re.sub(r'\s+', ' ', para)
        already = re.sub(r'\s+', ' ', '\n'.join(parts))
        if compact in already:
            continue
        prefix = compact[:80]
        if prefix and any(prefix in re.sub(r'\s+', ' ', p) or re.sub(r'\s+', ' ', p)[:80] in compact for p in parts):
            continue
        parts.append(para)
    if not parts:
        return ''
    body = '\n\n'.join(parts)
    return (
        '\n## Panel-specific overlay\n\n'
        f'{body}\n\n'
        'These overlay rules add to `references/soldier-runtime.md`. '
        'They never replace the source brief or the family runtime contract.\n'
    )


def render_skill(nnn: int, description: str, extracted: str) -> str:
    quoted = json.dumps(description, ensure_ascii=False)
    overlay = overlay_markdown(nnn, extracted)
    body = SKILL_BODY.format(nnn=f'{nnn:03d}', overlay=overlay)
    return (
        f'---\nname: xxd-panel-{nnn:03d}\ndescription: {quoted}\n---\n\n{body}'
    )


def render_adapter(template: str, nnn: int) -> str:
    return template.replace('{nnn}', f'{nnn:03d}')


def copy_if_changed(src: Path, dest: Path) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.read_bytes() == src.read_bytes():
        return False
    shutil.copy2(src, dest)
    return True


def write_if_changed(dest: Path, text: str) -> bool:
    data = text.encode()
    if dest.exists() and dest.read_bytes() == data:
        return False
    dest.write_text(text)
    return True


def apply_one(directory: Path, runtime: Path, zh_t: str, en_t: str, sample: Path,
              compose: Path, imagegen: Path) -> list[str]:
    nnn = panel_number(directory)
    changed = []
    skill_path = directory / 'SKILL.md'
    old_skill = skill_path.read_text() if skill_path.exists() else ''
    description = parse_description(old_skill) if old_skill else (
        f'Create XXD Panel {nnn:03d} raster artwork from one image or a directory batch '
        'while treating the bundled original style brief as the sole aesthetic authority. '
        f'Use when the user invokes xxd-panel-{nnn:03d} or requests the exact Panel {nnn:03d} style.'
    )
    extracted = extract_style_overlay(old_skill) if old_skill else ''
    if write_if_changed(skill_path, render_skill(nnn, description, extracted)):
        changed.append('SKILL.md')
    refs = directory / 'references'
    if copy_if_changed(runtime, refs / RUNTIME_NAME):
        changed.append(f'references/{RUNTIME_NAME}')
    if write_if_changed(refs / f'xxd-panel-{nnn:03d}-prompt.zh-CN.md', render_adapter(zh_t, nnn)):
        changed.append(f'references/xxd-panel-{nnn:03d}-prompt.zh-CN.md')
    if write_if_changed(refs / f'xxd-panel-{nnn:03d}-prompt.en.md', render_adapter(en_t, nnn)):
        changed.append(f'references/xxd-panel-{nnn:03d}-prompt.en.md')
    sample_dest = refs / SAMPLE_NAME
    if not sample_dest.exists():
        copy_if_changed(sample, sample_dest)
        changed.append(f'references/{SAMPLE_NAME}')
    scripts = directory / 'scripts'
    if copy_if_changed(imagegen, scripts / IMAGEGEN_NAME):
        changed.append(f'scripts/{IMAGEGEN_NAME}')
    if nnn != 154:
        if copy_if_changed(compose, scripts / COMPOSE_NAME):
            changed.append(f'scripts/{COMPOSE_NAME}')
    return changed


def apply(root: Path, panels: list[int] | None) -> int:
    runtime = REFS / RUNTIME_NAME
    zh_t = (REFS / ADAPTER_ZH).read_text()
    en_t = (REFS / ADAPTER_EN).read_text()
    sample = REFS / SAMPLE_NAME
    compose = CANON / COMPOSE_NAME
    imagegen = CANON / IMAGEGEN_NAME
    for required in (runtime, sample, compose, imagegen):
        if not required.is_file():
            raise SystemExit(f'missing canonical file: {required}')
    n_changed = 0
    for directory in soldier_dirs(root, panels):
        changed = apply_one(directory, runtime, zh_t, en_t, sample, compose, imagegen)
        if changed:
            n_changed += 1
            print(f'{directory.name}: ' + ', '.join(changed))
        else:
            print(f'{directory.name}: unchanged')
    print(f'updated {n_changed} Soldier repositories')
    return 0


def check_contamination(path: Path, nnn: int) -> list[str]:
    text = path.read_text()
    fails = []
    if path.name == IMAGEGEN_NAME:
        if not re.search(r'MAX_RESPONSE_BYTES\s*=\s*100\s*\*\s*1024\s*\*\s*1024', text):
            fails.append(f'{path}: MAX_RESPONSE_BYTES is not 100 MiB')
        if nnn != 100 and re.search(rf'MAX_RESPONSE_BYTES\s*=\s*{nnn}\b', text):
            fails.append(f'{path}: panel-number contamination in MAX_RESPONSE_BYTES')
    if path.name == COMPOSE_NAME:
        if nnn == 154:
            if 'NEAREST' not in text and 'Image.Resampling.NEAREST' not in text:
                fails.append(f'{path}: Panel 154 helper must keep nearest-neighbor design resampling')
            return fails
        if nnn != 100 and re.search(rf'axis_length \* {nnn}\b', text):
            fails.append(f'{path}: panel-number contamination in seam percentage')
        if nnn != 100 and re.search(rf'{nnn} - first\b', text):
            fails.append(f'{path}: panel-number contamination in 50/50 verdict')
        if 'axis_length * 100' not in text:
            fails.append(f'{path}: missing canonical 50/50 percentage using * 100')
    return fails


def check(root: Path, panels: list[int] | None) -> int:
    runtime = REFS / RUNTIME_NAME
    zh_t = (REFS / ADAPTER_ZH).read_text()
    en_t = (REFS / ADAPTER_EN).read_text()
    compose = CANON / COMPOSE_NAME
    imagegen = CANON / IMAGEGEN_NAME
    runtime_hash = sha(runtime)
    compose_hash = sha(compose)
    imagegen_hash = sha(imagegen)
    fails: list[str] = []
    dirs = soldier_dirs(root, panels)
    catalog = (root / 'xxd-panel-all' / 'references' / 'panel-catalog.md')
    if not catalog.is_file():
        catalog = REFS / 'panel-catalog.md'
    catalog_text = catalog.read_text() if catalog.is_file() else ''
    for directory in dirs:
        nnn = panel_number(directory)
        skill = directory / 'SKILL.md'
        if not skill.is_file():
            fails.append(f'{directory}: missing SKILL.md')
            continue
        skill_text = skill.read_text()
        if f'name: xxd-panel-{nnn:03d}' not in skill_text:
            fails.append(f'{skill}: frontmatter name mismatch')
        if 'Read `references/soldier-runtime.md` completely' not in skill_text:
            fails.append(f'{skill}: missing soldier-runtime read instruction')
        if f'~/Desktop/xxd/xxd-panel-{nnn:03d}/' not in skill_text:
            fails.append(f'{skill}: missing numbered output root')
        if nnn in OVERLAYS and '## Panel-specific overlay' not in skill_text:
            fails.append(f'{skill}: missing required overlay for Panel {nnn:03d}')
        copied = directory / 'references' / RUNTIME_NAME
        if not copied.is_file():
            fails.append(f'{copied}: missing')
        elif sha(copied) != runtime_hash:
            fails.append(f'{copied}: differs from canonical soldier-runtime.md')
        for lang, template in (('zh-CN', zh_t), ('en', en_t)):
            adapter = directory / 'references' / f'xxd-panel-{nnn:03d}-prompt.{lang}.md'
            if not adapter.is_file():
                fails.append(f'{adapter}: missing')
                continue
            text = adapter.read_text()
            expected = render_adapter(template, nnn)
            if text != expected:
                fails.append(f'{adapter}: does not match family adapter template')
            if '50:50' not in text:
                fails.append(f'{adapter}: missing 50:50 comparison geometry')
            if 'OUTPUT MODE: TOP_BOTTOM' not in text and '输出模式：TOP_BOTTOM' not in text:
                fails.append(f'{adapter}: missing TOP_BOTTOM mode block')
        if not (directory / 'references' / SAMPLE_NAME).is_file():
            fails.append(f'{directory}: missing references/{SAMPLE_NAME}')
        fails.extend(check_contamination(directory / 'scripts' / IMAGEGEN_NAME, nnn))
        fails.extend(check_contamination(directory / 'scripts' / COMPOSE_NAME, nnn))
        if nnn != 154 and sha(directory / 'scripts' / COMPOSE_NAME) != compose_hash:
            fails.append(f'{directory / "scripts" / COMPOSE_NAME}: differs from canonical helper')
        if sha(directory / 'scripts' / IMAGEGEN_NAME) != imagegen_hash:
            fails.append(f'{directory / "scripts" / IMAGEGEN_NAME}: differs from canonical helper')
        if catalog_text and not re.search(rf'^\| {nnn:03d} \|', catalog_text, re.M):
            fails.append(f'panel-catalog.md: missing Panel {nnn:03d}')
    if fails:
        print('\n'.join(fails))
        print(f'{len(fails)} problem(s) in {len(dirs)} Soldier(s)')
        return 1
    print(f'ok: {len(dirs)} Soldier(s) match the family runtime contract')
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('apply', 'check'))
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--panel', type=int, action='append')
    args = parser.parse_args()
    root = args.root.resolve()
    if args.command == 'apply':
        return apply(root, args.panel)
    return check(root, args.panel)


if __name__ == '__main__':
    sys.exit(main())
