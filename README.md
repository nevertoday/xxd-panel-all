# XXD Panel All · 将军 Skill

<a href="README.md"><strong>简体中文</strong></a> · <a href="README.en.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

`xxd-panel-all` 是 XXD Panel 系列的将军级 Skill。它先识别当前环境中已安装的 `xxd-panel-NNN` 士兵级 Skills，再承接以下任务：

如果你也有过这种时刻：手里一堆照片，不知道该用哪种风格；一个个试太慢，凭感觉乱选又容易后悔——这个 Skill 就是替你做第一轮判断的。你只要把图片或文件夹交过来，它会先看懂需求，再从已经安装的 Panel 里挑人、派活、收结果。你不用先背下 154 个编号。

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
| **士兵级** | `xxd-panel-NNN`（目录更新至 155） | 每个编号只执行自己独立的原始提示词与审美，把将军派发的单个任务完成为成品。 |

将军负责组织队伍，不替士兵作画。它不会改写、混合或覆盖任何士兵的原始美学；每张成品始终由被选中的编号 Skill 独立完成。

## 新增士兵

- [XXD Panel 114 · 复古粉彩手账涂鸦](https://github.com/nevertoday/xxd-panel-114)
- [XXD Panel 115 · 粉彩章印拼贴志](https://github.com/nevertoday/xxd-panel-115)
- [XXD Panel 116 · 浅纸粉彩涂鸦志](https://github.com/nevertoday/xxd-panel-116)
- [XXD Panel 117 · 细线淡彩留白志](https://github.com/nevertoday/xxd-panel-117)
- [XXD Panel 118 · 石墨留白素描志](https://github.com/nevertoday/xxd-panel-118)
- [XXD Panel 119 · 手缝布艺留白志](https://github.com/nevertoday/xxd-panel-119)
- [XXD Panel 120 · 建筑概念手绘志](https://github.com/nevertoday/xxd-panel-120)
- [XXD Panel 121 · 生活涂鸦编排志](https://github.com/nevertoday/xxd-panel-121)
- [XXD Panel 122 · 单色网点手写志](https://github.com/nevertoday/xxd-panel-122)
- [XXD Panel 123 · 红蓝角线彩铅志](https://github.com/nevertoday/xxd-panel-123)
- [XXD Panel 124 · 布艺拼贴留白志](https://github.com/nevertoday/xxd-panel-124)
- [XXD Panel 125 · 蜡笔童趣留白志](https://github.com/nevertoday/xxd-panel-125)
- [XXD Panel 126 · 诗意微缩拼贴志](https://github.com/nevertoday/xxd-panel-126)
- [XXD Panel 127 · 建筑混媒拼贴志](https://github.com/nevertoday/xxd-panel-127)
- [XXD Panel 128 · 珐琅徽章旅行志](https://github.com/nevertoday/xxd-panel-128)
- [XXD Panel 129 · 东方弥散留白志](https://github.com/nevertoday/xxd-panel-129)
- [XXD Panel 130 · 硬边几何切面志](https://github.com/nevertoday/xxd-panel-130)
- [XXD Panel 131 · 摄影涂鸦拼贴志](https://github.com/nevertoday/xxd-panel-131)
- [XXD Panel 132 · 钢笔淡彩旅行志](https://github.com/nevertoday/xxd-panel-132)
- [XXD Panel 133 · 点刻透明套印志](https://github.com/nevertoday/xxd-panel-133)
- [XXD Panel 134 · 绘本色域叙事志](https://github.com/nevertoday/xxd-panel-134)
- [XXD Panel 135 · 街头专色手绘志](https://github.com/nevertoday/xxd-panel-135)
- [XXD Panel 136 · 诗意超现实留白志](https://github.com/nevertoday/xxd-panel-136)
- [XXD Panel 137 · 蚀刻肌理拼贴志](https://github.com/nevertoday/xxd-panel-137)
- [XXD Panel 138 · 东方纸艺浮雕志](https://github.com/nevertoday/xxd-panel-138)
- [XXD Panel 139 · 文字编码线场志](https://github.com/nevertoday/xxd-panel-139)
- [XXD Panel 140 · 干性手绘视觉岛](https://github.com/nevertoday/xxd-panel-140)
- [XXD Panel 141 · 极简手绘线描志](https://github.com/nevertoday/xxd-panel-141)
- [XXD Panel 142 · 字形蒙版融合志](https://github.com/nevertoday/xxd-panel-142)
- [XXD Panel 143 · 文字造型视觉诗](https://github.com/nevertoday/xxd-panel-143)
- [XXD Panel 144 · 几何反白破框志](https://github.com/nevertoday/xxd-panel-144)
- [XXD Panel 145 · 复古限色版画志](https://github.com/nevertoday/xxd-panel-145)
- [XXD Panel 146 · 博物学丝巾印花志](https://github.com/nevertoday/xxd-panel-146)
- [XXD Panel 147 · 便当食材包装志](https://github.com/nevertoday/xxd-panel-147)
- [XXD Panel 148 · 视觉日记拼贴志](https://github.com/nevertoday/xxd-panel-148)
- [XXD Panel 149 · 手绘肌理扁平志](https://github.com/nevertoday/xxd-panel-149)
- [XXD Panel 150 · 复古现代剪纸志](https://github.com/nevertoday/xxd-panel-150)
- [XXD Panel 151 · 稚拙扁平手绘志](https://github.com/nevertoday/xxd-panel-151)
- [XXD Panel 152 · 色场基座纸艺志](https://github.com/nevertoday/xxd-panel-152)
- [XXD Panel 153 · 单色手帐涂鸦志](https://github.com/nevertoday/xxd-panel-153)
- [XXD Panel 154 · 复古像素留白志](https://github.com/nevertoday/xxd-panel-154)
- [XXD Panel 155 · 一点透视淡彩志](https://github.com/nevertoday/xxd-panel-155)

## 广告信息｜XXD 付费服务与会员

> **广告与商业信息声明：** 以下二维码、会员与付费服务链接属于小小东的广告信息。是否扫码或购买完全自愿，不影响本开源项目的访问与使用。


将军 Skills 已包含在 699 元/年的统一会员权益中，无需单独购买。 [WeChat](https://xiaoxiaodong.pages.dev/assets/wechat-qr.png)

## 知识星球＋成员提示词库＋Skills 所有将军会员 · 699 元/年

[知识星球](https://wx.zsxq.com/group/15554814142882)、[小小东成员提示词库](https://vip.xiaoxiaodong.ai/)与 Skills 所有将军会员是同一份会员权益：**一次年费同时开通三项权益，无需重复付费。**在知识星球开通后，可微信联系小小东领取成员提示词库兑换码；在成员提示词库自助开通后，可微信联系小小东加入知识星球并开通所有将军 Skills 会员权益。

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
├── agents/
│   └── openai.yaml
├── references/
│   ├── panel-catalog.md
│   └── runtime-preferences.md
└── scripts/
    └── panel_preferences.py
```

- `SKILL.md`：交互、推荐、浏览和批量路由规则
- `panel-catalog.md`：更新至 Panel 155 的检索目录，不是生图提示词
- `runtime-preferences.md`：沿用、修改、全新配置与隐私边界
- `panel_preferences.py`：只读写安全交付偏好的本地辅助脚本
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
