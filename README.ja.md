# XXD Panel All · 将軍 Skill

<a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="README.ja.md"><strong>日本語</strong></a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

`xxd-panel-all` は XXD Panel シリーズの将軍レベル Skill です。まず現在の環境にインストール済みの `xxd-panel-NNN` 兵士 Skills を確認し、次の仕事を引き受けます。

写真がたくさんあるのに、どのスタイルを使えばよいか分からない。一つずつ試すには時間がかかり、勘だけで選ぶと後悔しやすい——そんなとき、この Skill が最初の判断を代行します。画像やフォルダーを渡すだけで、要望を理解し、インストール済みの Panel から適任を選び、仕事を割り振って結果をまとめます。番号を先に暗記する必要はありません。

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
| **兵士レベル** | `xxd-panel-NNN` | 各番号は独立した自分の原始プロンプトと美学だけを実行し、将軍から渡された個別タスクを完成品にする。 |

将軍は部隊を組織し、兵士の代わりに描きません。兵士の原始美学を書き換えたり、混ぜたり、上書きしたりせず、すべての完成画像は選ばれた番号の Skill が独立して制作します。

<!-- xxd-soldier-roster:start -->

## 全部の兵士 · 16:9 左右対照サンプル

各タイルは、その兵士の 16:9 左右対照サンプル 1 枚です（左が現実写真、右が当該番号の転訳）。画像をクリックすると、その兵士の GitHub リポジトリが開きます。

