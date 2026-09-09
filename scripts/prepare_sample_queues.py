#!/usr/bin/env python3
"""Prepare deterministic, model-free eight-slot sample queues for panels."""
import argparse, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,default=Path('.')); ap.add_argument('--start',type=int,required=True); ap.add_argument('--end',type=int,required=True); a=ap.parse_args(); root=a.root.resolve()
    base=json.loads((root/'tmp/imagegen/170/manifest.json').read_text())
    for n in range(a.start,a.end+1):
        panel=root/f'xxd-panel-{n:03d}'
        if not panel.is_dir(): continue
        brief=(panel/'references/original-prompt/zh-CN.md').read_text().strip()
        rows=[]
        for row in base:
            delivery=('本次交付变量：仅使用附件 Image 1 作为本张独立作品的原始参考图，不引用其他照片、既有结果或其他编号风格。'
                      '生成一张完整 PNG 画布；严格执行当前原稿的上下 50:50 规则。'
                      '文字模式 prompt，目标语种 en-US；禁止第三条带、额外标题栏、底栏、内嵌面板或多图网格。')
            rows.append({'sample':row['sample'],'image':row['image'],'size':row['size'],'prompt':brief+'\n\n'+delivery})
        out=root/f'tmp/imagegen/{n}/manifest.json'; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
        print(f'{n}: queued {len(rows)} independent slots')
if __name__=='__main__': main()
