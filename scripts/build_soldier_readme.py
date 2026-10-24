#!/usr/bin/env python3
"""Render a Soldier's five READMEs from its style profile and the family template.

Each Soldier keeps only what is its own in `references/readme-profile.json`:
the style name, a one-line tagline, what the design looks like, search traits,
and which photos suit it. Everything shared (install, image setup, phrases,
FAQ, parameters) lives here, so every Soldier explains itself the same way.

Kept from the current README: sample captions, X links on the author's
samples, and the license section. The advertising block always comes from
`references/readme-ads/`. No network or model calls.

  python3 scripts/build_soldier_readme.py --root .. --panel 1            # write
  python3 scripts/build_soldier_readme.py --root .. --panel 1 --check    # diff only
  python3 scripts/build_soldier_readme.py --root .. --panel 1 --out-suffix .preview
"""
from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ADS = HERE.parent / 'references' / 'readme-ads'
ADS_START, ADS_END = '<!-- xxd-readme-ads:start -->', '<!-- xxd-readme-ads:end -->'
FILES = {'zh-CN': 'README.md', 'en': 'README.en.md', 'ja': 'README.ja.md', 'ko': 'README.ko.md', 'ar': 'README.ar.md'}
LANG_LINKS = (('zh-CN', 'README.md', '简体中文'), ('en', 'README.en.md', 'English'),
              ('ja', 'README.ja.md', '日本語'), ('ko', 'README.ko.md', '한국어'), ('ar', 'README.ar.md', 'العربية'))
PROMPT_LANGS = (('zh-CN', '中文原文'), ('en', 'English'), ('ja', '日本語'), ('ko', '한국어'), ('ar', 'العربية'))
SHOWN = 4  # samples per layout before the "more" fold

