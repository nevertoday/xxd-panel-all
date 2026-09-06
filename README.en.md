# XXD Panel All · General Skill

<a href="README.md">简体中文</a> · <a href="README.en.md"><strong>English</strong></a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

`xxd-panel-all` is the General-level Skill for the XXD Panel family. It first detects the installed `xxd-panel-NNN` Soldier Skills in the current environment, then handles these tasks:

If you have ever had a folder full of photographs but did not know which style to use—trying them one by one is too slow, while choosing by instinct can be unreliable—this Skill makes the first-round judgment for you. Give it an image or folder; it understands the request, selects suitable installed Panels, dispatches the work, and gathers the results. You do not need to memorise all 120 numbers first.

### Understand it in 30 seconds

- **Make one image:** state a theme or provide a photograph, and it recommends suitable Panels.
- **Compare styles:** choose several Panels and test the same image with each one.
- **Process a batch:** provide a folder and use shared settings or assign a Panel to each image.

The easiest opening is:

> Here is my image. First tell me which Panels you recommend and why each one suits it.

The complete installation, batch, and preference rules follow. It is usually faster to start using the Skill and return here when you need the details.

- Recommend Panels intelligently from an image or theme
- Browse styles by subject, visual feeling, or intended use
- Create directly with a specified Panel number
- Test one input with several Panels
- Assign every image in a folder to a suitable Panel

It handles questions, selection, and dispatch only. It does not become a new visual style and does not imitate an uninstalled Panel from a catalog summary.

## One General, one continually expanding company of aesthetic Soldiers

