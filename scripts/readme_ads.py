#!/usr/bin/env python3
"""Check Soldier README advertisements; emit an apply_patch patch to repair them.

No dependencies, network, model calls, or direct file writes.
  python3 scripts/readme_ads.py --root ..
  python3 scripts/readme_ads.py --root .. --panel 156 --patch
Review/apply the emitted patch, then rerun the checker before publication.
"""
from pathlib import Path
import argparse
import difflib
import re

NAMES = ('README.md', 'README.en.md', 'README.ja.md', 'README.ko.md', 'README.ar.md')
HEADINGS = ('许可证', 'License', 'ライセンス', '라이선스', 'الترخيص')
START, END = '<!-- xxd-readme-ads:start -->', '<!-- xxd-readme-ads:end -->'
TEMPLATES = Path(__file__).resolve().parents[1] / 'references/readme-ads'
REQUIRED = ('xxd-panel-all', '699', 'wx.zsxq.com/group/15554814142882',
            'vip.xiaoxiaodong.ai', 'xiaoxiaodong.pages.dev/assets/wechat-qr.png',
            'xxd-panel-command-system:start')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--panel', type=int, action='append')
    parser.add_argument('--patch', action='store_true', help='print patch; never write files')
    args = parser.parse_args()
    root = args.root.resolve()
    dirs = ([root / f'xxd-panel-{n:03}' for n in args.panel] if args.panel else
            sorted(root.glob('xxd-panel-[0-9][0-9][0-9]')))
    failures, patches, count = [], [], 0
    if not dirs:
        parser.error('no Soldier repositories found')
    for directory in dirs:
        for name, heading in zip(NAMES, HEADINGS):
            path = directory / name
            if not path.is_file():
                failures.append(f'{path}: missing README'); continue
            old = path.read_text(); count += 1
            if re.search(r'100\s*元|CNY\s*100|100\s*يوان', old):
                failures.append(f'{path}: obsolete separate General price; only 699/year membership is permitted'); continue
            template = (TEMPLATES / name).read_text().strip()
            rewards = ('wechat-reward-qr.png', 'alipay-reward-qr.png') if name == 'README.md' else ('buy-me-a-coffee-qr.png',)
            if START in old or END in old:
                if old.count(START) != 1 or old.count(END) != 1 or old.index(START) > old.index(END):
                    failures.append(f'{path}: invalid advertisement markers'); continue
                first, last = old.index(START), old.index(END) + len(END)
                new = old[:first] + template + old[last:]
            elif all(token in old for token in REQUIRED + rewards):
                continue  # Preserve legacy blocks; do not rewrite unrelated old documents.
            elif 'wx.zsxq.com/' in old or 'wechat-qr.png' in old:
                failures.append(f'{path}: partial legacy advertisement needs manual review'); continue
            else:
                match = re.search(r'^## '+re.escape(heading)+r'\s*$', old, re.M)
                if not match:
                    failures.append(f'{path}: missing license insertion anchor'); continue
                new = old[:match.start()] + template + '\n\n' + old[match.start():]
            if new != old:
                failures.append(f'{path}: advertisement missing or differs from template')
                diff = list(difflib.unified_diff(old.splitlines(), new.splitlines(), n=3))[2:]
                patches.append(f'*** Update File: {path}\n' + '\n'.join('@@' if line.startswith('@@') else line for line in diff))
    if args.patch:
        if patches:
            print('*** Begin Patch\n' + '\n'.join(patches) + '\n*** End Patch')
        return 0 if len(patches) == len(failures) else 1
    for failure in failures:
        print(failure)
    print(f'{count} README files checked; {len(failures)} issue(s)')
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