T = {
    'zh-CN': {
        'license': '许可证', 'colon': '：', 'locale': 'zh-CN', 'locale2': 'en-US',
        'hero_note': '上半是原照片，下半是这个风格画出来的样子。',
        'what': '这是什么',
        'what_intro': '一个给 AI Agent（Claude Code、Codex 等）用的 Skill。你给它一张照片，它按 Panel {nnn} 的原始提示词画出一张 PNG 成品。',
        'look': '画成什么样', 'traits': '关键词',
        'modes': '能出哪些图',
        'modes_text': '上下对照（上原图、下设计）、左右对照、只要设计图，或一套手机／平板／电脑／手表壁纸。可以多选，比例和像素随你定。',
        'not': '不是什么', 'not_text': '不是滤镜，也不是套模板：每张都从你的照片重新画，一张照片一个独立任务。',
        'start': '三步用起来',
        'step1': '**1. 安装。** Claude Code、Codex 等支持 Skills 的 Agent 都能用：',
        'step1_after': '装完重开一次 Agent 会话。也可以 `git clone` 本仓库，再把目录链接到 `~/.claude/skills/xxd-panel-{nnn}` 或 `~/.codex/skills/xxd-panel-{nnn}`。',
        'step2': '**2. 确认 Agent 能生图。** 这个 Skill 不自带生图模型，用的是你 Agent 的生图能力，首选 GPT Image 2。',
        'step2_codex': 'Codex 开着内置生图时直接能用。',
        'step2_other': 'Claude Code 等没有内置生图的 Agent，需要接一个 OpenAI 兼容的生图接口，五分钟配好，见[没有内置生图怎么配](#{anchor})。',
        'step2_after': '不确定也可以直接用。不能生图时 Skill 会先停下来告诉你，不会白跑。',
        'step3': '**3. 发照片，说一句话：**',
        'step3_say': '用 xxd-panel-{nnn} 把这张照片做成 3:4 上下对照海报，配中文标题。',
        'step3_after': '说清楚了就直接出图；没说到的（版式、比例、文字）它会问你，通常一两个问题。成品是 PNG，放在 `~/Desktop/xxd/xxd-panel-{nnn}/` 下本次任务的新文件夹里。',
        'fit': '什么照片效果好', 'good': '效果好', 'poor': '不太合适',
        'samples': '样张',
        'samples_intro': '下面每张都是这个 Skill 用一张照片生成的成品。上下对照和左右对照用的是不同的照片。',
        'tb': '上下对照：上原照片，下设计', 'lr': '左右对照：左原照片，右设计',
        'x': '作者原始样张', 'x_note': '小小东在 X 上发布这个风格时的样张，点图可看原帖。',
        'other': '其他样张',
        'more': '再看 {n} 张',
        'say': '常用说法',
        'say_intro': '不用记参数，直接说就行：',
        'say_head': ('你想要', '直接这样说'),
        'phrases': (
            ('上下对照', '做成 3:4 上下对照'),
            ('左右对照', '做成 16:9 左右对照，左边放原图'),
            ('只要设计图', '只要设计，不要原图，9:16 竖版'),
            ('一套壁纸', '做一套手机、平板、电脑、手表壁纸，风格连起来'),
            ('一次多种比例', '同一张做 1:1、3:4、16:9 各一张'),
            ('用自己的文字', '标题就写「让风经过这里」，一个字都别改'),
            ('不要文字', '不要任何文字'),
            ('指定文字语言', '文字用日语'),
            ('整个文件夹', '把这个文件夹里的照片都做成上下对照'),
            ('沿用上次', '沿用上次的设置'),
        ),
        'cli_intro': '习惯命令行也行，参数和上面一一对应：',
        'cli_more': '全部参数见[参数参考](#{anchor})。',
        'faq': '常见问题',
        'faqs': (
            ('一定要放原照片吗？', '不用。说「只要设计图」或者做壁纸，整张都是设计。'),
            ('文字是谁写的？', '默认由生图模型看着你的照片现写，你只定语言。要用自己的字就直说，会一字不改；也可以完全不要字。看起来像事实的信息（地名、日期、数字）只用你给的或照片里看得见的，不会编。'),
            ('不满意怎么办？', '说「再来一张」。它会从原照片重新画，而不是在上一张上修改，所以每次结果都不一样。'),
            ('批量会不会串？', '不会。每张照片单独生成，不借用别的照片的颜色、文字或构图。整批只问一次设置。'),
            ('我的照片会发到哪里？', '只发给你自己的 Agent 所用的生图模型。Skill 不往别处上传，也不在输出里显示接口地址和密钥。'),
            ('和其他 Panel 是什么关系？', 'XXD Panel 是一组风格，一个编号一种，互不影响，可以只装你喜欢的。想让 AI 按照片推荐风格，或者一次比较几个风格，用总目录 [xxd-panel-all](https://github.com/nevertoday/xxd-panel-all)。'),
        ),
        'prompt': '原始提示词',
        'prompt_text': '这个风格完全由小小东写的[原始提示词](references/original-prompt/zh-CN.md)决定。Skill 只在后面追加你选的版式、尺寸和文字设置，不总结、不翻译、不改写它。',
        'prompt_trans': '阅读译文（只供阅读，不参与出图）：',
        'setup': '没有内置生图怎么配',
        'setup_intro': '需要一个支持 `gpt-image-2`（或兼容模型）的 OpenAI 兼容接口和它的 API Key。下面单独建一份配置，不影响你 Codex 本身的设置：',
        'setup_url': '或你的兼容接口', 'setup_env': '写进 ~/.zshrc 或 ~/.bashrc，让 Agent 也能读到', 'setup_key': '你的密钥',
        'setup_check': '重开终端和 Agent 后，在本 Skill 目录里检查一次：',
        'setup_ok': '输出 `"ok":true` 就是通了；它只显示是否可用，不会打印地址和密钥。如果你的 Codex 已经通过兼容接口出图，不需要这一步。',
        'ref': '参数参考',
        'ref_rows': (
            ('`--mode`', '`top-bottom` 上下对照 · `left-right` 左右对照 · `design-only` 只要设计 · `wallpaper-pack` 四端壁纸；可多选'),
            ('`--size`', '`auto` 智能推荐 · `source` 跟随原图 · `1:1` `3:4` `4:3` `4:5` `5:4` `2:3` `3:2` `9:16` `16:9` `21:9` `5:7` `7:5` · 准确像素如 `2160x3840`；可多选'),
            ('`--text`', '`prompt` 模型按照片写 · `exact` 用你的原文（配合 `--copy "…"`） · `none` 不要文字'),
            ('`--locale`', '文字语言，如 `zh-CN` `en-US` `ja-JP` `ko-KR` `ar`'),
            ('`--wallpaper`', '`linked` 四张风格连贯 · `independent` 四张各自独立'),
            ('`--wallpaper-size`', '指定设备像素，如 `phone=1440x3200,desktop=3840x2160`'),
            ('`--out`', '换一个输出根目录（默认 `~/Desktop/xxd/xxd-panel-{nnn}/`）'),
            ('`--prefs`', '`last` 沿用上次 · `edit` 在上次基础上改 · `new` 重新选 · `off` 这次不记住 · `clear` 清除记录'),
        ),
        'ref_head': ('参数', '取值'),
        'ref_notes': (
            '参数齐全时不再提问，缺什么只问什么。`photo.jpg` 换成文件夹路径就是批量。',
            '多选会逐个生成：2 种模式 × 3 种比例 = 6 张，每张都按自己的画布重新构图，不是裁出来的。',
            '对照图严格 50:50：通常模型只画设计那一半，再由脚本把原照片原样拼上，所以分界在正中、原照片不会被改。',
            '文件名形如 `source-001-street-top-bottom-3x4-1152x1536.png`，全部平铺在一个任务文件夹里。',
            '只记住版式、尺寸、文字方式和语言这些设置，不记照片、文案和密钥。',
        ),
    },
    'en': {
        'license': 'License', 'colon': ':', 'locale': 'en-US', 'locale2': 'ja-JP',
        'hero_note': 'Top: the original photo. Bottom: the same photo in this style.',
        'what': 'What it is',
        'what_intro': 'A Skill for AI agents such as Claude Code and Codex. Give it a photo and it paints a finished PNG following the original Panel {nnn} prompt.',
        'look': 'What it looks like', 'traits': 'Keywords',
        'modes': 'What you can make',
        'modes_text': 'A top–bottom comparison (photo above, design below), a left–right comparison, the design alone, or a wallpaper set for phone, tablet, desktop and watch. Pick several at once, at any ratio or exact pixel size.',
        'not': 'What it is not', 'not_text': 'Not a filter and not a template: every image is redrawn from your photo, and each photo is its own job.',
        'start': 'Get started in three steps',
        'step1': '**1. Install.** Works with Claude Code, Codex and other agents that support Skills:',
        'step1_after': 'Then restart your agent session. You can also `git clone` this repository and link the folder to `~/.claude/skills/xxd-panel-{nnn}` or `~/.codex/skills/xxd-panel-{nnn}`.',
        'step2': '**2. Make sure your agent can generate images.** This Skill has no image model of its own; it uses your agent\'s image generation, preferably GPT Image 2.',
        'step2_codex': 'Codex works as is when its built-in image generation is on.',
        'step2_other': 'Claude Code and other agents without built-in image generation need an OpenAI-compatible image API. It takes about five minutes: see [Setting up image generation](#{anchor}).',
        'step2_after': 'Not sure? Just try it. If images can\'t be generated, the Skill stops and tells you before doing any work.',
        'step3': '**3. Send a photo and say one sentence:**',
        'step3_say': 'Use xxd-panel-{nnn} to turn this photo into a 3:4 top–bottom poster with an English title.',
        'step3_after': 'If your request is complete, it starts right away; anything you left out (layout, ratio, text) it asks about, usually in one or two questions. Results are PNGs in a new folder under `~/Desktop/xxd/xxd-panel-{nnn}/`.',
        'fit': 'Which photos work best', 'good': 'Works well', 'poor': 'Not a good fit',
        'samples': 'Samples',
        'samples_intro': 'Each image below is a finished result this Skill made from one photo. The top–bottom and left–right sets use different photos.',
        'tb': 'Top–bottom: photo above, design below', 'lr': 'Left–right: photo left, design right',
        'x': 'The author\'s original samples', 'x_note': 'Posted by Xiaoxiaodong on X when this style was released. Click an image to see the post.',
        'other': 'Other samples',
        'more': 'Show {n} more',
        'say': 'Just say it',
        'say_intro': 'No parameters to memorise. Say what you want:',
        'say_head': ('You want', 'Say'),
        'phrases': (
            ('Top–bottom comparison', 'Make a 3:4 top–bottom comparison'),
            ('Left–right comparison', 'Make a 16:9 left–right comparison, photo on the left'),
            ('Design only', 'Just the design, no photo, 9:16 portrait'),
            ('A wallpaper set', 'Make matching wallpapers for phone, tablet, desktop and watch'),
            ('Several ratios', 'Make this one at 1:1, 3:4 and 16:9'),
            ('Your own text', 'Use the title “Let the wind pass through” exactly as written'),
            ('No text', 'No text at all'),
            ('Text language', 'Write the text in Japanese'),
            ('A whole folder', 'Turn every photo in this folder into a top–bottom comparison'),
            ('Same as last time', 'Use my settings from last time'),
        ),
        'cli_intro': 'Prefer the command line? The flags map one to one:',
        'cli_more': 'All flags are listed under [Parameters](#{anchor}).',
        'faq': 'FAQ',
        'faqs': (
            ('Does the original photo have to appear?', 'No. Ask for “design only” or a wallpaper set and the whole canvas is design.'),
            ('Who writes the text?', 'By default the image model writes it from your photo; you only choose the language. Give your own words and they are used exactly; or ask for no text. Anything that looks factual (places, dates, numbers) comes only from you or from what is visible in the photo, never invented.'),
            ('What if I don\'t like the result?', 'Say “one more”. It redraws from the original photo instead of editing the last result, so every attempt is different.'),
            ('Do photos in a batch mix together?', 'No. Each photo is generated on its own and never borrows another photo\'s colours, text or layout. Settings are asked once for the whole batch.'),
            ('Where do my photos go?', 'Only to the image model your agent uses. The Skill uploads nothing elsewhere and never prints endpoints or keys.'),
            ('How does this relate to other Panels?', 'XXD Panels are a family of styles, one per number, fully independent; install only the ones you like. To have AI recommend a style for a photo, or compare several at once, use the catalog [xxd-panel-all](https://github.com/nevertoday/xxd-panel-all).'),
        ),
        'prompt': 'Original prompt',
        'prompt_text': 'This style is defined entirely by Xiaoxiaodong\'s [original prompt](references/original-prompt/zh-CN.md) (in Chinese). The Skill only appends the layout, size and text settings you choose; it never summarises, translates or rewrites the prompt.',
        'prompt_trans': 'Reading translations (for reading only; never sent to the image model): ',
        'setup': 'Setting up image generation',
        'setup_intro': 'You need an OpenAI-compatible API that serves `gpt-image-2` (or a compatible model) and its API key. This creates a separate config and leaves your Codex settings alone:',
        'setup_url': 'or your compatible endpoint', 'setup_env': 'add to ~/.zshrc or ~/.bashrc so your agent can read them', 'setup_key': 'your-key',
        'setup_check': 'Reopen your terminal and agent, then check once from this Skill\'s folder:',
        'setup_ok': '`"ok":true` means it works. The check only reports readiness; it never prints the endpoint or key. If your Codex already generates images through a compatible API, skip this step.',
        'ref': 'Parameters',
        'ref_rows': (
            ('`--mode`', '`top-bottom` · `left-right` · `design-only` · `wallpaper-pack` (phone, tablet, desktop, watch); combine freely'),
            ('`--size`', '`auto` recommended · `source` match the photo · `1:1` `3:4` `4:3` `4:5` `5:4` `2:3` `3:2` `9:16` `16:9` `21:9` `5:7` `7:5` · exact pixels such as `2160x3840`; combine freely'),
            ('`--text`', '`prompt` written from the photo · `exact` your words (with `--copy "…"`) · `none` no text'),
            ('`--locale`', 'text language, e.g. `zh-CN` `en-US` `ja-JP` `ko-KR` `ar`'),
            ('`--wallpaper`', '`linked` a matching set · `independent` four separate designs'),
            ('`--wallpaper-size`', 'device pixels, e.g. `phone=1440x3200,desktop=3840x2160`'),
            ('`--out`', 'another output root (default `~/Desktop/xxd/xxd-panel-{nnn}/`)'),
            ('`--prefs`', '`last` reuse · `edit` start from last time · `new` choose again · `off` don\'t remember this time · `clear` forget'),
        ),
        'ref_head': ('Flag', 'Values'),
        'ref_notes': (
            'With every value given, nothing is asked; otherwise only the missing values are. Pass a folder instead of `photo.jpg` to batch.',
            'Combinations are generated one by one: 2 modes × 3 sizes = 6 images, each composed for its own canvas rather than cropped.',
            'Comparisons are exactly 50:50. Usually the model paints only the design half and a script places the untouched photo beside it, so the split is centred and the photo is unchanged.',
            'Files are named like `source-001-street-top-bottom-3x4-1152x1536.png`, all in one flat task folder.',
            'Only layout, size, text mode and language are remembered, never photos, copy or keys.',
        ),
    },
    'ja': {
        'license': 'ライセンス', 'colon': '：', 'locale': 'ja-JP', 'locale2': 'en-US',
        'hero_note': '上が元の写真、下がこのスタイルで描き直したものです。',
        'what': 'これは何か',
        'what_intro': 'Claude Code や Codex などの AI エージェント向け Skill です。写真を 1 枚渡すと、Panel {nnn} の原文プロンプトに沿って PNG の完成作品を描きます。',
        'look': 'どんな絵になるか', 'traits': 'キーワード',
        'modes': '作れるもの',
        'modes_text': '上下比較（上に写真、下にデザイン）、左右比較、デザインのみ、またはスマホ／タブレット／PC／ウォッチの壁紙セット。複数選択でき、比率やピクセル数も自由です。',
        'not': 'これは違う', 'not_text': 'フィルターでもテンプレートでもありません。毎回あなたの写真から描き直し、写真 1 枚ごとに独立したタスクです。',
        'start': '3 ステップで始める',
        'step1': '**1. インストール。** Claude Code、Codex など Skills 対応のエージェントで使えます：',
        'step1_after': 'インストール後、エージェントのセッションを開き直してください。このリポジトリを `git clone` して `~/.claude/skills/xxd-panel-{nnn}` または `~/.codex/skills/xxd-panel-{nnn}` にリンクしても使えます。',
        'step2': '**2. エージェントが画像を生成できるか確認。** この Skill 自体は画像モデルを持たず、エージェントの画像生成（GPT Image 2 推奨）を使います。',
        'step2_codex': 'Codex は内蔵の画像生成が有効ならそのまま使えます。',
        'step2_other': 'Claude Code など内蔵の画像生成がないエージェントは、OpenAI 互換の画像 API が必要です。5 分ほどで設定できます：[画像生成の設定](#{anchor})。',
        'step2_after': 'わからなければそのまま試してください。生成できない場合は、作業を始める前に Skill が止まって知らせます。',
        'step3': '**3. 写真を送って、ひとこと：**',
        'step3_say': 'xxd-panel-{nnn} でこの写真を 3:4 の上下比較ポスターにして、日本語のタイトルを付けて。',
        'step3_after': '指示がそろっていればすぐ生成し、足りない点（レイアウト、比率、文字）は 1〜2 問ほど質問します。完成した PNG は `~/Desktop/xxd/xxd-panel-{nnn}/` の新しいフォルダに保存されます。',
        'fit': '向いている写真', 'good': '向いている', 'poor': 'あまり向いていない',
        'samples': 'サンプル',
        'samples_intro': '下の画像はすべて、この Skill が写真 1 枚から作った完成作品です。上下比較と左右比較では別の写真を使っています。',
        'tb': '上下比較：上が写真、下がデザイン', 'lr': '左右比較：左が写真、右がデザイン',
        'x': '作者のオリジナルサンプル', 'x_note': 'このスタイルの公開時に小小東が X に投稿したサンプルです。画像をクリックすると元の投稿を開きます。',
        'other': 'その他のサンプル',
        'more': 'さらに {n} 枚を見る',
        'say': 'こう言えば OK',
        'say_intro': 'パラメータを覚える必要はありません。そのまま伝えてください：',
        'say_head': ('やりたいこと', 'こう言う'),
        'phrases': (
            ('上下比較', '3:4 の上下比較にして'),
            ('左右比較', '16:9 の左右比較で、左に写真'),
            ('デザインのみ', '写真なしでデザインだけ、9:16 縦長'),
            ('壁紙セット', 'スマホ、タブレット、PC、ウォッチの壁紙を統一感のあるセットで'),
            ('複数の比率', '同じ写真で 1:1、3:4、16:9 を 1 枚ずつ'),
            ('自分の文字', 'タイトルは「風の通り道」、一字も変えないで'),
            ('文字なし', '文字は一切入れないで'),
            ('文字の言語', '文字は英語で'),
            ('フォルダごと', 'このフォルダの写真を全部上下比較にして'),
            ('前回と同じ', '前回の設定で'),
        ),
        'cli_intro': 'コマンドラインが好みなら、パラメータは上と一対一で対応します：',
        'cli_more': 'すべてのパラメータは[パラメータ一覧](#{anchor})にあります。',
        'faq': 'よくある質問',
        'faqs': (
            ('元の写真は必ず入りますか？', 'いいえ。「デザインだけ」や壁紙なら、画面全体がデザインになります。'),
            ('文字は誰が書くのですか？', '既定では画像モデルが写真を見て書き、あなたは言語だけを選びます。自分の文字を指定すれば一字も変えずに使い、文字なしにもできます。事実に見える情報（地名、日付、数字）は、あなたが渡したものか写真に写っているものだけを使い、作りません。'),
            ('気に入らなかったら？', '「もう 1 枚」と言ってください。前の結果を直すのではなく元の写真から描き直すので、毎回違う結果になります。'),
            ('まとめて処理すると混ざりませんか？', '混ざりません。写真ごとに個別に生成し、ほかの写真の色、文字、構図を借りません。設定は一括で 1 回だけ聞きます。'),
            ('写真はどこに送られますか？', 'エージェントが使う画像モデルにだけ送られます。Skill はほかへアップロードせず、接続先やキーも表示しません。'),
            ('ほかの Panel との関係は？', 'XXD Panel は番号ごとに 1 つのスタイルで、互いに独立しています。好きなものだけ入れてかまいません。写真に合うスタイルを AI に選ばせたい、複数を比べたいときは、カタログ [xxd-panel-all](https://github.com/nevertoday/xxd-panel-all) を使ってください。'),
        ),
        'prompt': '原文プロンプト',
        'prompt_text': 'このスタイルは小小東が書いた[原文プロンプト](references/original-prompt/zh-CN.md)（中国語）だけで決まります。Skill はあなたが選んだレイアウト、サイズ、文字の設定を末尾に足すだけで、要約・翻訳・書き換えはしません。',
        'prompt_trans': '参考訳（読むためのもので、画像生成には使いません）：',
        'setup': '画像生成の設定',
        'setup_intro': '`gpt-image-2`（または互換モデル）を提供する OpenAI 互換 API とその API キーが必要です。次の手順は別の設定ファイルを作るので、Codex 本体の設定には影響しません：',
        'setup_url': 'または互換エンドポイント', 'setup_env': '~/.zshrc か ~/.bashrc に書き、エージェントからも読めるようにする', 'setup_key': 'あなたのキー',
        'setup_check': 'ターミナルとエージェントを開き直してから、この Skill のフォルダで一度確認します：',
        'setup_ok': '`"ok":true` なら成功です。結果は使えるかどうかだけで、接続先やキーは表示されません。Codex がすでに互換 API で画像を生成できるなら、この手順は不要です。',
        'ref': 'パラメータ一覧',
        'ref_rows': (
            ('`--mode`', '`top-bottom` 上下比較 · `left-right` 左右比較 · `design-only` デザインのみ · `wallpaper-pack` 4 端末の壁紙；複数選択可'),
            ('`--size`', '`auto` おすすめ · `source` 写真に合わせる · `1:1` `3:4` `4:3` `4:5` `5:4` `2:3` `3:2` `9:16` `16:9` `21:9` `5:7` `7:5` · ピクセル指定（例 `2160x3840`）；複数選択可'),
            ('`--text`', '`prompt` 写真から書く · `exact` あなたの文字（`--copy "…"` と併用） · `none` 文字なし'),
            ('`--locale`', '文字の言語。例：`zh-CN` `en-US` `ja-JP` `ko-KR` `ar`'),
            ('`--wallpaper`', '`linked` 統一感のあるセット · `independent` 4 枚それぞれ独立'),
            ('`--wallpaper-size`', '端末ごとのピクセル。例：`phone=1440x3200,desktop=3840x2160`'),
            ('`--out`', '出力先のルートを変更（既定は `~/Desktop/xxd/xxd-panel-{nnn}/`）'),
            ('`--prefs`', '`last` 前回どおり · `edit` 前回から変更 · `new` 選び直す · `off` 今回は記録しない · `clear` 記録を消す'),
        ),
        'ref_head': ('パラメータ', '値'),
        'ref_notes': (
            '値がそろっていれば質問せず、足りないものだけを聞きます。`photo.jpg` の代わりにフォルダを渡すと一括処理になります。',
            '組み合わせは 1 枚ずつ生成します。2 モード × 3 サイズ = 6 枚で、どれも切り抜きではなくキャンバスごとに構図を組み直します。',
            '比較画像は正確に 50:50 です。通常はモデルがデザイン側だけを描き、スクリプトが元の写真をそのまま隣に並べるので、境目は中央で写真も変わりません。',
            'ファイル名は `source-001-street-top-bottom-3x4-1152x1536.png` のような形式で、すべて 1 つのタスクフォルダに平置きされます。',
            '記録するのはレイアウト、サイズ、文字の方式と言語だけで、写真、文字、キーは残しません。',
        ),
    },
    'ko': {
        'license': '라이선스', 'colon': ':', 'locale': 'ko-KR', 'locale2': 'en-US',
        'hero_note': '위는 원본 사진, 아래는 이 스타일로 다시 그린 모습입니다.',
        'what': '무엇인가요',
        'what_intro': 'Claude Code, Codex 같은 AI 에이전트용 Skill입니다. 사진 한 장을 주면 Panel {nnn}의 원본 프롬프트대로 완성된 PNG를 그립니다.',
        'look': '어떤 그림이 되나요', 'traits': '키워드',
        'modes': '만들 수 있는 것',
        'modes_text': '위아래 비교(위 사진, 아래 디자인), 좌우 비교, 디자인만, 또는 휴대폰·태블릿·PC·워치 배경화면 세트. 여러 개를 함께 고를 수 있고 비율과 픽셀도 자유입니다.',
        'not': '이런 것은 아닙니다', 'not_text': '필터도 템플릿도 아닙니다. 매번 사진에서 새로 그리며, 사진 한 장이 하나의 독립된 작업입니다.',
        'start': '세 단계로 시작하기',
        'step1': '**1. 설치.** Claude Code, Codex 등 Skills를 지원하는 에이전트에서 쓸 수 있습니다:',
        'step1_after': '설치 후 에이전트 세션을 다시 시작하세요. 이 저장소를 `git clone`한 뒤 `~/.claude/skills/xxd-panel-{nnn}` 또는 `~/.codex/skills/xxd-panel-{nnn}`에 링크해도 됩니다.',
        'step2': '**2. 에이전트가 이미지를 생성할 수 있는지 확인.** 이 Skill에는 자체 이미지 모델이 없고, 에이전트의 이미지 생성(GPT Image 2 권장)을 사용합니다.',
        'step2_codex': 'Codex는 내장 이미지 생성이 켜져 있으면 바로 쓸 수 있습니다.',
        'step2_other': 'Claude Code처럼 내장 이미지 생성이 없는 에이전트는 OpenAI 호환 이미지 API가 필요합니다. 5분 정도면 됩니다: [이미지 생성 설정](#{anchor}).',
        'step2_after': '잘 모르겠다면 그냥 써 보세요. 생성할 수 없으면 작업을 시작하기 전에 Skill이 멈추고 알려 줍니다.',
        'step3': '**3. 사진을 보내고 한 문장으로 말하기:**',
        'step3_say': 'xxd-panel-{nnn}으로 이 사진을 3:4 위아래 비교 포스터로 만들고 한국어 제목을 붙여 줘.',
        'step3_after': '요청이 충분하면 바로 생성하고, 빠진 것(레이아웃, 비율, 글자)은 보통 한두 가지만 묻습니다. 결과 PNG는 `~/Desktop/xxd/xxd-panel-{nnn}/` 아래 새 폴더에 저장됩니다.',
        'fit': '잘 맞는 사진', 'good': '잘 맞아요', 'poor': '잘 맞지 않아요',
        'samples': '샘플',
        'samples_intro': '아래 이미지는 모두 이 Skill이 사진 한 장으로 만든 완성작입니다. 위아래 비교와 좌우 비교는 서로 다른 사진을 썼습니다.',
        'tb': '위아래 비교: 위 사진, 아래 디자인', 'lr': '좌우 비교: 왼쪽 사진, 오른쪽 디자인',
        'x': '작가의 원본 샘플', 'x_note': '이 스타일을 공개할 때 샤오샤오둥이 X에 올린 샘플입니다. 이미지를 누르면 원래 게시물이 열립니다.',
        'other': '기타 샘플',
        'more': '{n}장 더 보기',
        'say': '이렇게 말하면 됩니다',
        'say_intro': '파라미터를 외울 필요 없이 그대로 말하세요:',
        'say_head': ('원하는 것', '이렇게 말하기'),
        'phrases': (
            ('위아래 비교', '3:4 위아래 비교로 만들어 줘'),
            ('좌우 비교', '16:9 좌우 비교, 왼쪽에 사진'),
            ('디자인만', '사진 없이 디자인만, 9:16 세로'),
            ('배경화면 세트', '휴대폰, 태블릿, PC, 워치 배경화면을 통일된 세트로'),
            ('여러 비율', '같은 사진으로 1:1, 3:4, 16:9 한 장씩'),
            ('내 글자 그대로', '제목은 「바람이 지나가는 곳」, 한 글자도 바꾸지 마'),
            ('글자 없음', '글자는 하나도 넣지 마'),
            ('글자 언어', '글자는 일본어로'),
            ('폴더 전체', '이 폴더의 사진을 전부 위아래 비교로'),
            ('지난번과 같이', '지난번 설정 그대로'),
        ),
        'cli_intro': '명령줄이 편하다면 파라미터가 위와 일대일로 대응합니다:',
        'cli_more': '전체 파라미터는 [파라미터 목록](#{anchor})에 있습니다.',
        'faq': '자주 묻는 질문',
        'faqs': (
            ('원본 사진이 꼭 들어가나요?', '아니요. "디자인만"이나 배경화면을 고르면 화면 전체가 디자인입니다.'),
            ('글자는 누가 쓰나요?', '기본적으로 이미지 모델이 사진을 보고 쓰고, 여러분은 언어만 고릅니다. 직접 쓴 글자를 주면 한 글자도 바꾸지 않고, 글자 없이도 만들 수 있습니다. 사실처럼 보이는 정보(지명, 날짜, 숫자)는 여러분이 준 것이나 사진에 보이는 것만 쓰고 지어내지 않습니다.'),
            ('마음에 들지 않으면요?', '"한 장 더"라고 하세요. 이전 결과를 고치는 대신 원본 사진에서 다시 그리므로 매번 결과가 다릅니다.'),
            ('여러 장을 한꺼번에 하면 섞이지 않나요?', '섞이지 않습니다. 사진마다 따로 생성하고 다른 사진의 색, 글자, 구도를 빌리지 않습니다. 설정은 한 번만 묻습니다.'),
            ('제 사진은 어디로 가나요?', '에이전트가 쓰는 이미지 모델로만 갑니다. Skill은 다른 곳에 올리지 않고 접속 주소나 키도 표시하지 않습니다.'),
            ('다른 Panel과는 어떤 관계인가요?', 'XXD Panel은 번호마다 스타일이 하나씩인 독립된 모음입니다. 마음에 드는 것만 설치해도 됩니다. 사진에 맞는 스타일을 AI가 추천하게 하거나 여러 개를 비교하려면 카탈로그 [xxd-panel-all](https://github.com/nevertoday/xxd-panel-all)을 쓰세요.'),
        ),
        'prompt': '원본 프롬프트',
        'prompt_text': '이 스타일은 샤오샤오둥이 쓴 [원본 프롬프트](references/original-prompt/zh-CN.md)(중국어)만으로 정해집니다. Skill은 여러분이 고른 레이아웃, 크기, 글자 설정을 뒤에 덧붙일 뿐, 요약하거나 번역하거나 고쳐 쓰지 않습니다.',
        'prompt_trans': '참고 번역(읽기용이며 이미지 생성에는 쓰지 않음): ',
        'setup': '이미지 생성 설정',
        'setup_intro': '`gpt-image-2`(또는 호환 모델)를 제공하는 OpenAI 호환 API와 그 API 키가 필요합니다. 아래 방법은 별도 설정을 만들어 Codex 자체 설정에는 영향을 주지 않습니다:',
        'setup_url': '또는 호환 엔드포인트', 'setup_env': '~/.zshrc 또는 ~/.bashrc에 넣어 에이전트도 읽을 수 있게', 'setup_key': '내-키',
        'setup_check': '터미널과 에이전트를 다시 연 뒤, 이 Skill 폴더에서 한 번 확인하세요:',
        'setup_ok': '`"ok":true`가 나오면 성공입니다. 사용 가능 여부만 보여 주고 주소나 키는 출력하지 않습니다. Codex가 이미 호환 API로 이미지를 만들고 있다면 이 단계는 필요 없습니다.',
        'ref': '파라미터 목록',
        'ref_rows': (
            ('`--mode`', '`top-bottom` 위아래 비교 · `left-right` 좌우 비교 · `design-only` 디자인만 · `wallpaper-pack` 4종 배경화면; 여러 개 선택 가능'),
            ('`--size`', '`auto` 추천 · `source` 사진 비율 · `1:1` `3:4` `4:3` `4:5` `5:4` `2:3` `3:2` `9:16` `16:9` `21:9` `5:7` `7:5` · 정확한 픽셀(예 `2160x3840`); 여러 개 선택 가능'),
            ('`--text`', '`prompt` 사진을 보고 작성 · `exact` 내 글자 그대로(`--copy "…"`와 함께) · `none` 글자 없음'),
            ('`--locale`', '글자 언어. 예: `zh-CN` `en-US` `ja-JP` `ko-KR` `ar`'),
            ('`--wallpaper`', '`linked` 통일된 세트 · `independent` 네 장 각각 독립'),
            ('`--wallpaper-size`', '기기별 픽셀. 예: `phone=1440x3200,desktop=3840x2160`'),
            ('`--out`', '출력 루트 변경(기본 `~/Desktop/xxd/xxd-panel-{nnn}/`)'),
            ('`--prefs`', '`last` 지난번 그대로 · `edit` 지난번에서 수정 · `new` 새로 고르기 · `off` 이번엔 기억 안 함 · `clear` 기록 삭제'),
        ),
        'ref_head': ('파라미터', '값'),
        'ref_notes': (
            '값이 모두 있으면 묻지 않고, 빠진 것만 묻습니다. `photo.jpg` 대신 폴더를 주면 일괄 처리합니다.',
            '조합은 한 장씩 생성합니다. 모드 2개 × 크기 3개 = 6장이며, 잘라 낸 것이 아니라 캔버스마다 구도를 새로 잡습니다.',
            '비교 이미지는 정확히 50:50입니다. 보통 모델은 디자인 쪽만 그리고 스크립트가 원본 사진을 그대로 옆에 붙이므로, 경계는 가운데이고 사진은 바뀌지 않습니다.',
            '파일 이름은 `source-001-street-top-bottom-3x4-1152x1536.png` 형식이며 모두 작업 폴더 하나에 평평하게 저장됩니다.',
            '레이아웃, 크기, 글자 방식과 언어만 기억하고 사진, 문구, 키는 저장하지 않습니다.',
        ),
    },
    'ar': {
        'license': 'الترخيص', 'colon': ':', 'locale': 'ar', 'locale2': 'en-US',
        'hero_note': 'في الأعلى الصورة الأصلية، وفي الأسفل الصورة نفسها بهذا الأسلوب.',
        'what': 'ما هذا',
        'what_intro': 'مهارة (Skill) لوكلاء الذكاء الاصطناعي مثل Claude Code وCodex. أعطها صورة فترسم عملاً نهائياً بصيغة PNG وفق الموجّه الأصلي للوحة {nnn}.',
        'look': 'كيف تبدو النتيجة', 'traits': 'كلمات مفتاحية',
        'modes': 'ما يمكنك صنعه',
        'modes_text': 'مقارنة علوية سفلية (الصورة فوق والتصميم تحت)، أو مقارنة يمين ويسار، أو التصميم وحده، أو مجموعة خلفيات للهاتف والجهاز اللوحي والحاسوب والساعة. يمكنك اختيار أكثر من نوع وبأي نسبة أو أبعاد.',
        'not': 'ما ليس هو', 'not_text': 'ليس فلتراً ولا قالباً: كل صورة تُرسم من جديد من صورتك، وكل صورة مهمة مستقلة.',
        'start': 'ابدأ في ثلاث خطوات',
        'step1': '**1. التثبيت.** يعمل مع Claude Code وCodex وغيرهما من الوكلاء الداعمين للمهارات:',
        'step1_after': 'ثم أعد تشغيل جلسة الوكيل. يمكنك أيضاً تنفيذ `git clone` لهذا المستودع وربط المجلد بـ `~/.claude/skills/xxd-panel-{nnn}` أو `~/.codex/skills/xxd-panel-{nnn}`.',
        'step2': '**2. تأكد أن وكيلك يستطيع توليد الصور.** لا تحتوي هذه المهارة على نموذج صور خاص بها، بل تستخدم قدرة وكيلك على توليد الصور، ويُفضَّل GPT Image 2.',
        'step2_codex': 'يعمل Codex مباشرة عندما يكون توليد الصور المدمج مفعّلاً.',
        'step2_other': 'أما Claude Code والوكلاء الذين لا يملكون توليد صور مدمجاً فيحتاجون إلى واجهة صور متوافقة مع OpenAI، ويستغرق الإعداد نحو خمس دقائق: راجع [إعداد توليد الصور](#{anchor}).',
        'step2_after': 'لست متأكداً؟ جرّب مباشرة. إذا تعذّر التوليد فستتوقف المهارة وتخبرك قبل أن تبدأ أي عمل.',
        'step3': '**3. أرسل صورة وقل جملة واحدة:**',
        'step3_say': 'استخدم xxd-panel-{nnn} لتحويل هذه الصورة إلى ملصق علوي سفلي بنسبة 3:4 مع عنوان بالعربية.',
        'step3_after': 'إذا كان طلبك كاملاً فسيبدأ فوراً، وما تركته (التخطيط أو النسبة أو النص) سيسألك عنه في سؤال أو سؤالين عادةً. تُحفظ النتائج بصيغة PNG في مجلد جديد داخل `~/Desktop/xxd/xxd-panel-{nnn}/`.',
        'fit': 'الصور الأنسب', 'good': 'تناسبه', 'poor': 'لا تناسبه كثيراً',
        'samples': 'نماذج',
        'samples_intro': 'كل صورة أدناه نتيجة نهائية صنعتها هذه المهارة من صورة واحدة. استُخدمت صور مختلفة للمقارنات العلوية السفلية والجانبية.',
        'tb': 'علوي سفلي: الصورة فوق والتصميم تحت', 'lr': 'يمين ويسار: الصورة يساراً والتصميم يميناً',
        'x': 'النماذج الأصلية للمؤلف', 'x_note': 'نشرها شياوشياودونغ على X عند إطلاق هذا الأسلوب. انقر على الصورة لفتح المنشور.',
        'other': 'نماذج أخرى',
        'more': 'عرض {n} أخرى',
        'say': 'قلها ببساطة',
        'say_intro': 'لا حاجة إلى حفظ المعاملات. قل ما تريد:',
        'say_head': ('تريد', 'قل'),
        'phrases': (
            ('مقارنة علوية سفلية', 'اجعلها مقارنة علوية سفلية بنسبة 3:4'),
            ('مقارنة يمين ويسار', 'اجعلها مقارنة جانبية 16:9 والصورة على اليسار'),
            ('التصميم فقط', 'التصميم فقط بلا صورة، عمودي 9:16'),
            ('مجموعة خلفيات', 'خلفيات متناسقة للهاتف والجهاز اللوحي والحاسوب والساعة'),
            ('عدة نسب', 'اصنع هذه الصورة بنسب 1:1 و3:4 و16:9'),
            ('نصك أنت', 'العنوان «دع الريح تمر» كما هو حرفياً'),
            ('بلا نص', 'بدون أي نص'),
            ('لغة النص', 'اكتب النص باليابانية'),
            ('مجلد كامل', 'حوّل كل صور هذا المجلد إلى مقارنات علوية سفلية'),
            ('مثل المرة السابقة', 'استخدم إعداداتي السابقة'),
        ),
        'cli_intro': 'تفضّل سطر الأوامر؟ المعاملات تقابل ما سبق واحداً بواحد:',
        'cli_more': 'كل المعاملات في قسم [المعاملات](#{anchor}).',
        'faq': 'أسئلة شائعة',
        'faqs': (
            ('هل يجب أن تظهر الصورة الأصلية؟', 'لا. اطلب «التصميم فقط» أو مجموعة خلفيات فتصبح اللوحة كلها تصميماً.'),
            ('من يكتب النص؟', 'افتراضياً يكتبه نموذج الصور انطلاقاً من صورتك، وأنت تختار اللغة فقط. إن أعطيته كلماتك استُخدمت حرفياً، ويمكنك طلب عدم وجود نص. أي معلومة تبدو واقعية (أماكن، تواريخ، أرقام) تأتي منك أو مما يظهر في الصورة فقط، ولا تُختلق.'),
            ('ماذا لو لم تعجبني النتيجة؟', 'قل «واحدة أخرى». يعيد الرسم من الصورة الأصلية بدلاً من تعديل النتيجة السابقة، لذا تختلف كل محاولة.'),
            ('هل تختلط الصور في الدفعة الواحدة؟', 'لا. تُولَّد كل صورة وحدها ولا تستعير ألوان صورة أخرى أو نصها أو تكوينها. وتُسأل عن الإعدادات مرة واحدة للدفعة كلها.'),
            ('إلى أين تذهب صوري؟', 'إلى نموذج الصور الذي يستخدمه وكيلك فقط. لا ترفع المهارة شيئاً إلى أي مكان آخر ولا تعرض العناوين أو المفاتيح.'),
            ('ما علاقة هذا بلوحات Panel الأخرى؟', 'لوحات XXD Panel عائلة من الأساليب، لكل رقم أسلوب مستقل، فثبّت ما يعجبك فقط. لتدع الذكاء الاصطناعي يقترح أسلوباً لصورة أو تقارن عدة أساليب، استخدم الفهرس [xxd-panel-all](https://github.com/nevertoday/xxd-panel-all).'),
        ),
        'prompt': 'الموجّه الأصلي',
        'prompt_text': 'يحدّد هذا الأسلوبَ بالكامل [الموجّهُ الأصلي](references/original-prompt/zh-CN.md) الذي كتبه شياوشياودونغ (بالصينية). تضيف المهارة في آخره فقط إعدادات التخطيط والحجم والنص التي تختارها، ولا تلخّصه أو تترجمه أو تعيد كتابته.',
        'prompt_trans': 'ترجمات للقراءة (للاطلاع فقط ولا تُرسل إلى نموذج الصور): ',
        'setup': 'إعداد توليد الصور',
        'setup_intro': 'تحتاج إلى واجهة متوافقة مع OpenAI تقدّم `gpt-image-2` (أو نموذجاً متوافقاً) ومفتاح API لها. الخطوات التالية تنشئ إعداداً منفصلاً ولا تمس إعدادات Codex:',
        'setup_url': 'or your compatible endpoint', 'setup_env': 'add to ~/.zshrc or ~/.bashrc so your agent can read them', 'setup_key': 'your-key',
        'setup_check': 'أعد فتح الطرفية والوكيل، ثم تحقّق مرة واحدة من مجلد هذه المهارة:',
        'setup_ok': 'إذا ظهر `"ok":true` فقد نجح الإعداد. يعرض الفحص الجاهزية فقط ولا يطبع العنوان أو المفتاح. إذا كان Codex يولّد الصور أصلاً عبر واجهة متوافقة فلا حاجة إلى هذه الخطوة.',
        'ref': 'المعاملات',
        'ref_rows': (
            ('`--mode`', '`top-bottom` علوي سفلي · `left-right` يمين ويسار · `design-only` التصميم فقط · `wallpaper-pack` خلفيات لأربعة أجهزة؛ يمكن الجمع'),
            ('`--size`', '`auto` موصى به · `source` مثل الصورة · `1:1` `3:4` `4:3` `4:5` `5:4` `2:3` `3:2` `9:16` `16:9` `21:9` `5:7` `7:5` · أبعاد دقيقة مثل `2160x3840`؛ يمكن الجمع'),
            ('`--text`', '`prompt` يُكتب من الصورة · `exact` كلماتك (مع `--copy "…"`) · `none` بلا نص'),
            ('`--locale`', 'لغة النص، مثل `zh-CN` `en-US` `ja-JP` `ko-KR` `ar`'),
            ('`--wallpaper`', '`linked` مجموعة متناسقة · `independent` أربعة تصاميم مستقلة'),
            ('`--wallpaper-size`', 'أبعاد كل جهاز، مثل `phone=1440x3200,desktop=3840x2160`'),
            ('`--out`', 'مجلد إخراج آخر (الافتراضي `~/Desktop/xxd/xxd-panel-{nnn}/`)'),
            ('`--prefs`', '`last` كالسابق · `edit` تعديل السابق · `new` اختيار جديد · `off` لا تحفظ هذه المرة · `clear` امسح السجل'),
        ),
        'ref_head': ('المعامل', 'القيم'),
        'ref_notes': (
            'إذا اكتملت القيم فلا أسئلة، وإلا تُسأل عن الناقص فقط. مرّر مجلداً بدلاً من `photo.jpg` للمعالجة الدفعية.',
            'تُولَّد التركيبات واحدة واحدة: نمطان × ثلاثة أحجام = 6 صور، كل منها مركّبة للوحتها لا مقصوصة.',
            'المقارنات 50:50 بدقة. عادةً يرسم النموذج نصف التصميم فقط ويضع برنامج الصورة الأصلية كما هي بجانبه، فيكون الفاصل في المنتصف ولا تتغير الصورة.',
            'أسماء الملفات بهذا الشكل `source-001-street-top-bottom-3x4-1152x1536.png`، وكلها في مجلد مهمة واحد.',
            'يُحفظ التخطيط والحجم وطريقة النص واللغة فقط، ولا تُحفظ الصور أو النصوص أو المفاتيح.',
        ),
    },
}