| Level | Skill | Responsibility |
|---|---|---|
| **General** | [`xxd-panel-all`](https://github.com/nevertoday/xxd-panel-all) | Detect available Soldiers; recommend by image, theme, and use; dispatch by number; organise same-image multi-style trials; assign and route image folders item by item. |
| **Soldier** | `xxd-panel-NNN` (catalog updated through 121) | Each number executes only its own independent original prompt and aesthetic, completing the individual task dispatched by the General. |

The General organises the company; it does not draw in place of a Soldier. It never rewrites, blends, or overrides a Soldier's original aesthetic. Every finished image is independently produced by the selected numbered Skill.

## New Soldiers

- [XXD Panel 114 · Retro Pastel Scrapbook Doodles](https://github.com/nevertoday/xxd-panel-114)
- [XXD Panel 115 · Pastel Stamp Collage Journal](https://github.com/nevertoday/xxd-panel-115)
- [XXD Panel 116 · Pale Paper Pastel Doodles](https://github.com/nevertoday/xxd-panel-116)
- [XXD Panel 117 · Fine-Line Pastel Journal](https://github.com/nevertoday/xxd-panel-117)
- [XXD Panel 118 · Graphite Whitespace Sketchbook](https://github.com/nevertoday/xxd-panel-118)
- [XXD Panel 119 · Hand-Stitched Fabric Journal](https://github.com/nevertoday/xxd-panel-119)
- [XXD Panel 120 · Architectural Concept Sketchbook](https://github.com/nevertoday/xxd-panel-120)
- [XXD Panel 121 · Lifestyle Doodle Editorial](https://github.com/nevertoday/xxd-panel-121)

## Advertisement | Paid XXD services and membership

> **Advertising and commercial-information notice:** The QR code, membership, and paid-service links below are advertisements from Xiaoxiaodong. Scanning or purchasing is entirely optional and does not affect access to or use of this open-source project.

### Xiaoxiaodong master control · General commander Skill · CNY 100

A one-time payment of CNY 100 provides this General commander Skill (`xxd-panel-all`) for central control, recommendation, selection, and batch dispatch of all Soldier Skills, together with help for installation, updates, company configuration, and dispatch methods. Contact [Xiaoxiaodong on WeChat](https://xiaoxiaodong.pages.dev/assets/wechat-qr.png) and include the note “General Commander Skill”.

## ZSXQ + member prompt library + all General Skills membership · CNY 699/year

[ZSXQ](https://wx.zsxq.com/group/15554814142882), the [Xiaoxiaodong member prompt library](https://vip.xiaoxiaodong.ai/), and membership for all General Skills are one combined benefit: **one annual payment activates all three; no duplicate payment is needed.** After joining through ZSXQ, contact Xiaoxiaodong on WeChat to receive a redemption code for the member prompt library. After joining through the member prompt library, contact Xiaoxiaodong on WeChat to enter the ZSXQ group and activate membership for all General Skills.

## Installation

```bash
git clone https://github.com/nevertoday/xxd-panel-all.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/xxd-panel-all" ~/.claude/skills/xxd-panel-all
```

You can also install directly with `npx skills`:

```bash
npx skills add https://github.com/xiaoxiaodong-ai/xxd-panel-all --skill xxd-panel-all
```

This command fetches the General repository from GitHub and installs `xxd-panel-all` into the current Agent. To install into the user-level Codex Skills directory, append `--global --agent codex --yes`. The General only dispatches work; actual creation also requires the relevant `xxd-panel-NNN` Soldier Skills to be installed separately.

If `~/.codex/skills` is not shared with `~/.claude/skills`, create another link:

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/xxd-panel-all" ~/.codex/skills/xxd-panel-all
```

Restart the Agent session after installation, then invoke:

```text
$xxd-panel-all
```

## Batch processing a directory

Provide an image directory directly in the invocation:

```text
$xxd-panel-all /path/to/images
```

The Skill immediately enters batch mode, scans images in the directory and its subdirectories, then asks for one assignment strategy:

1. Use one Panel for every image
2. Automatically match the best Panel to each image
3. Group similar images and use one Panel per group
4. Automatically assign only among several specified Panels

Shared delivery settings are collected once. Each image then enters its assigned `xxd-panel-NNN` as an independent task; images are never merged into a collage and cannot contaminate one another.

## Reuse the last preferences or configure afresh

When the current delivery settings remain incomplete and a previous XXD Panel preference is available, the General or Soldier first shows the previous modes, sizes, text and language, wallpaper relationship, and output location, then asks:

1. **Reuse directly:** reuse the last settings, with current explicit requirements taking priority.
2. **Reuse and edit:** start with the last settings and change only the selected fields.
3. **Fresh configuration:** ignore the saved settings and choose again from the beginning.

A fully specified request runs directly without extra questions. You may also use `--prefs last|edit|new|off|clear`. The preference record stores delivery settings only; it never stores source images, exact copy, Panel selection, generated results, model channels, API credentials, or other sensitive information.

```text
$xxd-panel-all /path/to/images --prefs last
$xxd-panel-all /path/to/images --prefs edit
$xxd-panel-all /path/to/images --prefs new
```

## Installation status

At runtime, a Panel has one of three states:

- `AVAILABLE`: installed now and callable directly
- `KNOWN_BUT_MISSING`: listed in the style catalog but not currently installed
- `UNKNOWN`: absent from the catalog

Recommendation, batch assignment, and direct creation use installed Panels only. Uninstalled styles can be browsed and recommended, but their child Skills must be installed before they can create.

## Project structure

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

- `SKILL.md`: interaction, recommendation, browsing, and batch-routing rules
- `panel-catalog.md`: searchable catalog updated through Panel 121; it is not an image-generation prompt
- `runtime-preferences.md`: reuse, edit, fresh-configuration, and privacy boundaries
- `panel_preferences.py`: local helper that reads and writes safe delivery preferences only
- `openai.yaml`: Skill interface metadata

## License

This project—including the Skill, prompts, scripts, documentation, and accompanying sample images—is licensed under the **PolyForm Noncommercial License 1.0.0**. See [LICENSE](LICENSE) for the full legal text and <https://polyformproject.org/licenses/noncommercial/1.0.0> for the official page.

In plain language:

- Individuals may use it for study, research, experimentation, testing, hobby projects, and private entertainment. Charities, educational institutions, public research, safety or health organisations, environmental organisations, and government institutions may also use it.
- For **noncommercial purposes**, you may use, copy, modify, create derivative works, and share it. When sharing, you must also provide this license (or the link above) and every `Required Notice:` statement supplied by the author.
- It may not be used in commercial products or services, paid delivery, sale of access or licences, or any use expected to lead to commercial application. Obtain separate written permission from the copyright holder before commercial use.
- The agreement grants only the copyright licence and limited patent licence expressly stated. It grants no trademarks, brand names, or other unstated rights, and you may not sublicense your licence to others.
- After written notice of a violation, you must return to compliance and take practical remedial steps within 32 days, or the licences terminate immediately. A written patent-infringement claim also terminates the patent licence.
- The material is provided “as is”, without warranty to the extent permitted by law. Users bear the risks and potential losses arising from its use.
