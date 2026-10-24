<div align="center">

# XXD Panel All｜スタイル総合カタログ

**354 種類の写真スタイルの総合入口。写真と用途を伝えれば、スタイル選び、比較、一括生成を手伝います。**

<a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <strong>日本語</strong> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

</div>

<table>
  <tr>
    <td width="33%"><a href="https://github.com/nevertoday/xxd-panel-001"><img src="./assets/roster/001.jpg" alt="XXD Panel 001 · レトロ無邪気手帳"></a></td>
    <td width="33%"><a href="https://github.com/nevertoday/xxd-panel-062"><img src="./assets/roster/062.jpg" alt="XXD Panel 062 · 賢くて不器用な線"></a></td>
    <td width="33%"><a href="https://github.com/nevertoday/xxd-panel-350"><img src="./assets/roster/350.jpg" alt="XXD Panel 350 · ネオンの精霊"></a></td>
  </tr>
</table>

## これは何か

XXD Panel は、写真をポスター、イラスト、壁紙に描き直す AI Skill のシリーズで、番号ごとに 1 つのスタイルがあり、現在 354 個、それぞれ独立しています。`xxd-panel-all` はその総合入口で、Claude Code や Codex など Skills 対応のエージェントで使えます：

- **選ぶ：** 写真やテーマを渡すと、インストール済みのスタイルから 1 つか 3 つを、その写真に合う理由とともに勧めます。
- **比べる：** 同じ写真を複数のスタイルで 1 枚ずつ作り、並べて見比べられます。
- **まとめて作る：** フォルダを渡せば、全部を同じスタイルにも、写真ごとに最適なスタイルにもできます。
- **自分では描かない：** 実際に描くのは番号付きのスタイル Skill です。カタログは選んで渡すだけで、スタイルを混ぜません。

## 3 ステップで始める

**1. カタログと、好きなスタイルをいくつかインストール。** 未インストールのスタイルも紹介・推薦はできますが、画像を作れるのはインストール済みのものだけです：

```bash
npx skills add https://github.com/nevertoday/xxd-panel-all --skill xxd-panel-all
npx skills add https://github.com/nevertoday/xxd-panel-001 --skill xxd-panel-001
```

まとめてインストール：

```bash
for n in 001 062 350; do npx skills add https://github.com/nevertoday/xxd-panel-$n --skill xxd-panel-$n; done
```

インストール後、エージェントのセッションを開き直してください。

**2. エージェントが画像を生成できるか確認。** この Skill 自体は画像モデルを持たず、エージェントの画像生成（GPT Image 2 推奨）を使います。

