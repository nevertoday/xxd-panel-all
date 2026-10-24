<div align="center">

# XXD Panel All｜风格总目录

**354 种照片风格的总入口：给它照片和用途，它帮你挑风格、比风格、批量出图。**

<strong>简体中文</strong> · <a href="README.en.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

</div>

<table>
  <tr>
    <td width="33%"><a href="https://github.com/nevertoday/xxd-panel-001"><img src="./assets/roster/001.jpg" alt="XXD Panel 001 · 复古稚趣志"></a></td>
    <td width="33%"><a href="https://github.com/nevertoday/xxd-panel-062"><img src="./assets/roster/062.jpg" alt="XXD Panel 062 · 聪明笨拙线"></a></td>
    <td width="33%"><a href="https://github.com/nevertoday/xxd-panel-350"><img src="./assets/roster/350.jpg" alt="XXD Panel 350 · 霓虹精灵"></a></td>
  </tr>
</table>

## 这是什么

XXD Panel 是一组把照片重新画成海报、插画和壁纸的 AI Skill，一个编号一种风格，目前有 354 个，各自独立。`xxd-panel-all` 是它们的总入口，适合 Claude Code、Codex 等支持 Skills 的 Agent：

- **帮你选：** 给一张照片或一个主题，它从你装好的风格里推荐一个或三个，并说明为什么适合这张图。
- **帮你比：** 同一张照片用几种风格各出一张，放在一起看。
- **帮你批量：** 给一个文件夹，可以全部用同一种风格，也可以每张自动配最合适的风格。
- **它自己不画：** 真正出图的是各个编号的风格 Skill。总目录只负责挑选和分派，不会把几种风格混在一起。

## 三步用起来

**1. 安装总目录，再装几个你喜欢的风格。** 没装的风格它也能介绍和推荐，但要装上才能出图：

```bash
npx skills add https://github.com/nevertoday/xxd-panel-all --skill xxd-panel-all
npx skills add https://github.com/nevertoday/xxd-panel-001 --skill xxd-panel-001
```

一次装好几个：

```bash
for n in 001 062 350; do npx skills add https://github.com/nevertoday/xxd-panel-$n --skill xxd-panel-$n; done
```

装完重开一次 Agent 会话。

**2. 确认 Agent 能生图。** 这个 Skill 不自带生图模型，用的是你 Agent 的生图能力，首选 GPT Image 2。

