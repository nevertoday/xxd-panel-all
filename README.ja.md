# XXD Panel All · 将軍 Skill

<a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="README.ja.md"><strong>日本語</strong></a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

`xxd-panel-all` は XXD Panel シリーズの将軍レベル Skill です。まず現在の環境にインストール済みの `xxd-panel-NNN` 兵士 Skills を確認し、次の仕事を引き受けます。

写真がたくさんあるのに、どのスタイルを使えばよいか分からない。一つずつ試すには時間がかかり、勘だけで選ぶと後悔しやすい——そんなとき、この Skill が最初の判断を代行します。画像やフォルダーを渡すだけで、要望を理解し、インストール済みの Panel から適任を選び、仕事を割り振って結果をまとめます。133 個の番号を先に暗記する必要はありません。

### 30 秒で分かること

- **1 枚作りたい：** テーマを伝えるか写真を渡すと、適した Panel を推薦します。
- **スタイルを比較したい：** 複数の Panel を指定し、同じ画像でそれぞれ試作します。
- **まとめて処理したい：** フォルダーを渡し、共通設定で処理するか画像ごとに割り当てます。

いちばん簡単な始め方は次の一言です。

> これが私の画像です。まず、おすすめの Panel と、それぞれが合う理由を教えてください。

以下にインストール、バッチ処理、設定の完全な説明があります。まず使い始め、必要になったとき詳細を確認するほうが通常は早いです。

- 画像やテーマから Panel を賢く推薦
- 題材、見た目の印象、用途からスタイルを閲覧
- Panel 番号を指定して直接制作
- 1 つの入力を複数 Panel で試作
- フォルダー内の各画像を適切な Panel に割り当て

この Skill が担うのは質問、選択、指揮だけです。新しいビジュアルスタイルになることも、未インストールの Panel をカタログ要約から模倣することもありません。

## 一人の将軍と、成長し続ける美的な兵士部隊