- Codex は内蔵の画像生成が有効ならそのまま使えます。
- Claude Code など内蔵の画像生成がないエージェントは、OpenAI 互換の画像 API が必要です。5 分ほどで設定できます：[画像生成の設定](#画像生成の設定)。

わからなければそのまま試してください。生成できない場合は、作業を始める前に Skill が止まって知らせます。

**3. 写真を送って、ひとこと：**

> xxd-panel-all で、この写真に合うスタイルを 3 つ、理由つきで勧めて。

選んだら、写真はそのスタイルの Skill に渡され、レイアウト、比率、文字はそちらが質問します。完成品は `~/Desktop/xxd/xxd-panel-NNN/` に保存されます。

## こう言えば OK

パラメータを覚える必要はありません。そのまま伝えてください：

| やりたいこと | こう言う |
|---|---|
| おすすめ | この写真に合うスタイルは？3 つ勧めて理由も |
| 雰囲気で探す | 黒い線で余白の多いスタイルはある？ |
| 用途で探す | スマホの壁紙に向くスタイルは？ |
| 番号を指定 | 062 でこの写真を作って |
| 比較 | 001、062、350 で 1 枚ずつ作って比べたい |
| フォルダ・同じスタイル | このフォルダを全部 014 で上下比較に |
| フォルダ・自動 | このフォルダの写真ごとに最適なスタイルを選んで |
| 前回と同じ | 前回の設定で |

## 全スタイル

全 354 個。各画像はそのスタイルの左右比較サンプル 1 枚です（左が写真、右がデザイン）。クリックするとリポジトリが開き、ほかのサンプルや使い方を見られます。

<!-- xxd-soldier-roster:start -->

<details open>
<summary><strong>001–050</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-001"><img src="./assets/roster/001.jpg" alt="XXD Panel 001 · レトロ無邪気手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-001"><strong>001</strong> · レトロ無邪気手帳</a><br><sub>写真を、軽やかで紙の質感があり、少し不器用でユーモラスなレトロ手描きイラストにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-002"><img src="./assets/roster/002.jpg" alt="XXD Panel 002 · 遊び心のバウハウス" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-002"><strong>002</strong> · 遊び心のバウハウス</a><br><sub>写真を、少しバウハウス風の幾何と揺れる輪郭、版ずれのあるレトロな雑誌イラストにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-003"><img src="./assets/roster/003.jpg" alt="XXD Panel 003 · 緊張感のある線の言葉" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-003"><strong>003</strong> · 緊張感のある線の言葉</a><br><sub>写真の中の方向、つながり、圧力、転機を、静かで張りつめた黒い一本の線にまとめます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-004"><img src="./assets/roster/004.jpg" alt="XXD Panel 004 · 都市一本線手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-004"><strong>004</strong> · 都市一本線手帳</a><br><sub>実在の街や場所の風景を、正確な一本線と幾何学的な遠近で描くコレクション向けの線画ポスターにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-005"><img src="./assets/roster/005.jpg" alt="XXD Panel 005 · 童話ダーク版" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-005"><strong>005</strong> · 童話ダーク版</a><br><sub>写真を、暗い大きな形に包まれ、要所だけ明るい色が光る童話版画にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-006"><img src="./assets/roster/006.jpg" alt="XXD Panel 006 · 余白の小劇場" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-006"><strong>006</strong> · 余白の小劇場</a><br><sub>写真を一つの小さな主役にまとめ、広い紙の余白に置いて、アートブックの表紙のようにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-007"><img src="./assets/roster/007.jpg" alt="XXD Panel 007 · 手描き観察ページ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-007"><strong>007</strong> · 手描き観察ページ</a><br><sub>写真を、小さな絵と断面図と手書きの短い言葉でつないだ生活観察ノートの一ページにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-008"><img src="./assets/roster/008.jpg" alt="XXD Panel 008 · パステルの幻境" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-008"><strong>008</strong> · パステルの幻境</a><br><sub>写真の人や物語を、明るく静かな、モニュメントバレーのようなパステルの不可能空間にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-009"><img src="./assets/roster/009.jpg" alt="XXD Panel 009 · 網点アンカープリント" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-009"><strong>009</strong> · 網点アンカープリント</a><br><sub>写真をごく小さな一点に絞り、広い紙の上に、密から疎へ消える網点で距離と空気を刷ります。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-010"><img src="./assets/roster/010.jpg" alt="XXD Panel 010 · モノクロ古書絵本" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-010"><strong>010</strong> · モノクロ古書絵本</a><br><sub>写真を、白に近い紙の上に太い黒クレヨンで塗った絵本のシルエットにします。色は黒と白だけです。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-011"><img src="./assets/roster/011.jpg" alt="XXD Panel 011 · 瞑想する線の詩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-011"><strong>011</strong> · 瞑想する線の詩</a><br><sub>写真を、ゆっくり見つめたくなる黒い細い連続線にまとめ、意味のある色を一点だけ残します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-012"><img src="./assets/roster/012.jpg" alt="XXD Panel 012 · 生命の幾何学" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-012"><strong>012</strong> · 生命の幾何学</a><br><sub>写真の主役を、一色の高密度な線の場から浮かび上がらせ、まわりに幾何学的な細線を広げます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-013"><img src="./assets/roster/013.jpg" alt="XXD Panel 013 · 旅の半券帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-013"><strong>013</strong> · 旅の半券帳</a><br><sub>写真を、左に水彩、右に半券を備えた、大切に取っておいた旅のチケットのような一枚にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-014"><img src="./assets/roster/014.jpg" alt="XXD Panel 014 · ペーパーレリーフ手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-014"><strong>014</strong> · ペーパーレリーフ手帳</a><br><sub>写真を、折り目や切り口、紙の繊維まで見える現代の折り紙彫刻に組み直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-015"><img src="./assets/roster/015.jpg" alt="XXD Panel 015 · 抽象の記憶録" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-015"><strong>015</strong> · 抽象の記憶録</a><br><sub>写真を分解して選び、いくつかの幾何形と繊細な編集文字で組み直し、アートブックの一ページのようにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-016"><img src="./assets/roster/016.jpg" alt="XXD Panel 016 · 動勢の版画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-016"><strong>016</strong> · 動勢の版画</a><br><sub>写真の中で本当に起きていることを、ごく小さな主役と、そのまわりの一つの動きにまとめます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-017"><img src="./assets/roster/017.jpg" alt="XXD Panel 017 · 無邪気グラフィック手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-017"><strong>017</strong> · 無邪気グラフィック手帳</a><br><sub>写真を、ざらついた黒い線と明るいベタ塗りの、韓国風の素朴な雑誌イラストにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-018"><img src="./assets/roster/018.jpg" alt="XXD Panel 018 · 切り絵手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-018"><strong>018</strong> · 切り絵手帳</a><br><sub>一つの切り絵の主役と、前・中・奥の数枚の紙、精密な小さな文字で、写真を手作りの重ね切り絵に作り直します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-019"><img src="./assets/roster/019.jpg" alt="XXD Panel 019 · レトログラフィック手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-019"><strong>019</strong> · レトログラフィック手帳</a><br><sub>写真の主役と関係を、ちゃんと見分けのつくレトロなモダニズムの平面イラストに組み直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-020"><img src="./assets/roster/020.jpg" alt="XXD Panel 020 · 厚塗りミニ風景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-020"><strong>020</strong> · 厚塗りミニ風景</a><br><sub>写真の主役と物語を、厚塗りの絵の具の塊から生えてくる、触れそうな立体のミニチュア風景にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-021"><img src="./assets/roster/021.jpg" alt="XXD Panel 021 · 黒の領域を越えて" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-021"><strong>021</strong> · 黒の領域を越えて</a><br><sub>写真の主役を真っ黒な長方形から身を乗り出させ、揺れる黒い線と白い形で描きます。色は白黒とグレーだけです。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-022"><img src="./assets/roster/022.jpg" alt="XXD Panel 022 · 色ドットのはみ出し" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-022"><strong>022</strong> · 色ドットのはみ出し</a><br><sub>写真の主役を、なめらかな線で真っ黒な長方形からはみ出させ、いちばん大事な一か所だけに色を置きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-023"><img src="./assets/roster/023.jpg" alt="XXD Panel 023 · 東洋の窓景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-023"><strong>023</strong> · 東洋の窓景</a><br><sub>写真を、主役に合わせて選んだ中国式の窓に収め、格子越しの日差しが淡い壁に落ちたような一枚にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-024"><img src="./assets/roster/024.jpg" alt="XXD Panel 024 · 感情の窓" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-024"><strong>024</strong> · 感情の窓</a><br><sub>写真の中の本物の被写体を、細長い淡い色の幾何学の窓に通し、ミニマルな上質の広告ポスターにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-025"><img src="./assets/roster/025.jpg" alt="XXD Panel 025 · 見えないイメージ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-025"><strong>025</strong> · 見えないイメージ</a><br><sub>写真を、一目で主役が見え、二度目にもう一つの絵が隠れているのに気づく、モランディ色のシルクスクリーン版画にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-026"><img src="./assets/roster/026.jpg" alt="XXD Panel 026 · 幾何学的秩序" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-026"><strong>026</strong> · 幾何学的秩序</a><br><sub>写真の中の事実を、静かでやさしく、それでも一目でわかる幾何学の秩序に置き換えます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-027"><img src="./assets/roster/027.jpg" alt="XXD Panel 027 · 紙上のレリーフ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-027"><strong>027</strong> · 紙上のレリーフ</a><br><sub>写真を、厚い乳白色の紙に押し出した東洋の博物館風の浅浮き彫りにし、要所にだけマットな金を置きます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-028"><img src="./assets/roster/028.jpg" alt="XXD Panel 028 · アイソメトリック・ミニ風景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-028"><strong>028</strong> · アイソメトリック・ミニ風景</a><br><sub>写真を、元の色で描いた紙の上のアイソメトリックなミニチュア模型、小さな建築ジオラマのように置き直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-029"><img src="./assets/roster/029.jpg" alt="XXD Panel 029 · 紙にゆっくり描く" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-029"><strong>029</strong> · 紙にゆっくり描く</a><br><sub>写真を、横長の低彩度の色面の上に描いたゆるやかなワックスパステル画にし、さらりと書いた一言を添えます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-030"><img src="./assets/roster/030.jpg" alt="XXD Panel 030 · 自然のはみ出し" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-030"><strong>030</strong> · 自然のはみ出し</a><br><sub>本物の葉、花びら、小枝、果実、種、草の茎、樹皮で、写真の主役を組み立て直します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-031"><img src="./assets/roster/031.jpg" alt="XXD Panel 031 · 寓意の拓本" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-031"><strong>031</strong> · 寓意の拓本</a><br><sub>まず写真の背後にある意味を読み取り、幾何学的に厳密で拓本のざらつきを持つ一つの中心モチーフにまとめます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-032"><img src="./assets/roster/032.jpg" alt="XXD Panel 032 · グラフィック・ワードマーク" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-032"><strong>032</strong> · グラフィック・ワードマーク</a><br><sub>写真の主役の決定的な特徴を、カスタムワードマークの文字の構造に組み込みます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-033"><img src="./assets/roster/033.jpg" alt="XXD Panel 033 · 鮮やかコラージュ手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-033"><strong>033</strong> · 鮮やかコラージュ手帳</a><br><sub>一枚の写真を、鮮やかで濃密、層のはっきりした現代の雑誌カバー・コラージュにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-034"><img src="./assets/roster/034.jpg" alt="XXD Panel 034 · 旅のスタンプ印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-034"><strong>034</strong> · 旅のスタンプ印</a><br><sub>写真を小さな多色ゴム版スタンプにまとめ、静かなフィールドノートを添えます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-035"><img src="./assets/roster/035.jpg" alt="XXD Panel 035 · ブロック再構築" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-035"><strong>035</strong> · ブロック再構築</a><br><sub>写真の主役を、鮮やかで一目でわかるボクセルブロックのコレクティブルに組み直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-036"><img src="./assets/roster/036.jpg" alt="XXD Panel 036 · 流線の絵本" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-036"><strong>036</strong> · 流線の絵本</a><br><sub>写真の中の関係を数本の連続した細い線で描き、透明な色を紙の上でゆっくり流します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-037"><img src="./assets/roster/037.jpg" alt="XXD Panel 037 · 流れる金の紋章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-037"><strong>037</strong> · 流れる金の紋章</a><br><sub>旅の写真を、コレクションしたくなる流金エナメルのバッジ一枚にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-038"><img src="./assets/roster/038.jpg" alt="XXD Panel 038 · 織物の暮らし手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-038"><strong>038</strong> · 織物の暮らし手帳</a><br><sub>写真と、写真が口にしない気持ちを、温かな手づくりのパッチワークに縫い上げます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-039"><img src="./assets/roster/039.jpg" alt="XXD Panel 039 · 刺繍のイメージ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-039"><strong>039</strong> · 刺繍のイメージ</a><br><sub>写真からいちばん残す価値のあるイメージを一つだけ選び、生き生きとした絹の光の中に刺繍します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-040"><img src="./assets/roster/040.jpg" alt="XXD Panel 040 · 落書きの相棒" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-040"><strong>040</strong> · 落書きの相棒</a><br><sub>写真でいちばん覚えておきたい実物を残し、黒い線の小人たちがそのまわりで小さな劇を演じます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-041"><img src="./assets/roster/041.jpg" alt="XXD Panel 041 · アイソメトリック研究室" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-041"><strong>041</strong> · アイソメトリック研究室</a><br><sub>写真の主役と、写真から引き出した一つのテーマを、透明感のある等角の研究図に組み立てます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-042"><img src="./assets/roster/042.jpg" alt="XXD Panel 042 · 脱構築水彩手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-042"><strong>042</strong> · 脱構築水彩手帳</a><br><sub>写真の主役を実際の構造に沿って層ごとに開き、組み立て直せる水彩の研究図に描きます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-043"><img src="./assets/roster/043.jpg" alt="XXD Panel 043 · 白い泡" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-043"><strong>043</strong> · 白い泡</a><br><sub>本物の白い石けんの泡で、暗く濡れた平面の上に写真の主役を描き直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-044"><img src="./assets/roster/044.jpg" alt="XXD Panel 044 · フラットな純金" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-044"><strong>044</strong> · フラットな純金</a><br><sub>写真の主役の決定的な形を、暗い地の上の薄い純金の層に押し込みます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-045"><img src="./assets/roster/045.jpg" alt="XXD Panel 045 · 癒しのブロック都市" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-045"><strong>045</strong> · 癒しのブロック都市</a><br><sub>写真の主役を、丸く、触れたくなる、やさしい色のブロック彫刻に組み直します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-046"><img src="./assets/roster/046.jpg" alt="XXD Panel 046 · 厚塗りミニ世界" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-046"><strong>046</strong> · 厚塗りミニ世界</a><br><sub>写真を、明るく生き生きとして、絵の具の厚みが感じられる厚塗りのミニチュア風景に組み直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-047"><img src="./assets/roster/047.jpg" alt="XXD Panel 047 · アイソメトリック厚塗り風景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-047"><strong>047</strong> · アイソメトリック厚塗り風景</a><br><sub>写真の主役を精巧な等角ミニチュアにして、生きた厚塗りの色域の中に立たせます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-048"><img src="./assets/roster/048.jpg" alt="XXD Panel 048 · 透明構造の手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-048"><strong>048</strong> · 透明構造の手帳</a><br><sub>写真の主役を半透明にして、その構造の論理を澄んだ設計図として描きます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-049"><img src="./assets/roster/049.jpg" alt="XXD Panel 049 · 木版の印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-049"><strong>049</strong> · 木版の印</a><br><sub>写真のいちばん心に残る部分を、爽やかで柔らかな限定色の木版画に彫ります。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-050"><img src="./assets/roster/050.jpg" alt="XXD Panel 050 · 旅の絵はがき" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-050"><strong>050</strong> · 旅の絵はがき</a><br><sub>一枚ごとの写真を、その場所のための空色のミニマルな旅のポスターにします。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>051–100</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-051"><img src="./assets/roster/051.jpg" alt="XXD Panel 051 · 手作りミニチュア島" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-051"><strong>051</strong> · 手作りミニチュア島</a><br><sub>写真の主役を、軽やかで触れたくなる手作りのペーパークラフト・ミニチュアにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-052"><img src="./assets/roster/052.jpg" alt="XXD Panel 052 · ペーパークラフトのミニ島" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-052"><strong>052</strong> · ペーパークラフトのミニ島</a><br><sub>写真の世界を手作りの紙のミニチュアにして、一本の風景の線の上にそっと浮かべます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-053"><img src="./assets/roster/053.jpg" alt="XXD Panel 053 · ペン淡彩の記録" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-053"><strong>053</strong> · ペン淡彩の記録</a><br><sub>観察したペンの線と数か所の淡彩で写真を書き留め、いちばんふさわしいところで筆を止めます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-054"><img src="./assets/roster/054.jpg" alt="XXD Panel 054 · 思い出シール帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-054"><strong>054</strong> · 思い出シール帳</a><br><sub>一つの思い出を、主役の絵と大きさの違う六枚のシールのかけらに分けます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-055"><img src="./assets/roster/055.jpg" alt="XXD Panel 055 · 絵画の記憶の場" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-055"><strong>055</strong> · 絵画の記憶の場</a><br><sub>写真の中の一筋の光、一つの動き、一つの空間の関係を、やさしい絵に描きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-056"><img src="./assets/roster/056.jpg" alt="XXD Panel 056 · 余白の記憶画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-056"><strong>056</strong> · 余白の記憶画</a><br><sub>写真から核となるイメージを一つだけ残し、巨大な余白の中に素朴な筆致と暖色寒色の跳ねる色で描き直します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-057"><img src="./assets/roster/057.jpg" alt="XXD Panel 057 · 幾何学の記憶の場" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-057"><strong>057</strong> · 幾何学の記憶の場</a><br><sub>幾何学の色面と秩序あるモザイクで、写真を静かで温かな現代のコラージュに組み直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-058"><img src="./assets/roster/058.jpg" alt="XXD Panel 058 · 詩的コンセプト風景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-058"><strong>058</strong> · 詩的コンセプト風景</a><br><sub>写真がほのめかしていることを読み取り、厳密な幾何学で詩的なコンセプト風景に組み立てます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-059"><img src="./assets/roster/059.jpg" alt="XXD Panel 059 · 手描き寓話録" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-059"><strong>059</strong> · 手描き寓話録</a><br><sub>写真が口にしなかった物語を、温かく、子どもらしく、さりげなく賢い寓話絵本の一ページに描きます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-060"><img src="./assets/roster/060.jpg" alt="XXD Panel 060 · 禅のミニマル詩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-060"><strong>060</strong> · 禅のミニマル詩</a><br><sub>写真を一〜三つの黒い形と巨大な余白に凝縮し、静かに余韻の残る視覚の思索にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-061"><img src="./assets/roster/061.jpg" alt="XXD Panel 061 · ビジュアル記憶帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-061"><strong>061</strong> · ビジュアル記憶帳</a><br><sub>写真を、紙の上に散らばって響き合ういくつかの視覚的な記憶のかけらに組み直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-062"><img src="./assets/roster/062.jpg" alt="XXD Panel 062 · 賢くて不器用な線" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-062"><strong>062</strong> · 賢くて不器用な線</a><br><sub>素朴な黒い線と写真から取った一色だけで、写真のいちばん覚えておきたい瞬間を描きます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-063"><img src="./assets/roster/063.jpg" alt="XXD Panel 063 · ピクセル隠喩手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-063"><strong>063</strong> · ピクセル隠喩手帳</a><br><sub>写真を、大きなピクセルの輪郭といくつかの柔らかな色面がつくる静かな比喩に組み直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-064"><img src="./assets/roster/064.jpg" alt="XXD Panel 064 · インディー・コラージュ頁" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-064"><strong>064</strong> · インディー・コラージュ頁</a><br><sub>写真を、静かで欠けがあり、時間の流れを感じる古紙コラージュの一頁にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-065"><img src="./assets/roster/065.jpg" alt="XXD Panel 065 · 二本線エディトリアル手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-065"><strong>065</strong> · 二本線エディトリアル手帳</a><br><sub>黒い線で骨組みを描き、写真から取った二色の線を版ずれのように重ねた手描き線画にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-066"><img src="./assets/roster/066.jpg" alt="XXD Panel 066 · 無邪気な物語の線" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-066"><strong>066</strong> · 無邪気な物語の線</a><br><sub>写真の動きと関係を、ゆるい黒線とやわらかなベタ塗りで、無邪気な小さな物語に描き直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-067"><img src="./assets/roster/067.jpg" alt="XXD Panel 067 · 日常ユーモア画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-067"><strong>067</strong> · 日常ユーモア画</a><br><sub>赤と青の二色の手描きインクだけで、写真のおもしろい一瞬を私的な観察ノートの一頁にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-068"><img src="./assets/roster/068.jpg" alt="XXD Panel 068 · 東洋写意帖" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-068"><strong>068</strong> · 東洋写意帖</a><br><sub>写意の墨線、淡彩、大きな余白で、写真を東洋の目で描き直します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-069"><img src="./assets/roster/069.jpg" alt="XXD Panel 069 · 鮮やか塗りの窓" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-069"><strong>069</strong> · 鮮やか塗りの窓</a><br><sub>幅広の筆数本で描いた絵の窓から、写真の主役が鮮やかな色をまとって抜け出します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-070"><img src="./assets/roster/070.jpg" alt="XXD Panel 070 · 厚塗り癒しの島" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-070"><strong>070</strong> · 厚塗り癒しの島</a><br><sub>写真の主役を、温かな白の広がりに浮かぶ小さく明るい島として描きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-071"><img src="./assets/roster/071.jpg" alt="XXD Panel 071 · パステル詩情帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-071"><strong>071</strong> · パステル詩情帳</a><br><sub>写真を、ほぼ白の紙に浮かぶいくつかのパステルの記憶に変え、ゆるい手書きの詩を添えます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-072"><img src="./assets/roster/072.jpg" alt="XXD Panel 072 · 明るい色彩手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-072"><strong>072</strong> · 明るい色彩手帳</a><br><sub>写真を、くっきりした所とかすんだ所がある明るいすりガラスの幾何学に抽象化します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-073"><img src="./assets/roster/073.jpg" alt="XXD Panel 073 · 幾何学都市手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-073"><strong>073</strong> · 幾何学都市手帳</a><br><sub>写真を、足場に囲まれた切断面のあるアイソメトリックな微縮建築模型に作り直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-074"><img src="./assets/roster/074.jpg" alt="XXD Panel 074 · 感情アイコン手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-074"><strong>074</strong> · 感情アイコン手帳</a><br><sub>写真の主役と気分を、正面から見たマットで奥行きのある角丸正方形のアイコン一つに凝縮します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-075"><img src="./assets/roster/075.jpg" alt="XXD Panel 075 · ダーククレヨン画稿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-075"><strong>075</strong> · ダーククレヨン画稿</a><br><sub>写真のいちばん覚えておきたい一筆を、生成りの手漉き紙に濃い色のクレヨンで残します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-076"><img src="./assets/roster/076.jpg" alt="XXD Panel 076 · マカロンクレヨン" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-076"><strong>076</strong> · マカロンクレヨン</a><br><sub>写真を、粗い濃色クレヨンと明るいマカロン色で、人の温もりがある旅の記憶に描きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-077"><img src="./assets/roster/077.jpg" alt="XXD Panel 077 · 旅雑誌イラスト" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-077"><strong>077</strong> · 旅雑誌イラスト</a><br><sub>写真を、紙の重なりと柔らかな影、英文の組版がある切り紙の旅雑誌の一頁にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-078"><img src="./assets/roster/078.jpg" alt="XXD Panel 078 · 金箔箔押し手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-078"><strong>078</strong> · 金箔箔押し手帳</a><br><sub>写真のいちばん大事な輪郭を細い線にし、シャンパンゴールドの箔でアイボリーのコットン紙に深く押し込みます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-079"><img src="./assets/roster/079.jpg" alt="XXD Panel 079 · ペン淡彩手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-079"><strong>079</strong> · ペン淡彩手帳</a><br><sub>幾何学的な直線、自由な墨線、数か所の淡彩で、写真を現場で描きかけたようなスケッチにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-080"><img src="./assets/roster/080.jpg" alt="XXD Panel 080 · 有機的グアッシュの場" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-080"><strong>080</strong> · 有機的グアッシュの場</a><br><sub>やわらかな有機的な形と植物色のグアッシュで、写真の気分と小さな比喩を広い余白の中に置きます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-081"><img src="./assets/roster/081.jpg" alt="XXD Panel 081 · 色糸の記念帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-081"><strong>081</strong> · 色糸の記念帳</a><br><sub>写真の色から選んだ二〜四色の均一な線で、写真を限定色刷りの私的な記念ポスターにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-082"><img src="./assets/roster/082.jpg" alt="XXD Panel 082 · 紙から飛び出す水彩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-082"><strong>082</strong> · 紙から飛び出す水彩</a><br><sub>写真のただ一人の主役が、不規則な水彩の色面から素朴な立体となって立ち上がります。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-083"><img src="./assets/roster/083.jpg" alt="XXD Panel 083 · ブサかわキャラ手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-083"><strong>083</strong> · ブサかわキャラ手帳</a><br><sub>写真から主役を一つだけ残し、そのいちばん可笑しい性格をわざと下手に不器用に、でもひと目でわかるように描きます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-084"><img src="./assets/roster/084.jpg" alt="XXD Panel 084 · 点描と線構成の手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-084"><strong>084</strong> · 点描と線構成の手帳</a><br><sub>幾何学的な細い線と濃淡のある小さな点で、写真を静かな都市の随筆にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-085"><img src="./assets/roster/085.jpg" alt="XXD Panel 085 · 手作り模型手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-085"><strong>085</strong> · 手作り模型手帳</a><br><sub>写真を、粘土、フェルト、切り紙、糸で作った小さな手作りの舞台にして、広い余白の中に置きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-086"><img src="./assets/roster/086.jpg" alt="XXD Panel 086 · 余白の版画手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-086"><strong>086</strong> · 余白の版画手帳</a><br><sub>写真から大事な三〜五つの要素だけを残し、余白を主役にした限定色のシルクスクリーン版画にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-087"><img src="./assets/roster/087.jpg" alt="XXD Panel 087 · 赤い糸の関係図" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-087"><strong>087</strong> · 赤い糸の関係図</a><br><sub>写真を一本一本の画鋲に分け、朱色の糸でつないで、部分どうしの関係が見える地図にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-088"><img src="./assets/roster/088.jpg" alt="XXD Panel 088 · 文字造形の詩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-088"><strong>088</strong> · 文字造形の詩</a><br><sub>文字、句読点、点で写真の主役を組み上げます。遠くからは絵、近づけば全部が文字です。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-089"><img src="./assets/roster/089.jpg" alt="XXD Panel 089 · 暮らしの小品帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-089"><strong>089</strong> · 暮らしの小品帳</a><br><sub>写真を一人の主役と暮らしの小さな断片に分け、力の抜けた私的な手帳の一頁に並べます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-090"><img src="./assets/roster/090.jpg" alt="XXD Panel 090 · ビジュアル思考マップ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-090"><strong>090</strong> · ビジュアル思考マップ</a><br><sub>写真に写ったものを描くのではなく、その裏にある関係と意味をビジュアル思考の地図として描きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-091"><img src="./assets/roster/091.jpg" alt="XXD Panel 091 · 青線の旅帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-091"><strong>091</strong> · 青線の旅帳</a><br><sub>一本の青いペンだけで、十分に見たら筆を止める旅のスケッチとして写真を描きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-092"><img src="./assets/roster/092.jpg" alt="XXD Panel 092 · 表現的線描手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-092"><strong>092</strong> · 表現的線描手帳</a><br><sub>写真を、ゆるい輪郭線と重ねたハッチング、広い余白の白黒ペン画にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-093"><img src="./assets/roster/093.jpg" alt="XXD Panel 093 · モダン幾何学絵画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-093"><strong>093</strong> · モダン幾何学絵画</a><br><sub>写真を、明るくマットで、縁に少し手の跡が残るモダニズムの幾何学色面に凝縮します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-094"><img src="./assets/roster/094.jpg" alt="XXD Panel 094 · 古典二色刷りの本" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-094"><strong>094</strong> · 古典二色刷りの本</a><br><sub>写真を、細い墨線と一色の特色、広い余白でできた古い本の挿絵にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-095"><img src="./assets/roster/095.jpg" alt="XXD Panel 095 · 赤黒図解手帳" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-095"><strong>095</strong> · 赤黒図解手帳</a><br><sub>黒い技術線と赤の特色、いくつかの小さな図解で、写真に写るものをわかりやすく説明します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-096"><img src="./assets/roster/096.jpg" alt="XXD Panel 096 · 民間通信カード" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-096"><strong>096</strong> · 民間通信カード</a><br><sub>写真を、本当にタイプされ、コピーされ、郵送されたような古い QSL カードにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-097"><img src="./assets/roster/097.jpg" alt="XXD Panel 097 · レトロ説明カード" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-097"><strong>097</strong> · レトロ説明カード</a><br><sub>写真を、役に立って少しおかしい、古い説明カードのような二色の図解に凝縮します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-098"><img src="./assets/roster/098.jpg" alt="XXD Panel 098 · 素朴な水彩の本" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-098"><strong>098</strong> · 素朴な水彩の本</a><br><sub>写真を、明るくゆるく、わざと不完全な絵本の一ページとして描き直します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-099"><img src="./assets/roster/099.jpg" alt="XXD Panel 099 · 書体マスコット" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-099"><strong>099</strong> · 書体マスコット</a><br><sub>写真の主役を覚えやすいマスコットに仕立て、背景に特大の文字を一行置きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-100"><img src="./assets/roster/100.jpg" alt="XXD Panel 100 · 民芸物語絵" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-100"><strong>100</strong> · 民芸物語絵</a><br><sub>写真を、クレヨンの粒子と暮らしの気配がある素朴な民芸の小さな物語にします。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>101–150</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-101"><img src="./assets/roster/101.jpg" alt="XXD Panel 101 · 九つの記憶ノート" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-101"><strong>101</strong> · 九つの記憶ノート</a><br><sub>一枚の写真を九つの小さな落書きに分け、自分だけの手帳のページに並べます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-102"><img src="./assets/roster/102.jpg" alt="XXD Panel 102 · 癒やしの幾何学誌" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-102"><strong>102</strong> · 癒やしの幾何学誌</a><br><sub>写真を、澄んで静かな、ほのかに生き生きとした幾何学の図形に凝縮します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-103"><img src="./assets/roster/103.jpg" alt="XXD Panel 103 · 鮮彩抽象アセンブリ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-103"><strong>103</strong> · 鮮彩抽象アセンブリ</a><br><sub>写真を鮮やかな大きな色面と粗い手描き線に分け、抽象画として組み直します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-104"><img src="./assets/roster/104.jpg" alt="XXD Panel 104 · 網点禅意誌" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-104"><strong>104</strong> · 網点禅意誌</a><br><sub>写真を、網点でできた形と数本の色の線、静かな余白に凝縮します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-105"><img src="./assets/roster/105.jpg" alt="XXD Panel 105 · 詩的余白集" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-105"><strong>105</strong> · 詩的余白集</a><br><sub>写真でいちばん美しい一瞬だけを選び、静かなミニマルな紙のコラージュにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-106"><img src="./assets/roster/106.jpg" alt="XXD Panel 106 · 柔彩ピクセル記" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-106"><strong>106</strong> · 柔彩ピクセル記</a><br><sub>写真を二つ三つの大事な形だけに削り、柔らかなパステルのピクセルでもう一度記憶します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-107"><img src="./assets/roster/107.jpg" alt="XXD Panel 107 · 画像ことば詩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-107"><strong>107</strong> · 画像ことば詩</a><br><sub>写真の花、窓、道、風を小さな絵にして文中の言葉と入れ替え、読める短い詩に組み上げます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-108"><img src="./assets/roster/108.jpg" alt="XXD Panel 108 · 新民藝切り絵誌" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-108"><strong>108</strong> · 新民藝切り絵誌</a><br><sub>写真のいちばんわかりやすい形を、静かで民藝の味わいのある色紙の切り絵コラージュにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-109"><img src="./assets/roster/109.jpg" alt="XXD Panel 109 · 柔和な幾何解構誌" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-109"><strong>109</strong> · 柔和な幾何解構誌</a><br><sub>写真をいくつかの大きくまとまった四角に分け、柔らかな色でわかりやすい姿に組み直します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-110"><img src="./assets/roster/110.jpg" alt="XXD Panel 110 · 日本風暮らしのシーン図鑑" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-110"><strong>110</strong> · 日本風暮らしのシーン図鑑</a><br><sub>写真の中の覚えておきたい小物を、道すじと余白のある暮らしの地図にまとめます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-111"><img src="./assets/roster/111.jpg" alt="XXD Panel 111 · テキスタイル・コラージュ誌" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-111"><strong>111</strong> · テキスタイル・コラージュ誌</a><br><sub>写真でいちばん覚えておきたい関係を、ぬくもりのある小さな布のコラージュに縫い上げます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-112"><img src="./assets/roster/112.jpg" alt="XXD Panel 112 · 金線ペーパー誌" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-112"><strong>112</strong> · 金線ペーパー誌</a><br><sub>不揃いな紙の色帯一本に、金がほのかに光る小さく静かな記憶をのせます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-113"><img src="./assets/roster/113.jpg" alt="XXD Panel 113 · 貝殻ピクセル・コラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-113"><strong>113</strong> · 貝殻ピクセル・コラージュ</a><br><sub>二百枚に満たない貝殻の角片で写真の主役を組み、縁からゆっくり余白へ散らします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-114"><img src="./assets/roster/114.jpg" alt="XXD Panel 114 · レトロ・パステル手帳ドゥードル" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-114"><strong>114</strong> · レトロ・パステル手帳ドゥードル</a><br><sub>写真を、紙が呼吸するようなパステルの手帳ドゥードル・コラージュとして描き直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-115"><img src="./assets/roster/115.jpg" alt="XXD Panel 115 · パステル印章コラージュ帖" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-115"><strong>115</strong> · パステル印章コラージュ帖</a><br><sub>写真の核となる記憶を、古い紙の上の小さなパステルの落書き印章として描きます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-116"><img src="./assets/roster/116.jpg" alt="XXD Panel 116 · 淡紙パステル落書き誌" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-116"><strong>116</strong> · 淡紙パステル落書き誌</a><br><sub>ごく淡い紙の上に、粒の粗い色クレヨンの線で写真のはっきりした輪郭を残します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-117"><img src="./assets/roster/117.jpg" alt="XXD Panel 117 · 細線淡彩余白誌" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-117"><strong>117</strong> · 細線淡彩余白誌</a><br><sub>写真からひとつの視覚の要を取り出し、細い線と淡彩で余白の多い一枚に組み直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-118"><img src="./assets/roster/118.jpg" alt="XXD Panel 118 · 石墨と余白の素描誌" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-118"><strong>118</strong> · 石墨と余白の素描誌</a><br><sub>写真の中の覚えておきたい関係を残し、鉛筆と余白で構図を組み直します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-119"><img src="./assets/roster/119.jpg" alt="XXD Panel 119 · 手縫い布と余白の記録" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-119"><strong>119</strong> · 手縫い布と余白の記録</a><br><sub>数枚の布と針目に、写真のいちばん温かな記憶を託します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-120"><img src="./assets/roster/120.jpg" alt="XXD Panel 120 · 建築コンセプト手描き帖" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-120"><strong>120</strong> · 建築コンセプト手描き帖</a><br><sub>写真の中の空間の記憶を、余白のたっぷりした建築コンセプトスケッチにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-121"><img src="./assets/roster/121.jpg" alt="XXD Panel 121 · 暮らしのドゥードル編集帖" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-121"><strong>121</strong> · 暮らしのドゥードル編集帖</a><br><sub>日常写真のちょっとした気持ちを、余白がたっぷりで絵と言葉の関係が気の利いた暮らしのイラストにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-122"><img src="./assets/roster/122.jpg" alt="XXD Panel 122 · 単色網点と手書きの余白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-122"><strong>122</strong> · 単色網点と手書きの余白</a><br><sub>写真の主役を黒とグレーの網点で刷った小さな絵にし、赤い手書きを一行だけ添えます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-123"><img src="./assets/roster/123.jpg" alt="XXD Panel 123 · 赤青の角線色鉛筆" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-123"><strong>123</strong> · 赤青の角線色鉛筆</a><br><sub>赤と青の色鉛筆と角ばった線で、写真の主役を小さく張りのある手描きに描き直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-124"><img src="./assets/roster/124.jpg" alt="XXD Panel 124 · 布コラージュの余白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-124"><strong>124</strong> · 布コラージュの余白</a><br><sub>大きな布切れ数枚と少しの縫い目で、写真の主役を温かいアップリケの絵に仕立てます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-125"><img src="./assets/roster/125.jpg" alt="XXD Panel 125 · クレヨン童画の余白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-125"><strong>125</strong> · クレヨン童画の余白</a><br><sub>素朴なクレヨンとオイルパステルで、写真の主役を明るい差し色のある絵本の小さな絵にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-126"><img src="./assets/roster/126.jpg" alt="XXD Panel 126 · 詩的なミニチュアコラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-126"><strong>126</strong> · 詩的なミニチュアコラージュ</a><br><sub>写真を切手ほどの水彩と破り紙のコラージュにし、広い手漉き紙の余白にそっと置きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-127"><img src="./assets/roster/127.jpg" alt="XXD Panel 127 · 建築ミクストメディア・コラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-127"><strong>127</strong> · 建築ミクストメディア・コラージュ</a><br><sub>写真を建築家の研究ノートのような小さなコラージュにし、構造線と手書きのメモを添えます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-128"><img src="./assets/roster/128.jpg" alt="XXD Panel 128 · 七宝メダルの旅" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-128"><strong>128</strong> · 七宝メダルの旅</a><br><sub>写真を丸い七宝焼きの記念メダルに収め、上品なセリフ体を添えてミニマルな旅のポスターにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-129"><img src="./assets/roster/129.jpg" alt="XXD Panel 129 · 東洋の拡散と余白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-129"><strong>129</strong> · 東洋の拡散と余白</a><br><sub>写真を東洋的なシルエットの記号にし、縁がやわらかく光る大きな純色の幾何を添えます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-130"><img src="./assets/roster/130.jpg" alt="XXD Panel 130 · ハードエッジ幾何面" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-130"><strong>130</strong> · ハードエッジ幾何面</a><br><sub>写真の主役を黒・白・グレーのハードエッジな幾何面に切り分け、強い差し色を一、二色入れます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-131"><img src="./assets/roster/131.jpg" alt="XXD Panel 131 · 写真と落書きコラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-131"><strong>131</strong> · 写真と落書きコラージュ</a><br><sub>写真を小さな切り抜きのかたまりにして白い紙に貼り、ラフな黒枠と落書きを少し描き足します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-132"><img src="./assets/roster/132.jpg" alt="XXD Panel 132 · ペン淡彩の旅" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-132"><strong>132</strong> · ペン淡彩の旅</a><br><sub>手の揺れが残るペン線と暖色の淡彩で、写真を切手ほどの小さな街角スケッチにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-133"><img src="./assets/roster/133.jpg" alt="XXD Panel 133 · 点刻と透明重ね刷り" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-133"><strong>133</strong> · 点刻と透明重ね刷り</a><br><sub>同じ色の半透明な形を何層も重ね刷りして写真の主役をつくり、重なるほど濃く、細かな点刻で立体を出します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-134"><img src="./assets/roster/134.jpg" alt="XXD Panel 134 · 絵本の色面物語" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-134"><strong>134</strong> · 絵本の色面物語</a><br><sub>上に大きな余白、真ん中に小さな物語の主役、下に混ざり合う色面を一面に敷き、絵本の一ページのようにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-135"><img src="./assets/roster/135.jpg" alt="XXD Panel 135 · ストリート特色手描き誌" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-135"><strong>135</strong> · ストリート特色手描き誌</a><br><sub>ざらついた手描き線、ぶつかり合う数色の特色、印刷の粒子で、写真をストリート系ジンのポスターにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-136"><img src="./assets/roster/136.jpg" alt="XXD Panel 136 · 詩的シュルレアリスムの余白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-136"><strong>136</strong> · 詩的シュルレアリスムの余白</a><br><sub>写真を素朴なシュールレアリスムの小さなキャンバス画に描き換え、不条理でいて的確な一つの関係を残します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-137"><img src="./assets/roster/137.jpg" alt="XXD Panel 137 · エッチング質感コラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-137"><strong>137</strong> · エッチング質感コラージュ</a><br><sub>細いエッチングの線でごく小さな主役を描き、ざらついた印刷の色面を一、二枚重ねます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-138"><img src="./assets/roster/138.jpg" alt="XXD Panel 138 · 東洋の紙レリーフ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-138"><strong>138</strong> · 東洋の紙レリーフ</a><br><sub>手漉きの綿紙を折り、浮き出し、切り重ねて、写真を白い紙の上の小さな浅浮き彫りにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-139"><img src="./assets/roster/139.jpg" alt="XXD Panel 139 · 文字符号の線場" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-139"><strong>139</strong> · 文字符号の線場</a><br><sub>写真をごく細い縦横の線の小さな場に符号化します。遠くからは抽象構造、近づくとかすかに元の姿が見えます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-140"><img src="./assets/roster/140.jpg" alt="XXD Panel 140 · 乾性手描きの視覚島" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-140"><strong>140</strong> · 乾性手描きの視覚島</a><br><sub>写真を白い紙の真ん中の小さなガッシュとオイルパステルの絵にまとめ、大切にしまった記憶のようにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-141"><img src="./assets/roster/141.jpg" alt="XXD Panel 141 · 極簡手描き線画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-141"><strong>141</strong> · 極簡手描き線画</a><br><sub>細く少し揺れる手描きの線を数本だけ使って写真の主役を描き、周りはほとんど余白にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-142"><img src="./assets/roster/142.jpg" alt="XXD Panel 142 · 拡張字形と画像マスク" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-142"><strong>142</strong> · 拡張字形と画像マスク</a><br><sub>写真から一語を選び、引き伸ばした字形の中に主役をはめ込んで、文字と画像を一つにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-143"><img src="./assets/roster/143.jpg" alt="XXD Panel 143 · 文字造形の視覚詩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-143"><strong>143</strong> · 文字造形の視覚詩</a><br><sub>写真から引き出した言葉で主役の輪郭と陰影を組み上げます。遠くからは絵、近づくとすべて文字です。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-144"><img src="./assets/roster/144.jpg" alt="XXD Panel 144 · 幾何白抜きと破枠線描" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-144"><strong>144</strong> · 幾何白抜きと破枠線描</a><br><sub>細い線描と一つの幾何の色面で写真の主役を描き直し、色面の中では白抜き、外に出ると線に戻します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-145"><img src="./assets/roster/145.jpg" alt="XXD Panel 145 · レトロ限定色版画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-145"><strong>145</strong> · レトロ限定色版画</a><br><sub>彫版風のハッチング、点描、網点で、写真を数色の特色で刷り重ねたレトロな小景にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-146"><img src="./assets/roster/146.jpg" alt="XXD Panel 146 · 博物学スカーフ印花" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-146"><strong>146</strong> · 博物学スカーフ印花</a><br><sub>繊細な彫線と数色の明るい平塗りで、写真の主役をスカーフの柄のような博物画のモチーフにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-147"><img src="./assets/roster/147.jpg" alt="XXD Panel 147 · 弁当食材パッケージ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-147"><strong>147</strong> · 弁当食材パッケージ</a><br><sub>写真の中のすべてを食材に置き換え、透明なコンビニ惣菜パックに詰めて真上から撮った商品写真にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-148"><img src="./assets/roster/148.jpg" alt="XXD Panel 148 · ビジュアル日記コラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-148"><strong>148</strong> · ビジュアル日記コラージュ</a><br><sub>写真の切れ端、付箋、テープ、チケット、手書きで、写真を余白たっぷりの私的な日記の一ページにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-149"><img src="./assets/roster/149.jpg" alt="XXD Panel 149 · 手描き質感フラットアート" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-149"><strong>149</strong> · 手描き質感フラットアート</a><br><sub>紙の粒子とパステルの質感がある大きな色面で、切り紙コラージュのように写真の主役を組み直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-150"><img src="./assets/roster/150.jpg" alt="XXD Panel 150 · レトロモダン切り紙" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-150"><strong>150</strong> · レトロモダン切り紙</a><br><sub>色紙で切り出したシルエットと幾何・有機の形で、写真をミッドセンチュリーモダンの小さな切り紙にします。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>151–200</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-151"><img src="./assets/roster/151.jpg" alt="XXD Panel 151 · 素朴なフラット手描き" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-151"><strong>151</strong> · 素朴なフラット手描き</a><br><sub>平塗りの色面とゆがんだ手描きの線で、写真のいちばん個性的な部分だけを描きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-152"><img src="./assets/roster/152.jpg" alt="XXD Panel 152 · 色面ベースのペーパーアート" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-152"><strong>152</strong> · 色面ベースのペーパーアート</a><br><sub>写真の主役を数枚の紙に切り分け、下を横切る一枚の色帯の上に貼り合わせます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-153"><img src="./assets/roster/153.jpg" alt="XXD Panel 153 · 単色手帳ドゥードル" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-153"><strong>153</strong> · 単色手帳ドゥードル</a><br><sub>方眼紙に緑のペン一本で、写真の主役をさらっと描いたような絵にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-154"><img src="./assets/roster/154.jpg" alt="XXD Panel 154 · レトロピクセルと余白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-154"><strong>154</strong> · レトロピクセルと余白</a><br><sub>写真の主役を 16-bit 風のレトロなピクセル画にして、広い余白に置きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-155"><img src="./assets/roster/155.jpg" alt="XXD Panel 155 · 一点透視の淡彩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-155"><strong>155</strong> · 一点透視の淡彩</a><br><sub>写真を一点透視のペン線画にして、ごく淡い水彩をそっと重ねます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-156"><img src="./assets/roster/156.jpg" alt="XXD Panel 156 · 双色版ずれイラスト" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-156"><strong>156</strong> · 双色版ずれイラスト</a><br><sub>写真の主役を二色のインクだけで、少し版ずれしたリソグラフ風の小さなイラストにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-157"><img src="./assets/roster/157.jpg" alt="XXD Panel 157 · 文物の墨拓と余白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-157"><strong>157</strong> · 文物の墨拓と余白</a><br><sub>写真の主役を古代の石刻の拓本にし、まだらで欠けた墨を広い紙面に静かに置きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-158"><img src="./assets/roster/158.jpg" alt="XXD Panel 158 · 紙のミクストメディア・コラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-158"><strong>158</strong> · 紙のミクストメディア・コラージュ</a><br><sub>破った本のページ、新聞の切れ端、ゆるい鉛筆の線で、写真の主役を小さな紙の作品にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-159"><img src="./assets/roster/159.jpg" alt="XXD Panel 159 · 文字網点の実験ポスター" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-159"><strong>159</strong> · 文字網点の実験ポスター</a><br><sub>文字、ドット、網点で写真の主役を組み直し、絵と噛み合うビットマップのタイトルを添えます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-160"><img src="./assets/roster/160.jpg" alt="XXD Panel 160 · 自由な線と淡彩の余白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-160"><strong>160</strong> · 自由な線と淡彩の余白</a><br><sub>ゆるいスケッチの線と透明水彩の数筆で、写真の主役を小さなペン淡彩画にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-161"><img src="./assets/roster/161.jpg" alt="XXD Panel 161 · 色面フレームと越境構図" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-161"><strong>161</strong> · 色面フレームと越境構図</a><br><sub>白い紙の中央に手で刷いた色面を第二の画面として置き、主役が少しだけその外にはみ出します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-162"><img src="./assets/roster/162.jpg" alt="XXD Panel 162 · 白い切り紙台紙の絵本イラスト" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-162"><strong>162</strong> · 白い切り紙台紙の絵本イラスト</a><br><sub>写真の主役をクレヨンの質感がある素朴な絵本の絵にし、手で切った白い紙を下に敷きます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-163"><img src="./assets/roster/163.jpg" alt="XXD Panel 163 · 中央の単色色面スタンプ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-163"><strong>163</strong> · 中央の単色色面スタンプ</a><br><sub>数枚のすっきりした単色の色面で、写真の主役を画面中央の小さなスタンプにまとめます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-164"><img src="./assets/roster/164.jpg" alt="XXD Panel 164 · 水墨と建築線描の小景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-164"><strong>164</strong> · 水墨と建築線描の小景</a><br><sub>写真を、淡墨の山水に建築家のスケッチのような線を重ねた小さな景色にし、橙をひとさしだけ入れます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-165"><img src="./assets/roster/165.jpg" alt="XXD Panel 165 · 中央の裂け目から現れる紙コラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-165"><strong>165</strong> · 中央の裂け目から現れる紙コラージュ</a><br><sub>淡い色の紙の真ん中を縦に裂き、その隙間から写真の主役が幾何学的な色面で現れます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-166"><img src="./assets/roster/166.jpg" alt="XXD Panel 166 · 等角投影の彫刻的浅浮彫ジオラマ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-166"><strong>166</strong> · 等角投影の彫刻的浅浮彫ジオラマ</a><br><sub>写真の主役を等角投影のミニチュア模型にし、浅浮彫のように層を重ねて浮き上がらせます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-167"><img src="./assets/roster/167.jpg" alt="XXD Panel 167 · 中央の波形と厚盛りインク" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-167"><strong>167</strong> · 中央の波形と厚盛りインク</a><br><sub>写真の主役を中央の抽象的な波に乗せ、全体を厚く盛ったインクで刷った浮彫のように仕上げます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-168"><img src="./assets/roster/168.jpg" alt="XXD Panel 168 · 紙白を残す重ね刷毛の色面" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-168"><strong>168</strong> · 紙白を残す重ね刷毛の色面</a><br><sub>白い紙に暖色の色面を重ねて刷き、写真の主役はそのとき塗り残した紙の白になります。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-169"><img src="./assets/roster/169.jpg" alt="XXD Panel 169 · 暖かな黄土色の小さな線画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-169"><strong>169</strong> · 暖かな黄土色の小さな線画</a><br><sub>ゆるい炭黒の線と黄土色の淡彩で、写真の主役を小さく独立した挿絵にし、要所を描いたら筆を止めます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-170"><img src="./assets/roster/170.jpg" alt="XXD Panel 170 · 黒と錆赤のドライメディア小景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-170"><strong>170</strong> · 黒と錆赤のドライメディア小景</a><br><sub>炭黒とわずかな錆赤だけで、ざらついたクレヨンの数筆で写真の主役をごく小さな挿絵にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-171"><img src="./assets/roster/171.jpg" alt="XXD Panel 171 · 縦線の骨格と微小な散点" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-171"><strong>171</strong> · 縦線の骨格と微小な散点</a><br><sub>広い温かな白に細く淡い縦線を数本立て、写真の人や物を小さな島のように散らします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-172"><img src="./assets/roster/172.jpg" alt="XXD Panel 172 · 中央の主題と半透明幾何レイヤー" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-172"><strong>172</strong> · 中央の主題と半透明幾何レイヤー</a><br><sub>写真の主役を画面の真ん中に小さく置き、その後ろに淡い半透明の幾何学の色片を浮かべます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-173"><img src="./assets/roster/173.jpg" alt="XXD Panel 173 · 象牙色の紙と文字の微小景観" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-173"><strong>173</strong> · 象牙色の紙と文字の微小景観</a><br><sub>写真を、古い本の紙と文字で組んだ小さな紙の景色に縮め、広い温かな白に浮かべます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-174"><img src="./assets/roster/174.jpg" alt="XXD Panel 174 · 素朴な手描きステッカーの集合" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-174"><strong>174</strong> · 素朴な手描きステッカーの集合</a><br><sub>写真の主役を太い筆の手描きステッカーに分け、画面中央で再びひとつの姿に集めます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-175"><img src="./assets/roster/175.jpg" alt="XXD Panel 175 · 琥珀の透過光と象牙色の紙彫小景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-175"><strong>175</strong> · 琥珀の透過光と象牙色の紙彫小景</a><br><sub>写真を重ねた象牙色の小さな紙彫りにし、紙の層のあいだから温かな琥珀色の光をこぼします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-176"><img src="./assets/roster/176.jpg" alt="XXD Panel 176 · 細密手描きの浅浮彫儀式図" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-176"><strong>176</strong> · 細密手描きの浅浮彫儀式図</a><br><sub>写真の主役を、工筆の細線で描いた精緻な陣図の中心に据え、層を重ねて浮かせ、外へ向かってまばらにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-177"><img src="./assets/roster/177.jpg" alt="XXD Panel 177 · 異形シルエットの版画ミクロ島" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-177"><strong>177</strong> · 異形シルエットの版画ミクロ島</a><br><sub>写真の核を小さな異形の版画の島に押し込め、墨紺、灰オリーブ、わずかな朱橙で刻みます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-178"><img src="./assets/roster/178.jpg" alt="XXD Panel 178 · 手帳の墨記" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-178"><strong>178</strong> · 手帳の墨記</a><br><sub>写真を、古いインクでさっと描いた小さな印にまとめます。古い手帳の隅のひと筆のように。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-179"><img src="./assets/roster/179.jpg" alt="XXD Panel 179 · リボン状の微小展示風景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-179"><strong>179</strong> · リボン状の微小展示風景</a><br><sub>写真の核をいくつかのミニチュアの展示品にし、宙に浮かぶ象牙色のリボンの上にまばらに並べます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-180"><img src="./assets/roster/180.jpg" alt="XXD Panel 180 · 旅の記憶を刻むレトロ円形スタンプ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-180"><strong>180</strong> · 旅の記憶を刻むレトロ円形スタンプ</a><br><sub>写真の主役と周囲の手がかり一、二点を、古びた象牙色の紙に押したレトロな丸い記念スタンプに刻みます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-181"><img src="./assets/roster/181.jpg" alt="XXD Panel 181 · 文人彩墨の小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-181"><strong>181</strong> · 文人彩墨の小品</a><br><sub>墨を骨に、淡彩を添えて、写真を余白の多い小さな文人画にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-182"><img src="./assets/roster/182.jpg" alt="XXD Panel 182 · ミニチュアピクセル小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-182"><strong>182</strong> · ミニチュアピクセル小品</a><br><sub>写真の主役を、エッジの硬い小さなピクセル図形にまとめ、広い余白に静かに置きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-183"><img src="./assets/roster/183.jpg" alt="XXD Panel 183 · 深緑のコーナー有機図形" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-183"><strong>183</strong> · 深緑のコーナー有機図形</a><br><sub>写真の主役を角に寄せた小さな自然図形にまとめ、クリーム地を深緑で引き締めます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-184"><img src="./assets/roster/184.jpg" alt="XXD Panel 184 · 正方形の日常手描き小景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-184"><strong>184</strong> · 正方形の日常手描き小景</a><br><sub>写真の暮らしのディテールを正方形の小さな場面に詰め、ゆるい線と色鉛筆、水彩で描きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-185"><img src="./assets/roster/185.jpg" alt="XXD Panel 185 · 淡色を添えた白黒ステッカー小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-185"><strong>185</strong> · 淡色を添えた白黒ステッカー小品</a><br><sub>写真の主役を、淡い色を一点だけ添えた小さな白黒の手描きステッカー図形にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-186"><img src="./assets/roster/186.jpg" alt="XXD Panel 186 · 淡色の九分割幾何学記憶" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-186"><strong>186</strong> · 淡色の九分割幾何学記憶</a><br><sub>写真を九つの記憶のかけらに分け、柔らかな平塗りの幾何学色面で九分割グリッドに並べます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-187"><img src="./assets/roster/187.jpg" alt="XXD Panel 187 · 大きな文字のアーカイブコラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-187"><strong>187</strong> · 大きな文字のアーカイブコラージュ</a><br><sub>写真の主役を写真の断片と製図線のアーカイブコラージュにし、背後に特大の文字を敷きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-188"><img src="./assets/roster/188.jpg" alt="XXD Panel 188 · 米色と金色の建築アーカイブ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-188"><strong>188</strong> · 米色と金色の建築アーカイブ</a><br><sub>写真の主役を小さな建築標本のように縮め、古紙色の余白にサンドゴールドの題字を添えます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-189"><img src="./assets/roster/189.jpg" alt="XXD Panel 189 · 二重枠とサイドバーのマッチ箱小景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-189"><strong>189</strong> · 二重枠とサイドバーのマッチ箱小景</a><br><sub>写真を古いマッチ箱ラベルの中の小さな挿絵にし、二重の枠と細いサイドバーで囲みます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-190"><img src="./assets/roster/190.jpg" alt="XXD Panel 190 · 寒色主体の素朴なパステル" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-190"><strong>190</strong> · 寒色主体の素朴なパステル</a><br><sub>写真を寒色のグレートーンを主にした小さな素朴なパステル画にし、暖色をほんの少し添えます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-191"><img src="./assets/roster/191.jpg" alt="XXD Panel 191 · 毛羽立つ矩形パステル色面" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-191"><strong>191</strong> · 毛羽立つ矩形パステル色面</a><br><sub>写真を縁の毛羽立った小さな矩形のパステル色面に描き、広い余白に浮かべます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-192"><img src="./assets/roster/192.jpg" alt="XXD Panel 192 · 限定色のレトロ図形小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-192"><strong>192</strong> · 限定色のレトロ図形小品</a><br><sub>写真をシルエットと色面の小さな図形にまとめ、二から四色のレトロな限定色で紙に刷ります。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-193"><img src="./assets/roster/193.jpg" alt="XXD Panel 193 · 低い台座の灰調水彩小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-193"><strong>193</strong> · 低い台座の灰調水彩小品</a><br><sub>写真を淡い低い台座に載った灰調の水彩の小さな形にまとめ、周りに紙の余白を広く残します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-194"><img src="./assets/roster/194.jpg" alt="XXD Panel 194 · 明るい敷地台座の軸測模型" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-194"><strong>194</strong> · 明るい敷地台座の軸測模型</a><br><sub>写真の主役を、平らな敷地台座から立ち上がる明るい色の軸測ブロック模型にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-195"><img src="./assets/roster/195.jpg" alt="XXD Panel 195 · 一色が光る歴史モンタージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-195"><strong>195</strong> · 一色が光る歴史モンタージュ</a><br><sub>写真を白黒と暖かいグレーのアーカイブ写真モンタージュに編み直し、元の写真の明るい一色だけを残します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-196"><img src="./assets/roster/196.jpg" alt="XXD Panel 196 · 俯瞰の幾何学人物小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-196"><strong>196</strong> · 俯瞰の幾何学人物小品</a><br><sub>写真の人物を真上から見下ろし、円とカプセル形でできた平面の幾何学人物に描き直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-197"><img src="./assets/roster/197.jpg" alt="XXD Panel 197 · 籠の中の世界を描く民芸イラスト" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-197"><strong>197</strong> · 籠の中の世界を描く民芸イラスト</a><br><sub>写真のテーマを籠の中に入れ、平面的で温かな新民芸の手描きで小さな世界として描きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-198"><img src="./assets/roster/198.jpg" alt="XXD Panel 198 · 限定色の浮遊ファッションコラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-198"><strong>198</strong> · 限定色の浮遊ファッションコラージュ</a><br><sub>写真の主役を宙に浮かぶコンセプチュアルなファッションイラストにし、コラージュと網点、限定色で刷ります。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-199"><img src="./assets/roster/199.jpg" alt="XXD Panel 199 · 明るく余白豊かな小型ファッションコラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-199"><strong>199</strong> · 明るく余白豊かな小型ファッションコラージュ</a><br><sub>写真の主役を宙に浮かぶ小さなファッションイラストの姿にし、明るく温かな白の大きな余白に置きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-200"><img src="./assets/roster/200.jpg" alt="XXD Panel 200 · 青灰色の単色手描き線画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-200"><strong>200</strong> · 青灰色の単色手描き線画</a><br><sub>青灰色一色のゆるやかな線で、写真をスケッチの跡が残る小さな線画にします。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>201–250</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-201"><img src="./assets/roster/201.jpg" alt="XXD Panel 201 · クリーム色の手作りミニチュア" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-201"><strong>201</strong> · クリーム色の手作りミニチュア</a><br><sub>写真の主役をクリーム色の手作りミニチュアの置物にし、広い余白に静かに置きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-202"><img src="./assets/roster/202.jpg" alt="XXD Panel 202 · 構造軸を持つ幾何学線図" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-202"><strong>202</strong> · 構造軸を持つ幾何学線図</a><br><sub>写真から数本の構造線を引き出し、主役をその線に掛かる青灰色の幾何学線図として描きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-203"><img src="./assets/roster/203.jpg" alt="XXD Panel 203 · 余白を活かす厚塗り絵葉書" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-203"><strong>203</strong> · 余白を活かす厚塗り絵葉書</a><br><sub>写真を厚塗りの油彩の小さな景色にして大きな余白に置き、アートな絵葉書のように仕上げます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-204"><img src="./assets/roster/204.jpg" alt="XXD Panel 204 · 柔らかな光と記憶の小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-204"><strong>204</strong> · 柔らかな光と記憶の小品</a><br><sub>写真の主役を、ソフトフォーカスの光とぼやけたシルエットの小さなかたまりに変え、光が残した記憶のようにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-205"><img src="./assets/roster/205.jpg" alt="XXD Panel 205 · 暖色の有機形写真コラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-205"><strong>205</strong> · 暖色の有機形写真コラージュ</a><br><sub>写真を丸みのある有機形に切り抜き、細い手描きの線を重ね、暖色とテラコッタを一点添えます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-206"><img src="./assets/roster/206.jpg" alt="XXD Panel 206 · 淡色の積層ペーパークラフト小景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-206"><strong>206</strong> · 淡色の積層ペーパークラフト小景</a><br><sub>写真の主役を重ねた紙でできた浅いレリーフの小景にし、柔らかな紙の色と広い余白で仕上げます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-207"><img src="./assets/roster/207.jpg" alt="XXD Panel 207 · 淡い青と白の混合メディア挿絵" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-207"><strong>207</strong> · 淡い青と白の混合メディア挿絵</a><br><sub>写真を中央に置いた写真と線画の小さなコラージュにし、淡い青と白の地の雑誌の挿し込みページのようにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-208"><img src="./assets/roster/208.jpg" alt="XXD Panel 208 · 青とピンクのモダニズム抽象" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-208"><strong>208</strong> · 青とピンクのモダニズム抽象</a><br><sub>写真を、青とピンクの色面と黒い線の質感でできた小さなモダニズムの抽象図形にまとめます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-209"><img src="./assets/roster/209.jpg" alt="XXD Panel 209 · 紙の質感を持つ極小画像アーカイブ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-209"><strong>209</strong> · 紙の質感を持つ極小画像アーカイブ</a><br><sub>写真を紙面の小さな画像に縮め、アーカイブ風の小さな文字を添えて、大切に保管された写真集の一頁のようにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-210"><img src="./assets/roster/210.jpg" alt="XXD Panel 210 · 寒色の軽やかな概念コラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-210"><strong>210</strong> · 寒色の軽やかな概念コラージュ</a><br><sub>写真の主役を小さな写真コラージュにし、寒色の青の手描き線、小さな吹き出し、記号を添えます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-211"><img src="./assets/roster/211.jpg" alt="XXD Panel 211 · 意味に基づく配色の幾何学小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-211"><strong>211</strong> · 意味に基づく配色の幾何学小品</a><br><sub>写真を幾何学的な色面の小さな図形にまとめ、色は主役の正体、素材、季節に合わせて選びます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-212"><img src="./assets/roster/212.jpg" alt="XXD Panel 212 · 近単色の彫刻的形態研究" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-212"><strong>212</strong> · 近単色の彫刻的形態研究</a><br><sub>写真の主役を、広い余白に浮かぶ小さな白い概念模型にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-213"><img src="./assets/roster/213.jpg" alt="XXD Panel 213 · 暖かな紙の寒色概念線画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-213"><strong>213</strong> · 暖かな紙の寒色概念線画</a><br><sub>写真の気分や関係を、暖かな古紙に寒色一色で描く小さな詩的線画にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-214"><img src="./assets/roster/214.jpg" alt="XXD Panel 214 · 固有色を活かす粗い切り絵小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-214"><strong>214</strong> · 固有色を活かす粗い切り絵小品</a><br><sub>写真を、広い白紙に置いた、本来の色を残す粗い切り絵の小さなイラストにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-215"><img src="./assets/roster/215.jpg" alt="XXD Panel 215 · 黄土色を添えた灰階軸測図" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-215"><strong>215</strong> · 黄土色を添えた灰階軸測図</a><br><sub>写真の主役を、黄土色を一点だけ添えた白と灰の精密な軸測図の小品にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-216"><img src="./assets/roster/216.jpg" alt="XXD Panel 216 · 広大な余白の極小印刷アイランド" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-216"><strong>216</strong> · 広大な余白の極小印刷アイランド</a><br><sub>写真を、広い暖色の紙面に置いたごく小さな単色の印刷ブロックに圧縮します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-217"><img src="./assets/roster/217.jpg" alt="XXD Panel 217 · 明るいデジタル混合メディアコラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-217"><strong>217</strong> · 明るいデジタル混合メディアコラージュ</a><br><sub>写真の主役を切り抜き、手描きの落書きや紙片と組み合わせて明るい雑誌風コラージュにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-218"><img src="./assets/roster/218.jpg" alt="XXD Panel 218 · ミニマルな絵本風ニードルフェルト" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-218"><strong>218</strong> · ミニマルな絵本風ニードルフェルト</a><br><sub>写真をごく簡潔な絵本の一場面にまとめ、柔らかな手作りの羊毛フェルトで仕上げます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-219"><img src="./assets/roster/219.jpg" alt="XXD Panel 219 · 色鉛筆を添えた旅日記スケッチ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-219"><strong>219</strong> · 色鉛筆を添えた旅日記スケッチ</a><br><sub>写真を旅手帳の黒いペンスケッチにし、色鉛筆で数か所だけ色を差します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-220"><img src="./assets/roster/220.jpg" alt="XXD Panel 220 · 丸みのある素朴な手描きドゥードル" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-220"><strong>220</strong> · 丸みのある素朴な手描きドゥードル</a><br><sub>写真を、丸くゆるい線で描き、ところどころだけ色を差したかわいい手描きドゥードルにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-221"><img src="./assets/roster/221.jpg" alt="XXD Panel 221 · 新中式の特色版画と余白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-221"><strong>221</strong> · 新中式の特色版画と余白</a><br><sub>写真を、印章のような小さな新中式の特色版画にまとめ、まわりに東洋的な余白を広く取ります。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-222"><img src="./assets/roster/222.jpg" alt="XXD Panel 222 · 建築的タイポグラフィ装置" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-222"><strong>222</strong> · 建築的タイポグラフィ装置</a><br><sub>写真の主役を、文字と幾何ブロックで組み上げた小さなカラフルなランドマークにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-223"><img src="./assets/roster/223.jpg" alt="XXD Panel 223 · レトロ版画のミニ図鑑" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-223"><strong>223</strong> · レトロ版画のミニ図鑑</a><br><sub>写真を、互いにつながらない小さな版画の図にばらし、古い図鑑の一頁のようにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-224"><img src="./assets/roster/224.jpg" alt="XXD Panel 224 · 磁器片の再構成" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-224"><strong>224</strong> · 磁器片の再構成</a><br><sub>写真の主役を中国磁器の破片で組み直し、すき間やひび、広い磁器の白を残します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-225"><img src="./assets/roster/225.jpg" alt="XXD Panel 225 · 事務用品の手描きコラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-225"><strong>225</strong> · 事務用品の手描きコラージュ</a><br><sub>付箋、クリップ、テープ、紙片で、写真を一頁の視覚日記に書き直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-226"><img src="./assets/roster/226.jpg" alt="XXD Panel 226 · アイシングクッキーの浅浮き彫り" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-226"><strong>226</strong> · アイシングクッキーの浅浮き彫り</a><br><sub>写真の主役と場面をいっしょに、マットで丸みのある小さなアイシングクッキーの浮き彫りにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-227"><img src="./assets/roster/227.jpg" alt="XXD Panel 227 · 刺繍ミッションパッチ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-227"><strong>227</strong> · 刺繍ミッションパッチ</a><br><sub>写真を、縁かがりとサテン刺繍の文字、短い番号をもつ一枚の機械刺繍ミッションパッチにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-228"><img src="./assets/roster/228.jpg" alt="XXD Panel 228 · 作家の手作り紙オブジェ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-228"><strong>228</strong> · 作家の手作り紙オブジェ</a><br><sub>写真を、独立系書店で見かけるような手作りの紙ものに作り直します。素朴な切り紙と少しの特色。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-229"><img src="./assets/roster/229.jpg" alt="XXD Panel 229 · 新民芸の静かな余白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-229"><strong>229</strong> · 新民芸の静かな余白</a><br><sub>写真の魂を、丸みのあるパステルの、静かで懐かしい新民芸風の小さな挿画にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-230"><img src="./assets/roster/230.jpg" alt="XXD Panel 230 · 負の形のモニュメント" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-230"><strong>230</strong> · 負の形のモニュメント</a><br><sub>密な手描きの短い線で主役を巨大な白い負の形として残し、そばにごく小さな人物を一人だけ置きます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-231"><img src="./assets/roster/231.jpg" alt="XXD Panel 231 · ネオ・ナイーブ手描き" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-231"><strong>231</strong> · ネオ・ナイーブ手描き</a><br><sub>写真を、揺れる色線、マーカー、色鉛筆で描いた小さくゆるい手描きにし、余白をたっぷり取ります。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-232"><img src="./assets/roster/232.jpg" alt="XXD Panel 232 · 横に重なる民芸風景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-232"><strong>232</strong> · 横に重なる民芸風景</a><br><sub>写真を、静かに横へ広がる帯状の風景に圧縮します。人はごく小さな句読点だけ。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-233"><img src="./assets/roster/233.jpg" alt="XXD Panel 233 · タフティングの繊維壁飾り" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-233"><strong>233</strong> · タフティングの繊維壁飾り</a><br><sub>写真を、淡い無地の地に散らした明るいループパイルの小さな壁飾り数点に作り直します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-234"><img src="./assets/roster/234.jpg" alt="XXD Panel 234 · デジタル編集のキービジュアル" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-234"><strong>234</strong> · デジタル編集のキービジュアル</a><br><sub>写真を、平らな色面、角丸モジュール、細い線、広い余白でできた若々しいキービジュアルにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-235"><img src="./assets/roster/235.jpg" alt="XXD Panel 235 · ミントのピクセル料理" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-235"><strong>235</strong> · ミントのピクセル料理</a><br><sub>写真を、ミント色の夢の中のピクセル料理バッジにします。中心はくっきり、まわりは白に溶けます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-236"><img src="./assets/roster/236.jpg" alt="XXD Panel 236 · 白黒の幾何記号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-236"><strong>236</strong> · 白黒の幾何記号</a><br><sub>写真を、途切れない白の真ん中に置いたごく小さな白黒の幾何記号に圧縮します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-237"><img src="./assets/roster/237.jpg" alt="XXD Panel 237 · Y2Kステッカーコラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-237"><strong>237</strong> · Y2Kステッカーコラージュ</a><br><sub>同じ主役を白フチのシール数枚に分け、淡い灰紫の neo-Y2K ZINE のページに散らします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-238"><img src="./assets/roster/238.jpg" alt="XXD Panel 238 · ゴシック絵本の小さな姿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-238"><strong>238</strong> · ゴシック絵本の小さな姿</a><br><sub>写真を、ほとんど空白の紙に置いた、小さく脆く少し暗いガッシュの絵本の姿にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-239"><img src="./assets/roster/239.jpg" alt="XXD Panel 239 · 特色の版ずれポスター" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-239"><strong>239</strong> · 特色の版ずれポスター</a><br><sub>写真を、文字が図になる特色孔版の実験ポスターにします。網点、版ずれ、暖かな紙。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-240"><img src="./assets/roster/240.jpg" alt="XXD Panel 240 · クレヨンの視覚日記" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-240"><strong>240</strong> · クレヨンの視覚日記</a><br><sub>写真を、描ききらないクレヨンの視覚日記の一頁にします。小さな主役、暖かな土色、広い空白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-241"><img src="./assets/roster/241.jpg" alt="XXD Panel 241 · 詩的な標本図鑑" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-241"><strong>241</strong> · 詩的な標本図鑑</a><br><sub>主役を詩的な標本の一頁にします。一部は精密なモノクロ写真、欠けた部分は空白の中の脆い手描きの輪郭。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-242"><img src="./assets/roster/242.jpg" alt="XXD Panel 242 · 素朴なお守りイラスト" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-242"><strong>242</strong> · 素朴なお守りイラスト</a><br><sub>写真の中のありふれたものを、深いマットな地に置いたキャンディ色の素朴なお守りにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-243"><img src="./assets/roster/243.jpg" alt="XXD Panel 243 · 青ボールペンの罫線手稿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-243"><strong>243</strong> · 青ボールペンの罫線手稿</a><br><sub>写真を、青いボールペンで描いた罫線ノートの一ページにします。線の密度に差があり、描く過程も残ります。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-244"><img src="./assets/roster/244.jpg" alt="XXD Panel 244 · 筆を止めたノート" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-244"><strong>244</strong> · 筆を止めたノート</a><br><sub>写真を、個人のノートにさっと描いた一筆にします。小さな主役、途切れる墨線、薄い水彩が少し。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-245"><img src="./assets/roster/245.jpg" alt="XXD Panel 245 · 記憶の余白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-245"><strong>245</strong> · 記憶の余白</a><br><sub>写真を静かな記憶の一ページにします。丸く簡略化した小さな主役のまわりに、広い白い紙。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-246"><img src="./assets/roster/246.jpg" alt="XXD Panel 246 · ネオ構成主義コラージュ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-246"><strong>246</strong> · ネオ構成主義コラージュ</a><br><sub>写真の主役一つを、幾何学の色面と構造線、広い余白でできたコンセプトポスターにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-247"><img src="./assets/roster/247.jpg" alt="XXD Panel 247 · やわらかな絵本" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-247"><strong>247</strong> · やわらかな絵本</a><br><sub>写真の中の一つの姿を、色鉛筆と水彩の小さな絵本の一場面にします。まわりは広い余白です。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-248"><img src="./assets/roster/248.jpg" alt="XXD Panel 248 · 古い旅の手帖" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-248"><strong>248</strong> · 古い旅の手帖</a><br><sub>写真のすべてではなく、見たあとに残った印象を描きます。淡い墨と水彩の旅の手帖の一ページです。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-249"><img src="./assets/roster/249.jpg" alt="XXD Panel 249 · 雰囲気ピクセル" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-249"><strong>249</strong> · 雰囲気ピクセル</a><br><sub>写真の一瞬を、レトロゲームの世界の静かな一コマにします。低解像度、やわらかな色面、広い余白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-250"><img src="./assets/roster/250.jpg" alt="XXD Panel 250 · 建築幾何の詩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-250"><strong>250</strong> · 建築幾何の詩</a><br><sub>写真の場面を、抽象的な建築の輪郭、幾何学の色面、静かな余白にまとめます。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>251–300</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-251"><img src="./assets/roster/251.jpg" alt="XXD Panel 251 · ピクセル生命アーカイブ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-251"><strong>251</strong> · ピクセル生命アーカイブ</a><br><sub>写真の主役を、グリッド上のピクセルの生命記号にします。未来の文明が保存した自然標本のように。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-252"><img src="./assets/roster/252.jpg" alt="XXD Panel 252 · 癒やしステッカー" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-252"><strong>252</strong> · 癒やしステッカー</a><br><sub>写真の主役を、丸くてやわらかな手帳用の小さなステッカーにします。まわりは静かな余白です。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-253"><img src="./assets/roster/253.jpg" alt="XXD Panel 253 · フラットな鍵" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-253"><strong>253</strong> · フラットな鍵</a><br><sub>写真のテーマを、澄んだ色面のフラットな記号にします。物語をもつ視覚の鍵のように。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-254"><img src="./assets/roster/254.jpg" alt="XXD Panel 254 · 東洋幾何アーカイブ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-254"><strong>254</strong> · 東洋幾何アーカイブ</a><br><sub>写真の主役を半透明の幾何学の断片に分解し、広い空白の中に浮かべます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-255"><img src="./assets/roster/255.jpg" alt="XXD Panel 255 · 旅の記念切手" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-255"><strong>255</strong> · 旅の記念切手</a><br><sub>写真の一瞬を小さな旅の記念切手に封じ込めます。まわりは広い白い紙面です。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-256"><img src="./assets/roster/256.jpg" alt="XXD Panel 256 · 素朴な民藝" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-256"><strong>256</strong> · 素朴な民藝</a><br><sub>写真を、中央に置いた素朴な民藝の小さな絵にします。主役一つ、気持ち一つ、金箔を少し。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-257"><img src="./assets/roster/257.jpg" alt="XXD Panel 257 · 静寂の一本線" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-257"><strong>257</strong> · 静寂の一本線</a><br><sub>写真の主役を、ごく細く少し不規則な一本の線にして、広い余白に浮かべます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-258"><img src="./assets/roster/258.jpg" alt="XXD Panel 258 · クリームの夢景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-258"><strong>258</strong> · クリームの夢景</a><br><sub>写真の主役を、クリームのようにやわらかい小さな彫刻にこね直し、クリーム色の広い空間に浮かべます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-259"><img src="./assets/roster/259.jpg" alt="XXD Panel 259 · 古典の詩稿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-259"><strong>259</strong> · 古典の詩稿</a><br><sub>写真の主役を、不完全な墨線で描いた古典的な詩稿の一ページにします。何年もたってから記憶で描いた一瞬のように。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-260"><img src="./assets/roster/260.jpg" alt="XXD Panel 260 · 幾何の記憶" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-260"><strong>260</strong> · 幾何の記憶</a><br><sub>写真を幾何学の記号でできた記憶の地図にします。主役は小さく、まわりは広い余白です。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-261"><img src="./assets/roster/261.jpg" alt="XXD Panel 261 · クレヨンの記憶" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-261"><strong>261</strong> · クレヨンの記憶</a><br><sub>その場所ではなく、そこに残った感じを描きます。色鉛筆とクレヨンで描いた小さな記憶です。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-262"><img src="./assets/roster/262.jpg" alt="XXD Panel 262 · フィルムの残像" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-262"><strong>262</strong> · フィルムの残像</a><br><sub>写真の主役を、彩度を抑えた古い映画の一コマの残像にして、広い余白に静かに浮かべます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-263"><img src="./assets/roster/263.jpg" alt="XXD Panel 263 · 記念の印章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-263"><strong>263</strong> · 記念の印章</a><br><sub>写真の主役を小さな記念の印章にします。大切にしまわれた文化の記念品のように。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-264"><img src="./assets/roster/264.jpg" alt="XXD Panel 264 · 手稿の落書き" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-264"><strong>264</strong> · 手稿の落書き</a><br><sub>写真を、個人のスケッチブックの一ページに描いた素朴な線画にします。描きかけでも、気持ちはたっぷり。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-265"><img src="./assets/roster/265.jpg" alt="XXD Panel 265 · 植物の紋章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-265"><strong>265</strong> · 植物の紋章</a><br><sub>写真の主役を、花と葉に囲まれた小さな紋章にします。長く大切にされてきた個人の印のように。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-266"><img src="./assets/roster/266.jpg" alt="XXD Panel 266 · シンボルマーク" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-266"><strong>266</strong> · シンボルマーク</a><br><sub>写真の主役を小さなミニマルな記号にします。文化施設やブランドのマークのように。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-267"><img src="./assets/roster/267.jpg" alt="XXD Panel 267 · 布のバッジ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-267"><strong>267</strong> · 布のバッジ</a><br><sub>写真の主役を小さな布のバッジにします。デニム、ステッチ、パッチワーク、ほつれた縁。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-268"><img src="./assets/roster/268.jpg" alt="XXD Panel 268 · 静かな記号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-268"><strong>268</strong> · 静かな記号</a><br><sub>写真の主役を、個人のコレクションに押された印のような、ごく小さく静かな記号にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-269"><img src="./assets/roster/269.jpg" alt="XXD Panel 269 · 実験手帖" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-269"><strong>269</strong> · 実験手帖</a><br><sub>写真の主役を、実験ノートに記された小さなコンセプト記号にします。墨線、網点、少しの色面。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-270"><img src="./assets/roster/270.jpg" alt="XXD Panel 270 · 東洋のトーテム" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-270"><strong>270</strong> · 東洋のトーテム</a><br><sub>写真の主役を、東洋の印章のような小さなトーテムにします。小さく厳かに、まわりは広い余白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-271"><img src="./assets/roster/271.jpg" alt="XXD Panel 271 · 個人の徽章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-271"><strong>271</strong> · 個人の徽章</a><br><sub>写真の主役を民藝の版画のような個人の徽章にします。輪郭一つ、特色を数色、紙の上のインク。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-272"><img src="./assets/roster/272.jpg" alt="XXD Panel 272 · モノクロの小さな魂" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-272"><strong>272</strong> · モノクロの小さな魂</a><br><sub>写真の主役を、少し表情と気分のある白黒の手描きキャラクターにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-273"><img src="./assets/roster/273.jpg" alt="XXD Panel 273 · アール・ヌーヴォー紋章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-273"><strong>273</strong> · アール・ヌーヴォー紋章</a><br><sub>写真の主役を、色をひとつだけ差したアール・ヌーヴォー調の細線の紋章にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-274"><img src="./assets/roster/274.jpg" alt="XXD Panel 274 · 夜色のクレヨン" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-274"><strong>274</strong> · 夜色のクレヨン</a><br><sub>黒い紙に、光るようなクレヨンの色線で写真の主役を小さなマークとして描きます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-275"><img src="./assets/roster/275.jpg" alt="XXD Panel 275 · 素朴なバッジ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-275"><strong>275</strong> · 素朴なバッジ</a><br><sub>写真の主役を、丸くて少し不器用な手作りの小さなバッジにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-276"><img src="./assets/roster/276.jpg" alt="XXD Panel 276 · 空間アーカイブ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-276"><strong>276</strong> · 空間アーカイブ</a><br><sub>写真の構造を分解し、極細線の未完成な空間スタディとして重ねます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-277"><img src="./assets/roster/277.jpg" alt="XXD Panel 277 · 幾何学マーク" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-277"><strong>277</strong> · 幾何学マーク</a><br><sub>写真の主役を、幾何学的なシルエットと平塗りの色面で組んだモダニズムの小さな記号にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-278"><img src="./assets/roster/278.jpg" alt="XXD Panel 278 · 文化の切り絵" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-278"><strong>278</strong> · 文化の切り絵</a><br><sub>写真の主役を、幾何学的な色面で組んだシルクスクリーン風の切り絵の小さな印章にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-279"><img src="./assets/roster/279.jpg" alt="XXD Panel 279 · システムの遺伝子" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-279"><strong>279</strong> · システムの遺伝子</a><br><sub>写真の主役を、幾何学モジュールと細線と小さな番号でできたポストデジタルの抽象マークにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-280"><img src="./assets/roster/280.jpg" alt="XXD Panel 280 · ピクセル標本" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-280"><strong>280</strong> · ピクセル標本</a><br><sub>写真の主役を、信号色をひとつだけ灯した低解像度のピクセル徽章として、記録ページに収めます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-281"><img src="./assets/roster/281.jpg" alt="XXD Panel 281 · 生きている象形" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-281"><strong>281</strong> · 生きている象形</a><br><sub>写真の主役を、平らで暗い色の、無表情なのに少し生き物めいた小さな象形にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-282"><img src="./assets/roster/282.jpg" alt="XXD Panel 282 · ソフトフォーカスの有機" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-282"><strong>282</strong> · ソフトフォーカスの有機</a><br><sub>写真の主役を、半透明の重なりと乳白色のパステルでできた小さな抽象マークにやわらげます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-283"><img src="./assets/roster/283.jpg" alt="XXD Panel 283 · 時代の徽章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-283"><strong>283</strong> · 時代の徽章</a><br><sub>写真の主役を、宇宙時代のどこかの機関が正式に発行したような徽章にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-284"><img src="./assets/roster/284.jpg" alt="XXD Panel 284 · 文明の紋章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-284"><strong>284</strong> · 文明の紋章</a><br><sub>写真の主役を幾何学の枠に収め、寒色と暖色がぶつかる小さな記念碑として刷り上げます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-285"><img src="./assets/roster/285.jpg" alt="XXD Panel 285 · 科学記念章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-285"><strong>285</strong> · 科学記念章</a><br><sub>写真の主役を、太い輪郭と網点インクの切手のような科学記念章に刷り上げます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-286"><img src="./assets/roster/286.jpg" alt="XXD Panel 286 · パステルのトーテム" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-286"><strong>286</strong> · パステルのトーテム</a><br><sub>写真の中でいちばん残したいイメージを、軽やかで少し不思議なパステルの小さなトーテムにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-287"><img src="./assets/roster/287.jpg" alt="XXD Panel 287 · 紙の上の小さなメモ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-287"><strong>287</strong> · 紙の上の小さなメモ</a><br><sub>写真の主役を、広い白紙の上に描かれた、とても小さな生き物のような記号にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-288"><img src="./assets/roster/288.jpg" alt="XXD Panel 288 · 収蔵の紋章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-288"><strong>288</strong> · 収蔵の紋章</a><br><sub>写真の主役を、古の学者が記録したような、羊皮紙色に細い彫り線で描いた研究の紋章にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-289"><img src="./assets/roster/289.jpg" alt="XXD Panel 289 · 民藝のしるし" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-289"><strong>289</strong> · 民藝のしるし</a><br><sub>写真の主役を、特徴を少し誇張した、手で刷ったような素朴な民藝の小さな記号にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-290"><img src="./assets/roster/290.jpg" alt="XXD Panel 290 · 古い絵本のしるし" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-290"><strong>290</strong> · 古い絵本のしるし</a><br><sub>写真の主役を、古い絵本に出てくるような、線が震え色の褪せた民間の小さな記号にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-291"><img src="./assets/roster/291.jpg" alt="XXD Panel 291 · やさしいトーテム" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-291"><strong>291</strong> · やさしいトーテム</a><br><sub>写真の主役を、童話のキャラクターのしるしのような、丸くやわらかな小さなトーテムにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-292"><img src="./assets/roster/292.jpg" alt="XXD Panel 292 · 手帳のこころ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-292"><strong>292</strong> · 手帳のこころ</a><br><sub>写真の主役を、記憶を頼りにさっと描いたような、手帳のしるしになる小さな感情アイコンにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-293"><img src="./assets/roster/293.jpg" alt="XXD Panel 293 · 詩のような小さなはんこ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-293"><strong>293</strong> · 詩のような小さなはんこ</a><br><sub>写真の主役を、古い紙に押した、少し不器用で小さな表情のある詩的なはんこにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-294"><img src="./assets/roster/294.jpg" alt="XXD Panel 294 · ごく小さな私の記号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-294"><strong>294</strong> · ごく小さな私の記号</a><br><sub>写真から、白黒のごく小さな私的な記号をひとつだけ残し、画面のほとんどを余白にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-295"><img src="./assets/roster/295.jpg" alt="XXD Panel 295 · 温かく不器用な記号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-295"><strong>295</strong> · 温かく不器用な記号</a><br><sub>写真の主役を、丸くて少しバランスの崩れた、温かく少し不器用な私的な記号にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-296"><img src="./assets/roster/296.jpg" alt="XXD Panel 296 · 身ぶりの痕跡" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-296"><strong>296</strong> · 身ぶりの痕跡</a><br><sub>写真の主役を、速さと方向をもった木炭や墨のひと筆の痕跡として残します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-297"><img src="./assets/roster/297.jpg" alt="XXD Panel 297 · 閉じる暗号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-297"><strong>297</strong> · 閉じる暗号</a><br><sub>写真の主役を、輪郭が途切れていて、見る人が自分で補って完成させる視覚の暗号にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-298"><img src="./assets/roster/298.jpg" alt="XXD Panel 298 · 木炭のしるし" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-298"><strong>298</strong> · 木炭のしるし</a><br><sub>写真の主役を、木炭、鉛筆、墨が残した半抽象の小さなしるしにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-299"><img src="./assets/roster/299.jpg" alt="XXD Panel 299 · コピーの残骸" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-299"><strong>299</strong> · コピーの残骸</a><br><sub>写真の主役を、何度もコピーされたような、見分けられても完全には戻らない白黒の残骸にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-300"><img src="./assets/roster/300.jpg" alt="XXD Panel 300 · 二値の残印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-300"><strong>300</strong> · 二値の残印</a><br><sub>純粋な黒と白だけで、写真の主役を余白からくり抜き、縁が薄れていく小さな印にします。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>301–350</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-301"><img src="./assets/roster/301.jpg" alt="XXD Panel 301 · デジタルの遺物" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-301"><strong>301</strong> · デジタルの遺物</a><br><sub>写真のいちばん強い特徴を、古いコンピュータに残されたような匿名の白黒デジタルトーテムにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-302"><img src="./assets/roster/302.jpg" alt="XXD Panel 302 · 民藝ネオ紋章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-302"><strong>302</strong> · 民藝ネオ紋章</a><br><sub>写真はそのままに、主役を温かく少しユーモラスなネオナイーブの手作り紋章にまとめます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-303"><img src="./assets/roster/303.jpg" alt="XXD Panel 303 · 幾何学シンボル" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-303"><strong>303</strong> · 幾何学シンボル</a><br><sub>写真はそのままに、主役を写真がなくても成り立つ幾何学的なマークに抽象化します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-304"><img src="./assets/roster/304.jpg" alt="XXD Panel 304 · 構成主義トーテム" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-304"><strong>304</strong> · 構成主義トーテム</a><br><sub>写真はそのままに、主役の気配を有機と幾何が引き合う抽象トーテムに凝縮します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-305"><img src="./assets/roster/305.jpg" alt="XXD Panel 305 · 切り絵トーテム" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-305"><strong>305</strong> · 切り絵トーテム</a><br><sub>写真はそのままに、主役を小さくしても見分けられる、切り絵とシルクスクリーンの民藝シンボルにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-306"><img src="./assets/roster/306.jpg" alt="XXD Panel 306 · 民藝シルエット" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-306"><strong>306</strong> · 民藝シルエット</a><br><sub>写真はそのままに、広い余白の紙面に小さな民藝のシルエットをひとつだけ残します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-307"><img src="./assets/roster/307.jpg" alt="XXD Panel 307 · 暮らしの小記" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-307"><strong>307</strong> · 暮らしの小記</a><br><sub>写真はそのままに、心に残ったひとときを温かな暮らしの小さなシンボルにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-308"><img src="./assets/roster/308.jpg" alt="XXD Panel 308 · 切り紙バッジ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-308"><strong>308</strong> · 切り紙バッジ</a><br><sub>写真はそのままに、主役をどこかの土地から持ち帰ったような紙の文化バッジに切り出します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-309"><img src="./assets/roster/309.jpg" alt="XXD Panel 309 · コンセプトミニマーク" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-309"><strong>309</strong> · コンセプトミニマーク</a><br><sub>写真はそのままに、主役を一か所だけ変えて、二度目に見ると別の意味が見える小さなバッジにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-310"><img src="./assets/roster/310.jpg" alt="XXD Panel 310 · 精神の場" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-310"><strong>310</strong> · 精神の場</a><br><sub>写真はそのままに、大きな有機的な形でごく小さな明るい焦点を包み、写真の奥にある気持ちを描きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-311"><img src="./assets/roster/311.jpg" alt="XXD Panel 311 · 古書の象形" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-311"><strong>311</strong> · 古書の象形</a><br><sub>写真はそのままに、主役を古い本や手彫りの印にあるような小さな象形の図案にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-312"><img src="./assets/roster/312.jpg" alt="XXD Panel 312 · 絵本の記憶" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-312"><strong>312</strong> · 絵本の記憶</a><br><sub>写真はそのままに、主役を古い絵本に浮かぶような静かな記憶の小さな印にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-313"><img src="./assets/roster/313.jpg" alt="XXD Panel 313 · 手帳の私印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-313"><strong>313</strong> · 手帳の私印</a><br><sub>写真はそのままに、主役を手帳に何度も描き直したような私的な記号にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-314"><img src="./assets/roster/314.jpg" alt="XXD Panel 314 · 幼い記憶の印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-314"><strong>314</strong> · 幼い記憶の印</a><br><sub>写真はそのままに、主役を古い絵本に残された小さな記憶の印にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-315"><img src="./assets/roster/315.jpg" alt="XXD Panel 315 · 民藝の標章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-315"><strong>315</strong> · 民藝の標章</a><br><sub>写真はそのままに、ひとつの輪郭や姿勢、部分を、切り絵とシルクスクリーンの民藝の標章にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-316"><img src="./assets/roster/316.jpg" alt="XXD Panel 316 · 手ざわりの小彫刻" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-316"><strong>316</strong> · 手ざわりの小彫刻</a><br><sub>写真はそのままに、主役をフェルトや樹脂粘土で手作りしたような小さなコレクション彫刻にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-317"><img src="./assets/roster/317.jpg" alt="XXD Panel 317 · まるい素朴トーテム" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-317"><strong>317</strong> · まるい素朴トーテム</a><br><sub>写真はそのままに、主役を丸くて少し不器用な、長く使い込まれたような民藝の小さなトーテムにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-318"><img src="./assets/roster/318.jpg" alt="XXD Panel 318 · 暮らしの印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-318"><strong>318</strong> · 暮らしの印</a><br><sub>写真はそのままに、そこに写る暮らしの空気を、温かな絵本風の小さなマークにします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-319"><img src="./assets/roster/319.jpg" alt="XXD Panel 319 · 詩的な記号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-319"><strong>319</strong> · 詩的な記号</a><br><sub>写真はそのままに、白い紙に詩的な小さな記号をひとつ残し、かすかな二つ目の意味を添えます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-320"><img src="./assets/roster/320.jpg" alt="XXD Panel 320 · 人格のシルエット" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-320"><strong>320</strong> · 人格のシルエット</a><br><sub>写真はそのままに、主役をシルエット優先で輪郭が途切れてもよいキャラクターの小さなマークにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-321"><img src="./assets/roster/321.jpg" alt="XXD Panel 321 · 墨ベタの古印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-321"><strong>321</strong> · 墨ベタの古印</a><br><sub>写真はそのままに、主役を古い植物図鑑や民俗図譜の小さな一図のように墨で刷り出します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-322"><img src="./assets/roster/322.jpg" alt="XXD Panel 322 · 幾何学コンポジション" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-322"><strong>322</strong> · 幾何学コンポジション</a><br><sub>写真はそのままに、主役を、まず形として成り立ち、そのあと元がわかるミッドセンチュリーの幾何学シンボルに組み直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-323"><img src="./assets/roster/323.jpg" alt="XXD Panel 323 · 白い線のエンブレム" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-323"><strong>323</strong> · 白い線のエンブレム</a><br><sub>写真はそのままに、主役を質感のある地に白い一本線で描き、小さなお店の看板のようにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-324"><img src="./assets/roster/324.jpg" alt="XXD Panel 324 · 小さな物の心象" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-324"><strong>324</strong> · 小さな物の心象</a><br><sub>写真はそのままに、大きな気持ちを、お守りのような小さな物ひとつに込めます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-325"><img src="./assets/roster/325.jpg" alt="XXD Panel 325 · 私的神話の印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-325"><strong>325</strong> · 私的神話の印</a><br><sub>写真はそのままに、主役を時間の重みを感じる私的な神話のトーテムとして封じます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-326"><img src="./assets/roster/326.jpg" alt="XXD Panel 326 · 粗削りトーテム" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-326"><strong>326</strong> · 粗削りトーテム</a><br><sub>写真はそのままに、ドライブラシとチョークで描いた控えめで粗削りなトーテムを余白に浮かべます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-327"><img src="./assets/roster/327.jpg" alt="XXD Panel 327 · 古い児童誌の印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-327"><strong>327</strong> · 古い児童誌の印</a><br><sub>写真はそのままに、主役を古い児童誌から切り抜いたような小さな印刷の印にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-328"><img src="./assets/roster/328.jpg" alt="XXD Panel 328 · レトロステッカーバッジ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-328"><strong>328</strong> · レトロステッカーバッジ</a><br><sub>写真はそのままに、主役をダイカットステッカーのようなレトロな ZINE 風バッジにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-329"><img src="./assets/roster/329.jpg" alt="XXD Panel 329 · ゆるい細線" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-329"><strong>329</strong> · ゆるい細線</a><br><sub>写真はそのままに、少し揺れる細い線で、静かでゆるい小さなアイコンを描きます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-330"><img src="./assets/roster/330.jpg" alt="XXD Panel 330 · 私だけの宝物" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-330"><strong>330</strong> · 私だけの宝物</a><br><sub>写真はそのままに、手帳の隅に、誰かひとりのものだったような私的な小さな印を残します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-331"><img src="./assets/roster/331.jpg" alt="XXD Panel 331 · 物語の縁飾り" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-331"><strong>331</strong> · 物語の縁飾り</a><br><sub>写真はそのままに、縁が物語を語り中央は静かに空いた、古い物語の本の一ページに描き直します。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-332"><img src="./assets/roster/332.jpg" alt="XXD Panel 332 · 物語の遺し印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-332"><strong>332</strong> · 物語の遺し印</a><br><sub>写真の主役を、古い物語の本から残されたような小さな印にまとめます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-333"><img src="./assets/roster/333.jpg" alt="XXD Panel 333 · 聖なる技術の遺印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-333"><strong>333</strong> · 聖なる技術の遺印</a><br><sub>写真の主役を、失われた文明が残したような回路レリーフの小さな印章にまとめます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-334"><img src="./assets/roster/334.jpg" alt="XXD Panel 334 · 神話の蔵書票" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-334"><strong>334</strong> · 神話の蔵書票</a><br><sub>写真の主役を、中央の記号を同じ文様が取り囲む神話的な蔵書票にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-335"><img src="./assets/roster/335.jpg" alt="XXD Panel 335 · アンダーグラウンド・スタンプ" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-335"><strong>335</strong> · アンダーグラウンド・スタンプ</a><br><sub>写真の主役を、ごく小さくしても見分けがつくアンダーグラウンドなストリートバッジにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-336"><img src="./assets/roster/336.jpg" alt="XXD Panel 336 · 中軸の神印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-336"><strong>336</strong> · 中軸の神印</a><br><sub>写真を、中軸と入れ子の枠に置かれた静かで神秘的な形而上の小さな印にまとめます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-337"><img src="./assets/roster/337.jpg" alt="XXD Panel 337 · ピクセルの残片" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-337"><strong>337</strong> · ピクセルの残片</a><br><sub>写真の主役を、古いインターネットから掘り出して標本箱に収めたようなローファイなピクセル片にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-338"><img src="./assets/roster/338.jpg" alt="XXD Panel 338 · ラスターの残紋" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-338"><strong>338</strong> · ラスターの残紋</a><br><sub>写真の主役を、強いシルエットと少ない情報、たった一つの異常点だけのラスター紋章にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-339"><img src="./assets/roster/339.jpg" alt="XXD Panel 339 · 未来の聖遺物" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-339"><strong>339</strong> · 未来の聖遺物</a><br><sub>写真の気配を、時間にすり減った未来の浅浮き彫りの記念メダルにまとめます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-340"><img src="./assets/roster/340.jpg" alt="XXD Panel 340 · 視覚の特異点" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-340"><strong>340</strong> · 視覚の特異点</a><br><sub>写真を、ほとんどが余白の中に置かれたごく小さな白黒の印にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-341"><img src="./assets/roster/341.jpg" alt="XXD Panel 341 · 第二の世界" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-341"><strong>341</strong> · 第二の世界</a><br><sub>写真のいちばん気の利いたきっかけが中央線を越え、紙の上で続きを起こします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-342"><img src="./assets/roster/342.jpg" alt="XXD Panel 342 · パンチの余韻" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-342"><strong>342</strong> · パンチの余韻</a><br><sub>一つの型で写真に穴を開け、抜き取った欠片を無地の余白に集め直します。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-343"><img src="./assets/roster/343.jpg" alt="XXD Panel 343 · 浮かぶピクセル画片" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-343"><strong>343</strong> · 浮かぶピクセル画片</a><br><sub>写真の主役を、中央に浮かび右下に柔らかな影を落とす淡いピクセルの小さな絵にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-344"><img src="./assets/roster/344.jpg" alt="XXD Panel 344 · ミニチュアの台座" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-344"><strong>344</strong> · ミニチュアの台座</a><br><sub>写真の主役を足もとの地面ごと切り出し、角の丸い台座に立つミニチュア模型にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-345"><img src="./assets/roster/345.jpg" alt="XXD Panel 345 · 暗い地のシルエット" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-345"><strong>345</strong> · 暗い地のシルエット</a><br><sub>写真の主役とそばの数点を平塗りのシルエットにし、暗い地の上にひとかたまりに重ねます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-346"><img src="./assets/roster/346.jpg" alt="XXD Panel 346 · リブガラスの表紙" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-346"><strong>346</strong> · リブガラスの表紙</a><br><sub>写真の主役を、細かな縦リブのガラス越しに撮った雑誌の表紙のような全面クローズアップにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-347"><img src="./assets/roster/347.jpg" alt="XXD Panel 347 · 衣装の小さな立ち姿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-347"><strong>347</strong> · 衣装の小さな立ち姿</a><br><sub>写真の主役を正面に立たせて小さな衣装を着せ、旅立つ絵本の登場人物にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-348"><img src="./assets/roster/348.jpg" alt="XXD Panel 348 · 図鑑の点描" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-348"><strong>348</strong> · 図鑑の点描</a><br><sub>写真の主役を古い博物図鑑に迎え入れ、一色のインクの点だけで標本画にします。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-349"><img src="./assets/roster/349.jpg" alt="XXD Panel 349 · 角片の小島" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-349"><strong>349</strong> · 角片の小島</a><br><sub>写真の主役と足もとの小さな地面を角丸の四角に分け、白地に浮かぶ小島のようにします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-350"><img src="./assets/roster/350.jpg" alt="XXD Panel 350 · ネオンの精霊" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-350"><strong>350</strong> · ネオンの精霊</a><br><sub>写真の一角を淡い線画にし、主役を光る虹色のぽっちゃりした精霊に変えます。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>351–354</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-351"><img src="./assets/roster/351.jpg" alt="XXD Panel 351 · マーカーの大きな手書き文字" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-351"><strong>351</strong> · マーカーの大きな手書き文字</a><br><sub>写真の隠喩をよれよれのマーカーの大きな文字にし、主役を落書きにして文字の中で遊ばせます。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-352"><img src="./assets/roster/352.jpg" alt="XXD Panel 352 · 黒線の小景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-352"><strong>352</strong> · 黒線の小景</a><br><sub>写真の主役とそばの小物を、大きな雲の下の静かな黒線の小景にします。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-353"><img src="./assets/roster/353.jpg" alt="XXD Panel 353 · 点描の光の円錐" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-353"><strong>353</strong> · 点描の光の円錐</a><br><sub>写真の主役を地上の小さな彫線シルエットにし、頭上に巨大な点描の光の円錐を立ちのぼらせます。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-354"><img src="./assets/roster/354.jpg" alt="XXD Panel 354 · 太墨の落書き" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-354"><strong>354</strong> · 太墨の落書き</a><br><sub>写真の主役を太い墨線で囲んだずんぐりした簡単な形にし、一本の太い地面線の上に立たせます。</sub></td>
  </tr>
</table>

</details>

<!-- xxd-soldier-roster:end -->

## よくある質問

**全部インストールする必要がありますか？** いいえ。好きなものだけで大丈夫です。未インストールのスタイルも「未インストール」と明示して紹介・推薦し、インストールすれば画像を作れます。

**どうやって合うスタイルを判断しますか？** 写真に写っているもの（主役、場面、色、文字）と、あなたが伝えた用途や雰囲気を、各スタイルの説明と照らし合わせて選び、理由を伝えます。人の外見から国籍や好みを推測することはしません。

**スタイルが混ざりませんか？** 混ざりません。1 枚の画像は 1 つのスタイルにだけ渡され、そのスタイル自身の原文プロンプトで描かれます。

**スタイルを直接使うのとの違いは？** 欲しいスタイルが決まっているなら、その番号の Skill を直接使うのが最速です。迷っているとき、比べたいとき、フォルダごと処理したいときはカタログを使ってください。

**まとめて処理すると混ざりませんか？** 混ざりません。写真ごとに個別に生成し、ほかの写真の色、文字、構図を借りません。設定は一括で 1 回だけ聞きます。

**写真はどこに送られますか？** エージェントが使う画像モデルにだけ送られます。Skill はほかへアップロードせず、接続先やキーも表示しません。

## 画像生成の設定

`gpt-image-2`（または互換モデル）を提供する OpenAI 互換 API とその API キーが必要です。次の手順は別の設定ファイルを作るので、Codex 本体の設定には影響しません：

```bash
mkdir -p ~/.xxd-imagegen
cat > ~/.xxd-imagegen/config.toml <<'EOF'
model_provider = "image"

[model_providers.image]
base_url = "https://api.openai.com/v1"   # または互換エンドポイント
env_key = "XXD_IMAGE_API_KEY"
EOF

# ~/.zshrc か ~/.bashrc に書き、エージェントからも読めるようにする
echo 'export XXD_IMAGEGEN_CODEX_DIR=~/.xxd-imagegen' >> ~/.zshrc
echo 'export XXD_IMAGE_API_KEY=あなたのキー' >> ~/.zshrc
```

ターミナルとエージェントを開き直してから、この Skill のフォルダで一度確認します：

```bash
python3 scripts/canonical/configured_imagegen.py probe
```

`"ok":true` なら成功です。結果は使えるかどうかだけで、接続先やキーは表示されません。Codex がすでに互換 API で画像を生成できるなら、この手順は不要です。

## パラメータ

カタログは単体のスタイルと同じ生成パラメータ（`--mode` `--size` `--text` `--locale` `--wallpaper` `--out`）を受け取り、そのまま各スタイルに渡します。詳しくは各スタイルの README の「パラメータ一覧」を見てください。`--prefs last|edit|new|off|clear` で前回の設定を使う、変える、無視することもできます。記録するのはレイアウト、サイズ、文字の方式と言語だけで、写真、文字、選んだスタイル、キーは残しません。

## メンテナンス担当者へ

このリポジトリには、シリーズ全体で共有するルールとスクリプトも入っています。各スタイルのリポジトリにはその写しがあります。

| ファイル | 用途 |
|---|---|
| `references/soldier-runtime.md` | 全スタイル共通の生成ルール。各スタイルのリポジトリに同期されます |
| `references/panel-catalog.md` | 推薦と検索のための番号目録。画像生成のプロンプトではありません |
| `references/readme-profile-guide.md` | スタイルの `readme-profile.json` の書き方 |
| `scripts/build_soldier_readme.py` | プロフィールから 5 言語の README、SKILL の説明、`openai.yaml` を生成 |
| `scripts/build_general_readme.py` | このページとスタイル一覧を生成 |
| `scripts/soldier_runtime.py` | 共通ルールとスクリプトを全スタイルのリポジトリに同期・検査 |
| `scripts/readme_ads.py` | スタイル README の広告ブロックを検査 |
| `scripts/brief_intake.py` | 新しいスタイルを作る前に原文プロンプトを検査（指摘のみで書き換えません） |
| `scripts/unsplash_sample_sources.py` | サンプル用の Unsplash 写真を選ぶ |

<!-- xxd-general-ads:start -->
## 広告情報｜XXD 有料サービスと会員制度

> **広告・商業情報に関する表示：** 以下の QR コード、会員制度、有料サービスへのリンクは小小東による広告情報です。スキャンや購入は完全に任意であり、このオープンソースプロジェクトへのアクセスや利用には影響しません。


すべての将軍 Skills は年額 CNY 699 の共通会員特典に含まれ、別途購入は不要です。 [WeChat](https://xiaoxiaodong.pages.dev/assets/wechat-qr.png)

## 知識星球＋会員プロンプトライブラリ＋全将軍 Skills 会員 · 年額 699 元

[知識星球](https://wx.zsxq.com/group/15554814142882)、[小小東会員プロンプトライブラリ](https://vip.xiaoxiaodong.ai/)、全将軍 Skills 会員は同一の会員特典です。**一度の年会費で 3 つすべてが有効になり、重複して支払う必要はありません。** 知識星球から加入した場合は、小小東へ WeChat で連絡して会員プロンプトライブラリの引換コードを受け取れます。会員プロンプトライブラリから加入した場合は、小小東へ WeChat で連絡して知識星球への参加と全将軍 Skills 会員特典の開通ができます。
<!-- xxd-general-ads:end -->

## ライセンス

本プロジェクト（Skill、プロンプト、スクリプト、文書、付属サンプル画像を含む）は **PolyForm Noncommercial License 1.0.0** の下で提供されます。完全な法的条文は [LICENSE](LICENSE)、公式ページは <https://polyformproject.org/licenses/noncommercial/1.0.0> を参照してください。

分かりやすく言うと：

- 個人は学習、研究、実験、テスト、趣味のプロジェクト、私的娯楽に使用できます。慈善団体、教育機関、公的研究・安全・保健機関、環境保護団体、政府機関も使用できます。
- **非商業目的**であれば、使用、複製、変更、派生物の作成、共有が可能です。共有時には本ライセンス（または上記リンク）と、作者が示したすべての `Required Notice:` 文を添付する必要があります。
- 商用製品・サービス、有料納品、アクセス権やライセンスの販売、商業利用につながることが予想される用途には使用できません。商用利用には著作権者から別途書面による許可を得てください。
- 本契約が付与するのは明記された著作権ライセンスと限定的な特許ライセンスだけです。商標、ブランド名、その他明記されていない権利は付与されず、ライセンスを第三者へ再許諾することもできません。
- 書面で違反通知を受けた場合、32 日以内に遵守状態へ戻り、実際の是正措置を取らなければライセンスは直ちに終了します。特許侵害を書面で主張した場合も特許ライセンスが終了します。
- 内容は法律が認める範囲で「現状のまま」提供され、保証はありません。利用に伴うリスクと損失は利用者が負います。
