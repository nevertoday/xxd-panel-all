# Writing a Soldier's readme-profile.json

`xxd-panel-NNN/references/readme-profile.json` holds the only Panel-specific words in a Soldier's five READMEs, its SKILL.md description and its `agents/openai.yaml` short description. `scripts/build_soldier_readme.py` renders everything else from the family template. `xxd-panel-001/references/readme-profile.json` is the reference example.

The reader is someone who has never heard of XXD, deciding in thirty seconds whether this style fits their photo. Write what they will see, in plain words.

## Sources, in order of authority

1. `references/original-prompt/zh-CN.md`: the style itself. Every claim about the look must come from here. Never invent a technique, colour or element the brief does not ask for.
2. `README.md` and `README.en.md`: the existing name (H1 after `｜`, emoji dropped), tagline, and for newer Soldiers the 适用场景 section and sample themes, which show the photos that worked.
3. `xxd-panel-all/references/panel-catalog.md`: the short direction and search traits.

## Fields

- `skill_description` (English, 200–1000 chars, for agents choosing a Skill). The format is `XXD Panel NNN｜<English name>: <what it does to a photo, in concrete visual terms>. Outputs PNG top-bottom or left-right comparisons, design-only images, or phone/tablet/desktop/watch wallpapers, from one photo or a folder. Use when the user invokes xxd-panel-NNN or asks for <style keywords> from a photo.` If the brief limits outputs, for example by forbidding left-right or fixing the language, say so.
- `short_description` (Chinese, one line, at most 80 chars): `<中文名>：<一句话说明>`, with no final 句号.
- One object for each language, `zh-CN`, `en`, `ja`, `ko` and `ar`, with these fields:
  - `name`: keep the existing name for that language. If that README only repeats the Chinese name, translate it naturally.
  - `tagline`: one sentence about what happens to the photo. Aim for at most 40 Chinese characters or 110 English characters, and end with a full stop.
  - `look`: two to four sentences describing what the result looks like:
    - what is kept from the photo;
    - how it is drawn (line, material, texture, colour);
    - composition and whitespace;
    - what text appears.

    Write for a viewer, not a model. Skip the 3:4 or 50:50 container, which is set per request, unless the brief's idea depends on the two halves.
  - `traits`: three to six short keywords, usually from the catalog search traits.
  - `good`: two to four photo types that suit the style, each with concrete examples ("一个人、一只猫、一辆自行车"). Base them on what the brief needs: a clear silhouette, a single subject, a scene, people, text or the like.
  - `poor`: two to four honest misfits:
    - photos the brief cannot handle well, for example detailed machines for block styles, photos full of shop signs for faithful styles, crowded scenes for single-subject styles;
    - looks the brief forbids.

## Language rules

- No internal vocabulary: REALITY VIEW, TRANSFORMED DESIGN, 审美权威, 契约, 交付, 运行适配器, 垫图, 士兵, 将军, Soldier, General, source brief, authority, contract. Say 原照片, 设计, 原始提示词 or the like instead.
- No `|` characters; they break the README tables.
- Translations should read as if written natively. They are faithful but not word for word. Arabic is Modern Standard Arabic. Keep proper nouns and technique names accurate (risograph, ukiyo-e, halftone).
- Do not praise ("高级", "惊艳", "premium"). Describe instead.

## Check

```bash
python3 xxd-panel-all/scripts/build_soldier_readme.py --root . --panel NNN --validate
```