def image_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data[:8] == b'\x89PNG\r\n\x1a\n':
        return struct.unpack('>II', data[16:24])
    i = 2  # JPEG: walk markers to the first SOF
    while i < len(data) - 9:
        if data[i] != 0xFF:
            i += 1
            continue
        marker = data[i + 1]
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            h, w = struct.unpack('>HH', data[i + 5:i + 9])
            return w, h
        i += 2 + struct.unpack('>H', data[i + 2:i + 4])[0]
    raise ValueError(f'unknown image size: {path}')


def samples(directory: Path, old: str) -> dict[str, list[dict]]:
    """Group samples by layout; keep each one's caption and X link from the current README."""
    groups: dict[str, list[dict]] = {'x': [], 'tb': [], 'lr': [], 'other': []}
    for path in sorted((directory / 'assets' / 'examples').glob('sample-*.*')):
        if path.suffix.lower() not in ('.png', '.jpg', '.jpeg', '.webp'):
            continue
        rel = f'./assets/examples/{path.name}'
        cap = re.search(re.escape(rel) + r'[^>]*>(?:</a>)?\s*<br>\s*<sub>(.*?)</sub>', old)
        link = re.search(r'<a href="(https://x\.com/[^"]+)">\s*<img src="' + re.escape(rel), old)
        item = {'src': rel, 'caption': cap.group(1).strip() if cap else '', 'link': link.group(1) if link else ''}
        w, h = image_size(path)
        if item['link']:
            groups['x'].append(item)
        elif w > h:  # comparisons: 16:9 left-right, or a Panel's own wide ratio (144 uses 7:6 halves)
            groups['lr'].append(item)
        elif h > w:
            groups['tb'].append(item)
        else:
            groups['other'].append(item)
    return groups


