#!/usr/bin/env python3
"""Read-only sample inventory and generation-input checks; never calls a model."""
import argparse
import hashlib
import json
import re
from pathlib import Path


def audit(root, start, end):
    errors = []
    hashes = {}
    report = []
    for number in range(start, end + 1):
        panel = root / f'xxd-panel-{number:03d}'
        if not panel.is_dir():
            continue
        images = sorted((panel / 'assets/examples').glob('sample-*.png'))
        for image in images:
            digest = hashlib.sha256(image.read_bytes()).hexdigest()
            if digest in hashes:
                errors.append(f'Duplicate artwork: {image} == {hashes[digest]}')
            hashes[digest] = str(image)
        manifest = root / f'tmp/imagegen/{number}/manifest.json'
        missing = []
        if manifest.exists():
            brief = (panel / 'references/original-prompt/zh-CN.md').read_text().strip()
            seen = set()
            for row in json.loads(manifest.read_text()):
                sample = row['sample']
                if sample in seen:
                    errors.append(f'{number}: duplicate queue slot {sample}')
                seen.add(sample)
                if not row.get('prompt', '').startswith(brief):
                    errors.append(f'{number}/{sample}: complete canonical prompt missing or stale')
                image_path = str(row['image'])
                if any(marker in image_path for marker in ('陈翔海报', 'tmp/imagegen/170')):
                    errors.append(f'{number}/{sample}: forbidden shared sample queue {image_path}')
                if not Path(row['image']).is_file():
                    errors.append(f'{number}/{sample}: source image missing')
                if not (panel / f'assets/examples/sample-{sample:02d}.png').exists():
                    missing.append(sample)
        readmes = sorted(panel.glob('README*.md'))
        linked = 0
        stale_claims = ('This compute-saving batch', '未生成示例图片',
                        '作例画像も生成していません', '예시 이미지를 생성하지 않았습니다',
                        'دون استدعاء نموذج صور')
        for readme in readmes:
            content = readme.read_text()
            links = re.findall(r'!\[[^\]]*\]\((assets/examples/sample-[^)]+)\)', content)
            if not links:
                continue
            linked += 1
            if any(claim in content for claim in stale_claims):
                errors.append(f'{readme}: gallery contradicts stale no-generation claim')
            if content.find('assets/examples/sample-') < content.find('</div>'):
                errors.append(f'{readme}: gallery misplaced inside title block')
            for link in links:
                if not (panel / link).is_file():
                    errors.append(f'{readme}: missing gallery image {link}')
        report.append(dict(panel=number, existing=len(images), linked_readmes=linked,
                           queued=manifest.exists(), missing_slots=missing))
    return dict(panels=report, errors=errors)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('.'))
    parser.add_argument('--start', type=int, default=159)
    parser.add_argument('--end', type=int, default=216)
    args = parser.parse_args()
    result = audit(args.root.resolve(), args.start, args.end)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(bool(result['errors']))
