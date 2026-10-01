# XXD Panel All · 将军 Skill

<a href="README.md"><strong>简体中文</strong></a> · <a href="README.en.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

`xxd-panel-all` 是 XXD Panel 系列的将军级 Skill。它先识别当前环境中已安装的 `xxd-panel-NNN` 士兵级 Skills，再承接以下任务：

如果你也有过这种时刻：手里一堆照片，不知道该用哪种风格；一个个试太慢，凭感觉乱选又容易后悔——这个 Skill 就是替你做第一轮判断的。你只要把图片或文件夹交过来，它会先看懂需求，再从已经安装的 Panel 里挑人、派活、收结果。你不用先背下全部编号。

### 30 秒看懂

- **想做一张图：** 说主题或直接给照片，它推荐合适的 Panel。
- **想比较风格：** 指定几个 Panel，同一张图分别试稿。
- **想批量处理：** 给一个文件夹，它可以统一设置，也可以按图片逐张分配。

最省事的开场白是：

> 这是我的图片。先告诉我你推荐哪几个 Panel，以及各自适合它的原因。

下面是完整的安装、批量规则和偏好设置；先用起来，再回来查细节，通常更快。

- 根据图片或主题智能推荐 Panel
- 按题材、视觉感觉或用途浏览风格
- 指定 Panel 编号直接制作
- 使用多个 Panel 对同一输入试稿
- 将一个目录中的图片逐张分配给合适的 Panel

它只负责问询、选择和调度，不会成为新的视觉风格，也不会用目录摘要模仿尚未安装的 Panel。

## 一位将军，一支持续扩展的审美士兵队伍