def cell(item: dict, alt: str) -> str:
    label = f'{alt} · {item["caption"]}' if item['caption'] else alt
    img = f'<img src="{item["src"]}" alt="{label}">'
    if item['link']:
        img = f'<a href="{item["link"]}">{img}</a>'
    if item['caption']:
        img += f'<br><sub>{item["caption"]}</sub>'
    return f'    <td width="50%">{img}</td>'


def table(items: list[dict], alt: str) -> str:
    rows = []
    for i in range(0, len(items), 2):
        pair = items[i:i + 2]
        rows.append('  <tr>\n' + '\n'.join(cell(it, alt) for it in pair) + '\n  </tr>')
    return '<table>\n' + '\n'.join(rows) + '\n</table>'


def gallery(items: list[dict], alt: str, more: str) -> str:
    out = table(items[:SHOWN], alt)
    if len(items) > SHOWN:
        rest = items[SHOWN:]
        out += f'\n\n<details>\n<summary>{more.format(n=len(rest))}</summary>\n\n{table(rest, alt)}\n\n</details>'
    return out


def anchor(heading: str) -> str:
    """GitHub's heading anchor: lowercase, drop punctuation, spaces to hyphens."""
    return re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')


def license_section(old: str, heading: str) -> str:
    m = re.search(r'^## ' + re.escape(heading) + r'\s*$', old, re.M)
    if not m:
        raise ValueError(f'missing ## {heading}')
    section = old[m.start():].rstrip()
    return section.removesuffix('</div>').rstrip() + '\n'  # the Arabic RTL wrapper is added again by render


