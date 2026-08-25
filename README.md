# XXD Panel All · 将军 Skill

`xxd-panel-all` 是 XXD Panel 系列的将军级 Skill。它先识别当前环境中已安装的 `xxd-panel-NNN` 士兵级 Skills，再承接以下任务：

- 根据图片或主题智能推荐 Panel
- 按题材、视觉感觉或用途浏览风格
- 指定 Panel 编号直接制作
- 使用多个 Panel 对同一输入试稿
- 将一个目录中的图片逐张分配给合适的 Panel

它只负责问询、选择和调度，不会成为新的视觉风格，也不会用目录摘要模仿尚未安装的 Panel。

## 一位将军，56 位审美士兵

| 层级 | Skill | 负责什么 |
|---|---|---|
| **将军级** | [`xxd-panel-all`](https://github.com/nevertoday/xxd-panel-all) | 识别可用士兵；按图片、主题和用途推荐；按编号点将；组织同图多风格试稿；为图片文件夹批量分配并逐项派发。 |
| **士兵级** | `xxd-panel-NNN`（当前 001–056） | 每个编号只执行自己独立的原始提示词与审美，把将军派发的单个任务完成为成品。 |

将军负责组织队伍，不替士兵作画。它不会改写、混合或覆盖任何士兵的原始美学；每张成品始终由被选中的编号 Skill 独立完成。

## 小小东 Skills 用户交流群 · 168 元

加入后可享用将军 Skill，并获得安装、版本更新、队伍配置和调度方式的答疑。一次支付 168 元加入交流群；请通过[小小东微信](https://xiaoxiaodong.pages.dev/assets/wechat-qr.png)联系并备注“Skills 用户交流群”。该权益不包含按小时的一对一深度咨询。

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
└── references/
    └── panel-catalog.md
```

- `SKILL.md`：交互、推荐、浏览和批量路由规则
- `panel-catalog.md`：Panel 001–056 的检索目录，不是生图提示词
- `openai.yaml`：Skill 的界面元数据
