# Soldier README advertisements

These five reusable blocks are documentation-only, not generation prompts. They preserve the existing XXD offer: CNY 100 for the General Command Skill and CNY 699/year for the shared three-part membership. Change commercial terms only on explicit owner instruction. Never replace panel numbers across these blocks.

Place the matching block before the README license, after examples and usage. Keep the disclosure above paid offers, the General/Soldier distinction, membership links, contact QR, and voluntary support. Chinese uses the existing WeChat/Alipay support destinations; other languages use the existing Buy Me a Coffee destination. No fixed roster count is embedded.

From the workspace containing the sibling repositories:

```bash
python3 xxd-panel-all/scripts/readme_ads.py --root . --panel 156
python3 xxd-panel-all/scripts/readme_ads.py --root . --panel 156 --patch
```

The second command only prints an `apply_patch` patch. Review and apply it, then rerun the first command. A nonzero check blocks publication. Omit `--panel` to check every local Soldier, or repeat it to select several. Repeated runs must not duplicate advertisements. Partial legacy blocks require manual review rather than automatic replacement.

The September 2026 audit found missing advertisements in Panels 108–155 (excluding absent 113): 47 repositories and 235 README files. The concise template introduced at 108 omitted the old advertising sections, and later templates inherited the omission. A separate number-substitution error affected offer prices in 101–107. Only README advertising was repaired; original prompts, artwork, runtime code, and existing unrelated worktree changes were preserved.