def render(directory: Path, lang: str, profile: dict, old: str) -> str:
    t, p = T[lang], profile[lang]
    nnn = directory.name.removeprefix('xxd-panel-')
    alt = f'XXD Panel {nnn}'
    g = samples(directory, old)
    links = ' · '.join(f'<strong>{label}</strong>' if code == lang else f'<a href="{file}">{label}</a>'
                       for code, file, label in LANG_LINKS)
    hero_items = (g['tb'] or g['x'] or g['lr'])[:2]
    out = [f'<div align="center">\n\n# XXD Panel {nnn}｜{p["name"]}\n\n**{p["tagline"]}**\n\n{links}\n\n</div>\n']
    if hero_items:
        out.append(table(hero_items, alt) + '\n')
        if hero_items[0] in g['tb']:
            out.append(f'<p align="center"><sub>{t["hero_note"]}</sub></p>\n')

    out.append(f'## {t["what"]}\n\n{t["what_intro"].format(nnn=nnn)}\n')
    c = t['colon']
    out.append(f'- **{t["look"]}{c}** {p["look"]}\n- **{t["traits"]}{c}** {" · ".join(p["traits"])}\n'
               f'- **{t["modes"]}{c}** {t["modes_text"]}\n- **{t["not"]}{c}** {t["not_text"]}\n')

    setup_anchor, ref_anchor = anchor(t['setup']), anchor(t['ref'])
    out.append(f'## {t["start"]}\n\n{t["step1"]}\n\n```bash\nnpx skills add https://github.com/nevertoday/xxd-panel-{nnn} --skill xxd-panel-{nnn}\n```\n\n'
               f'{t["step1_after"].format(nnn=nnn)}\n\n{t["step2"]}\n\n- {t["step2_codex"]}\n- {t["step2_other"].format(anchor=setup_anchor)}\n\n'
               f'{t["step2_after"]}\n\n{t["step3"]}\n\n> {t["step3_say"].format(nnn=nnn)}\n\n{t["step3_after"].format(nnn=nnn)}\n')

    out.append(f'## {t["fit"]}\n\n**{t["good"]}**\n\n' + '\n'.join(f'- {x}' for x in p['good']) +
               f'\n\n**{t["poor"]}**\n\n' + '\n'.join(f'- {x}' for x in p['poor']) + '\n')

    out.append(f'## {t["samples"]}\n\n{t["samples_intro"]}\n')
    for key in ('tb', 'lr', 'x', 'other'):
        if g[key]:
            note = f'\n{t["x_note"]}\n' if key == 'x' else ''
            out.append(f'### {t[key]}\n{note}\n{gallery(g[key], alt, t["more"])}\n')

    head = t['say_head']
    out.append(f'## {t["say"]}\n\n{t["say_intro"]}\n\n| {head[0]} | {head[1]} |\n|---|---|\n' +
               '\n'.join(f'| {a} | {b} |' for a, b in t['phrases']) +
               f'\n\n{t["cli_intro"]}\n\n```text\n/xxd-panel-{nnn} photo.jpg --mode top-bottom --size 3:4 --text prompt --locale {t["locale"]}\n'
               f'/xxd-panel-{nnn} photo.jpg --mode design-only --size 9:16 --text none\n'
               f'/xxd-panel-{nnn} ./photos --mode left-right --size 16:9 --text prompt --locale {t["locale2"]}\n```\n\n'
               f'{t["cli_more"].format(anchor=ref_anchor)}\n')

    out.append(f'## {t["faq"]}\n\n' + '\n\n'.join(f'**{q}** {a}' for q, a in t['faqs']) + '\n')

    trans = [(code, label) for code, label in PROMPT_LANGS[1:]
             if (directory / 'references' / 'original-prompt' / f'{code}.md').is_file()]
    prompt = f'## {t["prompt"]}\n\n{t["prompt_text"]}'
    if trans:
        prompt += f'\n\n{t["prompt_trans"]}' + ' · '.join(f'[{label}](references/original-prompt/{code}.md)' for code, label in trans)
    out.append(prompt + '\n')

    out.append(f'## {t["setup"]}\n\n{t["setup_intro"]}\n\n```bash\nmkdir -p ~/.xxd-imagegen\ncat > ~/.xxd-imagegen/config.toml <<\'EOF\'\n'
               f'model_provider = "image"\n\n[model_providers.image]\nbase_url = "https://api.openai.com/v1"   # {t["setup_url"]}\nenv_key = "XXD_IMAGE_API_KEY"\nEOF\n\n'
               f'# {t["setup_env"]}\necho \'export XXD_IMAGEGEN_CODEX_DIR=~/.xxd-imagegen\' >> ~/.zshrc\necho \'export XXD_IMAGE_API_KEY={t["setup_key"]}\' >> ~/.zshrc\n```\n\n'
               f'{t["setup_check"]}\n\n```bash\npython3 scripts/configured_imagegen.py probe\n```\n\n{t["setup_ok"]}\n')

    rh = t['ref_head']
    out.append(f'## {t["ref"]}\n\n| {rh[0]} | {rh[1]} |\n|---|---|\n' +
               '\n'.join(f'| {a} | {b.format(nnn=nnn)} |' for a, b in t['ref_rows']) + '\n\n' +
               '\n'.join(f'- {x}' for x in t['ref_notes']) + '\n')

    out.append((ADS / FILES[lang]).read_text().strip() + '\n')
    out.append(license_section(old, t['license']))
    if lang == 'ar':  # right-to-left from the header to the end, ads and license included
        out[0] = out[0].replace('<div align="center">', '<div align="center" dir="rtl">', 1)
        out[1:] = ['<div dir="rtl">\n'] + out[1:] + ['</div>\n']
    return '\n'.join(out)


