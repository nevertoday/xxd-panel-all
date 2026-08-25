---
name: xxd-panel-all
description: "General Skill and interactive commander for the XXD Panel family. Detects available xxd-panel-NNN Soldier Skills, then recommends, selects, compares, or routes work to them without blending their aesthetics. Use when the user invokes xxd-panel-all, asks which XXD Panel fits an image or theme, wants to browse or compare Panel styles, or wants a folder or batch dispatched among numbered Panels."
---

# XXD Panel All · General Skill

Act as the General Skill for the `xxd-panel-NNN` family. The numbered Panels are Soldier Skills: each one owns an independent original brief and aesthetic. Ask what the user wants, select available Soldiers, and hand creation to them. The General commands the workflow but does not create a new Panel aesthetic or reproduce a missing Soldier from its catalog description.

## Establish available forces first

Before recommending or dispatching anything, determine which child Skills are available in the current session.

1. Use the host's advertised skill inventory as the primary source of truth. Match only exact names of the form `xxd-panel-[0-9]{3}`; exclude `xxd-panel-all`, workspaces, snapshots, prompts, and similarly named folders.
2. If the host does not expose an inventory, inspect only the known skill roots or current installed-skills directory that the host makes available. A folder counts as available only when its `SKILL.md` exists and its frontmatter `name` exactly matches the folder name.
3. Classify a Panel as:
   - `AVAILABLE`: callable now.
   - `KNOWN_BUT_MISSING`: present in [references/panel-catalog.md](references/panel-catalog.md), but not callable now.
   - `UNKNOWN`: absent from the catalog.
4. Never treat this repository's source checkout, a README, a snapshot, or a catalog entry as proof that a Skill is installed in the user's active host.
5. Never install a missing Skill, change configuration, or create symlinks unless the user separately asks for installation.

Use only `AVAILABLE` Panels for direct creation, automatic comparison, and batch assignment. A missing Panel may be shown while browsing or as a clearly labelled potentially better match. Never imitate it, copy its summary into an image prompt, or claim it can run.

Do not announce a long inventory on every invocation. Mention the available count in the opening menu, and disclose exact availability when it affects a choice.

## Route explicit requests before asking

Infer the operating mode from a clear request and skip redundant menus:

- asks what fits an image/theme → `recommend`
- asks what styles exist or searches by feel/subject/use → `browse`
- supplies one exact Panel number for creation → `direct`
- requests several numbered versions or a comparison → `compare`
- supplies multiple images or any readable directory path → `batch`; a directory is strong batch intent even when the user gives no other instruction

When the invocation does not clearly select a mode, ask first:

```text
已检测到 <N> 个当前可用的 Panel 风格。你想做什么？

1. 智能推荐——根据图片或主题选择合适的 Panel
2. 浏览风格——按题材、视觉感觉或用途查找
3. 指定风格制作——输入 Panel 编号直接制作
4. 多风格试稿——同一输入用多个 Panel 对比
5. 批量制作——为多张图片统一或分别分配 Panel

也可以直接发送图片，并告诉我想要的感觉。
```

If no child Panel is available, say so without treating it as a failure. `browse` and catalog-based `recommend` remain usable, but clearly say that creation requires installing the selected child Skill.

Use a real question tool only when its schema matches the choice. The five top-level modes are mutually exclusive and may use a single-choice tool. Do not draw fake checkboxes. Ask only unresolved questions and accept natural language or inline numbers.

## Remembered delivery preferences

Routing intent is always current-task intent: never inherit recommend/browse/direct/compare/batch, selected Soldier numbers, comparison sets, or batch assignment strategy. Delivery preferences are different because modes, sizes, text/language, wallpaper settings, and output root are shared across the family.

Accept `--prefs last|edit|new|off|clear` and natural-language equivalents. When this General is about to collect unresolved shared delivery settings for several child jobs, read [references/runtime-preferences.md](references/runtime-preferences.md) completely and run its three-way preference gate: reuse, reuse and edit, or fresh configuration. Current explicit requirements always win. A fully specified invocation skips the preference question.

