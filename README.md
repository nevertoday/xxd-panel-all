# XXD Panel All · 将军 Skill

`xxd-panel-all` 是 XXD Panel 系列的将军级 Skill。它先识别当前环境中已安装的 `xxd-panel-NNN` 士兵级 Skills，再承接以下任务：

如果你也有过这种时刻：手里一堆照片，不知道该用哪种风格；一个个试太慢，凭感觉乱选又容易后悔——这个 Skill 就是替你做第一轮判断的。你只要把图片或文件夹交过来，它会先看懂需求，再从已经安装的 Panel 里挑人、派活、收结果。你不用先背下 78 个编号。

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

## 一位将军，78 位审美士兵

| 层级 | Skill | 负责什么 |
|---|---|---|
| **将军级** | [`xxd-panel-all`](https://github.com/nevertoday/xxd-panel-all) | 识别可用士兵；按图片、主题和用途推荐；按编号点将；组织同图多风格试稿；为图片文件夹批量分配并逐项派发。 |
| **士兵级** | `xxd-panel-NNN`（当前 001–081） | 每个编号只执行自己独立的原始提示词与审美，把将军派发的单个任务完成为成品。 |

将军负责组织队伍，不替士兵作画。它不会改写、混合或覆盖任何士兵的原始美学；每张成品始终由被选中的编号 Skill 独立完成。

## 小小东总控 · 将军总指挥 Skill · 100 元

一次支付 100 元获得本套将军总指挥 Skill（`xxd-panel-all`），用于主控、推荐、点将和批量调度全部士兵 Skills，并获得安装、版本更新、队伍配置和调度方式的答疑。请通过[小小东微信](https://xiaoxiaodong.pages.dev/assets/wechat-qr.png)联系并备注“将军总指挥 Skill”。

## 知识星球＋成员提示词库＋Skills 所有将军会员 · 699 元/年

[知识星球](https://wx.zsxq.com/group/15554814142882)、[小小东成员提示词库](https://vip.xiaoxiaodong.ai/)与 Skills 所有将军会员是同一份会员权益：**一次年费同时开通三项权益，无需重复付费。**在知识星球开通后，可微信联系小小东领取成员提示词库兑换码；在成员提示词库自助开通后，可微信联系小小东加入知识星球并开通所有将军 Skills 会员权益。

## 安装

```bash
git clone https://github.com/nevertoday/xxd-panel-all.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/xxd-panel-all" ~/.claude/skills/xxd-panel-all
```

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
- `panel-catalog.md`：Panel 001–081 的检索目录，不是生图提示词
- `runtime-preferences.md`：沿用、修改、全新配置与隐私边界
- `panel_preferences.py`：只读写安全交付偏好的本地辅助脚本
- `openai.yaml`：Skill 的界面元数据