def render_meta(directory: Path, profile: dict) -> dict[Path, str]:
    """SKILL.md description and agents/openai.yaml texts, the other places a visitor or agent reads first."""
    nnn = directory.name.removeprefix('xxd-panel-')
    out = {}
    skill = directory / 'SKILL.md'
    text = skill.read_text()
    desc = 'description: ' + json.dumps(profile['skill_description'], ensure_ascii=False)
    out[skill] = re.sub(r'^description:.*$', lambda _: desc, text, count=1, flags=re.M)
    yaml = directory / 'agents' / 'openai.yaml'
    text = yaml.read_text()
    short = '  short_description: ' + json.dumps(profile['short_description'], ensure_ascii=False)
    prompt = '  default_prompt: ' + json.dumps(
        f'Use $xxd-panel-{nnn} to turn my photo into {profile["en"]["name"]} artwork.', ensure_ascii=False)
    text = re.sub(r'^  short_description:.*$', lambda _: short, text, count=1, flags=re.M)
    out[yaml] = re.sub(r'^  default_prompt:.*$', lambda _: prompt, text, count=1, flags=re.M)
    return out


JARGON = ('REALITY VIEW', 'TRANSFORMED DESIGN', '审美权威', '契约', '交付前言', '运行适配器', '垫图', '士兵', '将军',
          'Soldier', 'General', 'source brief', 'authority', 'contract')