| 階層 | Skill | 担当 |
|---|---|---|
| **将軍レベル** | [`xxd-panel-all`](https://github.com/nevertoday/xxd-panel-all) | 利用可能な兵士を検出。画像・テーマ・用途から推薦。番号指定で指揮。同一画像の複数スタイル試作を編成。画像フォルダーを項目ごとに割り当てて派遣。 |
| **兵士レベル** | `xxd-panel-NNN`（カタログは 134 まで更新） | 各番号は独立した自分の原始プロンプトと美学だけを実行し、将軍から渡された個別タスクを完成品にする。 |

将軍は部隊を組織し、兵士の代わりに描きません。兵士の原始美学を書き換えたり、混ぜたり、上書きしたりせず、すべての完成画像は選ばれた番号の Skill が独立して制作します。

## 新しい兵士

- [XXD Panel 114 · レトロなパステル手帳ドゥードル](https://github.com/nevertoday/xxd-panel-114)
- [XXD Panel 115 · パステルスタンプ・コラージュ](https://github.com/nevertoday/xxd-panel-115)
- [XXD Panel 116 · 淡い紙のパステルドゥードル](https://github.com/nevertoday/xxd-panel-116)
- [XXD Panel 117 · 細線パステルの余白帖](https://github.com/nevertoday/xxd-panel-117)
- [XXD Panel 118 · グラファイト余白スケッチ](https://github.com/nevertoday/xxd-panel-118)
- [XXD Panel 119 · 手縫い布の余白帖](https://github.com/nevertoday/xxd-panel-119)
- [XXD Panel 120 · 建築コンセプト手描き帖](https://github.com/nevertoday/xxd-panel-120)
- [XXD Panel 121 · 暮らしのドゥードル編集帖](https://github.com/nevertoday/xxd-panel-121)
- [XXD Panel 122 · 単色網点と手書きの余白](https://github.com/nevertoday/xxd-panel-122)
- [XXD Panel 123 · 赤青の角線色鉛筆](https://github.com/nevertoday/xxd-panel-123)
- [XXD Panel 124 · 布コラージュの余白](https://github.com/nevertoday/xxd-panel-124)
- [XXD Panel 125 · クレヨン童画の余白](https://github.com/nevertoday/xxd-panel-125)
- [XXD Panel 126 · 詩的なミニチュアコラージュ](https://github.com/nevertoday/xxd-panel-126)
- [XXD Panel 127 · 建築ミクストメディア・コラージュ](https://github.com/nevertoday/xxd-panel-127)
- [XXD Panel 128 · 七宝メダルの旅](https://github.com/nevertoday/xxd-panel-128)
- [XXD Panel 129 · 東洋の拡散と余白](https://github.com/nevertoday/xxd-panel-129)
- [XXD Panel 130 · ハードエッジ幾何面](https://github.com/nevertoday/xxd-panel-130)
- [XXD Panel 131 · 写真と落書きコラージュ](https://github.com/nevertoday/xxd-panel-131)
- [XXD Panel 132 · ペン淡彩の旅](https://github.com/nevertoday/xxd-panel-132)
- [XXD Panel 133 · 点刻と透明重ね刷り](https://github.com/nevertoday/xxd-panel-133)
- [XXD Panel 134 · 絵本の色面物語](https://github.com/nevertoday/xxd-panel-134)

## 広告情報｜XXD 有料サービスと会員制度

> **広告・商業情報に関する表示：** 以下の QR コード、会員制度、有料サービスへのリンクは小小東による広告情報です。スキャンや購入は完全に任意であり、このオープンソースプロジェクトへのアクセスや利用には影響しません。

### 小小東総合管理 · 将軍総指揮 Skill · 100 元

100 元の一回払いで、本セットの将軍総指揮 Skill（`xxd-panel-all`）を入手できます。すべての兵士 Skills の統括、推薦、指名、バッチ指揮に使用でき、インストール、バージョン更新、部隊構成、指揮方法についてのサポートも含まれます。[小小東の WeChat](https://xiaoxiaodong.pages.dev/assets/wechat-qr.png) から「将軍総指揮 Skill」と添えてご連絡ください。

## 知識星球＋会員プロンプトライブラリ＋全将軍 Skills 会員 · 年額 699 元

[知識星球](https://wx.zsxq.com/group/15554814142882)、[小小東会員プロンプトライブラリ](https://vip.xiaoxiaodong.ai/)、全将軍 Skills 会員は同一の会員特典です。**一度の年会費で 3 つすべてが有効になり、重複して支払う必要はありません。** 知識星球から加入した場合は、小小東へ WeChat で連絡して会員プロンプトライブラリの引換コードを受け取れます。会員プロンプトライブラリから加入した場合は、小小東へ WeChat で連絡して知識星球への参加と全将軍 Skills 会員特典の開通ができます。

## インストール

```bash
git clone https://github.com/nevertoday/xxd-panel-all.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/xxd-panel-all" ~/.claude/skills/xxd-panel-all
```

`npx skills` で直接インストールすることもできます。

```bash
npx skills add https://github.com/xiaoxiaodong-ai/xxd-panel-all --skill xxd-panel-all
```

このコマンドは GitHub から将軍リポジトリを取得し、`xxd-panel-all` を現在の Agent にインストールします。ユーザーレベルの Codex Skills ディレクトリへ入れる場合は、末尾に `--global --agent codex --yes` を付けます。将軍は指揮だけを担当するため、実際の制作には必要な `xxd-panel-NNN` 兵士 Skills を別途インストールする必要があります。

`~/.codex/skills` が `~/.claude/skills` と共有されていない場合は、追加のリンクを作成します。

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/xxd-panel-all" ~/.codex/skills/xxd-panel-all
```

インストール後に Agent セッションを開き直し、次のように呼び出します。

```text
$xxd-panel-all
```

## ディレクトリのバッチ処理

呼び出し時に画像ディレクトリを直接指定できます。

```text
$xxd-panel-all /path/to/images
```

Skill はすぐにバッチモードへ入り、ディレクトリとサブディレクトリ内の画像を走査した後、割り当て方法を一つ尋ねます。

1. すべての画像に同じ Panel を使用
2. 各画像に最適な Panel を自動で割り当て
3. 類似画像をグループ化し、グループごとに同じ Panel を使用
4. 指定した複数の Panel の中だけで自動割り当て

共通の納品設定は一度だけ収集します。その後も各画像は対応する `xxd-panel-NNN` に独立したタスクとして入り、コラージュにまとめられたり、画像同士が影響し合ったりすることはありません。

## 前回の設定を引き継ぐ、または新しく設定する

今回の納品設定がまだ不足し、前回の XXD Panel 設定が見つかった場合、将軍または兵士は前回のモード、サイズ、文字と言語、壁紙の関係、出力先を表示してから尋ねます。

1. **そのまま引き継ぐ：** 前回の設定を使い、今回明示された要件を優先します。
2. **引き継いで変更：** 前回の設定を読み込み、選んだ項目だけを変更します。
3. **新しく設定：** 履歴を無視して最初から選びます。

要件がすべて明示されている場合は、余分な質問をせず直接実行します。`--prefs last|edit|new|off|clear` も明示的に使用できます。設定記録に保存するのは納品設定だけで、元画像、正確な文案、Panel 選択、生成結果、モデル経路、API 認証情報、その他の機密情報は保存しません。

```text
$xxd-panel-all /path/to/images --prefs last
$xxd-panel-all /path/to/images --prefs edit
$xxd-panel-all /path/to/images --prefs new
```

## インストール状態

実行時の Panel は次の 3 状態に分かれます。

- `AVAILABLE`：現在インストール済みで直接呼び出し可能
- `KNOWN_BUT_MISSING`：スタイルカタログにはあるが、現在は未インストール
- `UNKNOWN`：カタログに存在しない

推薦、バッチ割り当て、直接制作にはインストール済みの Panel だけを使用します。未インストールのスタイルも閲覧・推薦できますが、制作するには対応する子 Skill のインストールが必要です。

## プロジェクト構成

```text
xxd-panel-all/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── panel-catalog.md
│   └── runtime-preferences.md
└── scripts/
    └── panel_preferences.py
```

- `SKILL.md`：対話、推薦、閲覧、バッチルーティングの規則
- `panel-catalog.md`：Panel 134 まで更新された検索用カタログ。画像生成プロンプトではありません
- `runtime-preferences.md`：引き継ぎ、変更、新規設定、プライバシー境界
- `panel_preferences.py`：安全な納品設定だけを読み書きするローカル補助スクリプト
- `openai.yaml`：Skill のインターフェースメタデータ

## ライセンス

本プロジェクト（Skill、プロンプト、スクリプト、文書、付属サンプル画像を含む）は **PolyForm Noncommercial License 1.0.0** の下で提供されます。完全な法的条文は [LICENSE](LICENSE)、公式ページは <https://polyformproject.org/licenses/noncommercial/1.0.0> を参照してください。

分かりやすく言うと：

- 個人は学習、研究、実験、テスト、趣味のプロジェクト、私的娯楽に使用できます。慈善団体、教育機関、公的研究・安全・保健機関、環境保護団体、政府機関も使用できます。
- **非商業目的**であれば、使用、複製、変更、派生物の作成、共有が可能です。共有時には本ライセンス（または上記リンク）と、作者が示したすべての `Required Notice:` 文を添付する必要があります。
- 商用製品・サービス、有料納品、アクセス権やライセンスの販売、商業利用につながることが予想される用途には使用できません。商用利用には著作権者から別途書面による許可を得てください。
- 本契約が付与するのは明記された著作権ライセンスと限定的な特許ライセンスだけです。商標、ブランド名、その他明記されていない権利は付与されず、ライセンスを第三者へ再許諾することもできません。
- 書面で違反通知を受けた場合、32 日以内に遵守状態へ戻り、実際の是正措置を取らなければライセンスは直ちに終了します。特許侵害を書面で主張した場合も特許ライセンスが終了します。
- 内容は法律が認める範囲で「現状のまま」提供され、保証はありません。利用に伴うリスクと損失は利用者が負います。