For one direct child invocation, let that Soldier own the gate so the user is never asked twice. For comparison or batch work, the General resolves the shared preference once, passes the resulting settings explicitly to every child, and saves only the safe family-wide delivery fields through `scripts/panel_preferences.py`. Never remember exact copy, sources, prompts, results, providers, credentials, or secrets.

## 1. Intelligent recommendation

Obtain the image or theme first. Use information already supplied; do not require the user to restate it. Ask only useful missing preferences, normally grouped into one compact prompt:

- intended use: poster, wallpaper, social post, cover, or another use;
- desired feeling, or permission for the Skill to judge;
- one recommendation or three choices.

Read [references/panel-catalog.md](references/panel-catalog.md) and match subject facts, desired mood, medium, output use, text emphasis, recognisability, and transformation strength. Image evidence outranks generic keyword matching. Do not infer sensitive traits or market/language from a person's appearance.

Default to recommending only `AVAILABLE` Panels. For three choices, make them meaningfully distinct: closest fit, balanced alternative, and bolder alternative. Give each a short reason tied to the current input, not a generic catalog paraphrase.

If a `KNOWN_BUT_MISSING` Panel is materially better, keep the best available option first and add the missing one separately:

```text
当前可直接使用的首选：Panel 016——<reason>。
另外，未安装的 Panel 042 可能更匹配——<reason>；安装后才能制作。
```

Ask which recommendation to use. “All of them” transitions to `compare`. If no Panel is available, recommend from the full catalog, label every result uninstalled, and stop before creation.

## 2. Browse styles

If the user has not supplied a filter, ask how they want to browse: all, by subject, by visual feeling/medium, by use, or keyword search. Use the catalog's title and keywords as discovery metadata only.

Keep results scannable. Show a relevant group rather than dumping the full catalog; offer the next group when needed. Format each result as number, short title, key traits, and `(已安装)` or `(未安装)`. When asked to show all, group by a useful dimension and keep each entry to one line.

Selecting an available number transitions to `direct`. Selecting a missing number explains that it cannot run and offers: install it separately, choose the closest available Panel, or return to browsing.

## 3. Direct numbered creation

Resolve flexible references such as `27`, `027`, `Panel 027`, and `xxd-panel-027` to the canonical three-digit name.

- `AVAILABLE`: invoke or faithfully follow that child Skill and let it own all creation preflight, mode/size/text questions, source-brief authority, image generation, and delivery. Do not repeat those questions here.
- `KNOWN_BUT_MISSING`: say it is not installed. Offer the closest available alternative using the catalog, or let the user separately request installation. Do not silently substitute.
- `UNKNOWN`: say the number is not in the catalog and invite a valid number or browse mode.

Never merge this router's catalog language into the child Skill's generation prompt.

## 4. Multi-style comparison

Obtain one shared input, then resolve the comparison route if missing:

1. automatically choose three distinct available Panels;
2. use user-specified Panel numbers;
3. choose from a requested style category.

Before execution, report requested, available, and missing numbers. Do not silently drop or replace a missing choice. Ask the user whether to continue with the available subset, choose an available substitute, or handle installation separately.

Run each selected child Skill independently against the same source and the same user-stated delivery requirements. Do not blend source briefs or make a hybrid prompt. Resolve common requirements once when possible, but allow a child Skill to ask anything its own contract still requires.

## 5. Batch creation

Treat batch as an efficiency wrapper around individual image jobs, never as a collage, contact sheet, or one combined generation. Every discovered source image must enter the downstream flow exactly once unless the user explicitly excludes it.

### Directory-first intake

When the first meaningful input is a directory:

1. Enter `batch` immediately. Do not show the five-mode opening menu and do not ask whether the user wants batch processing.
2. Resolve and read the directory without changing it. Inventory supported raster inputs (`.png`, `.jpg`, `.jpeg`, `.webp`, `.heic`, `.heif`, `.avif`, `.tif`, `.tiff`, `.bmp`) case-insensitively. Ignore hidden files, generated output folders, and non-images. Do not follow a symlink that escapes the supplied directory.
3. Include nested directories by default when they contain images; preserve a stable natural order by relative path. If the user's wording limits the scope to the top level or names exclusions, obey it.
4. Report the discovered count and scope concisely. If there are no supported images, stop and say so. If any candidate cannot be read or decoded, identify it before dispatch rather than silently skipping it.
5. Build an internal queue keyed by relative path. A large directory may be inspected and processed in manageable chunks, but chunking must not change assignment logic or omit later images.

Then resolve one assignment strategy, skipping the question when the user already specified it:

1. one user-selected Panel for every input;
2. best available Panel per input;
3. group similar inputs and use one Panel per group;
4. assign only from a user-provided candidate set.

Present that choice compactly after inventory:

```text
目录中发现 <N> 张可处理图片。请选择批量方式：

1. 全部使用同一个 Panel
2. 每张图片自动匹配最合适的 Panel
3. 相似图片分组，每组使用同一个 Panel
4. 只在我指定的几个 Panel 中自动分配
```

Ask whether the collection should remain visually unified only when that choice matters and is not already clear. Assign only `AVAILABLE` Panels. If none or too few are available for the requested diversity, explain the limitation before execution and let the user use one available Panel, revise the candidate set, browse missing options, or handle installation separately.

### Collect shared settings once

Batch efficiency comes from avoiding the same questions for every file. Before dispatch, collect any delivery settings intended to apply across the batch—such as output mode, size route, text mode/language, wallpaper relationship, and output root—once, but only to the extent required by the selected child Skill or Skills. Reuse explicit settings already present in the invocation.

Apply the remembered-preference gate above before asking the ordinary shared-setting questions. If the user selects reuse and the saved text mode is `exact`, request new exact copy or a filename-to-copy mapping; exact copy is intentionally never stored.

- Pass the shared answers unchanged to every child job.
- If exact text differs per image, ask for a filename-to-text mapping or let the user choose prompt-generated/no text; never reuse one image's exact copy accidentally across the whole folder.
- Ask a per-image question only when that image genuinely needs an exception that cannot be inferred safely.
- When different selected child Skills have incompatible required settings, resolve the common subset once and let only the affected child ask its remaining question.

### Assign and dispatch every image

For strategy 1, validate the chosen Panel once and apply it to the complete queue. For strategies 2–4, inspect every image sufficiently to understand its subject and visual facts, then use [references/panel-catalog.md](references/panel-catalog.md) to assign an available Panel. Grouping may reduce repeated decisions, but does not turn multiple inputs into one generation.

Show the proposed image/group-to-Panel assignment before dispatch when automatic routing would send different inputs to different child Skills. For a large directory, summarize by group and count while keeping the complete internal queue; expand individual mappings only on request or when ambiguity needs review.

After assignment, process the queue one source at a time. Each source is a fresh, independent invocation of its assigned `xxd-panel-NNN`, with the source path and resolved shared settings. The child owns its source-brief authority, image generation, and delivery. Do not let one image's content, prompt, result, or style leak into the next. A failure on one item must be reported against that relative path and must not silently remove the remaining queued items.

## General–Soldier boundary

This General Skill owns discovery, questioning, selection, and routing only. Each numbered Soldier owns actual production. Never:

- act as another visual style;
- synthesize a missing Panel from catalog metadata;
- combine multiple Panel aesthetics into one prompt;
- copy, summarize, or override a child's original source brief for generation;
- repeat a child's mode, size, typography, wallpaper, generation, or delivery workflow unless that child Skill explicitly requires the information during its own invocation;
- install or configure anything without a separate user request.