def validate(profile: dict, nnn: int) -> list[str]:
    """Shape and plain-language checks for one readme-profile.json."""
    errs = []
    sd = profile.get('skill_description', '')
    if not sd.startswith(f'XXD Panel {nnn:03d}｜') or f'xxd-panel-{nnn:03d}' not in sd or not 200 <= len(sd) <= 1000:
        errs.append('skill_description: start with "XXD Panel NNN｜<English name>:", name xxd-panel-NNN, 200-1000 chars')
    short = profile.get('short_description', '')
    if not short or len(short) > 80 or '\n' in short:
        errs.append('short_description: one line, at most 80 chars')
    for lang in FILES:
        p = profile.get(lang)
        if not isinstance(p, dict):
            errs.append(f'{lang}: missing')
            continue
        for key in ('name', 'tagline', 'look'):
            if not isinstance(p.get(key), str) or not p[key].strip():
                errs.append(f'{lang}.{key}: missing')
        for key, lo, hi in (('traits', 3, 6), ('good', 2, 4), ('poor', 2, 4)):
            v = p.get(key)
            if not isinstance(v, list) or not lo <= len(v) <= hi or not all(isinstance(x, str) and x.strip() for x in v):
                errs.append(f'{lang}.{key}: {lo}-{hi} non-empty strings')
        text = ' '.join(str(v) for v in p.values())
        errs += [f'{lang}: internal jargon "{j}"' for j in JARGON if j in text]
        if '|' in text:
            errs.append(f'{lang}: "|" breaks Markdown tables')
    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--root', type=Path, required=True)
    ap.add_argument('--panel', type=int, action='append', required=True)
    ap.add_argument('--lang', action='append', choices=tuple(FILES), help='default: every language with a profile')
    ap.add_argument('--check', action='store_true', help='report which READMEs would change; write nothing')
    ap.add_argument('--out-suffix', default='', help='write README<suffix>.md beside the real one')
    ap.add_argument('--validate', action='store_true', help='check readme-profile.json only')
    a = ap.parse_args()
    changed = bad = 0
    for n in a.panel:
        directory = a.root.resolve() / f'xxd-panel-{n:03d}'
        profile = json.loads((directory / 'references' / 'readme-profile.json').read_text())
        if a.validate:
            errs = validate(profile, n)
            bad += bool(errs)
            print('\n'.join(f'{directory.name}: {e}' for e in errs) or f'{directory.name}: ok')
            continue
        targets = {}
        for lang in a.lang or [k for k in FILES if k in profile and k in T]:
            path = directory / FILES[lang]
            targets[path] = render(directory, lang, profile, path.read_text())
        if 'skill_description' in profile and not a.lang:
            targets.update(render_meta(directory, profile))
        for path, new in targets.items():
            dest = path.with_name(path.stem + a.out_suffix + path.suffix) if a.out_suffix else path
            if dest.exists() and dest.read_text() == new:
                continue
            changed += 1
            print(f'{"would write" if a.check else "wrote"} {dest}')
            if not a.check:
                dest.write_text(new)
    return 1 if bad or (a.check and changed) else 0


if __name__ == '__main__':
    sys.exit(main())
