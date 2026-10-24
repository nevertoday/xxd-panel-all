#!/usr/bin/env python3
"""Render the five xxd-panel-all READMEs: what the family is, how to start, and the style roster.

The roster reads every sibling Soldier's `references/readme-profile.json` (name and
tagline per language) and shows one left-right sample per Soldier as a thumbnail in
`assets/roster/`. Missing thumbnails are made from the Soldier's first wide sample;
existing ones are kept unless `--refresh-thumbs`. Install, image setup and the shared
FAQ answers come from build_soldier_readme.T so the General and Soldiers say the same
thing. The General's own advertising section and license are kept verbatim.

  python3.14 scripts/build_general_readme.py --root ..          # write
  python3.14 scripts/build_general_readme.py --root .. --check  # report only
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

import build_soldier_readme as sb

ALL = Path(__file__).resolve().parents[1]
ADS_START, ADS_END = '<!-- xxd-general-ads:start -->', '<!-- xxd-general-ads:end -->'
ROSTER_START, ROSTER_END = '<!-- xxd-soldier-roster:start -->', '<!-- xxd-soldier-roster:end -->'
# Where the General's advertising section ended before it had markers.
LEGACY_AD_END = {'zh-CN': '安装', 'en': 'Installation', 'ja': 'インストール', 'ko': '설치', 'ar': 'التثبيت'}
THUMB_WIDTH, THUMB_QUALITY = 800, 80
GROUP = 50  # roster entries per fold
COLS = 3
REPO = 'https://github.com/nevertoday/xxd-panel-{nnn}'

G = {
    'zh-CN': {
        'title': '风格总目录',
        'tagline': '{n} 种照片风格的总入口：给它照片和用途，它帮你挑风格、比风格、批量出图。',
        'what': '这是什么',
        'what_intro': 'XXD Panel 是一组把照片重新画成海报、插画和壁纸的 AI Skill，一个编号一种风格，目前有 {n} 个，各自独立。`xxd-panel-all` 是它们的总入口，适合 Claude Code、Codex 等支持 Skills 的 Agent：',
        'bullets': (
            ('帮你选', '给一张照片或一个主题，它从你装好的风格里推荐一个或三个，并说明为什么适合这张图。'),
            ('帮你比', '同一张照片用几种风格各出一张，放在一起看。'),
            ('帮你批量', '给一个文件夹，可以全部用同一种风格，也可以每张自动配最合适的风格。'),
            ('它自己不画', '真正出图的是各个编号的风格 Skill。总目录只负责挑选和分派，不会把几种风格混在一起。'),
        ),
        'start': '三步用起来',
        'step1': '**1. 安装总目录，再装几个你喜欢的风格。** 没装的风格它也能介绍和推荐，但要装上才能出图：',
        'step1_more': '一次装好几个：',
        'step1_after': '装完重开一次 Agent 会话。',
        'step3': '**3. 发照片，说一句话：**',
        'step3_say': '用 xxd-panel-all 看看这张照片适合哪几个风格，推荐三个并说说理由。',
        'step3_after': '选定以后，它把照片交给那个风格的 Skill 出图；版式、比例、文字这些由那个风格接着问你。成品放在 `~/Desktop/xxd/xxd-panel-NNN/` 下。',
        'say_rows': (
            ('推荐风格', '这张照片适合哪个风格？推荐三个，说说理由'),
            ('按感觉找', '有没有黑白线条、留白很多的风格？'),
            ('按用途找', '想做手机壁纸，哪些风格合适？'),
            ('指定编号', '用 062 做这张照片'),
            ('比较几种', '用 001、062、350 各做一张给我比较'),
            ('文件夹，同一风格', '把这个文件夹全部用 014 做成上下对照'),
            ('文件夹，自动配', '这个文件夹里每张照片自动选最合适的风格'),
            ('沿用上次', '沿用上次的设置'),
        ),
        'roster': '全部风格',
        'roster_intro': '共 {n} 个。每张图是该风格的一张左右对照样张（左原照片，右设计），点图进入它的仓库，那里有更多样张和用法。',
        'roster_group': '{a}–{b}',
        'faqs': (
            ('要把全部风格都装上吗？', '不用。装你喜欢的几个就行。没装的风格它照样能介绍、能推荐，只是会标明「未安装」，装上之后才能出图。'),
            ('它怎么判断哪个风格适合？', '看照片里有什么（主体、场景、颜色、文字）和你说的用途与感觉，对照每个风格的说明来挑，并把理由告诉你。不会根据人的长相去猜国籍或喜好。'),
            ('会把几种风格混在一起吗？', '不会。每张图只交给一个风格，按那个风格自己的原始提示词画。'),
            ('和直接用某个风格有什么区别？', '已经知道要哪种，直接用那个编号的 Skill 最快。还没想好、想比较几种、或者要处理一整个文件夹时，用总目录。'),
        ),
        'params': '参数',
        'params_text': '总目录接受和单个风格相同的出图参数（`--mode` `--size` `--text` `--locale` `--wallpaper` `--out`），会原样转给每个风格；完整说明见任意一个风格 README 的「参数参考」。另外支持 `--prefs last|edit|new|off|clear`，作用同单个风格：沿用、修改或忽略上次的设置。只记住版式、尺寸、文字方式和语言，不记照片、文案、所选风格和密钥。',
        'maint': '给维护者',
        'maint_intro': '这个仓库同时保存全家族共用的运行规则和维护脚本，每个风格仓库里都有它们的副本。',
        'maint_rows': (
            ('`references/soldier-runtime.md`', '所有风格共用的出图规则，同步到每个风格仓库'),
            ('`references/panel-catalog.md`', '编号目录，供推荐和检索；不是生图提示词'),
            ('`references/readme-profile-guide.md`', '怎么写一个风格的 `readme-profile.json`'),
            ('`scripts/build_soldier_readme.py`', '从风格档案生成某个风格的五种语言 README、SKILL 描述和 `openai.yaml`'),
            ('`scripts/build_general_readme.py`', '生成本页和风格目录'),
            ('`scripts/soldier_runtime.py`', '把共用规则和脚本同步到全部风格仓库，并检查'),
            ('`scripts/readme_ads.py`', '检查风格 README 的广告模块'),
            ('`scripts/brief_intake.py`', '新建风格前检查原始提示词（只提示，不改写）'),
            ('`scripts/unsplash_sample_sources.py`', '为样张挑选 Unsplash 照片'),
        ),
        'maint_head': ('文件', '用途'),
    },
    'en': {
        'title': 'Style Catalog',
        'tagline': 'One entry point for {n} photo styles: show it a photo and what it is for, and it picks, compares and batches styles for you.',
        'what': 'What it is',
        'what_intro': 'XXD Panels are AI Skills that redraw photos as posters, illustrations and wallpapers, one style per number — {n} so far, each independent. `xxd-panel-all` is their front door, for Claude Code, Codex and other agents that support Skills:',
        'bullets': (
            ('Picks for you', 'Give it a photo or a theme and it recommends one or three of your installed styles, with the reason each fits.'),
            ('Compares', 'Makes the same photo in several styles so you can see them side by side.'),
            ('Batches', 'Give it a folder: one style for everything, or the best style for each photo.'),
            ('Doesn\'t paint itself', 'The numbered style Skills make the images. The catalog only chooses and hands off, and never blends styles.'),
        ),
        'start': 'Get started in three steps',
        'step1': '**1. Install the catalog and a few styles you like.** It can describe and recommend styles you haven\'t installed, but only installed ones can make images:',
        'step1_more': 'Several at once:',
        'step1_after': 'Then restart your agent session.',
        'step3': '**3. Send a photo and say one sentence:**',
        'step3_say': 'Use xxd-panel-all to suggest three styles that suit this photo and say why.',
        'step3_after': 'Once you choose, it hands the photo to that style\'s Skill, which asks about layout, ratio and text. Results go to `~/Desktop/xxd/xxd-panel-NNN/`.',
        'say_rows': (
            ('A recommendation', 'Which style suits this photo? Suggest three and say why'),
            ('Search by feel', 'Any styles with black line and lots of whitespace?'),
            ('Search by use', 'Which styles work for a phone wallpaper?'),
            ('A specific number', 'Use 062 for this photo'),
            ('A comparison', 'Make one each with 001, 062 and 350 so I can compare'),
            ('A folder, one style', 'Turn this whole folder into top–bottom comparisons with 014'),
            ('A folder, auto-matched', 'Pick the best style for each photo in this folder'),
            ('Same as last time', 'Use my settings from last time'),
        ),
        'roster': 'All styles',
        'roster_intro': '{n} in total. Each image is one left–right sample of that style (photo left, design right). Click it to open the style\'s repository for more samples and usage.',
        'roster_group': '{a}–{b}',
        'faqs': (
            ('Do I need to install every style?', 'No. Install the ones you like. Styles you haven\'t installed can still be described and recommended, marked as not installed; install one to make images with it.'),
            ('How does it decide which style fits?', 'It looks at what is in the photo (subject, scene, colour, text) and at the use and feel you describe, compares that with each style\'s description, and tells you why. It never guesses nationality or taste from someone\'s appearance.'),
            ('Will it mix styles together?', 'No. Each image goes to one style, painted with that style\'s own original prompt.'),
            ('Why not use a style directly?', 'If you already know which style you want, its own Skill is quickest. Use the catalog when you are undecided, want to compare, or have a whole folder.'),
        ),
        'params': 'Parameters',
        'params_text': 'The catalog takes the same image flags as a single style (`--mode` `--size` `--text` `--locale` `--wallpaper` `--out`) and passes them unchanged to each style; see "Parameters" in any style\'s README. It also takes `--prefs last|edit|new|off|clear` to reuse, edit or ignore last time\'s settings. Only layout, size, text mode and language are remembered, never photos, copy, chosen styles or keys.',
        'maint': 'For maintainers',
        'maint_intro': 'This repository also holds the rules and scripts shared by the whole family; every style repository carries copies of them.',
        'maint_rows': (
            ('`references/soldier-runtime.md`', 'image-making rules shared by every style, synced into each style repository'),
            ('`references/panel-catalog.md`', 'numbered index for recommending and searching; not an image prompt'),
            ('`references/readme-profile-guide.md`', 'how to write a style\'s `readme-profile.json`'),
            ('`scripts/build_soldier_readme.py`', 'renders a style\'s five READMEs, SKILL description and `openai.yaml` from its profile'),
            ('`scripts/build_general_readme.py`', 'renders this page and the style roster'),
            ('`scripts/soldier_runtime.py`', 'syncs the shared rules and scripts to every style repository, and checks them'),
            ('`scripts/readme_ads.py`', 'checks the advertising block in style READMEs'),
            ('`scripts/brief_intake.py`', 'checks a new style\'s original prompt before it is built (reports only, never edits)'),
            ('`scripts/unsplash_sample_sources.py`', 'picks Unsplash photos for samples'),
        ),
        'maint_head': ('File', 'Purpose'),
    },
    'ja': {
        'title': 'スタイル総合カタログ',
        'tagline': '{n} 種類の写真スタイルの総合入口。写真と用途を伝えれば、スタイル選び、比較、一括生成を手伝います。',
        'what': 'これは何か',
        'what_intro': 'XXD Panel は、写真をポスター、イラスト、壁紙に描き直す AI Skill のシリーズで、番号ごとに 1 つのスタイルがあり、現在 {n} 個、それぞれ独立しています。`xxd-panel-all` はその総合入口で、Claude Code や Codex など Skills 対応のエージェントで使えます：',
        'bullets': (
            ('選ぶ', '写真やテーマを渡すと、インストール済みのスタイルから 1 つか 3 つを、その写真に合う理由とともに勧めます。'),
            ('比べる', '同じ写真を複数のスタイルで 1 枚ずつ作り、並べて見比べられます。'),
            ('まとめて作る', 'フォルダを渡せば、全部を同じスタイルにも、写真ごとに最適なスタイルにもできます。'),
            ('自分では描かない', '実際に描くのは番号付きのスタイル Skill です。カタログは選んで渡すだけで、スタイルを混ぜません。'),
        ),
        'start': '3 ステップで始める',
        'step1': '**1. カタログと、好きなスタイルをいくつかインストール。** 未インストールのスタイルも紹介・推薦はできますが、画像を作れるのはインストール済みのものだけです：',
        'step1_more': 'まとめてインストール：',
        'step1_after': 'インストール後、エージェントのセッションを開き直してください。',
        'step3': '**3. 写真を送って、ひとこと：**',
        'step3_say': 'xxd-panel-all で、この写真に合うスタイルを 3 つ、理由つきで勧めて。',
        'step3_after': '選んだら、写真はそのスタイルの Skill に渡され、レイアウト、比率、文字はそちらが質問します。完成品は `~/Desktop/xxd/xxd-panel-NNN/` に保存されます。',
        'say_rows': (
            ('おすすめ', 'この写真に合うスタイルは？3 つ勧めて理由も'),
            ('雰囲気で探す', '黒い線で余白の多いスタイルはある？'),
            ('用途で探す', 'スマホの壁紙に向くスタイルは？'),
            ('番号を指定', '062 でこの写真を作って'),
            ('比較', '001、062、350 で 1 枚ずつ作って比べたい'),
            ('フォルダ・同じスタイル', 'このフォルダを全部 014 で上下比較に'),
            ('フォルダ・自動', 'このフォルダの写真ごとに最適なスタイルを選んで'),
            ('前回と同じ', '前回の設定で'),
        ),
        'roster': '全スタイル',
        'roster_intro': '全 {n} 個。各画像はそのスタイルの左右比較サンプル 1 枚です（左が写真、右がデザイン）。クリックするとリポジトリが開き、ほかのサンプルや使い方を見られます。',
        'roster_group': '{a}–{b}',
        'faqs': (
            ('全部インストールする必要がありますか？', 'いいえ。好きなものだけで大丈夫です。未インストールのスタイルも「未インストール」と明示して紹介・推薦し、インストールすれば画像を作れます。'),
            ('どうやって合うスタイルを判断しますか？', '写真に写っているもの（主役、場面、色、文字）と、あなたが伝えた用途や雰囲気を、各スタイルの説明と照らし合わせて選び、理由を伝えます。人の外見から国籍や好みを推測することはしません。'),
            ('スタイルが混ざりませんか？', '混ざりません。1 枚の画像は 1 つのスタイルにだけ渡され、そのスタイル自身の原文プロンプトで描かれます。'),
            ('スタイルを直接使うのとの違いは？', '欲しいスタイルが決まっているなら、その番号の Skill を直接使うのが最速です。迷っているとき、比べたいとき、フォルダごと処理したいときはカタログを使ってください。'),
        ),
        'params': 'パラメータ',
        'params_text': 'カタログは単体のスタイルと同じ生成パラメータ（`--mode` `--size` `--text` `--locale` `--wallpaper` `--out`）を受け取り、そのまま各スタイルに渡します。詳しくは各スタイルの README の「パラメータ一覧」を見てください。`--prefs last|edit|new|off|clear` で前回の設定を使う、変える、無視することもできます。記録するのはレイアウト、サイズ、文字の方式と言語だけで、写真、文字、選んだスタイル、キーは残しません。',
        'maint': 'メンテナンス担当者へ',
        'maint_intro': 'このリポジトリには、シリーズ全体で共有するルールとスクリプトも入っています。各スタイルのリポジトリにはその写しがあります。',
        'maint_rows': (
            ('`references/soldier-runtime.md`', '全スタイル共通の生成ルール。各スタイルのリポジトリに同期されます'),
            ('`references/panel-catalog.md`', '推薦と検索のための番号目録。画像生成のプロンプトではありません'),
            ('`references/readme-profile-guide.md`', 'スタイルの `readme-profile.json` の書き方'),
            ('`scripts/build_soldier_readme.py`', 'プロフィールから 5 言語の README、SKILL の説明、`openai.yaml` を生成'),
            ('`scripts/build_general_readme.py`', 'このページとスタイル一覧を生成'),
            ('`scripts/soldier_runtime.py`', '共通ルールとスクリプトを全スタイルのリポジトリに同期・検査'),
            ('`scripts/readme_ads.py`', 'スタイル README の広告ブロックを検査'),
            ('`scripts/brief_intake.py`', '新しいスタイルを作る前に原文プロンプトを検査（指摘のみで書き換えません）'),
            ('`scripts/unsplash_sample_sources.py`', 'サンプル用の Unsplash 写真を選ぶ'),
        ),
        'maint_head': ('ファイル', '用途'),
    },
    'ko': {
        'title': '스타일 총목록',
        'tagline': '{n}가지 사진 스타일의 입구. 사진과 용도를 알려 주면 스타일을 고르고, 비교하고, 한꺼번에 만들어 줍니다.',
        'what': '무엇인가요',
        'what_intro': 'XXD Panel은 사진을 포스터, 일러스트, 배경화면으로 다시 그리는 AI Skill 모음으로, 번호마다 스타일이 하나씩 있고 지금 {n}개가 서로 독립돼 있습니다. `xxd-panel-all`은 그 입구이며 Claude Code, Codex 등 Skills를 지원하는 에이전트에서 씁니다:',
        'bullets': (
            ('골라 줍니다', '사진이나 주제를 주면 설치된 스타일 가운데 하나 또는 세 개를 추천하고, 왜 이 사진에 맞는지 알려 줍니다.'),
            ('비교해 줍니다', '같은 사진을 여러 스타일로 한 장씩 만들어 나란히 볼 수 있습니다.'),
            ('한꺼번에 만듭니다', '폴더를 주면 전부 같은 스타일로, 또는 사진마다 가장 맞는 스타일로 만듭니다.'),
            ('직접 그리지는 않습니다', '실제로 그리는 것은 번호가 붙은 스타일 Skill입니다. 총목록은 고르고 넘겨줄 뿐, 스타일을 섞지 않습니다.'),
        ),
        'start': '세 단계로 시작하기',
        'step1': '**1. 총목록과 마음에 드는 스타일 몇 개를 설치.** 설치하지 않은 스타일도 소개하고 추천할 수 있지만, 이미지는 설치한 스타일로만 만듭니다:',
        'step1_more': '여러 개를 한 번에:',
        'step1_after': '설치 후 에이전트 세션을 다시 시작하세요.',
        'step3': '**3. 사진을 보내고 한 문장으로 말하기:**',
        'step3_say': 'xxd-panel-all로 이 사진에 맞는 스타일 세 개를 이유와 함께 추천해 줘.',
        'step3_after': '고르고 나면 사진은 그 스타일의 Skill로 넘어가고, 레이아웃·비율·글자는 그쪽에서 묻습니다. 결과물은 `~/Desktop/xxd/xxd-panel-NNN/`에 저장됩니다.',
        'say_rows': (
            ('추천받기', '이 사진에 맞는 스타일은? 세 개 추천하고 이유도'),
            ('느낌으로 찾기', '검은 선에 여백이 많은 스타일 있어?'),
            ('용도로 찾기', '휴대폰 배경화면에 어울리는 스타일은?'),
            ('번호 지정', '062로 이 사진을 만들어 줘'),
            ('비교', '001, 062, 350으로 한 장씩 만들어 비교하게 해 줘'),
            ('폴더, 같은 스타일', '이 폴더 전부 014로 위아래 비교로 만들어 줘'),
            ('폴더, 자동 배정', '이 폴더의 사진마다 가장 맞는 스타일을 골라 줘'),
            ('지난번과 같이', '지난번 설정 그대로'),
        ),
        'roster': '전체 스타일',
        'roster_intro': '모두 {n}개. 각 이미지는 그 스타일의 좌우 비교 샘플 한 장입니다(왼쪽 사진, 오른쪽 디자인). 누르면 저장소가 열려 더 많은 샘플과 사용법을 볼 수 있습니다.',
        'roster_group': '{a}–{b}',
        'faqs': (
            ('스타일을 전부 설치해야 하나요?', '아니요. 마음에 드는 것만 설치하면 됩니다. 설치하지 않은 스타일도 "미설치"로 표시해 소개·추천하며, 설치하면 이미지를 만들 수 있습니다.'),
            ('어떤 스타일이 맞는지 어떻게 판단하나요?', '사진에 무엇이 있는지(주인공, 장면, 색, 글자)와 말해 준 용도·느낌을 각 스타일의 설명과 비교해 고르고, 이유를 알려 줍니다. 사람의 외모로 국적이나 취향을 추측하지 않습니다.'),
            ('스타일이 섞이지 않나요?', '섞이지 않습니다. 이미지 한 장은 스타일 하나에만 넘어가고, 그 스타일의 원본 프롬프트로 그려집니다.'),
            ('스타일을 바로 쓰는 것과 무엇이 다른가요?', '원하는 스타일이 정해져 있다면 그 번호의 Skill을 바로 쓰는 게 가장 빠릅니다. 아직 못 정했거나 비교하고 싶거나 폴더 전체를 처리할 때 총목록을 쓰세요.'),
        ),
        'params': '파라미터',
        'params_text': '총목록은 개별 스타일과 같은 생성 파라미터(`--mode` `--size` `--text` `--locale` `--wallpaper` `--out`)를 받아 각 스타일에 그대로 넘깁니다. 자세한 내용은 아무 스타일 README의 "파라미터 목록"을 보세요. `--prefs last|edit|new|off|clear`로 지난번 설정을 쓰거나, 고치거나, 무시할 수도 있습니다. 레이아웃, 크기, 글자 방식과 언어만 기억하고 사진, 문구, 고른 스타일, 키는 저장하지 않습니다.',
        'maint': '관리자용',
        'maint_intro': '이 저장소에는 전체 시리즈가 함께 쓰는 규칙과 스크립트도 있으며, 각 스타일 저장소에 사본이 있습니다.',
        'maint_rows': (
            ('`references/soldier-runtime.md`', '모든 스타일이 함께 쓰는 생성 규칙. 각 스타일 저장소로 동기화'),
            ('`references/panel-catalog.md`', '추천과 검색을 위한 번호 목록. 이미지 생성 프롬프트가 아님'),
            ('`references/readme-profile-guide.md`', '스타일의 `readme-profile.json` 작성법'),
            ('`scripts/build_soldier_readme.py`', '프로필로 5개 언어 README, SKILL 설명, `openai.yaml` 생성'),
            ('`scripts/build_general_readme.py`', '이 페이지와 스타일 목록 생성'),
            ('`scripts/soldier_runtime.py`', '공통 규칙과 스크립트를 모든 스타일 저장소에 동기화하고 검사'),
            ('`scripts/readme_ads.py`', '스타일 README의 광고 블록 검사'),
            ('`scripts/brief_intake.py`', '새 스타일을 만들기 전에 원본 프롬프트 검사(알려 주기만 하고 고치지 않음)'),
            ('`scripts/unsplash_sample_sources.py`', '샘플용 Unsplash 사진 고르기'),
        ),
        'maint_head': ('파일', '용도'),
    },
    'ar': {
        'title': 'فهرس الأساليب',
        'tagline': 'مدخل واحد إلى {n} أسلوباً للصور: أرِه الصورة وقل له الغرض، فيختار الأساليب ويقارنها ويعالج الدفعات عنك.',
        'what': 'ما هذا',
        'what_intro': 'لوحات XXD Panel مهارات ذكاء اصطناعي تعيد رسم الصور ملصقاتٍ ورسوماً وخلفيات، لكل رقم أسلوب مستقل، وعددها حتى الآن {n}. و`xxd-panel-all` هو مدخلها الرئيسي، ويعمل مع Claude Code وCodex وغيرهما من الوكلاء الداعمين للمهارات:',
        'bullets': (
            ('يختار لك', 'أعطه صورة أو موضوعاً فيقترح أسلوباً أو ثلاثة من الأساليب المثبّتة لديك، مع سبب ملاءمة كل منها.'),
            ('يقارن', 'يصنع الصورة نفسها بعدة أساليب لتراها جنباً إلى جنب.'),
            ('يعالج الدفعات', 'أعطه مجلداً: أسلوب واحد للجميع، أو الأسلوب الأنسب لكل صورة.'),
            ('لا يرسم بنفسه', 'مهارات الأساليب المرقّمة هي التي تصنع الصور. الفهرس يختار ويسلّم فقط، ولا يمزج الأساليب.'),
        ),
        'start': 'ابدأ في ثلاث خطوات',
        'step1': '**1. ثبّت الفهرس وبعض الأساليب التي تعجبك.** يمكنه وصف الأساليب غير المثبّتة واقتراحها، لكن الصور لا تُصنع إلا بالأساليب المثبّتة:',
        'step1_more': 'عدة أساليب دفعة واحدة:',
        'step1_after': 'ثم أعد تشغيل جلسة الوكيل.',
        'step3': '**3. أرسل صورة وقل جملة واحدة:**',
        'step3_say': 'استخدم xxd-panel-all لاقتراح ثلاثة أساليب تناسب هذه الصورة مع السبب.',
        'step3_after': 'بعد أن تختار، تُسلَّم الصورة إلى مهارة ذلك الأسلوب، فتسألك عن التخطيط والنسبة والنص. تُحفظ النتائج في `~/Desktop/xxd/xxd-panel-NNN/`.',
        'say_rows': (
            ('اقتراح', 'أي أسلوب يناسب هذه الصورة؟ اقترح ثلاثة مع السبب'),
            ('البحث بالإحساس', 'هل توجد أساليب بخطوط سوداء وفراغ كثير؟'),
            ('البحث بالغرض', 'أي الأساليب تناسب خلفية هاتف؟'),
            ('رقم محدد', 'استخدم 062 لهذه الصورة'),
            ('مقارنة', 'اصنع واحدة بكل من 001 و062 و350 لأقارن'),
            ('مجلد بأسلوب واحد', 'حوّل هذا المجلد كله إلى مقارنات علوية سفلية بالأسلوب 014'),
            ('مجلد بمطابقة تلقائية', 'اختر الأسلوب الأنسب لكل صورة في هذا المجلد'),
            ('مثل المرة السابقة', 'استخدم إعداداتي السابقة'),
        ),
        'roster': 'كل الأساليب',
        'roster_intro': 'المجموع {n}. كل صورة نموذج مقارنة جانبية واحد من ذلك الأسلوب (الصورة يساراً والتصميم يميناً). انقر عليها لفتح مستودع الأسلوب ورؤية مزيد من النماذج وطريقة الاستخدام.',
        'roster_group': '{a}–{b}',
        'faqs': (
            ('هل يجب تثبيت كل الأساليب؟', 'لا. ثبّت ما يعجبك فقط. تُوصف الأساليب غير المثبّتة وتُقترح مع وسمها بأنها غير مثبّتة، وبعد تثبيتها يمكن صنع الصور بها.'),
            ('كيف يقرّر أي أسلوب يناسب؟', 'ينظر إلى ما في الصورة (العنصر والمشهد واللون والنص) وإلى الغرض والإحساس اللذين تصفهما، ويقارن ذلك بوصف كل أسلوب، ثم يخبرك بالسبب. ولا يخمّن الجنسية أو الذوق من مظهر الشخص.'),
            ('هل يمزج الأساليب؟', 'لا. كل صورة تذهب إلى أسلوب واحد، وتُرسم بالموجّه الأصلي لذلك الأسلوب.'),
            ('لماذا لا أستخدم الأسلوب مباشرة؟', 'إذا كنت تعرف الأسلوب الذي تريده فمهارته هي الأسرع. استخدم الفهرس حين لم تقرر بعد، أو تريد المقارنة، أو لديك مجلد كامل.'),
        ),
        'params': 'المعاملات',
        'params_text': 'يقبل الفهرس معاملات الصور نفسها التي يقبلها الأسلوب الواحد (`--mode` `--size` `--text` `--locale` `--wallpaper` `--out`) ويمرّرها كما هي إلى كل أسلوب؛ راجع قسم «المعاملات» في README أي أسلوب. ويقبل أيضاً `--prefs last|edit|new|off|clear` لاستخدام إعدادات المرة السابقة أو تعديلها أو تجاهلها. يُحفظ التخطيط والحجم وطريقة النص واللغة فقط، ولا تُحفظ الصور أو النصوص أو الأساليب المختارة أو المفاتيح.',
        'maint': 'للمشرفين',
        'maint_intro': 'يحتوي هذا المستودع أيضاً على القواعد والبرامج المشتركة بين العائلة كلها، ولكل مستودع أسلوب نسخة منها.',
        'maint_rows': (
            ('`references/soldier-runtime.md`', 'قواعد صنع الصور المشتركة بين كل الأساليب، تُزامَن إلى كل مستودع'),
            ('`references/panel-catalog.md`', 'فهرس مرقّم للاقتراح والبحث، وليس موجّهاً لتوليد الصور'),
            ('`references/readme-profile-guide.md`', 'طريقة كتابة `readme-profile.json` لأسلوب'),
            ('`scripts/build_soldier_readme.py`', 'يولّد ملفات README الخمسة ووصف SKILL و`openai.yaml` من ملف الأسلوب'),
            ('`scripts/build_general_readme.py`', 'يولّد هذه الصفحة وقائمة الأساليب'),
            ('`scripts/soldier_runtime.py`', 'يزامن القواعد والبرامج المشتركة إلى كل مستودعات الأساليب ويفحصها'),
            ('`scripts/readme_ads.py`', 'يفحص كتلة الإعلان في README الأساليب'),
            ('`scripts/brief_intake.py`', 'يفحص الموجّه الأصلي لأسلوب جديد قبل بنائه (ينبّه فقط ولا يعدّل)'),
            ('`scripts/unsplash_sample_sources.py`', 'يختار صور Unsplash للنماذج'),
        ),
        'maint_head': ('الملف', 'الغرض'),
    },
}


def soldiers(root: Path) -> list[tuple[int, Path, dict]]:
    out = []
    for d in sorted(root.glob('xxd-panel-[0-9][0-9][0-9]')):
        prof = d / 'references' / 'readme-profile.json'
        if (d / 'SKILL.md').is_file() and prof.is_file():
            out.append((int(d.name[-3:]), d, json.loads(prof.read_text())))
    return out


def wide_sample(d: Path) -> Path:
    """sample-05 (the family's first left-right slot) when wide, else the first wide plain sample-NN (341+ start top-bottom)."""
    ex = d / 'assets' / 'examples'
    plain = sorted(p for p in ex.glob('sample-*.*') if re.fullmatch(r'sample-\d+\.(png|jpe?g)', p.name))
    for path in [p for p in plain if p.stem == 'sample-05'] + plain:
        w, h = sb.image_size(path)
        if w > h:
            return path
    raise FileNotFoundError(f'no wide sample in {d}')


def write_thumb(src: Path, dest: Path) -> None:
    from PIL import Image  # only needed when a thumbnail is (re)made
    with Image.open(src) as im:
        rgb = im.convert('RGB')
        if rgb.width != THUMB_WIDTH:
            rgb = rgb.resize((THUMB_WIDTH, max(1, round(rgb.height * THUMB_WIDTH / rgb.width))), Image.Resampling.LANCZOS)
        dest.parent.mkdir(parents=True, exist_ok=True)
        rgb.save(dest, format='JPEG', quality=THUMB_QUALITY, optimize=True)


def roster(lang: str, entries: list[tuple[int, Path, dict]]) -> str:
    g = G[lang]
    blocks = []
    for start in range(0, len(entries), GROUP):
        chunk = entries[start:start + GROUP]
        rows = []
        for i in range(0, len(chunk), COLS):
            cells = []
            for n, _, prof in chunk[i:i + COLS]:
                p = prof[lang]
                repo = REPO.format(nnn=f'{n:03d}')
                name = html.escape(p['name'])
                cells.append(f'    <td width="33%" valign="top"><a href="{repo}"><img src="./assets/roster/{n:03d}.jpg" '
                             f'alt="XXD Panel {n:03d} · {name}" width="100%"></a><br><a href="{repo}"><strong>{n:03d}</strong> · {name}</a>'
                             f'<br><sub>{html.escape(p["tagline"])}</sub></td>')
            rows.append('  <tr>\n' + '\n'.join(cells) + '\n  </tr>')
        label = g['roster_group'].format(a=f'{chunk[0][0]:03d}', b=f'{chunk[-1][0]:03d}')
        opened = ' open' if start == 0 else ''
        blocks.append(f'<details{opened}>\n<summary><strong>{label}</strong></summary>\n\n<table>\n' + '\n'.join(rows) + '\n</table>\n\n</details>')
    return '\n\n'.join(blocks)


def kept_sections(old: str, lang: str) -> tuple[str, str]:
    """The General's own advertising section and its license, verbatim."""
    t = sb.T[lang]
    if ADS_START in old:
        ads = old[old.index(ADS_START) + len(ADS_START):old.index(ADS_END)].strip()
    else:  # first run: the section sat between the old roster and the install heading
        a = old.index(ROSTER_END) + len(ROSTER_END)
        b = re.search(r'^## ' + re.escape(LEGACY_AD_END[lang]) + r'\s*$', old[a:], re.M).start() + a
        ads = old[a:b].strip()
    return ads, sb.license_section(old, t['license'])


def render(lang: str, entries: list, old: str) -> str:
    g, t = G[lang], sb.T[lang]
    n = len(entries)
    c = t['colon']
    links = ' · '.join(f'<strong>{label}</strong>' if code == lang else f'<a href="{file}">{label}</a>'
                       for code, file, label in sb.LANG_LINKS)
    ads, lic = kept_sections(old, lang)
    picks = [e for e in entries if e[0] in (1, 62, 350)] or entries[:3]
    out = [f'<div align="center">\n\n# XXD Panel All｜{g["title"]}\n\n**{g["tagline"].format(n=n)}**\n\n{links}\n\n</div>\n']
    out.append('<table>\n  <tr>\n' + '\n'.join(
        f'    <td width="33%"><a href="{REPO.format(nnn=f"{k:03d}")}"><img src="./assets/roster/{k:03d}.jpg" alt="XXD Panel {k:03d} · {html.escape(p[lang]["name"])}"></a></td>'
        for k, _, p in picks) + '\n  </tr>\n</table>\n')

    out.append(f'## {g["what"]}\n\n{g["what_intro"].format(n=n)}\n\n' +
               '\n'.join(f'- **{a}{c}** {b}' for a, b in g['bullets']) + '\n')

    setup_anchor = sb.anchor(t['setup'])
    out.append(f'## {g["start"]}\n\n{g["step1"]}\n\n```bash\nnpx skills add https://github.com/nevertoday/xxd-panel-all --skill xxd-panel-all\n'
               'npx skills add https://github.com/nevertoday/xxd-panel-001 --skill xxd-panel-001\n```\n\n'
               f'{g["step1_more"]}\n\n```bash\nfor n in 001 062 350; do npx skills add https://github.com/nevertoday/xxd-panel-$n --skill xxd-panel-$n; done\n```\n\n'
               f'{g["step1_after"]}\n\n{t["step2"]}\n\n- {t["step2_codex"]}\n- {t["step2_other"].format(anchor=setup_anchor)}\n\n{t["step2_after"]}\n\n'
               f'{g["step3"]}\n\n> {g["step3_say"]}\n\n{g["step3_after"]}\n')

    head = t['say_head']
    out.append(f'## {t["say"]}\n\n{t["say_intro"]}\n\n| {head[0]} | {head[1]} |\n|---|---|\n' +
               '\n'.join(f'| {a} | {b} |' for a, b in g['say_rows']) + '\n')

    out.append(f'## {g["roster"]}\n\n{g["roster_intro"].format(n=n)}\n\n{ROSTER_START}\n\n{roster(lang, entries)}\n\n{ROSTER_END}\n')

    shared = [t['faqs'][3], t['faqs'][4]]  # batches stay separate; where photos go
    out.append(f'## {t["faq"]}\n\n' + '\n\n'.join(f'**{q}** {a}' for q, a in list(g['faqs']) + shared) + '\n')
    out.append(sb.setup_section(t, 'scripts/canonical/configured_imagegen.py'))
    out.append(f'## {g["params"]}\n\n{g["params_text"]}\n')
    mh = g['maint_head']
    out.append(f'## {g["maint"]}\n\n{g["maint_intro"]}\n\n| {mh[0]} | {mh[1]} |\n|---|---|\n' +
               '\n'.join(f'| {a} | {b} |' for a, b in g['maint_rows']) + '\n')
    out.append(f'{ADS_START}\n{ads}\n{ADS_END}\n')
    out.append(lic)
    if lang == 'ar':
        out[0] = out[0].replace('<div align="center">', '<div align="center" dir="rtl">', 1)
        out[1:] = ['<div dir="rtl">\n'] + out[1:] + ['</div>\n']
    return '\n'.join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--root', type=Path, required=True, help='family root holding xxd-panel-all and the Soldiers')
    ap.add_argument('--check', action='store_true', help='report what would change; write nothing')
    ap.add_argument('--refresh-thumbs', action='store_true', help='remake every roster thumbnail')
    a = ap.parse_args()
    entries = soldiers(a.root.resolve())
    if not entries:
        ap.error('no Soldiers with readme-profile.json found')
    changed = 0
    for n, d, _ in entries:
        dest = ALL / 'assets' / 'roster' / f'{n:03d}.jpg'
        if a.refresh_thumbs or not dest.is_file():
            changed += 1
            print(f'{"would make" if a.check else "made"} {dest.relative_to(ALL)}')
            if not a.check:
                write_thumb(wide_sample(d), dest)
    for lang, name in sb.FILES.items():
        path = ALL / name
        new = render(lang, entries, path.read_text())
        if new != path.read_text():
            changed += 1
            print(f'{"would write" if a.check else "wrote"} {name}')
            if not a.check:
                path.write_text(new)
    print(f'{len(entries)} styles')
    return 1 if a.check and changed else 0


if __name__ == '__main__':
    sys.exit(main())