<table>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-001"><img src="./assets/roster/001.jpg" alt="XXD Panel 001 · レトロ無邪気手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-001"><strong>001</strong> · レトロ無邪気手帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-002"><img src="./assets/roster/002.jpg" alt="XXD Panel 002 · 遊び心のバウハウス" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-002"><strong>002</strong> · 遊び心のバウハウス</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-003"><img src="./assets/roster/003.jpg" alt="XXD Panel 003 · 緊張感のある線の言葉" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-003"><strong>003</strong> · 緊張感のある線の言葉</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-004"><img src="./assets/roster/004.jpg" alt="XXD Panel 004 · 都市一本線手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-004"><strong>004</strong> · 都市一本線手帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-005"><img src="./assets/roster/005.jpg" alt="XXD Panel 005 · 童話ダーク版" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-005"><strong>005</strong> · 童話ダーク版</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-006"><img src="./assets/roster/006.jpg" alt="XXD Panel 006 · 余白の小劇場" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-006"><strong>006</strong> · 余白の小劇場</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-007"><img src="./assets/roster/007.jpg" alt="XXD Panel 007 · 手描き観察ページ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-007"><strong>007</strong> · 手描き観察ページ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-008"><img src="./assets/roster/008.jpg" alt="XXD Panel 008 · パステルの幻境" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-008"><strong>008</strong> · パステルの幻境</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-009"><img src="./assets/roster/009.jpg" alt="XXD Panel 009 · 網点アンカープリント" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-009"><strong>009</strong> · 網点アンカープリント</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-010"><img src="./assets/roster/010.jpg" alt="XXD Panel 010 · モノクロ古書絵本" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-010"><strong>010</strong> · モノクロ古書絵本</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-011"><img src="./assets/roster/011.jpg" alt="XXD Panel 011 · 瞑想する線の詩" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-011"><strong>011</strong> · 瞑想する線の詩</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-012"><img src="./assets/roster/012.jpg" alt="XXD Panel 012 · 生命の幾何学" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-012"><strong>012</strong> · 生命の幾何学</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-013"><img src="./assets/roster/013.jpg" alt="XXD Panel 013 · 旅の半券帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-013"><strong>013</strong> · 旅の半券帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-014"><img src="./assets/roster/014.jpg" alt="XXD Panel 014 · ペーパーレリーフ手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-014"><strong>014</strong> · ペーパーレリーフ手帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-015"><img src="./assets/roster/015.jpg" alt="XXD Panel 015 · 抽象の記憶録" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-015"><strong>015</strong> · 抽象の記憶録</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-016"><img src="./assets/roster/016.jpg" alt="XXD Panel 016 · 動勢の版画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-016"><strong>016</strong> · 動勢の版画</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-017"><img src="./assets/roster/017.jpg" alt="XXD Panel 017 · 無邪気グラフィック手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-017"><strong>017</strong> · 無邪気グラフィック手帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-018"><img src="./assets/roster/018.jpg" alt="XXD Panel 018 · 切り絵手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-018"><strong>018</strong> · 切り絵手帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-019"><img src="./assets/roster/019.jpg" alt="XXD Panel 019 · レトログラフィック手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-019"><strong>019</strong> · レトログラフィック手帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-020"><img src="./assets/roster/020.jpg" alt="XXD Panel 020 · 厚塗りミニ風景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-020"><strong>020</strong> · 厚塗りミニ風景</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-021"><img src="./assets/roster/021.jpg" alt="XXD Panel 021 · 黒の領域を越えて" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-021"><strong>021</strong> · 黒の領域を越えて</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-022"><img src="./assets/roster/022.jpg" alt="XXD Panel 022 · 色ドットのはみ出し" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-022"><strong>022</strong> · 色ドットのはみ出し</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-023"><img src="./assets/roster/023.jpg" alt="XXD Panel 023 · 東洋の窓景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-023"><strong>023</strong> · 東洋の窓景</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-024"><img src="./assets/roster/024.jpg" alt="XXD Panel 024 · 感情の窓" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-024"><strong>024</strong> · 感情の窓</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-025"><img src="./assets/roster/025.jpg" alt="XXD Panel 025 · 見えないイメージ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-025"><strong>025</strong> · 見えないイメージ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-026"><img src="./assets/roster/026.jpg" alt="XXD Panel 026 · 幾何学的秩序" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-026"><strong>026</strong> · 幾何学的秩序</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-027"><img src="./assets/roster/027.jpg" alt="XXD Panel 027 · 紙上のレリーフ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-027"><strong>027</strong> · 紙上のレリーフ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-028"><img src="./assets/roster/028.jpg" alt="XXD Panel 028 · アイソメトリック・ミニ風景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-028"><strong>028</strong> · アイソメトリック・ミニ風景</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-029"><img src="./assets/roster/029.jpg" alt="XXD Panel 029 · 紙にゆっくり描く" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-029"><strong>029</strong> · 紙にゆっくり描く</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-030"><img src="./assets/roster/030.jpg" alt="XXD Panel 030 · 自然のはみ出し" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-030"><strong>030</strong> · 自然のはみ出し</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-031"><img src="./assets/roster/031.jpg" alt="XXD Panel 031 · 寓意の拓本" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-031"><strong>031</strong> · 寓意の拓本</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-032"><img src="./assets/roster/032.jpg" alt="XXD Panel 032 · グラフィック・ワードマーク" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-032"><strong>032</strong> · グラフィック・ワードマーク</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-033"><img src="./assets/roster/033.jpg" alt="XXD Panel 033 · 鮮やかコラージュ手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-033"><strong>033</strong> · 鮮やかコラージュ手帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-034"><img src="./assets/roster/034.jpg" alt="XXD Panel 034 · 旅のスタンプ印" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-034"><strong>034</strong> · 旅のスタンプ印</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-035"><img src="./assets/roster/035.jpg" alt="XXD Panel 035 · ブロック再構築" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-035"><strong>035</strong> · ブロック再構築</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-036"><img src="./assets/roster/036.jpg" alt="XXD Panel 036 · 流線の絵本" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-036"><strong>036</strong> · 流線の絵本</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-037"><img src="./assets/roster/037.jpg" alt="XXD Panel 037 · 流れる金の紋章" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-037"><strong>037</strong> · 流れる金の紋章</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-038"><img src="./assets/roster/038.jpg" alt="XXD Panel 038 · 織物の暮らし手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-038"><strong>038</strong> · 織物の暮らし手帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-039"><img src="./assets/roster/039.jpg" alt="XXD Panel 039 · 刺繍のイメージ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-039"><strong>039</strong> · 刺繍のイメージ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-040"><img src="./assets/roster/040.jpg" alt="XXD Panel 040 · 落書きの相棒" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-040"><strong>040</strong> · 落書きの相棒</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-041"><img src="./assets/roster/041.jpg" alt="XXD Panel 041 · アイソメトリック研究室" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-041"><strong>041</strong> · アイソメトリック研究室</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-042"><img src="./assets/roster/042.jpg" alt="XXD Panel 042 · 脱構築水彩手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-042"><strong>042</strong> · 脱構築水彩手帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-043"><img src="./assets/roster/043.jpg" alt="XXD Panel 043 · 白い泡" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-043"><strong>043</strong> · 白い泡</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-044"><img src="./assets/roster/044.jpg" alt="XXD Panel 044 · フラットな純金" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-044"><strong>044</strong> · フラットな純金</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-045"><img src="./assets/roster/045.jpg" alt="XXD Panel 045 · 癒しのブロック都市" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-045"><strong>045</strong> · 癒しのブロック都市</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-046"><img src="./assets/roster/046.jpg" alt="XXD Panel 046 · 厚塗りミニ世界" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-046"><strong>046</strong> · 厚塗りミニ世界</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-047"><img src="./assets/roster/047.jpg" alt="XXD Panel 047 · アイソメトリック厚塗り風景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-047"><strong>047</strong> · アイソメトリック厚塗り風景</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-048"><img src="./assets/roster/048.jpg" alt="XXD Panel 048 · 透明構造の手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-048"><strong>048</strong> · 透明構造の手帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-049"><img src="./assets/roster/049.jpg" alt="XXD Panel 049 · 木版の印" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-049"><strong>049</strong> · 木版の印</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-050"><img src="./assets/roster/050.jpg" alt="XXD Panel 050 · 旅の絵はがき" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-050"><strong>050</strong> · 旅の絵はがき</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-051"><img src="./assets/roster/051.jpg" alt="XXD Panel 051 · 手作りミニチュア島" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-051"><strong>051</strong> · 手作りミニチュア島</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-052"><img src="./assets/roster/052.jpg" alt="XXD Panel 052 · ペーパークラフトのミニ島" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-052"><strong>052</strong> · ペーパークラフトのミニ島</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-053"><img src="./assets/roster/053.jpg" alt="XXD Panel 053 · ペン淡彩の記録" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-053"><strong>053</strong> · ペン淡彩の記録</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-054"><img src="./assets/roster/054.jpg" alt="XXD Panel 054 · 思い出シール帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-054"><strong>054</strong> · 思い出シール帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-055"><img src="./assets/roster/055.jpg" alt="XXD Panel 055 · 絵画の記憶の場" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-055"><strong>055</strong> · 絵画の記憶の場</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-056"><img src="./assets/roster/056.jpg" alt="XXD Panel 056 · 余白の記憶画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-056"><strong>056</strong> · 余白の記憶画</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-057"><img src="./assets/roster/057.jpg" alt="XXD Panel 057 · 幾何学の記憶の場" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-057"><strong>057</strong> · 幾何学の記憶の場</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-058"><img src="./assets/roster/058.jpg" alt="XXD Panel 058 · 詩的コンセプト風景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-058"><strong>058</strong> · 詩的コンセプト風景</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-059"><img src="./assets/roster/059.jpg" alt="XXD Panel 059 · 手描き寓話録" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-059"><strong>059</strong> · 手描き寓話録</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-060"><img src="./assets/roster/060.jpg" alt="XXD Panel 060 · 禅のミニマル詩" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-060"><strong>060</strong> · 禅のミニマル詩</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-061"><img src="./assets/roster/061.jpg" alt="XXD Panel 061 · ビジュアル記憶帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-061"><strong>061</strong> · ビジュアル記憶帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-062"><img src="./assets/roster/062.jpg" alt="XXD Panel 062 · 賢くて不器用な線" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-062"><strong>062</strong> · 賢くて不器用な線</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-063"><img src="./assets/roster/063.jpg" alt="XXD Panel 063 · ピクセル隠喩手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-063"><strong>063</strong> · ピクセル隠喩手帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-064"><img src="./assets/roster/064.jpg" alt="XXD Panel 064 · インディー・コラージュ頁" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-064"><strong>064</strong> · インディー・コラージュ頁</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-065"><img src="./assets/roster/065.jpg" alt="XXD Panel 065 · 二本線エディトリアル手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-065"><strong>065</strong> · 二本線エディトリアル手帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-066"><img src="./assets/roster/066.jpg" alt="XXD Panel 066 · 無邪気な物語の線" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-066"><strong>066</strong> · 無邪気な物語の線</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-067"><img src="./assets/roster/067.jpg" alt="XXD Panel 067 · 日常ユーモア画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-067"><strong>067</strong> · 日常ユーモア画</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-068"><img src="./assets/roster/068.jpg" alt="XXD Panel 068 · 東洋写意帖" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-068"><strong>068</strong> · 東洋写意帖</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-069"><img src="./assets/roster/069.jpg" alt="XXD Panel 069 · 鮮やか塗りの窓" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-069"><strong>069</strong> · 鮮やか塗りの窓</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-070"><img src="./assets/roster/070.jpg" alt="XXD Panel 070 · 厚塗り癒しの島" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-070"><strong>070</strong> · 厚塗り癒しの島</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-071"><img src="./assets/roster/071.jpg" alt="XXD Panel 071 · パステル詩情帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-071"><strong>071</strong> · パステル詩情帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-072"><img src="./assets/roster/072.jpg" alt="XXD Panel 072 · 明るい色彩手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-072"><strong>072</strong> · 明るい色彩手帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-073"><img src="./assets/roster/073.jpg" alt="XXD Panel 073 · 幾何学都市手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-073"><strong>073</strong> · 幾何学都市手帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-074"><img src="./assets/roster/074.jpg" alt="XXD Panel 074 · 感情アイコン手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-074"><strong>074</strong> · 感情アイコン手帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-075"><img src="./assets/roster/075.jpg" alt="XXD Panel 075 · ダーククレヨン画稿" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-075"><strong>075</strong> · ダーククレヨン画稿</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-076"><img src="./assets/roster/076.jpg" alt="XXD Panel 076 · マカロンクレヨン" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-076"><strong>076</strong> · マカロンクレヨン</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-077"><img src="./assets/roster/077.jpg" alt="XXD Panel 077 · 旅雑誌イラスト" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-077"><strong>077</strong> · 旅雑誌イラスト</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-078"><img src="./assets/roster/078.jpg" alt="XXD Panel 078 · 金箔箔押し手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-078"><strong>078</strong> · 金箔箔押し手帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-079"><img src="./assets/roster/079.jpg" alt="XXD Panel 079 · ペン淡彩手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-079"><strong>079</strong> · ペン淡彩手帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-080"><img src="./assets/roster/080.jpg" alt="XXD Panel 080 · 有機的グアッシュの場" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-080"><strong>080</strong> · 有機的グアッシュの場</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-081"><img src="./assets/roster/081.jpg" alt="XXD Panel 081 · 色糸の記念帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-081"><strong>081</strong> · 色糸の記念帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-082"><img src="./assets/roster/082.jpg" alt="XXD Panel 082 · 紙から飛び出す水彩" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-082"><strong>082</strong> · 紙から飛び出す水彩</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-083"><img src="./assets/roster/083.jpg" alt="XXD Panel 083 · ブサかわキャラ手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-083"><strong>083</strong> · ブサかわキャラ手帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-084"><img src="./assets/roster/084.jpg" alt="XXD Panel 084 · 点描と線構成の手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-084"><strong>084</strong> · 点描と線構成の手帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-085"><img src="./assets/roster/085.jpg" alt="XXD Panel 085 · 手作り模型手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-085"><strong>085</strong> · 手作り模型手帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-086"><img src="./assets/roster/086.jpg" alt="XXD Panel 086 · 余白の版画手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-086"><strong>086</strong> · 余白の版画手帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-087"><img src="./assets/roster/087.jpg" alt="XXD Panel 087 · 赤い糸の関係図" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-087"><strong>087</strong> · 赤い糸の関係図</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-088"><img src="./assets/roster/088.jpg" alt="XXD Panel 088 · 文字造形の詩" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-088"><strong>088</strong> · 文字造形の詩</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-089"><img src="./assets/roster/089.jpg" alt="XXD Panel 089 · 暮らしの小品帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-089"><strong>089</strong> · 暮らしの小品帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-090"><img src="./assets/roster/090.jpg" alt="XXD Panel 090 · ビジュアル思考マップ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-090"><strong>090</strong> · ビジュアル思考マップ</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-091"><img src="./assets/roster/091.jpg" alt="XXD Panel 091 · 青線の旅帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-091"><strong>091</strong> · 青線の旅帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-092"><img src="./assets/roster/092.jpg" alt="XXD Panel 092 · 表現的線描手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-092"><strong>092</strong> · 表現的線描手帳</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-093"><img src="./assets/roster/093.jpg" alt="XXD Panel 093 · モダン幾何学絵画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-093"><strong>093</strong> · モダン幾何学絵画</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-094"><img src="./assets/roster/094.jpg" alt="XXD Panel 094 · 古典二色刷りの本" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-094"><strong>094</strong> · 古典二色刷りの本</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-095"><img src="./assets/roster/095.jpg" alt="XXD Panel 095 · 赤黒図解手帳" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-095"><strong>095</strong> · 赤黒図解手帳</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-096"><img src="./assets/roster/096.jpg" alt="XXD Panel 096 · 民間通信カード" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-096"><strong>096</strong> · 民間通信カード</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-097"><img src="./assets/roster/097.jpg" alt="XXD Panel 097 · レトロ説明カード" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-097"><strong>097</strong> · レトロ説明カード</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-098"><img src="./assets/roster/098.jpg" alt="XXD Panel 098 · 素朴な水彩の本" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-098"><strong>098</strong> · 素朴な水彩の本</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-099"><img src="./assets/roster/099.jpg" alt="XXD Panel 099 · 書体マスコット" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-099"><strong>099</strong> · 書体マスコット</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-100"><img src="./assets/roster/100.jpg" alt="XXD Panel 100 · 民芸物語絵" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-100"><strong>100</strong> · 民芸物語絵</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-101"><img src="./assets/roster/101.jpg" alt="XXD Panel 101 · 九つの記憶ノート" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-101"><strong>101</strong> · 九つの記憶ノート</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-102"><img src="./assets/roster/102.jpg" alt="XXD Panel 102 · 癒やしの幾何学誌" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-102"><strong>102</strong> · 癒やしの幾何学誌</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-103"><img src="./assets/roster/103.jpg" alt="XXD Panel 103 · 鮮彩抽象アセンブリ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-103"><strong>103</strong> · 鮮彩抽象アセンブリ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-104"><img src="./assets/roster/104.jpg" alt="XXD Panel 104 · 網点禅意誌" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-104"><strong>104</strong> · 網点禅意誌</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-105"><img src="./assets/roster/105.jpg" alt="XXD Panel 105 · 詩的余白集" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-105"><strong>105</strong> · 詩的余白集</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-106"><img src="./assets/roster/106.jpg" alt="XXD Panel 106 · 柔彩ピクセル記" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-106"><strong>106</strong> · 柔彩ピクセル記</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-107"><img src="./assets/roster/107.jpg" alt="XXD Panel 107 · 画像ことば詩" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-107"><strong>107</strong> · 画像ことば詩</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-108"><img src="./assets/roster/108.jpg" alt="XXD Panel 108 · 新民藝切り絵誌" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-108"><strong>108</strong> · 新民藝切り絵誌</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-109"><img src="./assets/roster/109.jpg" alt="XXD Panel 109 · 柔和な幾何解構誌" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-109"><strong>109</strong> · 柔和な幾何解構誌</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-110"><img src="./assets/roster/110.jpg" alt="XXD Panel 110 · 日本風暮らしのシーン図鑑" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-110"><strong>110</strong> · 日本風暮らしのシーン図鑑</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-111"><img src="./assets/roster/111.jpg" alt="XXD Panel 111 · テキスタイル・コラージュ誌" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-111"><strong>111</strong> · テキスタイル・コラージュ誌</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-112"><img src="./assets/roster/112.jpg" alt="XXD Panel 112 · 金線ペーパー誌" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-112"><strong>112</strong> · 金線ペーパー誌</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-113"><img src="./assets/roster/113.jpg" alt="XXD Panel 113 · 貝殻ピクセル・コラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-113"><strong>113</strong> · 貝殻ピクセル・コラージュ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-114"><img src="./assets/roster/114.jpg" alt="XXD Panel 114 · レトロ・パステル手帳ドゥードル" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-114"><strong>114</strong> · レトロ・パステル手帳ドゥードル</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-115"><img src="./assets/roster/115.jpg" alt="XXD Panel 115 · パステル印章コラージュ帖" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-115"><strong>115</strong> · パステル印章コラージュ帖</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-116"><img src="./assets/roster/116.jpg" alt="XXD Panel 116 · 淡紙パステル落書き誌" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-116"><strong>116</strong> · 淡紙パステル落書き誌</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-117"><img src="./assets/roster/117.jpg" alt="XXD Panel 117 · 細線淡彩余白誌" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-117"><strong>117</strong> · 細線淡彩余白誌</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-118"><img src="./assets/roster/118.jpg" alt="XXD Panel 118 · 石墨と余白の素描誌" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-118"><strong>118</strong> · 石墨と余白の素描誌</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-119"><img src="./assets/roster/119.jpg" alt="XXD Panel 119 · 手縫い布と余白の記録" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-119"><strong>119</strong> · 手縫い布と余白の記録</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-120"><img src="./assets/roster/120.jpg" alt="XXD Panel 120 · 建築コンセプト手描き帖" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-120"><strong>120</strong> · 建築コンセプト手描き帖</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-121"><img src="./assets/roster/121.jpg" alt="XXD Panel 121 · 暮らしのドゥードル編集帖" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-121"><strong>121</strong> · 暮らしのドゥードル編集帖</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-122"><img src="./assets/roster/122.jpg" alt="XXD Panel 122 · 単色網点と手書きの余白" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-122"><strong>122</strong> · 単色網点と手書きの余白</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-123"><img src="./assets/roster/123.jpg" alt="XXD Panel 123 · 赤青の角線色鉛筆" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-123"><strong>123</strong> · 赤青の角線色鉛筆</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-124"><img src="./assets/roster/124.jpg" alt="XXD Panel 124 · 布コラージュの余白" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-124"><strong>124</strong> · 布コラージュの余白</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-125"><img src="./assets/roster/125.jpg" alt="XXD Panel 125 · クレヨン童画の余白" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-125"><strong>125</strong> · クレヨン童画の余白</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-126"><img src="./assets/roster/126.jpg" alt="XXD Panel 126 · 詩的なミニチュアコラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-126"><strong>126</strong> · 詩的なミニチュアコラージュ</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-127"><img src="./assets/roster/127.jpg" alt="XXD Panel 127 · 建築ミクストメディア・コラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-127"><strong>127</strong> · 建築ミクストメディア・コラージュ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-128"><img src="./assets/roster/128.jpg" alt="XXD Panel 128 · 七宝メダルの旅" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-128"><strong>128</strong> · 七宝メダルの旅</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-129"><img src="./assets/roster/129.jpg" alt="XXD Panel 129 · 東洋の拡散と余白" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-129"><strong>129</strong> · 東洋の拡散と余白</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-130"><img src="./assets/roster/130.jpg" alt="XXD Panel 130 · ハードエッジ幾何面" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-130"><strong>130</strong> · ハードエッジ幾何面</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-131"><img src="./assets/roster/131.jpg" alt="XXD Panel 131 · 写真と落書きコラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-131"><strong>131</strong> · 写真と落書きコラージュ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-132"><img src="./assets/roster/132.jpg" alt="XXD Panel 132 · ペン淡彩の旅" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-132"><strong>132</strong> · ペン淡彩の旅</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-133"><img src="./assets/roster/133.jpg" alt="XXD Panel 133 · 点刻と透明重ね刷り" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-133"><strong>133</strong> · 点刻と透明重ね刷り</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-134"><img src="./assets/roster/134.jpg" alt="XXD Panel 134 · 絵本の色面物語" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-134"><strong>134</strong> · 絵本の色面物語</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-135"><img src="./assets/roster/135.jpg" alt="XXD Panel 135 · ストリート特色手描き誌" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-135"><strong>135</strong> · ストリート特色手描き誌</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-136"><img src="./assets/roster/136.jpg" alt="XXD Panel 136 · 詩的シュルレアリスムの余白" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-136"><strong>136</strong> · 詩的シュルレアリスムの余白</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-137"><img src="./assets/roster/137.jpg" alt="XXD Panel 137 · エッチング質感コラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-137"><strong>137</strong> · エッチング質感コラージュ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-138"><img src="./assets/roster/138.jpg" alt="XXD Panel 138 · 東洋の紙レリーフ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-138"><strong>138</strong> · 東洋の紙レリーフ</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-139"><img src="./assets/roster/139.jpg" alt="XXD Panel 139 · 文字符号の線場" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-139"><strong>139</strong> · 文字符号の線場</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-140"><img src="./assets/roster/140.jpg" alt="XXD Panel 140 · 乾性手描きの視覚島" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-140"><strong>140</strong> · 乾性手描きの視覚島</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-141"><img src="./assets/roster/141.jpg" alt="XXD Panel 141 · 極簡手描き線画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-141"><strong>141</strong> · 極簡手描き線画</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-142"><img src="./assets/roster/142.jpg" alt="XXD Panel 142 · 拡張字形と画像マスク" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-142"><strong>142</strong> · 拡張字形と画像マスク</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-143"><img src="./assets/roster/143.jpg" alt="XXD Panel 143 · 文字造形の視覚詩" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-143"><strong>143</strong> · 文字造形の視覚詩</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-144"><img src="./assets/roster/144.jpg" alt="XXD Panel 144 · 幾何白抜きと破枠線描" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-144"><strong>144</strong> · 幾何白抜きと破枠線描</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-145"><img src="./assets/roster/145.jpg" alt="XXD Panel 145 · レトロ限定色版画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-145"><strong>145</strong> · レトロ限定色版画</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-146"><img src="./assets/roster/146.jpg" alt="XXD Panel 146 · 博物学スカーフ印花" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-146"><strong>146</strong> · 博物学スカーフ印花</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-147"><img src="./assets/roster/147.jpg" alt="XXD Panel 147 · 弁当食材パッケージ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-147"><strong>147</strong> · 弁当食材パッケージ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-148"><img src="./assets/roster/148.jpg" alt="XXD Panel 148 · ビジュアル日記コラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-148"><strong>148</strong> · ビジュアル日記コラージュ</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-149"><img src="./assets/roster/149.jpg" alt="XXD Panel 149 · 手描き質感フラットアート" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-149"><strong>149</strong> · 手描き質感フラットアート</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-150"><img src="./assets/roster/150.jpg" alt="XXD Panel 150 · レトロモダン切り紙" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-150"><strong>150</strong> · レトロモダン切り紙</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-151"><img src="./assets/roster/151.jpg" alt="XXD Panel 151 · 素朴なフラット手描き" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-151"><strong>151</strong> · 素朴なフラット手描き</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-152"><img src="./assets/roster/152.jpg" alt="XXD Panel 152 · 色面ベースのペーパーアート" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-152"><strong>152</strong> · 色面ベースのペーパーアート</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-153"><img src="./assets/roster/153.jpg" alt="XXD Panel 153 · 単色手帳ドゥードル" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-153"><strong>153</strong> · 単色手帳ドゥードル</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-154"><img src="./assets/roster/154.jpg" alt="XXD Panel 154 · レトロピクセルと余白" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-154"><strong>154</strong> · レトロピクセルと余白</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-155"><img src="./assets/roster/155.jpg" alt="XXD Panel 155 · 一点透視の淡彩" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-155"><strong>155</strong> · 一点透視の淡彩</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-156"><img src="./assets/roster/156.jpg" alt="XXD Panel 156 · 双色版ずれイラスト" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-156"><strong>156</strong> · 双色版ずれイラスト</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-157"><img src="./assets/roster/157.jpg" alt="XXD Panel 157 · 文物の墨拓と余白" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-157"><strong>157</strong> · 文物の墨拓と余白</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-158"><img src="./assets/roster/158.jpg" alt="XXD Panel 158 · 紙のミクストメディア・コラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-158"><strong>158</strong> · 紙のミクストメディア・コラージュ</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-159"><img src="./assets/roster/159.jpg" alt="XXD Panel 159 · 文字網点の実験ポスター" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-159"><strong>159</strong> · 文字網点の実験ポスター</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-160"><img src="./assets/roster/160.jpg" alt="XXD Panel 160 · 自由な線と淡彩の余白" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-160"><strong>160</strong> · 自由な線と淡彩の余白</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-161"><img src="./assets/roster/161.jpg" alt="XXD Panel 161 · 色面フレームと越境構図" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-161"><strong>161</strong> · 色面フレームと越境構図</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-162"><img src="./assets/roster/162.jpg" alt="XXD Panel 162 · 白い切り紙台紙の絵本イラスト" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-162"><strong>162</strong> · 白い切り紙台紙の絵本イラスト</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-163"><img src="./assets/roster/163.jpg" alt="XXD Panel 163 · 中央の単色色面スタンプ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-163"><strong>163</strong> · 中央の単色色面スタンプ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-164"><img src="./assets/roster/164.jpg" alt="XXD Panel 164 · 水墨と建築線描の小景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-164"><strong>164</strong> · 水墨と建築線描の小景</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-165"><img src="./assets/roster/165.jpg" alt="XXD Panel 165 · 中央の裂け目から現れる紙コラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-165"><strong>165</strong> · 中央の裂け目から現れる紙コラージュ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-166"><img src="./assets/roster/166.jpg" alt="XXD Panel 166 · 等角投影の彫刻的浅浮彫ジオラマ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-166"><strong>166</strong> · 等角投影の彫刻的浅浮彫ジオラマ</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-167"><img src="./assets/roster/167.jpg" alt="XXD Panel 167 · 中央の波形と厚盛りインク" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-167"><strong>167</strong> · 中央の波形と厚盛りインク</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-168"><img src="./assets/roster/168.jpg" alt="XXD Panel 168 · 紙白を残す重ね刷毛の色面" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-168"><strong>168</strong> · 紙白を残す重ね刷毛の色面</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-169"><img src="./assets/roster/169.jpg" alt="XXD Panel 169 · 暖かな黄土色の小さな線画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-169"><strong>169</strong> · 暖かな黄土色の小さな線画</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-170"><img src="./assets/roster/170.jpg" alt="XXD Panel 170 · 黒と錆赤のドライメディア小景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-170"><strong>170</strong> · 黒と錆赤のドライメディア小景</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-171"><img src="./assets/roster/171.jpg" alt="XXD Panel 171 · 縦線の骨格と微小な散点" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-171"><strong>171</strong> · 縦線の骨格と微小な散点</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-172"><img src="./assets/roster/172.jpg" alt="XXD Panel 172 · 中央の主題と半透明幾何レイヤー" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-172"><strong>172</strong> · 中央の主題と半透明幾何レイヤー</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-173"><img src="./assets/roster/173.jpg" alt="XXD Panel 173 · 象牙色の紙と文字の微小景観" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-173"><strong>173</strong> · 象牙色の紙と文字の微小景観</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-174"><img src="./assets/roster/174.jpg" alt="XXD Panel 174 · 素朴な手描きステッカーの集合" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-174"><strong>174</strong> · 素朴な手描きステッカーの集合</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-175"><img src="./assets/roster/175.jpg" alt="XXD Panel 175 · 琥珀の透過光と象牙色の紙彫小景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-175"><strong>175</strong> · 琥珀の透過光と象牙色の紙彫小景</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-176"><img src="./assets/roster/176.jpg" alt="XXD Panel 176 · 細密手描きの浅浮彫儀式図" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-176"><strong>176</strong> · 細密手描きの浅浮彫儀式図</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-177"><img src="./assets/roster/177.jpg" alt="XXD Panel 177 · 異形シルエットの版画ミクロ島" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-177"><strong>177</strong> · 異形シルエットの版画ミクロ島</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-178"><img src="./assets/roster/178.jpg" alt="XXD Panel 178 · 異形シルエットの版画ミクロ島（同源）" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-178"><strong>178</strong> · 異形シルエットの版画ミクロ島（同源）</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-179"><img src="./assets/roster/179.jpg" alt="XXD Panel 179 · リボン状の微小展示風景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-179"><strong>179</strong> · リボン状の微小展示風景</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-180"><img src="./assets/roster/180.jpg" alt="XXD Panel 180 · 旅の記憶を刻むレトロ円形スタンプ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-180"><strong>180</strong> · 旅の記憶を刻むレトロ円形スタンプ</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-181"><img src="./assets/roster/181.jpg" alt="XXD Panel 181 · 文人彩墨の小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-181"><strong>181</strong> · 文人彩墨の小品</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-182"><img src="./assets/roster/182.jpg" alt="XXD Panel 182 · ミニチュアピクセル小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-182"><strong>182</strong> · ミニチュアピクセル小品</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-183"><img src="./assets/roster/183.jpg" alt="XXD Panel 183 · 深緑のコーナー有機図形" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-183"><strong>183</strong> · 深緑のコーナー有機図形</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-184"><img src="./assets/roster/184.jpg" alt="XXD Panel 184 · 正方形の日常手描き小景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-184"><strong>184</strong> · 正方形の日常手描き小景</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-185"><img src="./assets/roster/185.jpg" alt="XXD Panel 185 · 淡色を添えた白黒ステッカー小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-185"><strong>185</strong> · 淡色を添えた白黒ステッカー小品</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-186"><img src="./assets/roster/186.jpg" alt="XXD Panel 186 · 淡色の九分割幾何学記憶" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-186"><strong>186</strong> · 淡色の九分割幾何学記憶</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-187"><img src="./assets/roster/187.jpg" alt="XXD Panel 187 · 大きな文字のアーカイブコラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-187"><strong>187</strong> · 大きな文字のアーカイブコラージュ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-188"><img src="./assets/roster/188.jpg" alt="XXD Panel 188 · 米色と金色の建築アーカイブ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-188"><strong>188</strong> · 米色と金色の建築アーカイブ</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-189"><img src="./assets/roster/189.jpg" alt="XXD Panel 189 · 二重枠とサイドバーのマッチ箱小景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-189"><strong>189</strong> · 二重枠とサイドバーのマッチ箱小景</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-190"><img src="./assets/roster/190.jpg" alt="XXD Panel 190 · 寒色主体の素朴なパステル" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-190"><strong>190</strong> · 寒色主体の素朴なパステル</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-191"><img src="./assets/roster/191.jpg" alt="XXD Panel 191 · 毛羽立つ矩形パステル色面" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-191"><strong>191</strong> · 毛羽立つ矩形パステル色面</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-192"><img src="./assets/roster/192.jpg" alt="XXD Panel 192 · 限定色のレトロ図形小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-192"><strong>192</strong> · 限定色のレトロ図形小品</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-193"><img src="./assets/roster/193.jpg" alt="XXD Panel 193 · 低い台座の灰調水彩小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-193"><strong>193</strong> · 低い台座の灰調水彩小品</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-194"><img src="./assets/roster/194.jpg" alt="XXD Panel 194 · 明るい敷地台座の軸測模型" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-194"><strong>194</strong> · 明るい敷地台座の軸測模型</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-195"><img src="./assets/roster/195.jpg" alt="XXD Panel 195 · 一色が光る歴史モンタージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-195"><strong>195</strong> · 一色が光る歴史モンタージュ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-196"><img src="./assets/roster/196.jpg" alt="XXD Panel 196 · 俯瞰の幾何学人物小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-196"><strong>196</strong> · 俯瞰の幾何学人物小品</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-197"><img src="./assets/roster/197.jpg" alt="XXD Panel 197 · 籠の中の世界を描く民芸イラスト" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-197"><strong>197</strong> · 籠の中の世界を描く民芸イラスト</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-198"><img src="./assets/roster/198.jpg" alt="XXD Panel 198 · 限定色の浮遊ファッションコラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-198"><strong>198</strong> · 限定色の浮遊ファッションコラージュ</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-199"><img src="./assets/roster/199.jpg" alt="XXD Panel 199 · 明るく余白豊かな小型ファッションコラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-199"><strong>199</strong> · 明るく余白豊かな小型ファッションコラージュ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-200"><img src="./assets/roster/200.jpg" alt="XXD Panel 200 · 青灰色の単色手描き線画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-200"><strong>200</strong> · 青灰色の単色手描き線画</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-201"><img src="./assets/roster/201.jpg" alt="XXD Panel 201 · クリーム色の手作りミニチュア" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-201"><strong>201</strong> · クリーム色の手作りミニチュア</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-202"><img src="./assets/roster/202.jpg" alt="XXD Panel 202 · 構造軸を持つ幾何学線図" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-202"><strong>202</strong> · 構造軸を持つ幾何学線図</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-203"><img src="./assets/roster/203.jpg" alt="XXD Panel 203 · 余白を活かす厚塗り絵葉書" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-203"><strong>203</strong> · 余白を活かす厚塗り絵葉書</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-204"><img src="./assets/roster/204.jpg" alt="XXD Panel 204 · 柔らかな光と記憶の小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-204"><strong>204</strong> · 柔らかな光と記憶の小品</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-205"><img src="./assets/roster/205.jpg" alt="XXD Panel 205 · 暖色の有機形写真コラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-205"><strong>205</strong> · 暖色の有機形写真コラージュ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-206"><img src="./assets/roster/206.jpg" alt="XXD Panel 206 · 淡色の積層ペーパークラフト小景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-206"><strong>206</strong> · 淡色の積層ペーパークラフト小景</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-207"><img src="./assets/roster/207.jpg" alt="XXD Panel 207 · 淡い青と白の混合メディア挿絵" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-207"><strong>207</strong> · 淡い青と白の混合メディア挿絵</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-208"><img src="./assets/roster/208.jpg" alt="XXD Panel 208 · 青とピンクのモダニズム抽象" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-208"><strong>208</strong> · 青とピンクのモダニズム抽象</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-209"><img src="./assets/roster/209.jpg" alt="XXD Panel 209 · 紙の質感を持つ極小画像アーカイブ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-209"><strong>209</strong> · 紙の質感を持つ極小画像アーカイブ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-210"><img src="./assets/roster/210.jpg" alt="XXD Panel 210 · 寒色の軽やかな概念コラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-210"><strong>210</strong> · 寒色の軽やかな概念コラージュ</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-211"><img src="./assets/roster/211.jpg" alt="XXD Panel 211 · 意味に基づく配色の幾何学小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-211"><strong>211</strong> · 意味に基づく配色の幾何学小品</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-212"><img src="./assets/roster/212.jpg" alt="XXD Panel 212 · 近単色の彫刻的形態研究" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-212"><strong>212</strong> · 近単色の彫刻的形態研究</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-213"><img src="./assets/roster/213.jpg" alt="XXD Panel 213 · 暖かな紙の寒色概念線画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-213"><strong>213</strong> · 暖かな紙の寒色概念線画</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-214"><img src="./assets/roster/214.jpg" alt="XXD Panel 214 · 固有色を活かす粗い切り絵小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-214"><strong>214</strong> · 固有色を活かす粗い切り絵小品</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-215"><img src="./assets/roster/215.jpg" alt="XXD Panel 215 · 黄土色を添えた灰階軸測図" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-215"><strong>215</strong> · 黄土色を添えた灰階軸測図</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-216"><img src="./assets/roster/216.jpg" alt="XXD Panel 216 · 広大な余白の極小印刷アイランド" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-216"><strong>216</strong> · 広大な余白の極小印刷アイランド</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-217"><img src="./assets/roster/217.jpg" alt="XXD Panel 217 · 明るいデジタル混合メディアコラージュ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-217"><strong>217</strong> · 明るいデジタル混合メディアコラージュ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-218"><img src="./assets/roster/218.jpg" alt="XXD Panel 218 · ミニマルな絵本風ニードルフェルト" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-218"><strong>218</strong> · ミニマルな絵本風ニードルフェルト</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-219"><img src="./assets/roster/219.jpg" alt="XXD Panel 219 · 色鉛筆を添えた旅日記スケッチ" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-219"><strong>219</strong> · 色鉛筆を添えた旅日記スケッチ</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-220"><img src="./assets/roster/220.jpg" alt="XXD Panel 220 · 丸みのある素朴な手描きドゥードル" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-220"><strong>220</strong> · 丸みのある素朴な手描きドゥードル</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-221"><img src="./assets/roster/221.jpg" alt="XXD Panel 221 · 摄影与数码混合媒介拼贴海报" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-221"><strong>221</strong> · 摄影与数码混合媒介拼贴海报</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-222"><img src="./assets/roster/222.jpg" alt="XXD Panel 222 · 摄影与数码混合媒介拼贴海报" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-222"><strong>222</strong> · 摄影与数码混合媒介拼贴海报</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-223"><img src="./assets/roster/223.jpg" alt="XXD Panel 223 · 摄影与数码混合媒介拼贴海报" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-223"><strong>223</strong> · 摄影与数码混合媒介拼贴海报</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-224"><img src="./assets/roster/224.jpg" alt="XXD Panel 224 · 瓷器碎片拼合重构" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-224"><strong>224</strong> · 瓷器碎片拼合重构</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-225"><img src="./assets/roster/225.jpg" alt="XXD Panel 225 · 办公物件手绘拼贴" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-225"><strong>225</strong> · 办公物件手绘拼贴</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-226"><img src="./assets/roster/226.jpg" alt="XXD Panel 226 · 糖霜曲奇浅浮雕" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-226"><strong>226</strong> · 糖霜曲奇浅浮雕</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-227"><img src="./assets/roster/227.jpg" alt="XXD Panel 227 · 刺绣任务章" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-227"><strong>227</strong> · 刺绣任务章</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-228"><img src="./assets/roster/228.jpg" alt="XXD Panel 228 · 独立纸艺对象" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-228"><strong>228</strong> · 独立纸艺对象</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-229"><img src="./assets/roster/229.jpg" alt="XXD Panel 229 · 新民艺留白" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-229"><strong>229</strong> · 新民艺留白</a></p>
</td>
  </tr>