| 层级 | Skill | 负责什么 |
|---|---|---|
| **将军级** | [`xxd-panel-all`](https://github.com/nevertoday/xxd-panel-all) | 识别可用士兵；按图片、主题和用途推荐；按编号点将；组织同图多风格试稿；为图片文件夹批量分配并逐项派发。 |
| **士兵级** | `xxd-panel-NNN` | 每个编号只执行自己独立的原始提示词与审美，把将军派发的单个任务完成为成品。 |

将军负责组织队伍，不替士兵作画。它不会改写、混合或覆盖任何士兵的原始美学；每张成品始终由被选中的编号 Skill 独立完成。

<!-- xxd-soldier-roster:start -->

## 全部士兵 · 16:9 左右双联样张

每张是对应士兵的一张 16:9 左右对照样张（左为现实摄影，右为本编号转绘）。点击图片进入该士兵的 GitHub 仓库。

<table>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-001"><img src="./assets/roster/001.jpg" alt="XXD Panel 001 · 复古稚趣志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-001"><strong>001</strong> · 复古稚趣志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-002"><img src="./assets/roster/002.jpg" alt="XXD Panel 002 · 俏皮包豪斯" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-002"><strong>002</strong> · 俏皮包豪斯</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-003"><img src="./assets/roster/003.jpg" alt="XXD Panel 003 · 张力线语" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-003"><strong>003</strong> · 张力线语</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-004"><img src="./assets/roster/004.jpg" alt="XXD Panel 004 · 城市单线志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-004"><strong>004</strong> · 城市单线志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-005"><img src="./assets/roster/005.jpg" alt="XXD Panel 005 · 童话暗版" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-005"><strong>005</strong> · 童话暗版</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-006"><img src="./assets/roster/006.jpg" alt="XXD Panel 006 · 留白小剧场" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-006"><strong>006</strong> · 留白小剧场</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-007"><img src="./assets/roster/007.jpg" alt="XXD Panel 007 · 手绘观察页" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-007"><strong>007</strong> · 手绘观察页</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-008"><img src="./assets/roster/008.jpg" alt="XXD Panel 008 · 粉彩幻境" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-008"><strong>008</strong> · 粉彩幻境</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-009"><img src="./assets/roster/009.jpg" alt="XXD Panel 009 · 网点锚印" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-009"><strong>009</strong> · 网点锚印</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-010"><img src="./assets/roster/010.jpg" alt="XXD Panel 010 · 黑白旧童书" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-010"><strong>010</strong> · 黑白旧童书</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-011"><img src="./assets/roster/011.jpg" alt="XXD Panel 011 · 冥想线诗" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-011"><strong>011</strong> · 冥想线诗</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-012"><img src="./assets/roster/012.jpg" alt="XXD Panel 012 · 生命几何" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-012"><strong>012</strong> · 生命几何</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-013"><img src="./assets/roster/013.jpg" alt="XXD Panel 013 · 旅行票据册" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-013"><strong>013</strong> · 旅行票据册</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-014"><img src="./assets/roster/014.jpg" alt="XXD Panel 014 · 纸艺浮雕志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-014"><strong>014</strong> · 纸艺浮雕志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-015"><img src="./assets/roster/015.jpg" alt="XXD Panel 015 · 抽象记忆录" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-015"><strong>015</strong> · 抽象记忆录</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-016"><img src="./assets/roster/016.jpg" alt="XXD Panel 016 · 动势版画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-016"><strong>016</strong> · 动势版画</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-017"><img src="./assets/roster/017.jpg" alt="XXD Panel 017 · 稚趣平面志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-017"><strong>017</strong> · 稚趣平面志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-018"><img src="./assets/roster/018.jpg" alt="XXD Panel 018 · 手工剪纸志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-018"><strong>018</strong> · 手工剪纸志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-019"><img src="./assets/roster/019.jpg" alt="XXD Panel 019 · 复古平面志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-019"><strong>019</strong> · 复古平面志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-020"><img src="./assets/roster/020.jpg" alt="XXD Panel 020 · 厚涂微景观" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-020"><strong>020</strong> · 厚涂微景观</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-021"><img src="./assets/roster/021.jpg" alt="XXD Panel 021 · 黑域越界" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-021"><strong>021</strong> · 黑域越界</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-022"><img src="./assets/roster/022.jpg" alt="XXD Panel 022 · 彩点越界" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-022"><strong>022</strong> · 彩点越界</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-023"><img src="./assets/roster/023.jpg" alt="XXD Panel 023 · 东方窗景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-023"><strong>023</strong> · 东方窗景</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-024"><img src="./assets/roster/024.jpg" alt="XXD Panel 024 · 情绪窗口" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-024"><strong>024</strong> · 情绪窗口</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-025"><img src="./assets/roster/025.jpg" alt="XXD Panel 025 · 隐形意象" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-025"><strong>025</strong> · 隐形意象</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-026"><img src="./assets/roster/026.jpg" alt="XXD Panel 026 · 几何秩序" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-026"><strong>026</strong> · 几何秩序</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-027"><img src="./assets/roster/027.jpg" alt="XXD Panel 027 · 纸上浮雕" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-027"><strong>027</strong> · 纸上浮雕</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-028"><img src="./assets/roster/028.jpg" alt="XXD Panel 028 · 等距微景观" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-028"><strong>028</strong> · 等距微景观</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-029"><img src="./assets/roster/029.jpg" alt="XXD Panel 029 · 纸上慢写" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-029"><strong>029</strong> · 纸上慢写</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-030"><img src="./assets/roster/030.jpg" alt="XXD Panel 030 · 自然越界" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-030"><strong>030</strong> · 自然越界</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-031"><img src="./assets/roster/031.jpg" alt="XXD Panel 031 · 寓意拓印" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-031"><strong>031</strong> · 寓意拓印</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-032"><img src="./assets/roster/032.jpg" alt="XXD Panel 032 · 图形字标" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-032"><strong>032</strong> · 图形字标</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-033"><img src="./assets/roster/033.jpg" alt="XXD Panel 033 · 鲜彩拼贴志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-033"><strong>033</strong> · 鲜彩拼贴志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-034"><img src="./assets/roster/034.jpg" alt="XXD Panel 034 · 旅行章印" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-034"><strong>034</strong> · 旅行章印</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-035"><img src="./assets/roster/035.jpg" alt="XXD Panel 035 · 积木重构" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-035"><strong>035</strong> · 积木重构</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-036"><img src="./assets/roster/036.jpg" alt="XXD Panel 036 · 流线绘本" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-036"><strong>036</strong> · 流线绘本</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-037"><img src="./assets/roster/037.jpg" alt="XXD Panel 037 · 流金徽章" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-037"><strong>037</strong> · 流金徽章</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-038"><img src="./assets/roster/038.jpg" alt="XXD Panel 038 · 纺织生活志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-038"><strong>038</strong> · 纺织生活志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-039"><img src="./assets/roster/039.jpg" alt="XXD Panel 039 · 刺绣意象" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-039"><strong>039</strong> · 刺绣意象</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-040"><img src="./assets/roster/040.jpg" alt="XXD Panel 040 · 涂鸦同伴" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-040"><strong>040</strong> · 涂鸦同伴</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-041"><img src="./assets/roster/041.jpg" alt="XXD Panel 041 · 等距研究室" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-041"><strong>041</strong> · 等距研究室</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-042"><img src="./assets/roster/042.jpg" alt="XXD Panel 042 · 解构水彩志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-042"><strong>042</strong> · 解构水彩志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-043"><img src="./assets/roster/043.jpg" alt="XXD Panel 043 · 白色泡沫" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-043"><strong>043</strong> · 白色泡沫</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-044"><img src="./assets/roster/044.jpg" alt="XXD Panel 044 · 平面纯金" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-044"><strong>044</strong> · 平面纯金</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-045"><img src="./assets/roster/045.jpg" alt="XXD Panel 045 · 治愈积木城" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-045"><strong>045</strong> · 治愈积木城</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-046"><img src="./assets/roster/046.jpg" alt="XXD Panel 046 · 厚涂微世界" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-046"><strong>046</strong> · 厚涂微世界</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-047"><img src="./assets/roster/047.jpg" alt="XXD Panel 047 · 等距厚涂景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-047"><strong>047</strong> · 等距厚涂景</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-048"><img src="./assets/roster/048.jpg" alt="XXD Panel 048 · 透明结构志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-048"><strong>048</strong> · 透明结构志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-049"><img src="./assets/roster/049.jpg" alt="XXD Panel 049 · 木刻印记" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-049"><strong>049</strong> · 木刻印记</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-050"><img src="./assets/roster/050.jpg" alt="XXD Panel 050 · 旅行明信片" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-050"><strong>050</strong> · 旅行明信片</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-051"><img src="./assets/roster/051.jpg" alt="XXD Panel 051 · 手作微缩岛" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-051"><strong>051</strong> · 手作微缩岛</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-052"><img src="./assets/roster/052.jpg" alt="XXD Panel 052 · 纸艺微缩岛" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-052"><strong>052</strong> · 纸艺微缩岛</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-053"><img src="./assets/roster/053.jpg" alt="XXD Panel 053 · 钢笔淡彩录" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-053"><strong>053</strong> · 钢笔淡彩录</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-054"><img src="./assets/roster/054.jpg" alt="XXD Panel 054 · 记忆贴纸册" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-054"><strong>054</strong> · 记忆贴纸册</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-055"><img src="./assets/roster/055.jpg" alt="XXD Panel 055 · 绘画记忆场" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-055"><strong>055</strong> · 绘画记忆场</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-056"><img src="./assets/roster/056.jpg" alt="XXD Panel 056 · 留白记忆画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-056"><strong>056</strong> · 留白记忆画</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-057"><img src="./assets/roster/057.jpg" alt="XXD Panel 057 · 几何记忆场" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-057"><strong>057</strong> · 几何记忆场</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-058"><img src="./assets/roster/058.jpg" alt="XXD Panel 058 · 诗意观念景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-058"><strong>058</strong> · 诗意观念景</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-059"><img src="./assets/roster/059.jpg" alt="XXD Panel 059 · 手绘寓言录" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-059"><strong>059</strong> · 手绘寓言录</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-060"><img src="./assets/roster/060.jpg" alt="XXD Panel 060 · 禅意极简诗" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-060"><strong>060</strong> · 禅意极简诗</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-061"><img src="./assets/roster/061.jpg" alt="XXD Panel 061 · 视觉记忆簿" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-061"><strong>061</strong> · 视觉记忆簿</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-062"><img src="./assets/roster/062.jpg" alt="XXD Panel 062 · 聪明笨拙线" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-062"><strong>062</strong> · 聪明笨拙线</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-063"><img src="./assets/roster/063.jpg" alt="XXD Panel 063 · 像素隐喻志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-063"><strong>063</strong> · 像素隐喻志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-064"><img src="./assets/roster/064.jpg" alt="XXD Panel 064 · 独立拼贴页" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-064"><strong>064</strong> · 独立拼贴页</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-065"><img src="./assets/roster/065.jpg" alt="XXD Panel 065 · 双线编辑志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-065"><strong>065</strong> · 双线编辑志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-066"><img src="./assets/roster/066.jpg" alt="XXD Panel 066 · 童真叙事线" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-066"><strong>066</strong> · 童真叙事线</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-067"><img src="./assets/roster/067.jpg" alt="XXD Panel 067 · 日常幽默画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-067"><strong>067</strong> · 日常幽默画</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-068"><img src="./assets/roster/068.jpg" alt="XXD Panel 068 · 东方写意册" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-068"><strong>068</strong> · 东方写意册</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-069"><img src="./assets/roster/069.jpg" alt="XXD Panel 069 · 鲜彩涂抹窗" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-069"><strong>069</strong> · 鲜彩涂抹窗</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-070"><img src="./assets/roster/070.jpg" alt="XXD Panel 070 · 厚涂治愈岛" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-070"><strong>070</strong> · 厚涂治愈岛</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-071"><img src="./assets/roster/071.jpg" alt="XXD Panel 071 · 粉彩诗意簿" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-071"><strong>071</strong> · 粉彩诗意簿</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-072"><img src="./assets/roster/072.jpg" alt="XXD Panel 072 · 明亮色彩志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-072"><strong>072</strong> · 明亮色彩志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-073"><img src="./assets/roster/073.jpg" alt="XXD Panel 073 · 几何城市志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-073"><strong>073</strong> · 几何城市志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-074"><img src="./assets/roster/074.jpg" alt="XXD Panel 074 · 情绪图标志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-074"><strong>074</strong> · 情绪图标志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-075"><img src="./assets/roster/075.jpg" alt="XXD Panel 075 · 深色蜡笔稿" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-075"><strong>075</strong> · 深色蜡笔稿</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-076"><img src="./assets/roster/076.jpg" alt="XXD Panel 076 · 马卡龙蜡笔" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-076"><strong>076</strong> · 马卡龙蜡笔</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-077"><img src="./assets/roster/077.jpg" alt="XXD Panel 077 · 旅行杂志画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-077"><strong>077</strong> · 旅行杂志画</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-078"><img src="./assets/roster/078.jpg" alt="XXD Panel 078 · 金箔压印志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-078"><strong>078</strong> · 金箔压印志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-079"><img src="./assets/roster/079.jpg" alt="XXD Panel 079 · 钢笔淡彩志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-079"><strong>079</strong> · 钢笔淡彩志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-080"><img src="./assets/roster/080.jpg" alt="XXD Panel 080 · 有机水粉场" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-080"><strong>080</strong> · 有机水粉场</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-081"><img src="./assets/roster/081.jpg" alt="XXD Panel 081 · 彩线纪念册" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-081"><strong>081</strong> · 彩线纪念册</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-082"><img src="./assets/roster/082.jpg" alt="XXD Panel 082 · 水彩跃出纸" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-082"><strong>082</strong> · 水彩跃出纸</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-083"><img src="./assets/roster/083.jpg" alt="XXD Panel 083 · 丑萌角色志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-083"><strong>083</strong> · 丑萌角色志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-084"><img src="./assets/roster/084.jpg" alt="XXD Panel 084 · 点描线构志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-084"><strong>084</strong> · 点描线构志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-085"><img src="./assets/roster/085.jpg" alt="XXD Panel 085 · 手作模型志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-085"><strong>085</strong> · 手作模型志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-086"><img src="./assets/roster/086.jpg" alt="XXD Panel 086 · 留白版画志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-086"><strong>086</strong> · 留白版画志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-087"><img src="./assets/roster/087.jpg" alt="XXD Panel 087 · 红线关系图" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-087"><strong>087</strong> · 红线关系图</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-088"><img src="./assets/roster/088.jpg" alt="XXD Panel 088 · 文字造型诗" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-088"><strong>088</strong> · 文字造型诗</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-089"><img src="./assets/roster/089.jpg" alt="XXD Panel 089 · 生活小品簿" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-089"><strong>089</strong> · 生活小品簿</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-090"><img src="./assets/roster/090.jpg" alt="XXD Panel 090 · 视觉思维图" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-090"><strong>090</strong> · 视觉思维图</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-091"><img src="./assets/roster/091.jpg" alt="XXD Panel 091 · 蓝线旅行册" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-091"><strong>091</strong> · 蓝线旅行册</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-092"><img src="./assets/roster/092.jpg" alt="XXD Panel 092 · 表现线描志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-092"><strong>092</strong> · 表现线描志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-093"><img src="./assets/roster/093.jpg" alt="XXD Panel 093 · 现代几何画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-093"><strong>093</strong> · 现代几何画</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-094"><img src="./assets/roster/094.jpg" alt="XXD Panel 094 · 古典双色书" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-094"><strong>094</strong> · 古典双色书</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-095"><img src="./assets/roster/095.jpg" alt="XXD Panel 095 · 红黑图解志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-095"><strong>095</strong> · 红黑图解志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-096"><img src="./assets/roster/096.jpg" alt="XXD Panel 096 · 民间通信卡" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-096"><strong>096</strong> · 民间通信卡</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-097"><img src="./assets/roster/097.jpg" alt="XXD Panel 097 · 复古说明卡" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-097"><strong>097</strong> · 复古说明卡</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-098"><img src="./assets/roster/098.jpg" alt="XXD Panel 098 · 稚拙水彩书" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-098"><strong>098</strong> · 稚拙水彩书</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-099"><img src="./assets/roster/099.jpg" alt="XXD Panel 099 · 字体吉祥物" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-099"><strong>099</strong> · 字体吉祥物</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-100"><img src="./assets/roster/100.jpg" alt="XXD Panel 100 · 民艺叙事画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-100"><strong>100</strong> · 民艺叙事画</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-101"><img src="./assets/roster/101.jpg" alt="XXD Panel 101 · 九宫记忆簿" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-101"><strong>101</strong> · 九宫记忆簿</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-102"><img src="./assets/roster/102.jpg" alt="XXD Panel 102 · 治愈几何志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-102"><strong>102</strong> · 治愈几何志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-103"><img src="./assets/roster/103.jpg" alt="XXD Panel 103 · 鲜彩抽象拼" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-103"><strong>103</strong> · 鲜彩抽象拼</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-104"><img src="./assets/roster/104.jpg" alt="XXD Panel 104 · 网点禅意志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-104"><strong>104</strong> · 网点禅意志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-105"><img src="./assets/roster/105.jpg" alt="XXD Panel 105 · 诗意留白集" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-105"><strong>105</strong> · 诗意留白集</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-106"><img src="./assets/roster/106.jpg" alt="XXD Panel 106 · 柔彩像素记" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-106"><strong>106</strong> · 柔彩像素记</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-107"><img src="./assets/roster/107.jpg" alt="XXD Panel 107 · 图像替词诗" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-107"><strong>107</strong> · 图像替词诗</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-108"><img src="./assets/roster/108.jpg" alt="XXD Panel 108 · 新民艺剪纸志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-108"><strong>108</strong> · 新民艺剪纸志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-109"><img src="./assets/roster/109.jpg" alt="XXD Panel 109 · 柔和几何解构志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-109"><strong>109</strong> · 柔和几何解构志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-110"><img src="./assets/roster/110.jpg" alt="XXD Panel 110 · 日系生活场景图鉴" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-110"><strong>110</strong> · 日系生活场景图鉴</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-111"><img src="./assets/roster/111.jpg" alt="XXD Panel 111 · 纺织拼贴志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-111"><strong>111</strong> · 纺织拼贴志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-112"><img src="./assets/roster/112.jpg" alt="XXD Panel 112 · 金线纸本志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-112"><strong>112</strong> · 金线纸本志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-113"><img src="./assets/roster/113.jpg" alt="XXD Panel 113 · 贝壳像素留白志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-113"><strong>113</strong> · 贝壳像素留白志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-114"><img src="./assets/roster/114.jpg" alt="XXD Panel 114 · 复古粉彩手账涂鸦" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-114"><strong>114</strong> · 复古粉彩手账涂鸦</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-115"><img src="./assets/roster/115.jpg" alt="XXD Panel 115 · 粉彩章印拼贴志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-115"><strong>115</strong> · 粉彩章印拼贴志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-116"><img src="./assets/roster/116.jpg" alt="XXD Panel 116 · 浅纸粉彩涂鸦志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-116"><strong>116</strong> · 浅纸粉彩涂鸦志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-117"><img src="./assets/roster/117.jpg" alt="XXD Panel 117 · 细线淡彩留白志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-117"><strong>117</strong> · 细线淡彩留白志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-118"><img src="./assets/roster/118.jpg" alt="XXD Panel 118 · 石墨留白素描志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-118"><strong>118</strong> · 石墨留白素描志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-119"><img src="./assets/roster/119.jpg" alt="XXD Panel 119 · 手缝布艺留白志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-119"><strong>119</strong> · 手缝布艺留白志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-120"><img src="./assets/roster/120.jpg" alt="XXD Panel 120 · 建筑概念手绘志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-120"><strong>120</strong> · 建筑概念手绘志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-121"><img src="./assets/roster/121.jpg" alt="XXD Panel 121 · 生活涂鸦编排志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-121"><strong>121</strong> · 生活涂鸦编排志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-122"><img src="./assets/roster/122.jpg" alt="XXD Panel 122 · 单色网点手写志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-122"><strong>122</strong> · 单色网点手写志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-123"><img src="./assets/roster/123.jpg" alt="XXD Panel 123 · 红蓝角线彩铅志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-123"><strong>123</strong> · 红蓝角线彩铅志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-124"><img src="./assets/roster/124.jpg" alt="XXD Panel 124 · 布艺拼贴留白志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-124"><strong>124</strong> · 布艺拼贴留白志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-125"><img src="./assets/roster/125.jpg" alt="XXD Panel 125 · 蜡笔童趣留白志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-125"><strong>125</strong> · 蜡笔童趣留白志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-126"><img src="./assets/roster/126.jpg" alt="XXD Panel 126 · 诗意微缩拼贴志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-126"><strong>126</strong> · 诗意微缩拼贴志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-127"><img src="./assets/roster/127.jpg" alt="XXD Panel 127 · 建筑混媒拼贴志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-127"><strong>127</strong> · 建筑混媒拼贴志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-128"><img src="./assets/roster/128.jpg" alt="XXD Panel 128 · 珐琅徽章旅行志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-128"><strong>128</strong> · 珐琅徽章旅行志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-129"><img src="./assets/roster/129.jpg" alt="XXD Panel 129 · 东方弥散留白志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-129"><strong>129</strong> · 东方弥散留白志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-130"><img src="./assets/roster/130.jpg" alt="XXD Panel 130 · 硬边几何切面志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-130"><strong>130</strong> · 硬边几何切面志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-131"><img src="./assets/roster/131.jpg" alt="XXD Panel 131 · 摄影涂鸦拼贴志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-131"><strong>131</strong> · 摄影涂鸦拼贴志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-132"><img src="./assets/roster/132.jpg" alt="XXD Panel 132 · 钢笔淡彩旅行志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-132"><strong>132</strong> · 钢笔淡彩旅行志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-133"><img src="./assets/roster/133.jpg" alt="XXD Panel 133 · 点刻透明套印志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-133"><strong>133</strong> · 点刻透明套印志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-134"><img src="./assets/roster/134.jpg" alt="XXD Panel 134 · 绘本色域叙事志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-134"><strong>134</strong> · 绘本色域叙事志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-135"><img src="./assets/roster/135.jpg" alt="XXD Panel 135 · 街头专色手绘志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-135"><strong>135</strong> · 街头专色手绘志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-136"><img src="./assets/roster/136.jpg" alt="XXD Panel 136 · 诗意超现实留白志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-136"><strong>136</strong> · 诗意超现实留白志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-137"><img src="./assets/roster/137.jpg" alt="XXD Panel 137 · 蚀刻肌理拼贴志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-137"><strong>137</strong> · 蚀刻肌理拼贴志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-138"><img src="./assets/roster/138.jpg" alt="XXD Panel 138 · 东方纸艺浮雕志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-138"><strong>138</strong> · 东方纸艺浮雕志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-139"><img src="./assets/roster/139.jpg" alt="XXD Panel 139 · 文字编码线场志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-139"><strong>139</strong> · 文字编码线场志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-140"><img src="./assets/roster/140.jpg" alt="XXD Panel 140 · 干性手绘视觉岛" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-140"><strong>140</strong> · 干性手绘视觉岛</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-141"><img src="./assets/roster/141.jpg" alt="XXD Panel 141 · 极简手绘线描志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-141"><strong>141</strong> · 极简手绘线描志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-142"><img src="./assets/roster/142.jpg" alt="XXD Panel 142 · 字形蒙版融合志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-142"><strong>142</strong> · 字形蒙版融合志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-143"><img src="./assets/roster/143.jpg" alt="XXD Panel 143 · 文字造型视觉诗" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-143"><strong>143</strong> · 文字造型视觉诗</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-144"><img src="./assets/roster/144.jpg" alt="XXD Panel 144 · 几何反白破框志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-144"><strong>144</strong> · 几何反白破框志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-145"><img src="./assets/roster/145.jpg" alt="XXD Panel 145 · 复古限色版画志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-145"><strong>145</strong> · 复古限色版画志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-146"><img src="./assets/roster/146.jpg" alt="XXD Panel 146 · 博物学丝巾印花志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-146"><strong>146</strong> · 博物学丝巾印花志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-147"><img src="./assets/roster/147.jpg" alt="XXD Panel 147 · 便当食材包装志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-147"><strong>147</strong> · 便当食材包装志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-148"><img src="./assets/roster/148.jpg" alt="XXD Panel 148 · 视觉日记拼贴志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-148"><strong>148</strong> · 视觉日记拼贴志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-149"><img src="./assets/roster/149.jpg" alt="XXD Panel 149 · 手绘肌理扁平志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-149"><strong>149</strong> · 手绘肌理扁平志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-150"><img src="./assets/roster/150.jpg" alt="XXD Panel 150 · 复古现代剪纸志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-150"><strong>150</strong> · 复古现代剪纸志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-151"><img src="./assets/roster/151.jpg" alt="XXD Panel 151 · 稚拙扁平手绘志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-151"><strong>151</strong> · 稚拙扁平手绘志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-152"><img src="./assets/roster/152.jpg" alt="XXD Panel 152 · 色场基座纸艺志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-152"><strong>152</strong> · 色场基座纸艺志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-153"><img src="./assets/roster/153.jpg" alt="XXD Panel 153 · 单色手帐涂鸦志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-153"><strong>153</strong> · 单色手帐涂鸦志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-154"><img src="./assets/roster/154.jpg" alt="XXD Panel 154 · 复古像素留白志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-154"><strong>154</strong> · 复古像素留白志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-155"><img src="./assets/roster/155.jpg" alt="XXD Panel 155 · 一点透视淡彩志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-155"><strong>155</strong> · 一点透视淡彩志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-156"><img src="./assets/roster/156.jpg" alt="XXD Panel 156 · 双色错版插画志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-156"><strong>156</strong> · 双色错版插画志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-157"><img src="./assets/roster/157.jpg" alt="XXD Panel 157 · 文物墨拓留白志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-157"><strong>157</strong> · 文物墨拓留白志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-158"><img src="./assets/roster/158.jpg" alt="XXD Panel 158 · 纸本综合拼贴志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-158"><strong>158</strong> · 纸本综合拼贴志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-159"><img src="./assets/roster/159.jpg" alt="XXD Panel 159 · 字符网点实验志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-159"><strong>159</strong> · 字符网点实验志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-160"><img src="./assets/roster/160.jpg" alt="XXD Panel 160 · 松线淡彩留白志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-160"><strong>160</strong> · 松线淡彩留白志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-161"><img src="./assets/roster/161.jpg" alt="XXD Panel 161 · 框景色场越界志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-161"><strong>161</strong> · 框景色场越界志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-162"><img src="./assets/roster/162.jpg" alt="XXD Panel 162 · 白衬剪纸绘本志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-162"><strong>162</strong> · 白衬剪纸绘本志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-163"><img src="./assets/roster/163.jpg" alt="XXD Panel 163 · 居中纯色章印志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-163"><strong>163</strong> · 居中纯色章印志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-164"><img src="./assets/roster/164.jpg" alt="XXD Panel 164 · 水墨建筑微景志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-164"><strong>164</strong> · 水墨建筑微景志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-165"><img src="./assets/roster/165.jpg" alt="XXD Panel 165 · 中央撕纸揭景志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-165"><strong>165</strong> · 中央撕纸揭景志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-166"><img src="./assets/roster/166.jpg" alt="XXD Panel 166 · 等距浮雕微缩志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-166"><strong>166</strong> · 等距浮雕微缩志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-167"><img src="./assets/roster/167.jpg" alt="XXD Panel 167 · 波形厚墨浮雕志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-167"><strong>167</strong> · 波形厚墨浮雕志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-168"><img src="./assets/roster/168.jpg" alt="XXD Panel 168 · 留纸白叠刷色场志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-168"><strong>168</strong> · 留纸白叠刷色场志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-169"><img src="./assets/roster/169.jpg" alt="XXD Panel 169 · 暖赭小幅墨线志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-169"><strong>169</strong> · 暖赭小幅墨线志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-170"><img src="./assets/roster/170.jpg" alt="XXD Panel 170 · 黑锈红干笔小景志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-170"><strong>170</strong> · 黑锈红干笔小景志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-171"><img src="./assets/roster/171.jpg" alt="XXD Panel 171 · 竖线微型散点志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-171"><strong>171</strong> · 竖线微型散点志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-172"><img src="./assets/roster/172.jpg" alt="XXD Panel 172 · 居中透明几何志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-172"><strong>172</strong> · 居中透明几何志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-173"><img src="./assets/roster/173.jpg" alt="XXD Panel 173 · 象牙纸本文字微景志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-173"><strong>173</strong> · 象牙纸本文字微景志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-174"><img src="./assets/roster/174.jpg" alt="XXD Panel 174 · 稚拙贴纸聚合志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-174"><strong>174</strong> · 稚拙贴纸聚合志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-175"><img src="./assets/roster/175.jpg" alt="XXD Panel 175 · 琥珀透光纸雕小景志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-175"><strong>175</strong> · 琥珀透光纸雕小景志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-176"><img src="./assets/roster/176.jpg" alt="XXD Panel 176 · 工笔阵盘微立体志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-176"><strong>176</strong> · 工笔阵盘微立体志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-177"><img src="./assets/roster/177.jpg" alt="XXD Panel 177 · 异形微岛版画志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-177"><strong>177</strong> · 异形微岛版画志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-178"><img src="./assets/roster/178.jpg" alt="XXD Panel 178 · 异形微岛版画志（同源）" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-178"><strong>178</strong> · 异形微岛版画志（同源）</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-179"><img src="./assets/roster/179.jpg" alt="XXD Panel 179 · 丝带微缩陈列志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-179"><strong>179</strong> · 丝带微缩陈列志</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-180"><img src="./assets/roster/180.jpg" alt="XXD Panel 180 · 复古圆章旅行手账志" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-180"><strong>180</strong> · 复古圆章旅行手账志</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-181"><img src="./assets/roster/181.jpg" alt="XXD Panel 181 · 文人彩墨写意小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-181"><strong>181</strong> · 文人彩墨写意小品</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-182"><img src="./assets/roster/182.jpg" alt="XXD Panel 182 · 微缩像素图形小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-182"><strong>182</strong> · 微缩像素图形小品</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-183"><img src="./assets/roster/183.jpg" alt="XXD Panel 183 · 深绿角隅自然图形" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-183"><strong>183</strong> · 深绿角隅自然图形</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-184"><img src="./assets/roster/184.jpg" alt="XXD Panel 184 · 方形生活手绘盒景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-184"><strong>184</strong> · 方形生活手绘盒景</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-185"><img src="./assets/roster/185.jpg" alt="XXD Panel 185 · 黑白浅色贴纸小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-185"><strong>185</strong> · 黑白浅色贴纸小品</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-186"><img src="./assets/roster/186.jpg" alt="XXD Panel 186 · 柔色九宫格几何记忆" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-186"><strong>186</strong> · 柔色九宫格几何记忆</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-187"><img src="./assets/roster/187.jpg" alt="XXD Panel 187 · 巨型字体档案拼贴" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-187"><strong>187</strong> · 巨型字体档案拼贴</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-188"><img src="./assets/roster/188.jpg" alt="XXD Panel 188 · 米金留白建筑档案" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-188"><strong>188</strong> · 米金留白建筑档案</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-189"><img src="./assets/roster/189.jpg" alt="XXD Panel 189 · 双框侧栏火柴盒小景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-189"><strong>189</strong> · 双框侧栏火柴盒小景</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-190"><img src="./assets/roster/190.jpg" alt="XXD Panel 190 · 冷主暖辅朴拙粉彩" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-190"><strong>190</strong> · 冷主暖辅朴拙粉彩</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-191"><img src="./assets/roster/191.jpg" alt="XXD Panel 191 · 毛边矩形粉彩色域" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-191"><strong>191</strong> · 毛边矩形粉彩色域</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-192"><img src="./assets/roster/192.jpg" alt="XXD Panel 192 · 复古限色图形小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-192"><strong>192</strong> · 复古限色图形小品</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-193"><img src="./assets/roster/193.jpg" alt="XXD Panel 193 · 基座承托灰调水彩" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-193"><strong>193</strong> · 基座承托灰调水彩</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-194"><img src="./assets/roster/194.jpg" alt="XXD Panel 194 · 明快基座轴测体量" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-194"><strong>194</strong> · 明快基座轴测体量</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-195"><img src="./assets/roster/195.jpg" alt="XXD Panel 195 · 一抹亮色历史蒙太奇" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-195"><strong>195</strong> · 一抹亮色历史蒙太奇</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-196"><img src="./assets/roster/196.jpg" alt="XXD Panel 196 · 俯视几何抽象人物" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-196"><strong>196</strong> · 俯视几何抽象人物</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-197"><img src="./assets/roster/197.jpg" alt="XXD Panel 197 · 笼中世界新民艺" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-197"><strong>197</strong> · 笼中世界新民艺</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-198"><img src="./assets/roster/198.jpg" alt="XXD Panel 198 · 限色失重时装拼贴" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-198"><strong>198</strong> · 限色失重时装拼贴</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-199"><img src="./assets/roster/199.jpg" alt="XXD Panel 199 · 明快留白时装拼贴" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-199"><strong>199</strong> · 明快留白时装拼贴</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-200"><img src="./assets/roster/200.jpg" alt="XXD Panel 200 · 蓝灰单色手绘线描" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-200"><strong>200</strong> · 蓝灰单色手绘线描</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-201"><img src="./assets/roster/201.jpg" alt="XXD Panel 201 · 奶油手作微缩立体" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-201"><strong>201</strong> · 奶油手作微缩立体</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-202"><img src="./assets/roster/202.jpg" alt="XXD Panel 202 · 结构主线几何线图" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-202"><strong>202</strong> · 结构主线几何线图</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-203"><img src="./assets/roster/203.jpg" alt="XXD Panel 203 · 留白厚涂明信片" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-203"><strong>203</strong> · 留白厚涂明信片</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-204"><img src="./assets/roster/204.jpg" alt="XXD Panel 204 · 柔焦光影记忆小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-204"><strong>204</strong> · 柔焦光影记忆小品</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-205"><img src="./assets/roster/205.jpg" alt="XXD Panel 205 · 暖调有机形摄影拼贴" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-205"><strong>205</strong> · 暖调有机形摄影拼贴</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-206"><img src="./assets/roster/206.jpg" alt="XXD Panel 206 · 柔色纸雕微缩小景" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-206"><strong>206</strong> · 柔色纸雕微缩小景</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-207"><img src="./assets/roster/207.jpg" alt="XXD Panel 207 · 浅蓝白混合媒介插页" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-207"><strong>207</strong> · 浅蓝白混合媒介插页</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-208"><img src="./assets/roster/208.jpg" alt="XXD Panel 208 · 蓝粉现代主义抽象" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-208"><strong>208</strong> · 蓝粉现代主义抽象</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-209"><img src="./assets/roster/209.jpg" alt="XXD Panel 209 · 极简纸张影像档案" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-209"><strong>209</strong> · 极简纸张影像档案</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-210"><img src="./assets/roster/210.jpg" alt="XXD Panel 210 · 冷调轻量概念拼贴" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-210"><strong>210</strong> · 冷调轻量概念拼贴</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-211"><img src="./assets/roster/211.jpg" alt="XXD Panel 211 · 语义配色几何小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-211"><strong>211</strong> · 语义配色几何小品</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-212"><img src="./assets/roster/212.jpg" alt="XXD Panel 212 · 近单色概念形体模型" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-212"><strong>212</strong> · 近单色概念形体模型</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-213"><img src="./assets/roster/213.jpg" alt="XXD Panel 213 · 暖纸冷色观念线稿" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-213"><strong>213</strong> · 暖纸冷色观念线稿</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-214"><img src="./assets/roster/214.jpg" alt="XXD Panel 214 · 真实固有色粗粝剪纸" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-214"><strong>214</strong> · 真实固有色粗粝剪纸</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-215"><img src="./assets/roster/215.jpg" alt="XXD Panel 215 · 灰阶赭黄极简轴测" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-215"><strong>215</strong> · 灰阶赭黄极简轴测</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-216"><img src="./assets/roster/216.jpg" alt="XXD Panel 216 · 九成留白单色视觉岛" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-216"><strong>216</strong> · 九成留白单色视觉岛</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-217"><img src="./assets/roster/217.jpg" alt="XXD Panel 217 · 明快数码混合媒介拼贴" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-217"><strong>217</strong> · 明快数码混合媒介拼贴</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-218"><img src="./assets/roster/218.jpg" alt="XXD Panel 218 · 极简绘本羊毛毡插画" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-218"><strong>218</strong> · 极简绘本羊毛毡插画</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-219"><img src="./assets/roster/219.jpg" alt="XXD Panel 219 · 彩铅点染旅行手帐线稿" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-219"><strong>219</strong> · 彩铅点染旅行手帐线稿</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-220"><img src="./assets/roster/220.jpg" alt="XXD Panel 220 · 圆润稚拙手绘涂鸦小品" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-220"><strong>220</strong> · 圆润稚拙手绘涂鸦小品</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-221"><img src="./assets/roster/221.jpg" alt="XXD Panel 221 · 新中式专色版画留白" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-221"><strong>221</strong> · 新中式专色版画留白</a></p>
</td>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-222"><img src="./assets/roster/222.jpg" alt="XXD Panel 222 · 建筑化字体图形装置" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-222"><strong>222</strong> · 建筑化字体图形装置</a></p>
</td>
  </tr>
  <tr>
    <td width="50%" valign="top">
<a href="https://github.com/nevertoday/xxd-panel-223"><img src="./assets/roster/223.jpg" alt="XXD Panel 223 · 复古雕版微型图集" width="100%"></a>
<p align="center"><a href="https://github.com/nevertoday/xxd-panel-223"><strong>223</strong> · 复古雕版微型图集</a></p>
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

## 广告信息｜XXD 付费服务与会员

> **广告与商业信息声明：** 以下二维码、会员与付费服务链接属于小小东的广告信息。是否扫码或购买完全自愿，不影响本开源项目的访问与使用。


全部 将军总指挥 Skills 已包含在 699 元/年的统一会员权益中，无需单独购买。 [WeChat](https://xiaoxiaodong.pages.dev/assets/wechat-qr.png)

## 知识星球＋成员提示词库＋全部 将军总指挥 Skills 会员 · 699 元/年

[知识星球](https://wx.zsxq.com/group/15554814142882)、[小小东成员提示词库](https://vip.xiaoxiaodong.ai/)与全部 将军总指挥 Skills 会员是同一份会员权益：**一次年费同时开通三项权益，无需重复付费。**开通后可扫描微信二维码，与小小东进行一对一沟通，获得 AI 学习、工具使用和实际项目答疑；同时按需领取成员提示词库兑换码，并加入全部 将军总指挥 Skills 会员权益。

## 安装

```bash
git clone https://github.com/nevertoday/xxd-panel-all.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/xxd-panel-all" ~/.claude/skills/xxd-panel-all
```

也可以直接使用 `npx skills` 安装：

```bash
npx skills add https://github.com/xiaoxiaodong-ai/xxd-panel-all --skill xxd-panel-all
```

该命令会从 GitHub 获取将军仓库，并把 `xxd-panel-all` 安装到当前 Agent。若要安装到用户级 Codex Skills 目录，可在命令末尾加上 `--global --agent codex --yes`。将军只负责调度；要实际制作，还需要另外安装所需的 `xxd-panel-NNN` 士兵 Skills。

如果 `~/.codex/skills` 没有与 `~/.claude/skills` 共用，可以另外建立链接：

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/xxd-panel-all" ~/.codex/skills/xxd-panel-all
```

安装后重新打开 Agent 会话，然后调用：

```text
$xxd-panel-all
```

## 目录批量处理

可以在调用时直接提供图片目录：

```text
$xxd-panel-all /path/to/images
```

Skill 会直接进入批量模式，扫描目录和子目录中的图片，然后询问一种分配方式：

1. 全部图片使用同一个 Panel
2. 每张图片自动匹配最合适的 Panel
3. 相似图片分组，每组使用同一个 Panel
4. 只在指定的几个 Panel 中自动分配

公共交付设置只收集一次；随后每张图片仍作为独立任务进入对应的 `xxd-panel-NNN`，不会合并成拼图或让不同图片互相污染。

## 继承上次偏好，或全新配置

当本次交付设置还不完整、且检测到上一次 XXD Panel 偏好时，将军或士兵会先展示上次的模式、尺寸、文字与语言、壁纸关系和输出位置，再询问：

1. **直接沿用**：沿用上次设置，本次已经明确说出的要求优先。
2. **沿用并修改**：先带入上次设置，只修改你选中的项目。
3. **全新配置**：忽略历史设置，从头选择。

完整参数仍然直接执行，不增加多余问询。也可以显式使用 `--prefs last|edit|new|off|clear`。偏好记录只保存交付设置，不保存原图、准确文案、Panel 选择、生成结果、模型通道、API 凭据或其他敏感信息。

```text
$xxd-panel-all /path/to/images --prefs last
$xxd-panel-all /path/to/images --prefs edit
$xxd-panel-all /path/to/images --prefs new
```

## 安装状态

Panel 在运行时分为三种状态：

- `AVAILABLE`：当前已安装，可以直接调用
- `KNOWN_BUT_MISSING`：风格目录中存在，但当前未安装
- `UNKNOWN`：不在当前目录中

推荐、批量分配和直接制作只使用已经安装的 Panel。未安装的风格可以浏览和推荐，但必须安装对应子 Skill 后才能制作。

## 项目结构

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

- `SKILL.md`：交互、推荐、浏览和批量路由规则
- `assets/roster/`：每位士兵一张 16:9 左右双联样张；README 中点击图片进入对应 GitHub 仓库
- `panel-catalog.md`：编号检索目录，不是生图提示词
- `soldier-runtime.md`：全家族士兵运行时合同；每个士兵仓库持有逐字副本
- `runtime-preferences.md`：沿用、修改、全新配置与隐私边界
- `panel_preferences.py`：只读写安全交付偏好的本地辅助脚本
- `soldier_roster.py`：从各士兵 `sample-05.png` 生成 README 花名册
- `openai.yaml`：Skill 的界面元数据

## 许可证

本项目（包括 Skill、提示词、脚本、文档及随附样张）采用 **PolyForm Noncommercial License 1.0.0**。完整法律条文请见 [LICENSE](LICENSE)，官方页面见 <https://polyformproject.org/licenses/noncommercial/1.0.0>。

用人话说：

- 个人可以用于学习、研究、实验、测试、兴趣项目和私人娱乐；慈善机构、教育机构、公共研究/安全/卫生机构、环保组织及政府机构也可以使用。
- 在**非商业目的**下，你可以使用、复制、修改、制作衍生作品并分享；分享时必须同时提供本许可证（或上面的链接）以及作者提供的所有 `Required Notice:` 声明。
- 不允许用于商业产品或服务、收费交付、出售访问权或许可，或任何预期会带来商业应用的用途。需要商业使用时，请先向版权方另行取得书面许可。
- 本协议只授予其中明确写出的著作权许可和有限的专利许可，不授予商标、品牌名称或其他未明确授予的权利，也不能把你的许可再转授给他人。
- 如果收到书面违约通知，须在 32 天内纠正并采取实际补救措施，否则许可会立即终止；就专利侵权提出书面主张也会终止专利许可。
- 内容按“现状”提供，在法律允许的范围内不作任何担保，使用风险和可能的损失由使用者自行承担。