- Codex 开着内置生图时直接能用。
- Claude Code 等没有内置生图的 Agent，需要接一个 OpenAI 兼容的生图接口，五分钟配好，见[没有内置生图怎么配](#没有内置生图怎么配)。

不确定也可以直接用。不能生图时 Skill 会先停下来告诉你，不会白跑。

**3. 发照片，说一句话：**

> 用 xxd-panel-all 看看这张照片适合哪几个风格，推荐三个并说说理由。

选定以后，它把照片交给那个风格的 Skill 出图；版式、比例、文字这些由那个风格接着问你。成品放在 `~/Desktop/xxd/xxd-panel-NNN/` 下。

## 常用说法

不用记参数，直接说就行：

| 你想要 | 直接这样说 |
|---|---|
| 推荐风格 | 这张照片适合哪个风格？推荐三个，说说理由 |
| 按感觉找 | 有没有黑白线条、留白很多的风格？ |
| 按用途找 | 想做手机壁纸，哪些风格合适？ |
| 指定编号 | 用 062 做这张照片 |
| 比较几种 | 用 001、062、350 各做一张给我比较 |
| 文件夹，同一风格 | 把这个文件夹全部用 014 做成上下对照 |
| 文件夹，自动配 | 这个文件夹里每张照片自动选最合适的风格 |
| 沿用上次 | 沿用上次的设置 |

## 全部风格

共 354 个。每张图是该风格的一张左右对照样张（左原照片，右设计），点图进入它的仓库，那里有更多样张和用法。

<!-- xxd-soldier-roster:start -->

<details open>
<summary><strong>001–050</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-001"><img src="./assets/roster/001.jpg" alt="XXD Panel 001 · 复古稚趣志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-001"><strong>001</strong> · 复古稚趣志</a><br><sub>把一张照片画成轻盈、带纸感、有点笨拙幽默的复古手绘插画。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-002"><img src="./assets/roster/002.jpg" alt="XXD Panel 002 · 俏皮包豪斯" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-002"><strong>002</strong> · 俏皮包豪斯</a><br><sub>把照片画成带一点包豪斯几何、手抖轮廓和旧印刷错位的复古编辑插画。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-003"><img src="./assets/roster/003.jpg" alt="XXD Panel 003 · 张力线语" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-003"><strong>003</strong> · 张力线语</a><br><sub>把照片里的方向、牵连、压力和转机，收成一组安静又紧绷的黑色连续线。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-004"><img src="./assets/roster/004.jpg" alt="XXD Panel 004 · 城市单线志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-004"><strong>004</strong> · 城市单线志</a><br><sub>把一个真实的城市或地点场景，提炼成精准单线、几何透视的收藏级线描海报。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-005"><img src="./assets/roster/005.jpg" alt="XXD Panel 005 · 童话暗版" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-005"><strong>005</strong> · 童话暗版</a><br><sub>把照片压成被大块暗色包住、只在关键处闪出亮色的童话版画。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-006"><img src="./assets/roster/006.jpg" alt="XXD Panel 006 · 留白小剧场" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-006"><strong>006</strong> · 留白小剧场</a><br><sub>把照片提炼成一个小小的主体，放在大片纸面留白里，像一本艺术书的封面。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-007"><img src="./assets/roster/007.jpg" alt="XXD Panel 007 · 手绘观察页" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-007"><strong>007</strong> · 手绘观察页</a><br><sub>把照片拆成一页小图、剖面和手写短句串起来的生活观察笔记。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-008"><img src="./assets/roster/008.jpg" alt="XXD Panel 008 · 粉彩幻境" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-008"><strong>008</strong> · 粉彩幻境</a><br><sub>把照片里的人和故事，转成明亮、安静、像纪念碑谷一样的粉彩不可能空间。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-009"><img src="./assets/roster/009.jpg" alt="XXD Panel 009 · 网点锚印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-009"><strong>009</strong> · 网点锚印</a><br><sub>把照片压成一个极小的锚点，放在大片纸面里，用由密到疏的网点印出距离和空气。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-010"><img src="./assets/roster/010.jpg" alt="XXD Panel 010 · 黑白旧童书" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-010"><strong>010</strong> · 黑白旧童书</a><br><sub>把照片压成近白纸面上用粗黑蜡笔涂出来的童书剪影，只有黑和白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-011"><img src="./assets/roster/011.jpg" alt="XXD Panel 011 · 冥想线诗" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-011"><strong>011</strong> · 冥想线诗</a><br><sub>把照片提炼成一根可以慢慢凝视的黑色连续细线，只留一点有意义的颜色。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-012"><img src="./assets/roster/012.jpg" alt="XXD Panel 012 · 生命几何" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-012"><strong>012</strong> · 生命几何</a><br><sub>让照片主体从一片单色高密线场中聚合显形，外围由几何秩序的细线向外散开。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-013"><img src="./assets/roster/013.jpg" alt="XXD Panel 013 · 旅行票据册" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-013"><strong>013</strong> · 旅行票据册</a><br><sub>把照片收进一张左边水彩、右边票根、像被好好收藏的旅行票据。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-014"><img src="./assets/roster/014.jpg" alt="XXD Panel 014 · 纸艺浮雕志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-014"><strong>014</strong> · 纸艺浮雕志</a><br><sub>把照片重构成一件看得见折痕、切边和纸纤维的当代折纸雕塑。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-015"><img src="./assets/roster/015.jpg" alt="XXD Panel 015 · 抽象记忆录" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-015"><strong>015</strong> · 抽象记忆录</a><br><sub>把照片拆开、筛选、重组成几块几何形和一套精致的编辑小字，像艺术书里的一页。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-016"><img src="./assets/roster/016.jpg" alt="XXD Panel 016 · 动势版画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-016"><strong>016</strong> · 动势版画</a><br><sub>把照片里真正发生的事，压缩成一个极小的主体和围绕它的一场运动。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-017"><img src="./assets/roster/017.jpg" alt="XXD Panel 017 · 稚趣平面志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-017"><strong>017</strong> · 稚趣平面志</a><br><sub>把照片画成粗糙黑线描边、明亮纯色平涂的韩式稚拙编辑插画。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-018"><img src="./assets/roster/018.jpg" alt="XXD Panel 018 · 手工剪纸志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-018"><strong>018</strong> · 手工剪纸志</a><br><sub>用一个剪纸主体、几层前中后纸片和一套精密小字，把照片重做成手工层叠剪纸。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-019"><img src="./assets/roster/019.jpg" alt="XXD Panel 019 · 复古平面志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-019"><strong>019</strong> · 复古平面志</a><br><sub>把照片里的主体和关系，重构成仍然认得出来的复古现代主义平面插画。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-020"><img src="./assets/roster/020.jpg" alt="XXD Panel 020 · 厚涂微景观" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-020"><strong>020</strong> · 厚涂微景观</a><br><sub>把照片里的主体和故事，做成长在一块厚涂颜料里、摸得到的立体微缩场景。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-021"><img src="./assets/roster/021.jpg" alt="XXD Panel 021 · 黑域越界" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-021"><strong>021</strong> · 黑域越界</a><br><sub>让照片主体从一块纯黑矩形里探出身来，用抖动的黑线和白色负形画成，只有黑白灰。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-022"><img src="./assets/roster/022.jpg" alt="XXD Panel 022 · 彩点越界" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-022"><strong>022</strong> · 彩点越界</a><br><sub>让照片主体用流畅线稿从一块纯黑矩形里越界而出，只在最关键的一处点上颜色。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-023"><img src="./assets/roster/023.jpg" alt="XXD Panel 023 · 东方窗景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-023"><strong>023</strong> · 东方窗景</a><br><sub>把照片放进一扇按主体挑选的中式窗里，像阳光透过窗棂落在一面浅色墙上。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-024"><img src="./assets/roster/024.jpg" alt="XXD Panel 024 · 情绪窗口" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-024"><strong>024</strong> · 情绪窗口</a><br><sub>让照片里真实的物象穿过一扇窄长的浅色几何窗口，做成一张极简的高级商业海报。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-025"><img src="./assets/roster/025.jpg" alt="XXD Panel 025 · 隐形意象" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-025"><strong>025</strong> · 隐形意象</a><br><sub>把照片做成一张一眼看见主体、第二眼才发现藏着另一幅画面的莫兰迪丝网版画。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-026"><img src="./assets/roster/026.jpg" alt="XXD Panel 026 · 几何秩序" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-026"><strong>026</strong> · 几何秩序</a><br><sub>把照片里的事实，转成安静、温和、仍能一眼认出的几何秩序。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-027"><img src="./assets/roster/027.jpg" alt="XXD Panel 027 · 纸上浮雕" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-027"><strong>027</strong> · 纸上浮雕</a><br><sub>把照片压印成一张乳白厚纸上的东方博物馆式浅浮雕，只在关键处点一点哑金。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-028"><img src="./assets/roster/028.jpg" alt="XXD Panel 028 · 等距微景观" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-028"><strong>028</strong> · 等距微景观</a><br><sub>把照片安放成一件用原图配色画出的等距纸上微缩模型，像一座小小的建筑沙盘。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-029"><img src="./assets/roster/029.jpg" alt="XXD Panel 029 · 纸上慢写" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-029"><strong>029</strong> · 纸上慢写</a><br><sub>把照片画成一块横向低饱和色块上的松弛蜡粉笔手绘，配一句随手写下的短句。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-030"><img src="./assets/roster/030.jpg" alt="XXD Panel 030 · 自然越界" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-030"><strong>030</strong> · 自然越界</a><br><sub>用真实的叶片、花瓣、枝条、果实、种子、草茎和树皮，把照片主体重新拼出来。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-031"><img src="./assets/roster/031.jpg" alt="XXD Panel 031 · 寓意拓印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-031"><strong>031</strong> · 寓意拓印</a><br><sub>先读懂照片背后的寓意，再提炼成一个几何严谨、带拓印粗粝感的核心母题。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-032"><img src="./assets/roster/032.jpg" alt="XXD Panel 032 · 图形字标" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-032"><strong>032</strong> · 图形字标</a><br><sub>把照片主体最关键的特征，做进一枚定制字标的字母结构里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-033"><img src="./assets/roster/033.jpg" alt="XXD Panel 033 · 鲜彩拼贴志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-033"><strong>033</strong> · 鲜彩拼贴志</a><br><sub>把一张照片变成鲜明、浓郁、层次清楚的现代杂志封面拼贴。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-034"><img src="./assets/roster/034.jpg" alt="XXD Panel 034 · 旅行章印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-034"><strong>034</strong> · 旅行章印</a><br><sub>把照片提炼成一枚小小的多色橡皮章，配上一段安静的田野注释。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-035"><img src="./assets/roster/035.jpg" alt="XXD Panel 035 · 积木重构" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-035"><strong>035</strong> · 积木重构</a><br><sub>把照片主体搭成一件明艳、一眼能认出来的像素积木收藏品。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-036"><img src="./assets/roster/036.jpg" alt="XXD Panel 036 · 流线绘本" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-036"><strong>036</strong> · 流线绘本</a><br><sub>用几根连续细线画出照片里的关系，让透明的色彩在纸上慢慢流动。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-037"><img src="./assets/roster/037.jpg" alt="XXD Panel 037 · 流金徽章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-037"><strong>037</strong> · 流金徽章</a><br><sub>把一段旅途的照片做成一枚可收藏的流金珐琅徽章。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-038"><img src="./assets/roster/038.jpg" alt="XXD Panel 038 · 纺织生活志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-038"><strong>038</strong> · 纺织生活志</a><br><sub>把照片和它没说出口的情绪，缝成一幅温暖的手工拼布贴画。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-039"><img src="./assets/roster/039.jpg" alt="XXD Panel 039 · 刺绣意象" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-039"><strong>039</strong> · 刺绣意象</a><br><sub>从照片里只挑一个最值得留下的意象，绣进一片灵动的丝光里。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-040"><img src="./assets/roster/040.jpg" alt="XXD Panel 040 · 涂鸦同伴" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-040"><strong>040</strong> · 涂鸦同伴</a><br><sub>留下照片里最值得记住的真实主体，让几个黑线小人围着它演一场小戏。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-041"><img src="./assets/roster/041.jpg" alt="XXD Panel 041 · 等距研究室" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-041"><strong>041</strong> · 等距研究室</a><br><sub>把照片主体和一个来自照片的主题隐喻，搭成一张清透的等距研究图。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-042"><img src="./assets/roster/042.jpg" alt="XXD Panel 042 · 解构水彩志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-042"><strong>042</strong> · 解构水彩志</a><br><sub>沿着真实结构把照片主体分层展开，画成一张能重新组装的水彩研究图。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-043"><img src="./assets/roster/043.jpg" alt="XXD Panel 043 · 白色泡沫" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-043"><strong>043</strong> · 白色泡沫</a><br><sub>用真实的白色皂沫，在一块深色湿润的平面上重新描出照片主体。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-044"><img src="./assets/roster/044.jpg" alt="XXD Panel 044 · 平面纯金" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-044"><strong>044</strong> · 平面纯金</a><br><sub>把照片主体最关键的形态，压成深色底面上的一层薄薄纯金。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-045"><img src="./assets/roster/045.jpg" alt="XXD Panel 045 · 治愈积木城" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-045"><strong>045</strong> · 治愈积木城</a><br><sub>把照片主体重新搭成一件圆润、可触、颜色温柔的积木雕塑。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-046"><img src="./assets/roster/046.jpg" alt="XXD Panel 046 · 厚涂微世界" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-046"><strong>046</strong> · 厚涂微世界</a><br><sub>把照片重构成一座明亮、鲜活、摸得到颜料厚度的厚涂微景观。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-047"><img src="./assets/roster/047.jpg" alt="XXD Panel 047 · 等距厚涂景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-047"><strong>047</strong> · 等距厚涂景</a><br><sub>让照片主体变成一件精致的轴测微缩模型，站进一块有生命的厚涂色域。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-048"><img src="./assets/roster/048.jpg" alt="XXD Panel 048 · 透明结构志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-048"><strong>048</strong> · 透明结构志</a><br><sub>让照片主体变得半透明，把它的结构逻辑画成一张清透的蓝图。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-049"><img src="./assets/roster/049.jpg" alt="XXD Panel 049 · 木刻印记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-049"><strong>049</strong> · 木刻印记</a><br><sub>把照片里最动人的那部分，刻成一枚清新柔和的限色木刻版画。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-050"><img src="./assets/roster/050.jpg" alt="XXD Panel 050 · 旅行明信片" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-050"><strong>050</strong> · 旅行明信片</a><br><sub>把每张照片画成一张为它量身定制的空气蓝极简旅行海报。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>051–100</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-051"><img src="./assets/roster/051.jpg" alt="XXD Panel 051 · 手作微缩岛" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-051"><strong>051</strong> · 手作微缩岛</a><br><sub>把照片主体做成一件轻盈可触的手工纸艺微缩模型。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-052"><img src="./assets/roster/052.jpg" alt="XXD Panel 052 · 纸艺微缩岛" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-052"><strong>052</strong> · 纸艺微缩岛</a><br><sub>让照片里的世界变成手工纸艺微缩场景，轻轻悬浮在一条风景线上。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-053"><img src="./assets/roster/053.jpg" alt="XXD Panel 053 · 钢笔淡彩录" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-053"><strong>053</strong> · 钢笔淡彩录</a><br><sub>用观察式的钢笔线条和几处淡彩记下照片，在最恰当的地方停笔。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-054"><img src="./assets/roster/054.jpg" alt="XXD Panel 054 · 记忆贴纸册" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-054"><strong>054</strong> · 记忆贴纸册</a><br><sub>把一段记忆拆成一张主视觉和六枚大小不一的贴纸碎片。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-055"><img src="./assets/roster/055.jpg" alt="XXD Panel 055 · 绘画记忆场" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-055"><strong>055</strong> · 绘画记忆场</a><br><sub>把照片里的一束光、一个动作和一种空间关系，画成一幅温柔的绘画。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-056"><img src="./assets/roster/056.jpg" alt="XXD Panel 056 · 留白记忆画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-056"><strong>056</strong> · 留白记忆画</a><br><sub>只留下照片里一个核心意象，在巨大留白里用稚拙笔触和暖冷跳色重新画出来。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-057"><img src="./assets/roster/057.jpg" alt="XXD Panel 057 · 几何记忆场" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-057"><strong>057</strong> · 几何记忆场</a><br><sub>用几何块面和有秩序的马赛克，把照片重组成一幅安静而温暖的现代拼贴。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-058"><img src="./assets/roster/058.jpg" alt="XXD Panel 058 · 诗意观念景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-058"><strong>058</strong> · 诗意观念景</a><br><sub>读懂照片在暗示什么，用严谨的几何把它搭成一幅诗意的观念景观。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-059"><img src="./assets/roster/059.jpg" alt="XXD Panel 059 · 手绘寓言录" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-059"><strong>059</strong> · 手绘寓言录</a><br><sub>把照片里没说出口的故事，画成一页温暖、童真又聪明的寓言绘本。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-060"><img src="./assets/roster/060.jpg" alt="XXD Panel 060 · 禅意极简诗" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-060"><strong>060</strong> · 禅意极简诗</a><br><sub>用一到三个黑色形体和巨大的留白，把照片提炼成一页安静而有回声的视觉哲思。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-061"><img src="./assets/roster/061.jpg" alt="XXD Panel 061 · 视觉记忆簿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-061"><strong>061</strong> · 视觉记忆簿</a><br><sub>把照片重组成几块散落在纸面上、彼此呼应的视觉记忆片段。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-062"><img src="./assets/roster/062.jpg" alt="XXD Panel 062 · 聪明笨拙线" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-062"><strong>062</strong> · 聪明笨拙线</a><br><sub>用稚拙黑线和一枚原照片里的颜色，画出照片里最值得记住的瞬间。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-063"><img src="./assets/roster/063.jpg" alt="XXD Panel 063 · 像素隐喻志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-063"><strong>063</strong> · 像素隐喻志</a><br><sub>把照片重组成一个像素大轮廓和几块柔和色块之间的小小隐喻。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-064"><img src="./assets/roster/064.jpg" alt="XXD Panel 064 · 独立拼贴页" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-064"><strong>064</strong> · 独立拼贴页</a><br><sub>把照片变成一页安静、残缺、带时间感的旧纸拼贴档案。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-065"><img src="./assets/roster/065.jpg" alt="XXD Panel 065 · 双线编辑志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-065"><strong>065</strong> · 双线编辑志</a><br><sub>用一根黑线搭骨架，再用照片里的两种颜色画出错位套色的手绘线稿。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-066"><img src="./assets/roster/066.jpg" alt="XXD Panel 066 · 童真叙事线" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-066"><strong>066</strong> · 童真叙事线</a><br><sub>用松弛的黑线和柔和平涂色，把照片里的动作和关系画成一个童真小故事。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-067"><img src="./assets/roster/067.jpg" alt="XXD Panel 067 · 日常幽默画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-067"><strong>067</strong> · 日常幽默画</a><br><sub>只用红蓝两色手绘墨，把照片里的一个有趣瞬间记成一页私人观察笔记。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-068"><img src="./assets/roster/068.jpg" alt="XXD Panel 068 · 东方写意册" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-068"><strong>068</strong> · 东方写意册</a><br><sub>用写意墨线、淡彩和大片留白，以东方的眼光重新画一张照片。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-069"><img src="./assets/roster/069.jpg" alt="XXD Panel 069 · 鲜彩涂抹窗" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-069"><strong>069</strong> · 鲜彩涂抹窗</a><br><sub>用几笔宽大的粗刷刷出一扇画窗，让照片里的主体带着鲜亮色彩从笔触里走出来。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-070"><img src="./assets/roster/070.jpg" alt="XXD Panel 070 · 厚涂治愈岛" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-070"><strong>070</strong> · 厚涂治愈岛</a><br><sub>把照片里的主体画成一座小小的明亮岛屿，安放在大片暖白里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-071"><img src="./assets/roster/071.jpg" alt="XXD Panel 071 · 粉彩诗意簿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-071"><strong>071</strong> · 粉彩诗意簿</a><br><sub>把照片化成几片漂浮在近白纸面上的粉彩记忆，配一段松弛的手写诗句。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-072"><img src="./assets/roster/072.jpg" alt="XXD Panel 072 · 明亮色彩志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-072"><strong>072</strong> · 明亮色彩志</a><br><sub>把照片抽象成一组明亮的雾面玻璃几何，有的清晰，有的朦胧。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-073"><img src="./assets/roster/073.jpg" alt="XXD Panel 073 · 几何城市志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-073"><strong>073</strong> · 几何城市志</a><br><sub>把照片重建成一座被剖开、搭着脚手架的等距微缩建筑模型。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-074"><img src="./assets/roster/074.jpg" alt="XXD Panel 074 · 情绪图标志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-074"><strong>074</strong> · 情绪图标志</a><br><sub>把照片里的主体和情绪提炼成一枚正面、哑光、有立体层次的圆角方形图标。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-075"><img src="./assets/roster/075.jpg" alt="XXD Panel 075 · 深色蜡笔稿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-075"><strong>075</strong> · 深色蜡笔稿</a><br><sub>用深色蜡笔在米白手工纸上，留下照片里最值得记住的那一笔。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-076"><img src="./assets/roster/076.jpg" alt="XXD Panel 076 · 马卡龙蜡笔" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-076"><strong>076</strong> · 马卡龙蜡笔</a><br><sub>用粗粝的深色蜡笔和明亮的马卡龙色块，把照片画成一段有人情味的旅行记忆。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-077"><img src="./assets/roster/077.jpg" alt="XXD Panel 077 · 旅行杂志画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-077"><strong>077</strong> · 旅行杂志画</a><br><sub>把照片做成一页有纸张层次、柔和投影和英文排版的纸雕旅行杂志。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-078"><img src="./assets/roster/078.jpg" alt="XXD Panel 078 · 金箔压印志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-078"><strong>078</strong> · 金箔压印志</a><br><sub>把照片最关键的轮廓画成细线，用香槟金箔深深压进暖米白棉纸里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-079"><img src="./assets/roster/079.jpg" alt="XXD Panel 079 · 钢笔淡彩志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-079"><strong>079</strong> · 钢笔淡彩志</a><br><sub>用几何直线、自由墨线和几处淡彩，把照片画成一页像在现场画到一半的速写。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-080"><img src="./assets/roster/080.jpg" alt="XXD Panel 080 · 有机水粉场" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-080"><strong>080</strong> · 有机水粉场</a><br><sub>用柔软的有机形状和植物色水粉，把照片的情绪和一个小小隐喻放进大片留白里。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-081"><img src="./assets/roster/081.jpg" alt="XXD Panel 081 · 彩线纪念册" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-081"><strong>081</strong> · 彩线纪念册</a><br><sub>用两到四种照片里的颜色画等粗单线，把照片变成一张限色印刷的私人纪念海报。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-082"><img src="./assets/roster/082.jpg" alt="XXD Panel 082 · 水彩跃出纸" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-082"><strong>082</strong> · 水彩跃出纸</a><br><sub>让照片里唯一的主角带着稚拙的立体感，从一片不规则水彩里站起来。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-083"><img src="./assets/roster/083.jpg" alt="XXD Panel 083 · 丑萌角色志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-083"><strong>083</strong> · 丑萌角色志</a><br><sub>只留下照片里一个主体，把它最好笑的那点性格故意画丑、画笨，但一眼认得出。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-084"><img src="./assets/roster/084.jpg" alt="XXD Panel 084 · 点描线构志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-084"><strong>084</strong> · 点描线构志</a><br><sub>用几何细线和疏密不一的小点，把照片画成一篇安静的城市随笔。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-085"><img src="./assets/roster/085.jpg" alt="XXD Panel 085 · 手作模型志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-085"><strong>085</strong> · 手作模型志</a><br><sub>用黏土、毛毡、手剪纸和线绳，把照片搭成大片留白里一座小小的手工舞台。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-086"><img src="./assets/roster/086.jpg" alt="XXD Panel 086 · 留白版画志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-086"><strong>086</strong> · 留白版画志</a><br><sub>只留下照片里三到五个关键信息，压成一幅留白先行的限色丝网版画。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-087"><img src="./assets/roster/087.jpg" alt="XXD Panel 087 · 红线关系图" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-087"><strong>087</strong> · 红线关系图</a><br><sub>把照片拆成一枚枚图钉，用朱红线绳连成一张看得见的关系地图。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-088"><img src="./assets/roster/088.jpg" alt="XXD Panel 088 · 文字造型诗" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-088"><strong>088</strong> · 文字造型诗</a><br><sub>用文字、标点和点阵把照片里的主体拼出来，远看是图，近看全是字。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-089"><img src="./assets/roster/089.jpg" alt="XXD Panel 089 · 生活小品簿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-089"><strong>089</strong> · 生活小品簿</a><br><sub>把照片拆成一个主角和几片生活小碎片，排成一页松弛的私人手账。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-090"><img src="./assets/roster/090.jpg" alt="XXD Panel 090 · 视觉思维图" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-090"><strong>090</strong> · 视觉思维图</a><br><sub>不画照片里的东西，而是把它背后的关系和意义画成一张视觉思维地图。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-091"><img src="./assets/roster/091.jpg" alt="XXD Panel 091 · 蓝线旅行册" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-091"><strong>091</strong> · 蓝线旅行册</a><br><sub>只用一支蓝笔，把照片画成一页观察到足够就停笔的旅行速写。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-092"><img src="./assets/roster/092.jpg" alt="XXD Panel 092 · 表现线描志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-092"><strong>092</strong> · 表现线描志</a><br><sub>把照片画成松散轮廓、多种排线和大片留白的黑白钢笔线描。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-093"><img src="./assets/roster/093.jpg" alt="XXD Panel 093 · 现代几何画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-093"><strong>093</strong> · 现代几何画</a><br><sub>把照片压缩成明亮、哑光、边缘略带手感的现代主义几何色块。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-094"><img src="./assets/roster/094.jpg" alt="XXD Panel 094 · 古典双色书" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-094"><strong>094</strong> · 古典双色书</a><br><sub>把照片画成一页细墨线、一种专色和大片留白的旧书插图。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-095"><img src="./assets/roster/095.jpg" alt="XXD Panel 095 · 红黑图解志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-095"><strong>095</strong> · 红黑图解志</a><br><sub>用黑色技术细线、红色专色和几张小图解，把照片里的东西讲清楚。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-096"><img src="./assets/roster/096.jpg" alt="XXD Panel 096 · 民间通信卡" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-096"><strong>096</strong> · 民间通信卡</a><br><sub>把照片变成一张像真的被打字、复印、寄出过的老式 QSL 通信卡。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-097"><img src="./assets/roster/097.jpg" alt="XXD Panel 097 · 复古说明卡" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-097"><strong>097</strong> · 复古说明卡</a><br><sub>把照片压缩成一张有用、有点好笑、像老说明卡的双色图解。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-098"><img src="./assets/roster/098.jpg" alt="XXD Panel 098 · 稚拙水彩书" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-098"><strong>098</strong> · 稚拙水彩书</a><br><sub>把照片重新讲成一页明亮、松弛、故意不完美的绘本插画。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-099"><img src="./assets/roster/099.jpg" alt="XXD Panel 099 · 字体吉祥物" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-099"><strong>099</strong> · 字体吉祥物</a><br><sub>把照片里的主角设计成一个好记的吉祥物，配一行超大字做背景。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-100"><img src="./assets/roster/100.jpg" alt="XXD Panel 100 · 民艺叙事画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-100"><strong>100</strong> · 民艺叙事画</a><br><sub>把照片讲成一个有蜡笔颗粒、有生活感的稚拙民艺小故事。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>101–150</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-101"><img src="./assets/roster/101.jpg" alt="XXD Panel 101 · 九宫记忆簿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-101"><strong>101</strong> · 九宫记忆簿</a><br><sub>把一张照片拆成九个值得记住的小涂鸦，排成一页私人手帐。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-102"><img src="./assets/roster/102.jpg" alt="XXD Panel 102 · 治愈几何志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-102"><strong>102</strong> · 治愈几何志</a><br><sub>把照片提炼成一枚清透、安静、带点生命力的几何图形。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-103"><img src="./assets/roster/103.jpg" alt="XXD Panel 103 · 鲜彩抽象拼" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-103"><strong>103</strong> · 鲜彩抽象拼</a><br><sub>把照片拆成鲜亮的大色块和粗糙手绘线，重新拼成一幅抽象画。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-104"><img src="./assets/roster/104.jpg" alt="XXD Panel 104 · 网点禅意志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-104"><strong>104</strong> · 网点禅意志</a><br><sub>把照片提炼成网点组成的形体、几道彩色线条和安静的留白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-105"><img src="./assets/roster/105.jpg" alt="XXD Panel 105 · 诗意留白集" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-105"><strong>105</strong> · 诗意留白集</a><br><sub>只挑出照片里最美的一幕，做成一张安静的极简纸片拼贴。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-106"><img src="./assets/roster/106.jpg" alt="XXD Panel 106 · 柔彩像素记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-106"><strong>106</strong> · 柔彩像素记</a><br><sub>把照片删到只剩两三个关键形状，再用柔和的粉彩像素重新记住它。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-107"><img src="./assets/roster/107.jpg" alt="XXD Panel 107 · 图像替词诗" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-107"><strong>107</strong> · 图像替词诗</a><br><sub>把照片里的花、窗、路和风画成小图，替换句子里的词，拼成一句能读懂的短诗。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-108"><img src="./assets/roster/108.jpg" alt="XXD Panel 108 · 新民艺剪纸志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-108"><strong>108</strong> · 新民艺剪纸志</a><br><sub>把照片里最好认的形状，剪成一枚安静、有民艺味的彩纸拼贴。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-109"><img src="./assets/roster/109.jpg" alt="XXD Panel 109 · 柔和几何解构志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-109"><strong>109</strong> · 柔和几何解构志</a><br><sub>把照片拆成几块完整的大方块，再用柔和的颜色拼回一个好认的形象。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-110"><img src="./assets/roster/110.jpg" alt="XXD Panel 110 · 日系生活场景图鉴" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-110"><strong>110</strong> · 日系生活场景图鉴</a><br><sub>把照片里值得记住的小物，整理成一张有路线、有留白的生活地图。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-111"><img src="./assets/roster/111.jpg" alt="XXD Panel 111 · 纺织拼贴志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-111"><strong>111</strong> · 纺织拼贴志</a><br><sub>把照片里最值得记住的关系，缝成一枚有温度的布艺拼贴。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-112"><img src="./assets/roster/112.jpg" alt="XXD Panel 112 · 金线纸本志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-112"><strong>112</strong> · 金线纸本志</a><br><sub>让一条不规整的纸面色块，托住一枚安静、带一点金光的小小记忆。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-113"><img src="./assets/roster/113.jpg" alt="XXD Panel 113 · 贝壳像素留白志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-113"><strong>113</strong> · 贝壳像素留白志</a><br><sub>用不到两百块贝壳方片拼出照片的主体，让边缘慢慢散进留白里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-114"><img src="./assets/roster/114.jpg" alt="XXD Panel 114 · 复古粉彩手账涂鸦" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-114"><strong>114</strong> · 复古粉彩手账涂鸦</a><br><sub>把照片重新画成一页带纸张呼吸感的粉彩手账涂鸦拼贴。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-115"><img src="./assets/roster/115.jpg" alt="XXD Panel 115 · 粉彩章印拼贴志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-115"><strong>115</strong> · 粉彩章印拼贴志</a><br><sub>把照片的核心记忆，画成复古纸上一枚粉彩涂鸦小章印。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-116"><img src="./assets/roster/116.jpg" alt="XXD Panel 116 · 浅纸粉彩涂鸦志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-116"><strong>116</strong> · 浅纸粉彩涂鸦志</a><br><sub>在一张很浅的纸上，用粗颗粒彩色蜡笔线留下照片清楚的轮廓。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-117"><img src="./assets/roster/117.jpg" alt="XXD Panel 117 · 细线淡彩留白志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-117"><strong>117</strong> · 细线淡彩留白志</a><br><sub>抓住照片里的一个视觉锚点，用细线和淡彩重新安排一张留白很多的画。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-118"><img src="./assets/roster/118.jpg" alt="XXD Panel 118 · 石墨留白素描志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-118"><strong>118</strong> · 石墨留白素描志</a><br><sub>留下照片里值得记住的关系，用铅笔和大片留白重新构图。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-119"><img src="./assets/roster/119.jpg" alt="XXD Panel 119 · 手缝布艺留白志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-119"><strong>119</strong> · 手缝布艺留白志</a><br><sub>让少数几块布片和针迹，留下照片里最温暖的那一点记忆。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-120"><img src="./assets/roster/120.jpg" alt="XXD Panel 120 · 建筑概念手绘志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-120"><strong>120</strong> · 建筑概念手绘志</a><br><sub>把照片里的空间记忆，变成一张留白充分的建筑概念草图。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-121"><img src="./assets/roster/121.jpg" alt="XXD Panel 121 · 生活涂鸦编排志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-121"><strong>121</strong> · 生活涂鸦编排志</a><br><sub>把日常照片里的一点情绪，画成留白充足、图文搭配聪明的生活插画。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-122"><img src="./assets/roster/122.jpg" alt="XXD Panel 122 · 单色网点手写志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-122"><strong>122</strong> · 单色网点手写志</a><br><sub>把照片的主体变成黑灰网点印出来的小图，旁边只留一行红色手写。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-123"><img src="./assets/roster/123.jpg" alt="XXD Panel 123 · 红蓝角线彩铅志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-123"><strong>123</strong> · 红蓝角线彩铅志</a><br><sub>用红蓝两支彩铅和带棱角的线条，把照片主体重新画成一张小而有张力的手绘。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-124"><img src="./assets/roster/124.jpg" alt="XXD Panel 124 · 布艺拼贴留白志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-124"><strong>124</strong> · 布艺拼贴留白志</a><br><sub>用几块大布片和几道针脚，把照片的主体拼成一张温暖的贴布小画。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-125"><img src="./assets/roster/125.jpg" alt="XXD Panel 125 · 蜡笔童趣留白志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-125"><strong>125</strong> · 蜡笔童趣留白志</a><br><sub>用稚拙的蜡笔和油画棒，把照片的主体画成一枚带亮色点睛的绘本小图。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-126"><img src="./assets/roster/126.jpg" alt="XXD Panel 126 · 诗意微缩拼贴志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-126"><strong>126</strong> · 诗意微缩拼贴志</a><br><sub>把照片缩成一枚邮戳大小的水彩撕纸拼贴，安放在大片手工纸留白里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-127"><img src="./assets/roster/127.jpg" alt="XXD Panel 127 · 建筑混媒拼贴志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-127"><strong>127</strong> · 建筑混媒拼贴志</a><br><sub>把照片做成一张像建筑师研究笔记的小型拼贴，带几条结构线和手写批注。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-128"><img src="./assets/roster/128.jpg" alt="XXD Panel 128 · 珐琅徽章旅行志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-128"><strong>128</strong> · 珐琅徽章旅行志</a><br><sub>把照片压进一枚圆形珐琅纪念章，配几行优雅衬线字，像一张极简旅行海报。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-129"><img src="./assets/roster/129.jpg" alt="XXD Panel 129 · 东方弥散留白志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-129"><strong>129</strong> · 东方弥散留白志</a><br><sub>把照片化成一个东方剪影符号，配一大块边缘柔化发光的纯色几何。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-130"><img src="./assets/roster/130.jpg" alt="XXD Panel 130 · 硬边几何切面志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-130"><strong>130</strong> · 硬边几何切面志</a><br><sub>把照片的主体切成黑白灰的硬边几何块面，再插进一两块强调色。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-131"><img src="./assets/roster/131.jpg" alt="XXD Panel 131 · 摄影涂鸦拼贴志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-131"><strong>131</strong> · 摄影涂鸦拼贴志</a><br><sub>把照片剪成一小簇碎片贴在白纸上，再随手画上黑框和几个涂鸦。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-132"><img src="./assets/roster/132.jpg" alt="XXD Panel 132 · 钢笔淡彩旅行志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-132"><strong>132</strong> · 钢笔淡彩旅行志</a><br><sub>用带手抖的钢笔线和几笔暖色淡彩，把照片画成一张邮戳大小的城市速写。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-133"><img src="./assets/roster/133.jpg" alt="XXD Panel 133 · 点刻透明套印志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-133"><strong>133</strong> · 点刻透明套印志</a><br><sub>用几层同色半透明形状层层套印照片主体，叠得越多颜色越深，再用细点刻出体积。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-134"><img src="./assets/roster/134.jpg" alt="XXD Panel 134 · 绘本色域叙事志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-134"><strong>134</strong> · 绘本色域叙事志</a><br><sub>上方大片留白，中间一个小小的故事主体，底下一整片混色色块，像一页绘本。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-135"><img src="./assets/roster/135.jpg" alt="XXD Panel 135 · 街头专色手绘志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-135"><strong>135</strong> · 街头专色手绘志</a><br><sub>用粗粝的手绘线、几种撞色专色和印刷颗粒，把照片做成一张街头小志海报。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-136"><img src="./assets/roster/136.jpg" alt="XXD Panel 136 · 诗意超现实留白志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-136"><strong>136</strong> · 诗意超现实留白志</a><br><sub>把照片改写成一幅稚拙的超现实布面小画，留下一个荒诞又准确的画面关系。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-137"><img src="./assets/roster/137.jpg" alt="XXD Panel 137 · 蚀刻肌理拼贴志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-137"><strong>137</strong> · 蚀刻肌理拼贴志</a><br><sub>用纤细的蚀刻线画出一个极小的主体，再叠上一两块粗粝的印刷色块。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-138"><img src="./assets/roster/138.jpg" alt="XXD Panel 138 · 东方纸艺浮雕志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-138"><strong>138</strong> · 东方纸艺浮雕志</a><br><sub>用手工棉纸的褶皱、压凸和切层，把照片做成白纸上一枚小小的浅浮雕。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-139"><img src="./assets/roster/139.jpg" alt="XXD Panel 139 · 文字编码线场志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-139"><strong>139</strong> · 文字编码线场志</a><br><sub>把照片编码成一小片极细的横竖线场，远看是抽象结构，近看才隐约认出原物。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-140"><img src="./assets/roster/140.jpg" alt="XXD Panel 140 · 干性手绘视觉岛" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-140"><strong>140</strong> · 干性手绘视觉岛</a><br><sub>把照片提炼成白纸中央一小块水粉油画棒画，像被珍藏的一段记忆。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-141"><img src="./assets/roster/141.jpg" alt="XXD Panel 141 · 极简手绘线描志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-141"><strong>141</strong> · 极简手绘线描志</a><br><sub>用几根纤细、略带抖动的手绘线勾出照片的主体，周围几乎全是留白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-142"><img src="./assets/roster/142.jpg" alt="XXD Panel 142 · 字形蒙版融合志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-142"><strong>142</strong> · 字形蒙版融合志</a><br><sub>从照片里提炼一个词，把主体嵌进拉长延展的字形里，让字和图合成一体。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-143"><img src="./assets/roster/143.jpg" alt="XXD Panel 143 · 文字造型视觉诗" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-143"><strong>143</strong> · 文字造型视觉诗</a><br><sub>用从照片里提炼的文字拼出主体的轮廓和明暗，远看是图，近看全是字。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-144"><img src="./assets/roster/144.jpg" alt="XXD Panel 144 · 几何反白破框志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-144"><strong>144</strong> · 几何反白破框志</a><br><sub>用细线描和一块几何色块重画照片主体，进入色块处反白，越出边框处变回线条。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-145"><img src="./assets/roster/145.jpg" alt="XXD Panel 145 · 复古限色版画志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-145"><strong>145</strong> · 复古限色版画志</a><br><sub>用雕版式排线、点描和网点，把照片印成一幅几种专色套印的复古小景。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-146"><img src="./assets/roster/146.jpg" alt="XXD Panel 146 · 博物学丝巾印花志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-146"><strong>146</strong> · 博物学丝巾印花志</a><br><sub>用精细刻线和几种明快平涂色，把照片主体画成丝巾印花般的博物学小图案。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-147"><img src="./assets/roster/147.jpg" alt="XXD Panel 147 · 便当食材包装志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-147"><strong>147</strong> · 便当食材包装志</a><br><sub>把照片里的一切换成食材，装进一个透明便利店熟食盒，拍成俯视商品照。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-148"><img src="./assets/roster/148.jpg" alt="XXD Panel 148 · 视觉日记拼贴志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-148"><strong>148</strong> · 视觉日记拼贴志</a><br><sub>用照片碎片、便签、胶带、票据和手写，把照片拼成一页留白很多的私人日记。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-149"><img src="./assets/roster/149.jpg" alt="XXD Panel 149 · 手绘肌理扁平志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-149"><strong>149</strong> · 手绘肌理扁平志</a><br><sub>用带纸纹和粉蜡笔颗粒的大色块，像剪纸拼贴一样把照片主体重新拼出来。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-150"><img src="./assets/roster/150.jpg" alt="XXD Panel 150 · 复古现代剪纸志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-150"><strong>150</strong> · 复古现代剪纸志</a><br><sub>用几张彩纸剪出的剪影和几何、有机形，把照片做成一幅中世纪现代风的剪纸小画。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>151–200</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-151"><img src="./assets/roster/151.jpg" alt="XXD Panel 151 · 稚拙扁平手绘志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-151"><strong>151</strong> · 稚拙扁平手绘志</a><br><sub>用平涂色块和歪歪扭扭的手绘线，只画出照片里最有性格的那一部分。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-152"><img src="./assets/roster/152.jpg" alt="XXD Panel 152 · 色场基座纸艺志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-152"><strong>152</strong> · 色场基座纸艺志</a><br><sub>把照片主体剪成几片纸，拼贴在一条横贯底部的纯色色带上。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-153"><img src="./assets/roster/153.jpg" alt="XXD Panel 153 · 单色手帐涂鸦志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-153"><strong>153</strong> · 单色手帐涂鸦志</a><br><sub>像用一支绿色水笔在方格纸上随手画下照片里的主角。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-154"><img src="./assets/roster/154.jpg" alt="XXD Panel 154 · 复古像素留白志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-154"><strong>154</strong> · 复古像素留白志</a><br><sub>把照片主角做成一枚 16-bit 风格的复古像素小图，留出大片空白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-155"><img src="./assets/roster/155.jpg" alt="XXD Panel 155 · 一点透视淡彩志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-155"><strong>155</strong> · 一点透视淡彩志</a><br><sub>把照片画成一张一点透视的钢笔线稿，再轻轻铺一层极淡的水彩。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-156"><img src="./assets/roster/156.jpg" alt="XXD Panel 156 · 双色错版插画志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-156"><strong>156</strong> · 双色错版插画志</a><br><sub>只用两种油墨，把照片主角印成一张带点套印错位的 Risograph 风小插画。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-157"><img src="./assets/roster/157.jpg" alt="XXD Panel 157 · 文物墨拓留白志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-157"><strong>157</strong> · 文物墨拓留白志</a><br><sub>把照片主角变成一张古代石刻拓片，墨色斑驳残缺，安静地落在大片纸面上。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-158"><img src="./assets/roster/158.jpg" alt="XXD Panel 158 · 纸本综合拼贴志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-158"><strong>158</strong> · 纸本综合拼贴志</a><br><sub>用撕下的书页、报纸碎片和松散铅笔线，把照片主角拼成一小幅纸本作品。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-159"><img src="./assets/roster/159.jpg" alt="XXD Panel 159 · 字符网点实验志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-159"><strong>159</strong> · 字符网点实验志</a><br><sub>用字符、点阵和网点重新拼出照片主角，再配一个和图像咬在一起的位图标题。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-160"><img src="./assets/roster/160.jpg" alt="XXD Panel 160 · 松线淡彩留白志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-160"><strong>160</strong> · 松线淡彩留白志</a><br><sub>用松散的速写墨线和几笔透明水彩，把照片主角画成一小幅钢笔淡彩。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-161"><img src="./assets/roster/161.jpg" alt="XXD Panel 161 · 框景色场越界志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-161"><strong>161</strong> · 框景色场越界志</a><br><sub>在白纸中间刷一块手工色场当小画布，主角住在里面，又有一点探出边外。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-162"><img src="./assets/roster/162.jpg" alt="XXD Panel 162 · 白衬剪纸绘本志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-162"><strong>162</strong> · 白衬剪纸绘本志</a><br><sub>把照片主角画成蜡笔质感的童趣绘本小图，背后垫一块手剪的白纸。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-163"><img src="./assets/roster/163.jpg" alt="XXD Panel 163 · 居中纯色章印志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-163"><strong>163</strong> · 居中纯色章印志</a><br><sub>用几块干净的纯色色块，把照片主角压成一枚放在正中央的小图章。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-164"><img src="./assets/roster/164.jpg" alt="XXD Panel 164 · 水墨建筑微景志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-164"><strong>164</strong> · 水墨建筑微景志</a><br><sub>把照片化成一幅淡墨山水里的微缩建筑小景，线条像建筑师的手稿，只点一点橙色。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-165"><img src="./assets/roster/165.jpg" alt="XXD Panel 165 · 中央撕纸揭景志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-165"><strong>165</strong> · 中央撕纸揭景志</a><br><sub>在一张浅色纸正中撕开一道裂缝，照片主角用几何色块从缝里露出来。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-166"><img src="./assets/roster/166.jpg" alt="XXD Panel 166 · 等距浮雕微缩志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-166"><strong>166</strong> · 等距浮雕微缩志</a><br><sub>把照片主角做成一座等距视角的微缩模型，层层浮起，像一块低浮雕。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-167"><img src="./assets/roster/167.jpg" alt="XXD Panel 167 · 波形厚墨浮雕志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-167"><strong>167</strong> · 波形厚墨浮雕志</a><br><sub>让照片主角落在一道居中的抽象波浪上，整张像厚厚的油墨压印出来的浮雕。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-168"><img src="./assets/roster/168.jpg" alt="XXD Panel 168 · 留纸白叠刷色场志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-168"><strong>168</strong> · 留纸白叠刷色场志</a><br><sub>在白纸上层层刷出一块暖色色场，照片主角是刷色时特意留下的那片纸白。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-169"><img src="./assets/roster/169.jpg" alt="XXD Panel 169 · 暖赭小幅墨线志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-169"><strong>169</strong> · 暖赭小幅墨线志</a><br><sub>用松动的炭黑墨线和几笔赭黄淡彩，把照片主角画成一小幅孤立插图，画到重点就停笔。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-170"><img src="./assets/roster/170.jpg" alt="XXD Panel 170 · 黑锈红干笔小景志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-170"><strong>170</strong> · 黑锈红干笔小景志</a><br><sub>只用炭黑和一点锈红，几笔粗粝的蜡笔就把照片主角画成一枚极小的插图。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-171"><img src="./assets/roster/171.jpg" alt="XXD Panel 171 · 竖线微型散点志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-171"><strong>171</strong> · 竖线微型散点志</a><br><sub>在大片暖白里立几根细淡的竖线，照片里的人和物变成零星散开的小岛。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-172"><img src="./assets/roster/172.jpg" alt="XXD Panel 172 · 居中透明几何志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-172"><strong>172</strong> · 居中透明几何志</a><br><sub>照片主角小小地放在正中央，身后浮着几块淡淡的半透明几何色片。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-173"><img src="./assets/roster/173.jpg" alt="XXD Panel 173 · 象牙纸本文字微景志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-173"><strong>173</strong> · 象牙纸本文字微景志</a><br><sub>把照片压成一小块由旧书页和文字搭成的纸上微景，悬在大片暖白里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-174"><img src="./assets/roster/174.jpg" alt="XXD Panel 174 · 稚拙贴纸聚合志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-174"><strong>174</strong> · 稚拙贴纸聚合志</a><br><sub>把照片主角拆成一枚枚粗笔手绘贴纸，再在画面中心聚成一个整体。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-175"><img src="./assets/roster/175.jpg" alt="XXD Panel 175 · 琥珀透光纸雕小景志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-175"><strong>175</strong> · 琥珀透光纸雕小景志</a><br><sub>把照片做成一小件层叠的象牙色纸雕，纸层之间透出暖暖的琥珀光。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-176"><img src="./assets/roster/176.jpg" alt="XXD Panel 176 · 工笔阵盘微立体志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-176"><strong>176</strong> · 工笔阵盘微立体志</a><br><sub>让照片主角坐镇一座工笔细线画成的精密阵盘中心，层层浮起，越往外越疏。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-177"><img src="./assets/roster/177.jpg" alt="XXD Panel 177 · 异形微岛版画志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-177"><strong>177</strong> · 异形微岛版画志</a><br><sub>把照片的核心压进一座小小的异形版画岛，用墨藏青、灰橄榄绿和一点朱砂橙刻出来。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-178"><img src="./assets/roster/178.jpg" alt="XXD Panel 178 · 手账墨记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-178"><strong>178</strong> · 手账墨记</a><br><sub>把照片压成一枚用旧墨水随手画下的小记号，像旧手账角落里的一笔。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-179"><img src="./assets/roster/179.jpg" alt="XXD Panel 179 · 丝带微缩陈列志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-179"><strong>179</strong> · 丝带微缩陈列志</a><br><sub>把照片的核心做成几件微缩展品，疏疏地摆在一条漂浮的象牙色丝带上。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-180"><img src="./assets/roster/180.jpg" alt="XXD Panel 180 · 复古圆章旅行手账志" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-180"><strong>180</strong> · 复古圆章旅行手账志</a><br><sub>把照片主角和一两个环境线索刻成一枚圆形复古纪念章，盖在泛旧的象牙纸上。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-181"><img src="./assets/roster/181.jpg" alt="XXD Panel 181 · 文人彩墨写意小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-181"><strong>181</strong> · 文人彩墨写意小品</a><br><sub>以墨为骨、淡彩为辅，把照片画成一小幅留白很多的文人画小品。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-182"><img src="./assets/roster/182.jpg" alt="XXD Panel 182 · 微缩像素图形小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-182"><strong>182</strong> · 微缩像素图形小品</a><br><sub>把照片主体压缩成一枚硬边方块像素小图，安静地放在大片留白里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-183"><img src="./assets/roster/183.jpg" alt="XXD Panel 183 · 深绿角隅自然图形" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-183"><strong>183</strong> · 深绿角隅自然图形</a><br><sub>把照片主体概括成角落里的一小组自然图形，奶油底上用深绿压住一角。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-184"><img src="./assets/roster/184.jpg" alt="XXD Panel 184 · 方形生活手绘盒景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-184"><strong>184</strong> · 方形生活手绘盒景</a><br><sub>把照片里的生活细节装进一个方形小场景，用松动线稿和彩铅水彩画出来。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-185"><img src="./assets/roster/185.jpg" alt="XXD Panel 185 · 黑白浅色贴纸小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-185"><strong>185</strong> · 黑白浅色贴纸小品</a><br><sub>把照片主体画成一枚小小的黑白手绘贴纸图形，只点一处浅色。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-186"><img src="./assets/roster/186.jpg" alt="XXD Panel 186 · 柔色九宫格几何记忆" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-186"><strong>186</strong> · 柔色九宫格几何记忆</a><br><sub>把照片拆成九个记忆片段，用柔和的扁平几何色块排成一个九宫格。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-187"><img src="./assets/roster/187.jpg" alt="XXD Panel 187 · 巨型字体档案拼贴" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-187"><strong>187</strong> · 巨型字体档案拼贴</a><br><sub>把照片主体做成摄影切片加制图线稿的档案拼贴，背后压一组超大字体。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-188"><img src="./assets/roster/188.jpg" alt="XXD Panel 188 · 米金留白建筑档案" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-188"><strong>188</strong> · 米金留白建筑档案</a><br><sub>把照片主体缩成一枚小小的建筑标本，放在旧纸色留白里，配沙金色标题。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-189"><img src="./assets/roster/189.jpg" alt="XXD Panel 189 · 双框侧栏火柴盒小景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-189"><strong>189</strong> · 双框侧栏火柴盒小景</a><br><sub>把照片画成旧火柴盒标签里的一幅小插图，外有双层边框和一条窄侧栏。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-190"><img src="./assets/roster/190.jpg" alt="XXD Panel 190 · 冷主暖辅朴拙粉彩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-190"><strong>190</strong> · 冷主暖辅朴拙粉彩</a><br><sub>把照片画成一幅小小的朴拙粉彩小品，冷灰调为主，只点一点暖色。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-191"><img src="./assets/roster/191.jpg" alt="XXD Panel 191 · 毛边矩形粉彩色域" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-191"><strong>191</strong> · 毛边矩形粉彩色域</a><br><sub>把照片画进一块边缘毛化的小矩形粉彩色域，让它悬浮在大片留白里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-192"><img src="./assets/roster/192.jpg" alt="XXD Panel 192 · 复古限色图形小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-192"><strong>192</strong> · 复古限色图形小品</a><br><sub>把照片压成一枚剪影色块小图形，用二到四种复古限色印在纸上。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-193"><img src="./assets/roster/193.jpg" alt="XXD Panel 193 · 基座承托灰调水彩" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-193"><strong>193</strong> · 基座承托灰调水彩</a><br><sub>把照片画成一组放在浅色低基座上的灰调水彩小形体，四周留出大片纸面。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-194"><img src="./assets/roster/194.jpg" alt="XXD Panel 194 · 明快基座轴测体量" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-194"><strong>194</strong> · 明快基座轴测体量</a><br><sub>把照片主体做成从一块平面基座上长出来的等轴测体块模型，配色明亮。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-195"><img src="./assets/roster/195.jpg" alt="XXD Panel 195 · 一抹亮色历史蒙太奇" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-195"><strong>195</strong> · 一抹亮色历史蒙太奇</a><br><sub>把照片重新剪辑成一段黑白暖灰的档案影像蒙太奇，只留一抹原图里的亮色。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-196"><img src="./assets/roster/196.jpg" alt="XXD Panel 196 · 俯视几何抽象人物" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-196"><strong>196</strong> · 俯视几何抽象人物</a><br><sub>把照片里的人从正上方看下去，画成由圆形和胶囊形组成的扁平几何人物。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-197"><img src="./assets/roster/197.jpg" alt="XXD Panel 197 · 笼中世界新民艺" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-197"><strong>197</strong> · 笼中世界新民艺</a><br><sub>把照片的主题装进一只笼子里，用扁平温暖的新民艺手绘画成一个小世界。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-198"><img src="./assets/roster/198.jpg" alt="XXD Panel 198 · 限色失重时装拼贴" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-198"><strong>198</strong> · 限色失重时装拼贴</a><br><sub>把照片主体画成漂浮失重的概念时装插画，用拼贴、网点和限定色印出来。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-199"><img src="./assets/roster/199.jpg" alt="XXD Panel 199 · 明快留白时装拼贴" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-199"><strong>199</strong> · 明快留白时装拼贴</a><br><sub>把照片主体缩成几枚漂浮的小尺度时装插画形象，放在大片明亮的暖白里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-200"><img src="./assets/roster/200.jpg" alt="XXD Panel 200 · 蓝灰单色手绘线描" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-200"><strong>200</strong> · 蓝灰单色手绘线描</a><br><sub>只用一种蓝灰色松弛线条，把照片画成一个带草图痕迹的小小线描。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>201–250</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-201"><img src="./assets/roster/201.jpg" alt="XXD Panel 201 · 奶油手作微缩立体" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-201"><strong>201</strong> · 奶油手作微缩立体</a><br><sub>把照片主体做成一件奶油色系的手作微缩摆件，安静地放在大片留白里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-202"><img src="./assets/roster/202.jpg" alt="XXD Panel 202 · 结构主线几何线图" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-202"><strong>202</strong> · 结构主线几何线图</a><br><sub>先从照片里提炼几条结构主线，再把主体画成挂在线上的蓝灰几何线图。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-203"><img src="./assets/roster/203.jpg" alt="XXD Panel 203 · 留白厚涂明信片" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-203"><strong>203</strong> · 留白厚涂明信片</a><br><sub>把照片画成一枚厚涂油画小景，落在大片留白里，像一张艺术明信片。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-204"><img src="./assets/roster/204.jpg" alt="XXD Panel 204 · 柔焦光影记忆小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-204"><strong>204</strong> · 柔焦光影记忆小品</a><br><sub>把照片主体化成一小块柔焦的光影和模糊剪影，像一段被光留下的记忆。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-205"><img src="./assets/roster/205.jpg" alt="XXD Panel 205 · 暖调有机形摄影拼贴" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-205"><strong>205</strong> · 暖调有机形摄影拼贴</a><br><sub>把照片裁成一块圆润的有机形，叠上纤细的手绘线稿，配暖调和一点陶土橘。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-206"><img src="./assets/roster/206.jpg" alt="XXD Panel 206 · 柔色纸雕微缩小景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-206"><strong>206</strong> · 柔色纸雕微缩小景</a><br><sub>把照片主体做成一层层纸片叠成的浅浮雕小景，用柔和的纸色和大片留白。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-207"><img src="./assets/roster/207.jpg" alt="XXD Panel 207 · 浅蓝白混合媒介插页" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-207"><strong>207</strong> · 浅蓝白混合媒介插页</a><br><sub>把照片做成居中的一小块照片加线稿拼贴，像浅蓝白底上的一页杂志插页。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-208"><img src="./assets/roster/208.jpg" alt="XXD Panel 208 · 蓝粉现代主义抽象" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-208"><strong>208</strong> · 蓝粉现代主义抽象</a><br><sub>把照片提炼成一小团蓝粉色块和黑色线纹组成的现代主义抽象图形。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-209"><img src="./assets/roster/209.jpg" alt="XXD Panel 209 · 极简纸张影像档案" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-209"><strong>209</strong> · 极简纸张影像档案</a><br><sub>把照片压成纸面上的一小块图像，配几行档案式小字，像一页被认真保存的摄影书。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-210"><img src="./assets/roster/210.jpg" alt="XXD Panel 210 · 冷调轻量概念拼贴" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-210"><strong>210</strong> · 冷调轻量概念拼贴</a><br><sub>把照片主体缩成一小块摄影拼贴，配上冷蓝色的手绘线条、小气泡和符号。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-211"><img src="./assets/roster/211.jpg" alt="XXD Panel 211 · 语义配色几何小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-211"><strong>211</strong> · 语义配色几何小品</a><br><sub>把照片压成一枚几何色块小图形，颜色按主体的身份、材质或季节来选。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-212"><img src="./assets/roster/212.jpg" alt="XXD Panel 212 · 近单色概念形体模型" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-212"><strong>212</strong> · 近单色概念形体模型</a><br><sub>把照片主体收成一件悬在大片空白里的小型白色概念模型。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-213"><img src="./assets/roster/213.jpg" alt="XXD Panel 213 · 暖纸冷色观念线稿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-213"><strong>213</strong> · 暖纸冷色观念线稿</a><br><sub>把照片里的情绪和关系，收成暖旧纸上一枚冷色单线的诗意小品。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-214"><img src="./assets/roster/214.jpg" alt="XXD Panel 214 · 真实固有色粗粝剪纸" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-214"><strong>214</strong> · 真实固有色粗粝剪纸</a><br><sub>把照片收成大片白纸上一小块保留真实颜色的粗糙剪纸小插图。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-215"><img src="./assets/roster/215.jpg" alt="XXD Panel 215 · 灰阶赭黄极简轴测" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-215"><strong>215</strong> · 灰阶赭黄极简轴测</a><br><sub>把照片主体画成一枚白灰色的精密轴测图解小品，只点一处赭黄。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-216"><img src="./assets/roster/216.jpg" alt="XXD Panel 216 · 九成留白单色视觉岛" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-216"><strong>216</strong> · 九成留白单色视觉岛</a><br><sub>把照片压成一大片暖色纸面上一个极小的单色印刷图像块。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-217"><img src="./assets/roster/217.jpg" alt="XXD Panel 217 · 明快数码混合媒介拼贴" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-217"><strong>217</strong> · 明快数码混合媒介拼贴</a><br><sub>把照片主体抠出来，配上手绘涂鸦和纸片，拼成一张明快的杂志拼贴。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-218"><img src="./assets/roster/218.jpg" alt="XXD Panel 218 · 极简绘本羊毛毡插画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-218"><strong>218</strong> · 极简绘本羊毛毡插画</a><br><sub>把照片概括成一小幅极简绘本画，再用柔软的手工羊毛毡做出来。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-219"><img src="./assets/roster/219.jpg" alt="XXD Panel 219 · 彩铅点染旅行手帐线稿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-219"><strong>219</strong> · 彩铅点染旅行手帐线稿</a><br><sub>把照片画成一页旅行手帐里的黑色速写，只用彩铅点几处颜色。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-220"><img src="./assets/roster/220.jpg" alt="XXD Panel 220 · 圆润稚拙手绘涂鸦小品" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-220"><strong>220</strong> · 圆润稚拙手绘涂鸦小品</a><br><sub>把照片画成一枚圆润松散、只在局部点色的可爱手绘涂鸦。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-221"><img src="./assets/roster/221.jpg" alt="XXD Panel 221 · 新中式专色版画留白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-221"><strong>221</strong> · 新中式专色版画留白</a><br><sub>把照片收成一枚章印般的小型新中式专色版画，四周是大片东方留白。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-222"><img src="./assets/roster/222.jpg" alt="XXD Panel 222 · 建筑化字体图形装置" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-222"><strong>222</strong> · 建筑化字体图形装置</a><br><sub>把照片主体变成一座由文字和几何块搭起来的小型彩色地标。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-223"><img src="./assets/roster/223.jpg" alt="XXD Panel 223 · 复古雕版微型图集" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-223"><strong>223</strong> · 复古雕版微型图集</a><br><sub>把照片拆成一组互不相连的小型雕版图形，像旧图鉴里的一页插图。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-224"><img src="./assets/roster/224.jpg" alt="XXD Panel 224 · 瓷器碎片拼合重构" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-224"><strong>224</strong> · 瓷器碎片拼合重构</a><br><sub>用中国瓷器碎片把照片主体重新拼起来，留着缺口、裂纹和大片瓷白。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-225"><img src="./assets/roster/225.jpg" alt="XXD Panel 225 · 办公物件手绘拼贴" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-225"><strong>225</strong> · 办公物件手绘拼贴</a><br><sub>用便签、回形针、胶带和纸片，把照片重新写成一页视觉日记。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-226"><img src="./assets/roster/226.jpg" alt="XXD Panel 226 · 糖霜曲奇浅浮雕" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-226"><strong>226</strong> · 糖霜曲奇浅浮雕</a><br><sub>把照片里的主体和场景，一起做成一枚哑光、圆润的糖霜曲奇小浮雕。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-227"><img src="./assets/roster/227.jpg" alt="XXD Panel 227 · 刺绣任务章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-227"><strong>227</strong> · 刺绣任务章</a><br><sub>把照片压缩成一枚带锁边、缎面绣字和简短编号的机绣任务章。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-228"><img src="./assets/roster/228.jpg" alt="XXD Panel 228 · 独立纸艺对象" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-228"><strong>228</strong> · 独立纸艺对象</a><br><sub>把照片重做成一件独立书店里能见到的手作纸品：稚拙剪纸、少量专色。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-229"><img src="./assets/roster/229.jpg" alt="XXD Panel 229 · 新民艺留白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-229"><strong>229</strong> · 新民艺留白</a><br><sub>把照片的灵魂收成一小块圆润、粉彩、安静怀旧的新民艺插画。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-230"><img src="./assets/roster/230.jpg" alt="XXD Panel 230 · 负形纪念碑" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-230"><strong>230</strong> · 负形纪念碑</a><br><sub>用密集的手绘短线把主体留成一块巨大的白色负形，旁边只站着一个极小的小人。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-231"><img src="./assets/roster/231.jpg" alt="XXD Panel 231 · 新稚拙手绘" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-231"><strong>231</strong> · 新稚拙手绘</a><br><sub>把照片收成一小块松动的彩色手绘：摇晃描边、马克笔和彩铅，四周大量留白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-232"><img src="./assets/roster/232.jpg" alt="XXD Panel 232 · 横向层状民艺" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-232"><strong>232</strong> · 横向层状民艺</a><br><sub>把照片压成一层层安静展开的横向色带风景，人物只是极小的标点。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-233"><img src="./assets/roster/233.jpg" alt="XXD Panel 233 · 簇绒纤维壁饰" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-233"><strong>233</strong> · 簇绒纤维壁饰</a><br><sub>把照片重做成几小块亮色圈绒纱线壁饰，散落在浅色纯底上。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-234"><img src="./assets/roster/234.jpg" alt="XXD Panel 234 · 数字编辑主视觉" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-234"><strong>234</strong> · 数字编辑主视觉</a><br><sub>把照片收成一张年轻的数字编辑主视觉：纯色块、圆角模块、细线和大留白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-235"><img src="./assets/roster/235.jpg" alt="XXD Panel 235 · 薄荷像素料理" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-235"><strong>235</strong> · 薄荷像素料理</a><br><sub>把照片收成一枚薄荷色梦境里的像素料理徽章：中心清楚，四周淡进白色。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-236"><img src="./assets/roster/236.jpg" alt="XXD Panel 236 · 黑白几何符号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-236"><strong>236</strong> · 黑白几何符号</a><br><sub>把照片压成正中一枚极小的黑白几何符号，四周是一整片不中断的白。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-237"><img src="./assets/roster/237.jpg" alt="XXD Panel 237 · Y2K贴纸拼贴" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-237"><strong>237</strong> · Y2K贴纸拼贴</a><br><sub>把同一主体拆成几张白边贴纸，散落在一页淡灰紫的 neo-Y2K 小志上。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-238"><img src="./assets/roster/238.jpg" alt="XXD Panel 238 · 哥特绘本微物" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-238"><strong>238</strong> · 哥特绘本微物</a><br><sub>把照片收成一个微小、脆弱、略带黑暗的水粉绘本形象，四周几乎全是空白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-239"><img src="./assets/roster/239.jpg" alt="XXD Panel 239 · 专色错版海报" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-239"><strong>239</strong> · 专色错版海报</a><br><sub>把照片做成一张专色孔版实验海报：大字当图形，网点、错版、暖白纸。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-240"><img src="./assets/roster/240.jpg" alt="XXD Panel 240 · 蜡笔视觉日记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-240"><strong>240</strong> · 蜡笔视觉日记</a><br><sub>把照片收成一页没画完的蜡笔视觉日记：小主体、暖土色、大量空白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-241"><img src="./assets/roster/241.jpg" alt="XXD Panel 241 · 标本诗学图鉴" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-241"><strong>241</strong> · 标本诗学图鉴</a><br><sub>把主体做成一页诗意标本：一部分是精密黑白照片，缺口是空白里的脆弱手绘轮廓。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-242"><img src="./assets/roster/242.jpg" alt="XXD Panel 242 · 稚拙护符插画" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-242"><strong>242</strong> · 稚拙护符插画</a><br><sub>把照片里的普通对象画成一枚居中的稚拙护符，深色哑光底上一块糖果色剪影。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-243"><img src="./assets/roster/243.jpg" alt="XXD Panel 243 · 蓝笔横线手稿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-243"><strong>243</strong> · 蓝笔横线手稿</a><br><sub>把照片画成一页蓝色圆珠笔横线笔记，排线有疏有密，画的过程都留着。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-244"><img src="./assets/roster/244.jpg" alt="XXD Panel 244 · 停笔笔记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-244"><strong>244</strong> · 停笔笔记</a><br><sub>把照片收成私人笔记本里随手的一笔：小小的主体、断续墨线、几处薄水彩。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-245"><img src="./assets/roster/245.jpg" alt="XXD Panel 245 · 记忆留白" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-245"><strong>245</strong> · 记忆留白</a><br><sub>把照片收成一页安静的记忆：圆润简化的小主体，四周是大片白纸。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-246"><img src="./assets/roster/246.jpg" alt="XXD Panel 246 · 新构成拼贴" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-246"><strong>246</strong> · 新构成拼贴</a><br><sub>把照片里的一个主体收成几何色块、结构线和大片留白组成的观念海报。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-247"><img src="./assets/roster/247.jpg" alt="XXD Panel 247 · 柔性童书" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-247"><strong>247</strong> · 柔性童书</a><br><sub>把照片里的一个形象收成彩铅水彩的童书小品，四周是大片留白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-248"><img src="./assets/roster/248.jpg" alt="XXD Panel 248 · 旧旅行手记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-248"><strong>248</strong> · 旧旅行手记</a><br><sub>不画照片里的全部，只画看过之后留下的印象：轻墨和淡水彩的一页旅行手记。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-249"><img src="./assets/roster/249.jpg" alt="XXD Panel 249 · 氛围像素" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-249"><strong>249</strong> · 氛围像素</a><br><sub>把照片里的一个瞬间压成复古游戏世界里安静的一格：低分辨率、柔和色块、大片留白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-250"><img src="./assets/roster/250.jpg" alt="XXD Panel 250 · 建筑几何诗" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-250"><strong>250</strong> · 建筑几何诗</a><br><sub>把照片里的场景收成抽象建筑轮廓、几何色块和安静的留白。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>251–300</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-251"><img src="./assets/roster/251.jpg" alt="XXD Panel 251 · 像素生命档" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-251"><strong>251</strong> · 像素生命档</a><br><sub>把照片主体压成网格上的像素生命符号，像一件被未来保存下来的自然标本。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-252"><img src="./assets/roster/252.jpg" alt="XXD Panel 252 · 治愈贴纸" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-252"><strong>252</strong> · 治愈贴纸</a><br><sub>把照片里的主体收成一枚圆润柔软的手帐小贴纸，四周是安静的留白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-253"><img src="./assets/roster/253.jpg" alt="XXD Panel 253 · 扁平钥匙" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-253"><strong>253</strong> · 扁平钥匙</a><br><sub>把照片的主题压成一个纯净色块的扁平符号，像一把有故事的视觉钥匙。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-254"><img src="./assets/roster/254.jpg" alt="XXD Panel 254 · 东方几何档" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-254"><strong>254</strong> · 东方几何档</a><br><sub>把照片主体拆成半透明的几何切片，悬在一大片空白里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-255"><img src="./assets/roster/255.jpg" alt="XXD Panel 255 · 旅行纪念邮" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-255"><strong>255</strong> · 旅行纪念邮</a><br><sub>把照片里的瞬间封进一枚小小的旅行纪念邮票，四周是大片空白纸面。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-256"><img src="./assets/roster/256.jpg" alt="XXD Panel 256 · 稚拙民艺" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-256"><strong>256</strong> · 稚拙民艺</a><br><sub>把照片收成一幅居中的稚拙民艺小画：一个主体、一种情绪、一点金箔。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-257"><img src="./assets/roster/257.jpg" alt="XXD Panel 257 · 寂静单线" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-257"><strong>257</strong> · 寂静单线</a><br><sub>把照片主体收成一根极细、不完全规则的单线，悬在大片留白里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-258"><img src="./assets/roster/258.jpg" alt="XXD Panel 258 · 奶油梦境" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-258"><strong>258</strong> · 奶油梦境</a><br><sub>把照片主体重新捏成一件极小的柔软奶油雕塑，浮在奶油色的空旷空间里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-259"><img src="./assets/roster/259.jpg" alt="XXD Panel 259 · 古典诗稿" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-259"><strong>259</strong> · 古典诗稿</a><br><sub>把照片主体画成一页不完美墨线的古典诗稿，像艺术家多年后凭记忆画下的一瞬。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-260"><img src="./assets/roster/260.jpg" alt="XXD Panel 260 · 几何记忆" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-260"><strong>260</strong> · 几何记忆</a><br><sub>把照片收成一张由几何符号组成的记忆地图，主体很小，四周大片留白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-261"><img src="./assets/roster/261.jpg" alt="XXD Panel 261 · 蜡笔记忆" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-261"><strong>261</strong> · 蜡笔记忆</a><br><sub>不画那个地方，只画它留下的感觉：彩铅和蜡笔画出的一小段记忆。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-262"><img src="./assets/roster/262.jpg" alt="XXD Panel 262 · 胶片残影" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-262"><strong>262</strong> · 胶片残影</a><br><sub>把照片主体收成一帧低饱和的旧电影残影，安静地悬在大片留白里。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-263"><img src="./assets/roster/263.jpg" alt="XXD Panel 263 · 纪念图章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-263"><strong>263</strong> · 纪念图章</a><br><sub>把照片主体收成一枚小小的纪念图章，像一件被收藏起来的文化纪念品。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-264"><img src="./assets/roster/264.jpg" alt="XXD Panel 264 · 手稿涂鸦" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-264"><strong>264</strong> · 手稿涂鸦</a><br><sub>把照片收成私人速写本里的一页天真线稿：画得不完整，但情绪很满。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-265"><img src="./assets/roster/265.jpg" alt="XXD Panel 265 · 植物徽记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-265"><strong>265</strong> · 植物徽记</a><br><sub>把照片主体收成一枚花叶围合的小徽记，像一个被保存下来的私人印记。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-266"><img src="./assets/roster/266.jpg" alt="XXD Panel 266 · 符号标识" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-266"><strong>266</strong> · 符号标识</a><br><sub>把照片主体提炼成一枚小小的极简符号，像文化机构或品牌的标识。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-267"><img src="./assets/roster/267.jpg" alt="XXD Panel 267 · 织物徽章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-267"><strong>267</strong> · 织物徽章</a><br><sub>把照片主体做成一枚小小的布艺徽章：牛仔布、缝线、拼接和毛边。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-268"><img src="./assets/roster/268.jpg" alt="XXD Panel 268 · 安静符号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-268"><strong>268</strong> · 安静符号</a><br><sub>把照片主体收成一个极小、安静、像私人收藏标记的视觉符号。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-269"><img src="./assets/roster/269.jpg" alt="XXD Panel 269 · 实验手记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-269"><strong>269</strong> · 实验手记</a><br><sub>把照片主体收成实验手册里的一个小型概念符号：墨线、网点和少量色块。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-270"><img src="./assets/roster/270.jpg" alt="XXD Panel 270 · 东方图腾" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-270"><strong>270</strong> · 东方图腾</a><br><sub>把照片主体收成一枚东方印章般的小图腾，小而庄重，四周大片留白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-271"><img src="./assets/roster/271.jpg" alt="XXD Panel 271 · 私人徽记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-271"><strong>271</strong> · 私人徽记</a><br><sub>把照片主体收成一枚民艺印刷感的私人徽记：一个轮廓、几块专色、纸上的油墨。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-272"><img src="./assets/roster/272.jpg" alt="XXD Panel 272 · 单色灵魂" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-272"><strong>272</strong> · 单色灵魂</a><br><sub>把照片主体收成一个有一点表情和脾气的黑白手绘小角色。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-273"><img src="./assets/roster/273.jpg" alt="XXD Panel 273 · 新艺术纹章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-273"><strong>273</strong> · 新艺术纹章</a><br><sub>把照片主体收成一枚新艺术风格的细线纹章，只点一种颜色。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-274"><img src="./assets/roster/274.jpg" alt="XXD Panel 274 · 夜色蜡笔" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-274"><strong>274</strong> · 夜色蜡笔</a><br><sub>在黑色纸面上，用发光般的彩色蜡笔线条把照片主体画成一枚小标志。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-275"><img src="./assets/roster/275.jpg" alt="XXD Panel 275 · 朴拙徽章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-275"><strong>275</strong> · 朴拙徽章</a><br><sub>把照片主体收成一枚圆润、略笨、像印在旧绘本里的手工小徽章。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-276"><img src="./assets/roster/276.jpg" alt="XXD Panel 276 · 空间档案" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-276"><strong>276</strong> · 空间档案</a><br><sub>把照片里的结构拆开，叠成一份极细线条的未完成空间研究。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-277"><img src="./assets/roster/277.jpg" alt="XXD Panel 277 · 几何标识" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-277"><strong>277</strong> · 几何标识</a><br><sub>把照片主体收成一个用几何剪影和扁平色块拼成的现代主义小符号。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-278"><img src="./assets/roster/278.jpg" alt="XXD Panel 278 · 文化剪影" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-278"><strong>278</strong> · 文化剪影</a><br><sub>把照片主体剪成一枚几何色块拼成、带丝网印刷感的剪纸小印章。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-279"><img src="./assets/roster/279.jpg" alt="XXD Panel 279 · 系统基因" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-279"><strong>279</strong> · 系统基因</a><br><sub>把照片主体压成一枚由几何模块、细线和小编号组成的后数字抽象标识。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-280"><img src="./assets/roster/280.jpg" alt="XXD Panel 280 · 像素标本" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-280"><strong>280</strong> · 像素标本</a><br><sub>把照片主体收成档案页上一枚低分辨率、只亮一点信号色的像素徽记。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-281"><img src="./assets/roster/281.jpg" alt="XXD Panel 281 · 象形生命" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-281"><strong>281</strong> · 象形生命</a><br><sub>把照片主体收成一个扁平、深色、面无表情却有一点生命感的小象形。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-282"><img src="./assets/roster/282.jpg" alt="XXD Panel 282 · 柔焦有机" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-282"><strong>282</strong> · 柔焦有机</a><br><sub>把照片主体柔化成一枚半透明叠层、乳白粉彩的抽象小标识。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-283"><img src="./assets/roster/283.jpg" alt="XXD Panel 283 · 时代徽章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-283"><strong>283</strong> · 时代徽章</a><br><sub>把照片主体收成一枚像被太空时代某个机构正式发行过的徽章。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-284"><img src="./assets/roster/284.jpg" alt="XXD Panel 284 · 文明徽记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-284"><strong>284</strong> · 文明徽记</a><br><sub>把照片主体放进几何框里，印成一枚冷暖对撞的微型纪念碑。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-285"><img src="./assets/roster/285.jpg" alt="XXD Panel 285 · 科学纪念章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-285"><strong>285</strong> · 科学纪念章</a><br><sub>把照片主体印成一枚粗轮廓、带网点油墨的邮票式科学纪念章。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-286"><img src="./assets/roster/286.jpg" alt="XXD Panel 286 · 粉彩图腾" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-286"><strong>286</strong> · 粉彩图腾</a><br><sub>把照片里最值得留下的一个意象，收成一枚轻盈、略带奇异感的粉彩小图腾。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-287"><img src="./assets/roster/287.jpg" alt="XXD Panel 287 · 纸上小记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-287"><strong>287</strong> · 纸上小记</a><br><sub>把照片主体收成大片空白纸上一个很小的、像被画出来的小生命。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-288"><img src="./assets/roster/288.jpg" alt="XXD Panel 288 · 典藏徽记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-288"><strong>288</strong> · 典藏徽记</a><br><sub>把照片主体收成一枚像古代学者记录过的、细刻线画在羊皮纸色上的研究徽章。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-289"><img src="./assets/roster/289.jpg" alt="XXD Panel 289 · 民艺记号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-289"><strong>289</strong> · 民艺记号</a><br><sub>把照片主体收成一枚放大了特征、像手工印出来的稚拙民艺小符号。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-290"><img src="./assets/roster/290.jpg" alt="XXD Panel 290 · 旧绘本符" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-290"><strong>290</strong> · 旧绘本符</a><br><sub>把照片主体收成旧绘本里一枚轮廓发抖、颜色褪旧的民间小符号。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-291"><img src="./assets/roster/291.jpg" alt="XXD Panel 291 · 温柔图腾" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-291"><strong>291</strong> · 温柔图腾</a><br><sub>把照片主体收成一个圆润、柔软、像童话角色标记的温柔小图腾。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-292"><img src="./assets/roster/292.jpg" alt="XXD Panel 292 · 手账灵魂" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-292"><strong>292</strong> · 手账灵魂</a><br><sub>把照片主体收成一个像凭记忆随手画下的情绪小图标，像私人手账里的标记。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-293"><img src="./assets/roster/293.jpg" alt="XXD Panel 293 · 诗意小章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-293"><strong>293</strong> · 诗意小章</a><br><sub>把照片主体压成旧纸上一枚略笨、有一点小表情的诗意小章。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-294"><img src="./assets/roster/294.jpg" alt="XXD Panel 294 · 极小私符" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-294"><strong>294</strong> · 极小私符</a><br><sub>从照片里只留下一枚极小的黑白私人符号，空白占掉绝大部分画面。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-295"><img src="./assets/roster/295.jpg" alt="XXD Panel 295 · 暖拙符号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-295"><strong>295</strong> · 暖拙符号</a><br><sub>把照片主体收成一个圆润、略失衡、暖而有点笨的私人小标志。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-296"><img src="./assets/roster/296.jpg" alt="XXD Panel 296 · 手势痕迹" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-296"><strong>296</strong> · 手势痕迹</a><br><sub>把照片主体收成一笔有速度和方向的炭笔或墨迹痕迹。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-297"><img src="./assets/roster/297.jpg" alt="XXD Panel 297 · 闭合暗号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-297"><strong>297</strong> · 闭合暗号</a><br><sub>把照片主体收成一个轮廓断开、需要看的人自己补全的视觉暗号。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-298"><img src="./assets/roster/298.jpg" alt="XXD Panel 298 · 炭笔印记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-298"><strong>298</strong> · 炭笔印记</a><br><sub>把照片主体收成一枚由炭笔、石墨和墨迹留下的半抽象小印记。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-299"><img src="./assets/roster/299.jpg" alt="XXD Panel 299 · 复印残档" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-299"><strong>299</strong> · 复印残档</a><br><sub>把照片主体收成一枚像被反复复印过、能认出却无法完全复原的黑白残档。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-300"><img src="./assets/roster/300.jpg" alt="XXD Panel 300 · 二值残印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-300"><strong>300</strong> · 二值残印</a><br><sub>只用纯黑和纯白，把照片主体从空白里挖成一枚边缘衰减的小印章。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>301–350</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-301"><img src="./assets/roster/301.jpg" alt="XXD Panel 301 · 数字遗物" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-301"><strong>301</strong> · 数字遗物</a><br><sub>把照片里最强的识别点收成一枚像旧电脑里留下来的匿名黑白数字图腾。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-302"><img src="./assets/roster/302.jpg" alt="XXD Panel 302 · 民艺新章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-302"><strong>302</strong> · 民艺新章</a><br><sub>保留原照片，把主体收成一枚温暖、有点幽默的新稚拙手工徽章。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-303"><img src="./assets/roster/303.jpg" alt="XXD Panel 303 · 几何符号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-303"><strong>303</strong> · 几何符号</a><br><sub>保留原照片，把主体抽成一枚脱离原图也能成立的几何标志。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-304"><img src="./assets/roster/304.jpg" alt="XXD Panel 304 · 构成图腾" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-304"><strong>304</strong> · 构成图腾</a><br><sub>保留原照片，把主体的气质压成一枚有机与几何相互拉扯的抽象图腾。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-305"><img src="./assets/roster/305.jpg" alt="XXD Panel 305 · 剪纸图腾" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-305"><strong>305</strong> · 剪纸图腾</a><br><sub>保留原照片，把主体剪成一枚缩小后也认得出的剪纸丝网民艺符号。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-306"><img src="./assets/roster/306.jpg" alt="XXD Panel 306 · 民艺剪影" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-306"><strong>306</strong> · 民艺剪影</a><br><sub>保留原照片，在大片空白的纸面上只留下一个很小的民艺剪影。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-307"><img src="./assets/roster/307.jpg" alt="XXD Panel 307 · 生活小记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-307"><strong>307</strong> · 生活小记</a><br><sub>保留原照片，把一个被记住的瞬间收成一个温暖的生活小符号。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-308"><img src="./assets/roster/308.jpg" alt="XXD Panel 308 · 纸剪徽章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-308"><strong>308</strong> · 纸剪徽章</a><br><sub>保留原照片，把主体剪成一枚像从某个地方带回来的纸质文化徽章。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-309"><img src="./assets/roster/309.jpg" alt="XXD Panel 309 · 概念小标" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-309"><strong>309</strong> · 概念小标</a><br><sub>保留原照片，把主体收成一枚只动一处、第二眼才看出新意思的小徽章。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-310"><img src="./assets/roster/310.jpg" alt="XXD Panel 310 · 精神场域" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-310"><strong>310</strong> · 精神场域</a><br><sub>保留原照片，让一大块有机形体包着一个极小的亮色焦点，画出照片背后的情绪。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-311"><img src="./assets/roster/311.jpg" alt="XXD Panel 311 · 旧书象形" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-311"><strong>311</strong> · 旧书象形</a><br><sub>保留原照片，把主体收成像旧书或手工印章里的一个小象形图案。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-312"><img src="./assets/roster/312.jpg" alt="XXD Panel 312 · 童书记忆" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-312"><strong>312</strong> · 童书记忆</a><br><sub>保留原照片，把主体收成旧童书里漂着的一枚安静的记忆小章。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-313"><img src="./assets/roster/313.jpg" alt="XXD Panel 313 · 手帐私章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-313"><strong>313</strong> · 手帐私章</a><br><sub>保留原照片，把主体收成像在手帐里反复画过的一枚私人符号。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-314"><img src="./assets/roster/314.jpg" alt="XXD Panel 314 · 记忆童印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-314"><strong>314</strong> · 记忆童印</a><br><sub>保留原照片，把主体收成旧童书里留下来的一枚记忆小印。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-315"><img src="./assets/roster/315.jpg" alt="XXD Panel 315 · 民艺标识" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-315"><strong>315</strong> · 民艺标识</a><br><sub>保留原照片，把一个轮廓、姿态或局部收成剪纸丝网的民艺文化标识。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-316"><img src="./assets/roster/316.jpg" alt="XXD Panel 316 · 触觉小雕" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-316"><strong>316</strong> · 触觉小雕</a><br><sub>保留原照片，把主体收成一枚像毛毡或软陶手工捏出来的小收藏雕塑。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-317"><img src="./assets/roster/317.jpg" alt="XXD Panel 317 · 圆拙图腾" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-317"><strong>317</strong> · 圆拙图腾</a><br><sub>保留原照片，把主体收成一个圆润、略笨、像长期用过的民艺小图腾。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-318"><img src="./assets/roster/318.jpg" alt="XXD Panel 318 · 生活印记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-318"><strong>318</strong> · 生活印记</a><br><sub>保留原照片，把一段生活的气质收成一个温暖的绘本风小标志。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-319"><img src="./assets/roster/319.jpg" alt="XXD Panel 319 · 诗性记号" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-319"><strong>319</strong> · 诗性记号</a><br><sub>保留原照片，在白纸上留下一个诗意的小符号，外加一点轻轻的第二层意思。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-320"><img src="./assets/roster/320.jpg" alt="XXD Panel 320 · 人格剪影" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-320"><strong>320</strong> · 人格剪影</a><br><sub>保留原照片，把主体收成一个剪影优先、轮廓可以断开的角色小标记。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-321"><img src="./assets/roster/321.jpg" alt="XXD Panel 321 · 墨块旧章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-321"><strong>321</strong> · 墨块旧章</a><br><sub>保留原照片，把主体墨印成旧植物手册或民俗图鉴里的一枚小图。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-322"><img src="./assets/roster/322.jpg" alt="XXD Panel 322 · 几何构成" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-322"><strong>322</strong> · 几何构成</a><br><sub>保留原照片，把主体重组成一枚先好看、再认得出的中世纪现代几何符号。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-323"><img src="./assets/roster/323.jpg" alt="XXD Panel 323 · 白线徽记" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-323"><strong>323</strong> · 白线徽记</a><br><sub>保留原照片，把主体用一根白色单线画在有质感的底上，像一家小店的标识。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-324"><img src="./assets/roster/324.jpg" alt="XXD Panel 324 · 微物心象" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-324"><strong>324</strong> · 微物心象</a><br><sub>保留原照片，把一份很大的情绪收进一个像护符般的微小物件里。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-325"><img src="./assets/roster/325.jpg" alt="XXD Panel 325 · 神话私章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-325"><strong>325</strong> · 神话私章</a><br><sub>保留原照片，把主体收成一枚有时间感的个人神话图腾。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-326"><img src="./assets/roster/326.jpg" alt="XXD Panel 326 · 粗拙图腾" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-326"><strong>326</strong> · 粗拙图腾</a><br><sub>保留原照片，把主体收成干刷和粉笔做成、悬在空白里的克制粗拙图腾。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-327"><img src="./assets/roster/327.jpg" alt="XXD Panel 327 · 童刊遗符" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-327"><strong>327</strong> · 童刊遗符</a><br><sub>保留原照片，把主体收成像从旧儿童刊物里裁下来的一枚小印刷记号。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-328"><img src="./assets/roster/328.jpg" alt="XXD Panel 328 · 贴纸复徽" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-328"><strong>328</strong> · 贴纸复徽</a><br><sub>保留原照片，把主体收成一枚像模切贴纸的复古小志徽章。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-329"><img src="./assets/roster/329.jpg" alt="XXD Panel 329 · 余裕细线" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-329"><strong>329</strong> · 余裕细线</a><br><sub>保留原照片，用一根轻轻摇晃的细线画出一个安静的余裕小图标。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-330"><img src="./assets/roster/330.jpg" alt="XXD Panel 330 · 私人珍藏" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-330"><strong>330</strong> · 私人珍藏</a><br><sub>保留原照片，在手帐角落留下一枚只属于某个人的私人小印记。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-331"><img src="./assets/roster/331.jpg" alt="XXD Panel 331 · 书页边饰" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-331"><strong>331</strong> · 书页边饰</a><br><sub>保留原照片，把它改写成一页边缘讲故事、中央安静留白的旧故事书。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-332"><img src="./assets/roster/332.jpg" alt="XXD Panel 332 · 故事遗徽" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-332"><strong>332</strong> · 故事遗徽</a><br><sub>把照片里的主体收成一枚像从老故事书里留下来的小小印记。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-333"><img src="./assets/roster/333.jpg" alt="XXD Panel 333 · 圣技遗徽" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-333"><strong>333</strong> · 圣技遗徽</a><br><sub>把照片主体收成一枚像失落文明留下的电路浮雕小印章。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-334"><img src="./assets/roster/334.jpg" alt="XXD Panel 334 · 神话书票" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-334"><strong>334</strong> · 神话书票</a><br><sub>把照片主体收成一张中心一枚符号、四周纹样环绕的神话藏书票。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-335"><img src="./assets/roster/335.jpg" alt="XXD Panel 335 · 地下图章" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-335"><strong>335</strong> · 地下图章</a><br><sub>把照片主体收成一枚缩到很小也认得出的地下文化街头徽章。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-336"><img src="./assets/roster/336.jpg" alt="XXD Panel 336 · 中轴神印" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-336"><strong>336</strong> · 中轴神印</a><br><sub>把照片收成中轴和层层框架里的一枚安静、神秘的形而上小印章。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-337"><img src="./assets/roster/337.jpg" alt="XXD Panel 337 · 像素残片" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-337"><strong>337</strong> · 像素残片</a><br><sub>把照片主体收成标本框里一块像从旧互联网挖出来的低保真像素残片。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-338"><img src="./assets/roster/338.jpg" alt="XXD Panel 338 · 栅格残徽" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-338"><strong>338</strong> · 栅格残徽</a><br><sub>把照片主体收成一枚强剪影、弱信息、只留一个异常点的栅格残徽。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-339"><img src="./assets/roster/339.jpg" alt="XXD Panel 339 · 未来圣物" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-339"><strong>339</strong> · 未来圣物</a><br><sub>把照片的气质收成一枚被时间磨损过的未来浅浮雕纪念章。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-340"><img src="./assets/roster/340.jpg" alt="XXD Panel 340 · 视觉奇点" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-340"><strong>340</strong> · 视觉奇点</a><br><sub>把照片收成一枚极小的黑白记号，周围几乎全是空白。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-341"><img src="./assets/roster/341.jpg" alt="XXD Panel 341 · 第二世界" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-341"><strong>341</strong> · 第二世界</a><br><sub>让照片里最聪明的一处契机越过中线，在纸面上继续发生。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-342"><img src="./assets/roster/342.jpg" alt="XXD Panel 342 · 打孔余韵" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-342"><strong>342</strong> · 打孔余韵</a><br><sub>用同一枚模具给照片打孔，再让取下的碎片在纯色留白里重新聚合。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-343"><img src="./assets/roster/343.jpg" alt="XXD Panel 343 · 悬浮像素画片" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-343"><strong>343</strong> · 悬浮像素画片</a><br><sub>把照片主体收成一块居中悬浮、右下带柔影的淡彩像素小画。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-344"><img src="./assets/roster/344.jpg" alt="XXD Panel 344 · 微缩地台" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-344"><strong>344</strong> · 微缩地台</a><br><sub>把照片主体连同脚下一小片地面，做成立在圆角地台上的微缩模型。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-345"><img src="./assets/roster/345.jpg" alt="XXD Panel 345 · 暗底剪影" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-345"><strong>345</strong> · 暗底剪影</a><br><sub>把照片主体和身边几样东西压成平涂剪影，叠成一簇立在深色底上。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-346"><img src="./assets/roster/346.jpg" alt="XXD Panel 346 · 棱纹玻璃" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-346"><strong>346</strong> · 棱纹玻璃</a><br><sub>把照片主体推成满版近景，像隔着细密竖棱玻璃拍下的杂志封面。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-347"><img src="./assets/roster/347.jpg" alt="XXD Panel 347 · 戏服小立像" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-347"><strong>347</strong> · 戏服小立像</a><br><sub>让照片主体正面站好、披上小戏服，变成绘本里准备远行的角色。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-348"><img src="./assets/roster/348.jpg" alt="XXD Panel 348 · 图鉴墨点" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-348"><strong>348</strong> · 图鉴墨点</a><br><sub>把照片主体请进老博物图鉴，用同一种墨一点一点点成标本插图。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-349"><img src="./assets/roster/349.jpg" alt="XXD Panel 349 · 碎方小岛" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-349"><strong>349</strong> · 碎方小岛</a><br><sub>把照片主体和脚下一小块地方拆成圆角方块，像小岛浮在白底中间。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-350"><img src="./assets/roster/350.jpg" alt="XXD Panel 350 · 霓虹精灵" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-350"><strong>350</strong> · 霓虹精灵</a><br><sub>把照片角落画成浅淡线稿，让主体变成一只发光的彩虹软胖精灵。</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>351–354</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-351"><img src="./assets/roster/351.jpg" alt="XXD Panel 351 · 马克笔大字" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-351"><strong>351</strong> · 马克笔大字</a><br><sub>把照片的隐喻写成一行歪扭的马克笔大字，让主体变成小涂鸦闯进字里。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-352"><img src="./assets/roster/352.jpg" alt="XXD Panel 352 · 黑线小景" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-352"><strong>352</strong> · 黑线小景</a><br><sub>把照片主体和身边几样小东西画成大云下面一个安静的黑线小景。</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-353"><img src="./assets/roster/353.jpg" alt="XXD Panel 353 · 点描光锥" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-353"><strong>353</strong> · 点描光锥</a><br><sub>把照片主体压成地上的刻线小剪影，头顶升起一束巨大的点描光锥。</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-354"><img src="./assets/roster/354.jpg" alt="XXD Panel 354 · 粗墨涂鸦" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-354"><strong>354</strong> · 粗墨涂鸦</a><br><sub>把照片主体画成粗墨线圈住的圆胖简笔形，站在一条粗黑地面线上。</sub></td>
  </tr>
</table>

</details>

<!-- xxd-soldier-roster:end -->

## 常见问题

**要把全部风格都装上吗？** 不用。装你喜欢的几个就行。没装的风格它照样能介绍、能推荐，只是会标明「未安装」，装上之后才能出图。

**它怎么判断哪个风格适合？** 看照片里有什么（主体、场景、颜色、文字）和你说的用途与感觉，对照每个风格的说明来挑，并把理由告诉你。不会根据人的长相去猜国籍或喜好。

**会把几种风格混在一起吗？** 不会。每张图只交给一个风格，按那个风格自己的原始提示词画。

**和直接用某个风格有什么区别？** 已经知道要哪种，直接用那个编号的 Skill 最快。还没想好、想比较几种、或者要处理一整个文件夹时，用总目录。

**批量会不会串？** 不会。每张照片单独生成，不借用别的照片的颜色、文字或构图。整批只问一次设置。

**我的照片会发到哪里？** 只发给你自己的 Agent 所用的生图模型。Skill 不往别处上传，也不在输出里显示接口地址和密钥。

## 没有内置生图怎么配

需要一个支持 `gpt-image-2`（或兼容模型）的 OpenAI 兼容接口和它的 API Key。下面单独建一份配置，不影响你 Codex 本身的设置：

```bash
mkdir -p ~/.xxd-imagegen
cat > ~/.xxd-imagegen/config.toml <<'EOF'
model_provider = "image"

[model_providers.image]
base_url = "https://api.openai.com/v1"   # 或你的兼容接口
env_key = "XXD_IMAGE_API_KEY"
EOF

# 写进 ~/.zshrc 或 ~/.bashrc，让 Agent 也能读到
echo 'export XXD_IMAGEGEN_CODEX_DIR=~/.xxd-imagegen' >> ~/.zshrc
echo 'export XXD_IMAGE_API_KEY=你的密钥' >> ~/.zshrc
```

重开终端和 Agent 后，在本 Skill 目录里检查一次：

```bash
python3 scripts/canonical/configured_imagegen.py probe
```

输出 `"ok":true` 就是通了；它只显示是否可用，不会打印地址和密钥。如果你的 Codex 已经通过兼容接口出图，不需要这一步。

## 参数

总目录接受和单个风格相同的出图参数（`--mode` `--size` `--text` `--locale` `--wallpaper` `--out`），会原样转给每个风格；完整说明见任意一个风格 README 的「参数参考」。另外支持 `--prefs last|edit|new|off|clear`，作用同单个风格：沿用、修改或忽略上次的设置。只记住版式、尺寸、文字方式和语言，不记照片、文案、所选风格和密钥。

## 给维护者

这个仓库同时保存全家族共用的运行规则和维护脚本，每个风格仓库里都有它们的副本。

| 文件 | 用途 |
|---|---|
| `references/soldier-runtime.md` | 所有风格共用的出图规则，同步到每个风格仓库 |
| `references/panel-catalog.md` | 编号目录，供推荐和检索；不是生图提示词 |
| `references/readme-profile-guide.md` | 怎么写一个风格的 `readme-profile.json` |
| `scripts/build_soldier_readme.py` | 从风格档案生成某个风格的五种语言 README、SKILL 描述和 `openai.yaml` |
| `scripts/build_general_readme.py` | 生成本页和风格目录 |
| `scripts/soldier_runtime.py` | 把共用规则和脚本同步到全部风格仓库，并检查 |
| `scripts/readme_ads.py` | 检查风格 README 的广告模块 |
| `scripts/brief_intake.py` | 新建风格前检查原始提示词（只提示，不改写） |
| `scripts/unsplash_sample_sources.py` | 为样张挑选 Unsplash 照片 |

<!-- xxd-general-ads:start -->
## 广告信息｜XXD 付费服务与会员

> **广告与商业信息声明：** 以下二维码、会员与付费服务链接属于小小东的广告信息。是否扫码或购买完全自愿，不影响本开源项目的访问与使用。


全部 将军总指挥 Skills 已包含在 699 元/年的统一会员权益中，无需单独购买。 [WeChat](https://xiaoxiaodong.pages.dev/assets/wechat-qr.png)

## 知识星球＋成员提示词库＋全部 将军总指挥 Skills 会员 · 699 元/年

[知识星球](https://wx.zsxq.com/group/15554814142882)、[小小东成员提示词库](https://vip.xiaoxiaodong.ai/)与全部 将军总指挥 Skills 会员是同一份会员权益：**一次年费同时开通三项权益，无需重复付费。**开通后可扫描微信二维码，与小小东进行一对一沟通，获得 AI 学习、工具使用和实际项目答疑；同时按需领取成员提示词库兑换码，并加入全部 将军总指挥 Skills 会员权益。
<!-- xxd-general-ads:end -->

## 许可证

本项目（包括 Skill、提示词、脚本、文档及随附样张）采用 **PolyForm Noncommercial License 1.0.0**。完整法律条文请见 [LICENSE](LICENSE)，官方页面见 <https://polyformproject.org/licenses/noncommercial/1.0.0>。

用人话说：

- 个人可以用于学习、研究、实验、测试、兴趣项目和私人娱乐；慈善机构、教育机构、公共研究/安全/卫生机构、环保组织及政府机构也可以使用。
- 在**非商业目的**下，你可以使用、复制、修改、制作衍生作品并分享；分享时必须同时提供本许可证（或上面的链接）以及作者提供的所有 `Required Notice:` 声明。
- 不允许用于商业产品或服务、收费交付、出售访问权或许可，或任何预期会带来商业应用的用途。需要商业使用时，请先向版权方另行取得书面许可。
- 本协议只授予其中明确写出的著作权许可和有限的专利许可，不授予商标、品牌名称或其他未明确授予的权利，也不能把你的许可再转授给他人。
- 如果收到书面违约通知，须在 32 天内纠正并采取实际补救措施，否则许可会立即终止；就专利侵权提出书面主张也会终止专利许可。
- 内容按“现状”提供，在法律允许的范围内不作任何担保，使用风险和可能的损失由使用者自行承担。