</table>

<!-- xxd-soldier-roster:end -->

## 広告情報｜XXD 有料サービスと会員制度

> **広告・商業情報に関する表示：** 以下の QR コード、会員制度、有料サービスへのリンクは小小東による広告情報です。スキャンや購入は完全に任意であり、このオープンソースプロジェクトへのアクセスや利用には影響しません。


すべての将軍 Skills は年額 CNY 699 の共通会員特典に含まれ、別途購入は不要です。 [WeChat](https://xiaoxiaodong.pages.dev/assets/wechat-qr.png)

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
├── assets/
│   └── roster/
├── agents/
│   └── openai.yaml
├── references/
│   ├── panel-catalog.md
│   ├── runtime-preferences.md
│   ├── soldier-runtime.md
│   ├── soldier-adapter.zh-CN.md
│   ├── soldier-adapter.en.md
│   └── sample-workflow.md
└── scripts/
    ├── panel_preferences.py
    ├── soldier_roster.py
    ├── soldier_runtime.py
    └── canonical/
```

- `SKILL.md`：対話、推薦、閲覧、バッチルーティングの規則
- `assets/roster/`：兵士ごとに 1 枚の 16:9 左右対照サンプル。README の画像をクリックすると当該 GitHub リポジトリが開きます
- `panel-catalog.md`：番号検索用カタログ。画像生成プロンプトではありません
- `soldier-runtime.md`：家族共通の兵士ランタイム契約。各兵士リポジトリが逐語コピーを保持します
- `runtime-preferences.md`：引き継ぎ、変更、新規設定、プライバシー境界
- `panel_preferences.py`：安全な納品設定だけを読み書きするローカル補助スクリプト
- `soldier_roster.py`：各兵士の `sample-05.png` から README 名簿を生成
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
