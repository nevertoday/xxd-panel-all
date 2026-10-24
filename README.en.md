<div align="center">

# XXD Panel All｜Style Catalog

**One entry point for 354 photo styles: show it a photo and what it is for, and it picks, compares and batches styles for you.**

<a href="README.md">简体中文</a> · <strong>English</strong> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.ar.md">العربية</a>

</div>

<table>
  <tr>
    <td width="33%"><a href="https://github.com/nevertoday/xxd-panel-001"><img src="./assets/roster/001.jpg" alt="XXD Panel 001 · Retro Whimsy Journal"></a></td>
    <td width="33%"><a href="https://github.com/nevertoday/xxd-panel-062"><img src="./assets/roster/062.jpg" alt="XXD Panel 062 · Clever Clumsy Line"></a></td>
    <td width="33%"><a href="https://github.com/nevertoday/xxd-panel-350"><img src="./assets/roster/350.jpg" alt="XXD Panel 350 · Neon Spirits"></a></td>
  </tr>
</table>

## What it is

XXD Panels are AI Skills that redraw photos as posters, illustrations and wallpapers, one style per number — 354 so far, each independent. `xxd-panel-all` is their front door, for Claude Code, Codex and other agents that support Skills:

- **Picks for you:** Give it a photo or a theme and it recommends one or three of your installed styles, with the reason each fits.
- **Compares:** Makes the same photo in several styles so you can see them side by side.
- **Batches:** Give it a folder: one style for everything, or the best style for each photo.
- **Doesn't paint itself:** The numbered style Skills make the images. The catalog only chooses and hands off, and never blends styles.

## Get started in three steps

**1. Install the catalog and a few styles you like.** It can describe and recommend styles you haven't installed, but only installed ones can make images:

```bash
npx skills add https://github.com/nevertoday/xxd-panel-all --skill xxd-panel-all
npx skills add https://github.com/nevertoday/xxd-panel-001 --skill xxd-panel-001
```

Several at once:

```bash
for n in 001 062 350; do npx skills add https://github.com/nevertoday/xxd-panel-$n --skill xxd-panel-$n; done
```

Then restart your agent session.

**2. Make sure your agent can generate images.** This Skill has no image model of its own; it uses your agent's image generation, preferably GPT Image 2.

- Codex works as is when its built-in image generation is on.
- Claude Code and other agents without built-in image generation need an OpenAI-compatible image API. It takes about five minutes: see [Setting up image generation](#setting-up-image-generation).

Not sure? Just try it. If images can't be generated, the Skill stops and tells you before doing any work.

**3. Send a photo and say one sentence:**

> Use xxd-panel-all to suggest three styles that suit this photo and say why.

Once you choose, it hands the photo to that style's Skill, which asks about layout, ratio and text. Results go to `~/Desktop/xxd/xxd-panel-NNN/`.

## Just say it

No parameters to memorise. Say what you want:

| You want | Say |
|---|---|
| A recommendation | Which style suits this photo? Suggest three and say why |
| Search by feel | Any styles with black line and lots of whitespace? |
| Search by use | Which styles work for a phone wallpaper? |
| A specific number | Use 062 for this photo |
| A comparison | Make one each with 001, 062 and 350 so I can compare |
| A folder, one style | Turn this whole folder into top–bottom comparisons with 014 |
| A folder, auto-matched | Pick the best style for each photo in this folder |
| Same as last time | Use my settings from last time |

## All styles

354 in total. Each image is one left–right sample of that style (photo left, design right). Click it to open the style's repository for more samples and usage.

<!-- xxd-soldier-roster:start -->

<details open>
<summary><strong>001–050</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-001"><img src="./assets/roster/001.jpg" alt="XXD Panel 001 · Retro Whimsy Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-001"><strong>001</strong> · Retro Whimsy Journal</a><br><sub>Turns a photo into a light, paper-textured, slightly clumsy and witty retro hand-drawn illustration.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-002"><img src="./assets/roster/002.jpg" alt="XXD Panel 002 · Playful Bauhaus" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-002"><strong>002</strong> · Playful Bauhaus</a><br><sub>Turns a photo into a retro editorial drawing with a touch of Bauhaus geometry, wobbly outlines and off-register print.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-003"><img src="./assets/roster/003.jpg" alt="XXD Panel 003 · Taut Line Language" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-003"><strong>003</strong> · Taut Line Language</a><br><sub>Pulls the direction, connection, pressure and release in a photo into one quiet, tense black continuous line.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-004"><img src="./assets/roster/004.jpg" alt="XXD Panel 004 · Urban Single-Line Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-004"><strong>004</strong> · Urban Single-Line Journal</a><br><sub>Distils a real city or place scene into a collectible modern poster of precise single lines and clear perspective.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-005"><img src="./assets/roster/005.jpg" alt="XXD Panel 005 · Dark Fairytale Edition" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-005"><strong>005</strong> · Dark Fairytale Edition</a><br><sub>Compresses a photo into a fairy-tale print wrapped in dark shapes, with small flashes of bright colour.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-006"><img src="./assets/roster/006.jpg" alt="XXD Panel 006 · Negative-Space Theater" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-006"><strong>006</strong> · Negative-Space Theater</a><br><sub>Reduces a photo to one small subject on a vast field of paper, like the cover of an art book.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-007"><img src="./assets/roster/007.jpg" alt="XXD Panel 007 · Hand-Drawn Observation Page" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-007"><strong>007</strong> · Hand-Drawn Observation Page</a><br><sub>Breaks a photo into a page of small drawings, cross-sections and handwritten notes you look at and read together.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-008"><img src="./assets/roster/008.jpg" alt="XXD Panel 008 · Pastel Dreamscape" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-008"><strong>008</strong> · Pastel Dreamscape</a><br><sub>Turns the people and story in a photo into a bright, quiet, Monument Valley-like pastel impossible space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-009"><img src="./assets/roster/009.jpg" alt="XXD Panel 009 · Halftone Anchor Print" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-009"><strong>009</strong> · Halftone Anchor Print</a><br><sub>Compresses a photo into one tiny anchor on vast paper, with halftone dots fading from dense to sparse for distance and air.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-010"><img src="./assets/roster/010.jpg" alt="XXD Panel 010 · Black-and-White Storybook" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-010"><strong>010</strong> · Black-and-White Storybook</a><br><sub>Compresses a photo into a rough black-crayon picture-book silhouette on near-white paper, in black and white only.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-011"><img src="./assets/roster/011.jpg" alt="XXD Panel 011 · Meditative Line Poem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-011"><strong>011</strong> · Meditative Line Poem</a><br><sub>Distils a photo into one thin, continuous black line worth looking at slowly, with a single meaningful touch of colour.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-012"><img src="./assets/roster/012.jpg" alt="XXD Panel 012 · Geometry of Life" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-012"><strong>012</strong> · Geometry of Life</a><br><sub>Lets the subject of a photo gather out of a dense one-colour line field, with geometric fine lines spreading around it.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-013"><img src="./assets/roster/013.jpg" alt="XXD Panel 013 · Travel Ticket Album" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-013"><strong>013</strong> · Travel Ticket Album</a><br><sub>Keeps your photo in a ticket with watercolour on the left and a stub on the right, like a treasured travel keepsake.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-014"><img src="./assets/roster/014.jpg" alt="XXD Panel 014 · Paper Relief Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-014"><strong>014</strong> · Paper Relief Journal</a><br><sub>Rebuilds a photo as a contemporary folded-paper sculpture where you can see creases, cut edges and paper fibre.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-015"><img src="./assets/roster/015.jpg" alt="XXD Panel 015 · Abstract Memoir" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-015"><strong>015</strong> · Abstract Memoir</a><br><sub>Takes a photo apart and rebuilds it from a few geometric shapes and a refined set of tiny editorial text, like an art-book page.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-016"><img src="./assets/roster/016.jpg" alt="XXD Panel 016 · Kinetic Woodblock Print" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-016"><strong>016</strong> · Kinetic Woodblock Print</a><br><sub>Compresses what really happens in a photo into one tiny subject and a single field of motion around it.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-017"><img src="./assets/roster/017.jpg" alt="XXD Panel 017 · Childlike Graphic Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-017"><strong>017</strong> · Childlike Graphic Journal</a><br><sub>Turns a photo into a bright Korean-style flat editorial illustration with rough black outlines and solid colour.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-018"><img src="./assets/roster/018.jpg" alt="XXD Panel 018 · Handcut Paper Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-018"><strong>018</strong> · Handcut Paper Journal</a><br><sub>Remakes a photo as hand-cut layered paper: one paper subject, a few front, middle and back layers and precise tiny type.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-019"><img src="./assets/roster/019.jpg" alt="XXD Panel 019 · Retro Graphic Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-019"><strong>019</strong> · Retro Graphic Journal</a><br><sub>Rebuilds the subject and relationship in a photo as a retro modernist flat illustration that is still recognisable.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-020"><img src="./assets/roster/020.jpg" alt="XXD Panel 020 · Impasto Micro-Landscape" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-020"><strong>020</strong> · Impasto Micro-Landscape</a><br><sub>Turns the subject and story of a photo into a tactile miniature scene growing out of a slab of thick impasto paint.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-021"><img src="./assets/roster/021.jpg" alt="XXD Panel 021 · Crossing the Black Field" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-021"><strong>021</strong> · Crossing the Black Field</a><br><sub>Lets the subject of a photo lean out of a pure-black rectangle, drawn in shaky black line and white shapes, in black, white and grey only.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-022"><img src="./assets/roster/022.jpg" alt="XXD Panel 022 · Color-Dot Trespass" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-022"><strong>022</strong> · Color-Dot Trespass</a><br><sub>Lets the subject of a photo break out of a pure-black rectangle in clean line, with colour on one key spot only.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-023"><img src="./assets/roster/023.jpg" alt="XXD Panel 023 · Eastern Window View" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-023"><strong>023</strong> · Eastern Window View</a><br><sub>Frames your photo in a Chinese window chosen to suit it, like sunlight falling through a lattice onto a pale wall.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-024"><img src="./assets/roster/024.jpg" alt="XXD Panel 024 · Mood Window" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-024"><strong>024</strong> · Mood Window</a><br><sub>Lets a real subject from your photo pass through one narrow, pale geometric window, as a minimal high-end commercial poster.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-025"><img src="./assets/roster/025.jpg" alt="XXD Panel 025 · Invisible Imagery" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-025"><strong>025</strong> · Invisible Imagery</a><br><sub>Turns a photo into a Morandi-toned screenprint where you see the subject first and a hidden picture on a second look.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-026"><img src="./assets/roster/026.jpg" alt="XXD Panel 026 · Geometric Order" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-026"><strong>026</strong> · Geometric Order</a><br><sub>Translates the facts of a photo into quiet, gentle geometry that you can still recognise at a glance.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-027"><img src="./assets/roster/027.jpg" alt="XXD Panel 027 · Relief on Paper" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-027"><strong>027</strong> · Relief on Paper</a><br><sub>Presses a photo into an Eastern museum-style bas-relief on thick ivory paper, with matte gold only where it matters.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-028"><img src="./assets/roster/028.jpg" alt="XXD Panel 028 · Isometric Micro-Landscape" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-028"><strong>028</strong> · Isometric Micro-Landscape</a><br><sub>Sets your photo down as an isometric paper miniature in its own colours, like a small architectural model.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-029"><img src="./assets/roster/029.jpg" alt="XXD Panel 029 · Slow Sketch on Paper" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-029"><strong>029</strong> · Slow Sketch on Paper</a><br><sub>Redraws a photo in relaxed wax pastel across one horizontal block of muted colour, with one casual handwritten line.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-030"><img src="./assets/roster/030.jpg" alt="XXD Panel 030 · Nature Unbound" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-030"><strong>030</strong> · Nature Unbound</a><br><sub>Rebuilds the subject of a photo from real leaves, petals, twigs, fruit, seeds, grass stems and bark.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-031"><img src="./assets/roster/031.jpg" alt="XXD Panel 031 · Allegorical Rubbing" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-031"><strong>031</strong> · Allegorical Rubbing</a><br><sub>Reads the meaning behind a photo first, then distils it into one geometric motif with the rough texture of a folk rubbing.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-032"><img src="./assets/roster/032.jpg" alt="XXD Panel 032 · Graphic Wordmark" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-032"><strong>032</strong> · Graphic Wordmark</a><br><sub>Builds the defining feature of your photo&#x27;s subject into the letters of a custom wordmark.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-033"><img src="./assets/roster/033.jpg" alt="XXD Panel 033 · Vivid Collage Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-033"><strong>033</strong> · Vivid Collage Journal</a><br><sub>Turns one photo into a vivid, richly coloured, clearly layered modern magazine-cover collage.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-034"><img src="./assets/roster/034.jpg" alt="XXD Panel 034 · Travel Stamp Marks" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-034"><strong>034</strong> · Travel Stamp Marks</a><br><sub>Distils a photo into one small multicolour rubber stamp with a quiet field note beside it.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-035"><img src="./assets/roster/035.jpg" alt="XXD Panel 035 · Building-Block Reconstruction" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-035"><strong>035</strong> · Building-Block Reconstruction</a><br><sub>Rebuilds the subject of your photo as one bright, instantly recognisable voxel-block collectible.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-036"><img src="./assets/roster/036.jpg" alt="XXD Panel 036 · Streamline Picture Book" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-036"><strong>036</strong> · Streamline Picture Book</a><br><sub>Draws the relationship in your photo with a few continuous fine lines and lets translucent colour drift across the paper.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-037"><img src="./assets/roster/037.jpg" alt="XXD Panel 037 · Flowing Gold Emblem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-037"><strong>037</strong> · Flowing Gold Emblem</a><br><sub>Turns a photo from your journey into one collectible gilded enamel badge.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-038"><img src="./assets/roster/038.jpg" alt="XXD Panel 038 · Textile Life Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-038"><strong>038</strong> · Textile Life Journal</a><br><sub>Sews your photo and the feeling it leaves unsaid into a warm hand-made patchwork picture.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-039"><img src="./assets/roster/039.jpg" alt="XXD Panel 039 · Embroidered Imagery" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-039"><strong>039</strong> · Embroidered Imagery</a><br><sub>Picks the one image in your photo most worth keeping and embroiders it in shimmering silk.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-040"><img src="./assets/roster/040.jpg" alt="XXD Panel 040 · Doodle Companion" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-040"><strong>040</strong> · Doodle Companion</a><br><sub>Keeps the one real thing in your photo most worth remembering and lets a few black-line doodle people act out a small story around it.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-041"><img src="./assets/roster/041.jpg" alt="XXD Panel 041 · Isometric Lab" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-041"><strong>041</strong> · Isometric Lab</a><br><sub>Builds your photo&#x27;s subject and one theme drawn from the photo into a light, clear isometric study.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-042"><img src="./assets/roster/042.jpg" alt="XXD Panel 042 · Deconstructed Watercolor Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-042"><strong>042</strong> · Deconstructed Watercolor Journal</a><br><sub>Opens your photo&#x27;s subject layer by layer along its real structure, painted as a watercolour study you could reassemble.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-043"><img src="./assets/roster/043.jpg" alt="XXD Panel 043 · White Foam" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-043"><strong>043</strong> · White Foam</a><br><sub>Redraws your photo&#x27;s subject in real white soap foam on a dark, wet flat surface.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-044"><img src="./assets/roster/044.jpg" alt="XXD Panel 044 · Flat Pure Gold" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-044"><strong>044</strong> · Flat Pure Gold</a><br><sub>Presses the defining shape of your photo&#x27;s subject into a thin layer of pure gold on a dark ground.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-045"><img src="./assets/roster/045.jpg" alt="XXD Panel 045 · Cozy Block City" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-045"><strong>045</strong> · Cozy Block City</a><br><sub>Rebuilds the subject of your photo as a rounded, touchable block sculpture in gentle colours.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-046"><img src="./assets/roster/046.jpg" alt="XXD Panel 046 · Impasto Micro-World" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-046"><strong>046</strong> · Impasto Micro-World</a><br><sub>Rebuilds your photo as a bright, lively miniature landscape you can almost feel the thick paint of.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-047"><img src="./assets/roster/047.jpg" alt="XXD Panel 047 · Isometric Impasto Scene" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-047"><strong>047</strong> · Isometric Impasto Scene</a><br><sub>Turns your photo&#x27;s subject into a refined isometric miniature standing inside a field of living impasto paint.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-048"><img src="./assets/roster/048.jpg" alt="XXD Panel 048 · Transparent Structure Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-048"><strong>048</strong> · Transparent Structure Journal</a><br><sub>Makes the subject of your photo semi-transparent and draws its structural logic as a clear blueprint.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-049"><img src="./assets/roster/049.jpg" alt="XXD Panel 049 · Woodcut Mark" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-049"><strong>049</strong> · Woodcut Mark</a><br><sub>Carves the most moving part of your photo into a fresh, soft limited-colour woodcut print.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-050"><img src="./assets/roster/050.jpg" alt="XXD Panel 050 · Travel Postcard" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-050"><strong>050</strong> · Travel Postcard</a><br><sub>Turns each photo into its own airy-blue minimalist travel poster.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>051–100</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-051"><img src="./assets/roster/051.jpg" alt="XXD Panel 051 · Handmade Miniature Island" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-051"><strong>051</strong> · Handmade Miniature Island</a><br><sub>Turns the subject of your photo into a light, touchable handmade paper-craft miniature.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-052"><img src="./assets/roster/052.jpg" alt="XXD Panel 052 · Paper Miniature Island" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-052"><strong>052</strong> · Paper Miniature Island</a><br><sub>Turns the world in your photo into a handmade paper miniature floating gently along one landscape line.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-053"><img src="./assets/roster/053.jpg" alt="XXD Panel 053 · Pen-and-Wash Record" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-053"><strong>053</strong> · Pen-and-Wash Record</a><br><sub>Records your photo in observed pen lines and a few touches of wash, stopping exactly where it should.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-054"><img src="./assets/roster/054.jpg" alt="XXD Panel 054 · Memory Sticker Album" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-054"><strong>054</strong> · Memory Sticker Album</a><br><sub>Splits one memory into a main image and six stickers of unequal size.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-055"><img src="./assets/roster/055.jpg" alt="XXD Panel 055 · Painted Memory Field" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-055"><strong>055</strong> · Painted Memory Field</a><br><sub>Paints a beam of light, a gesture and a spatial relationship from your photo as one gentle picture.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-056"><img src="./assets/roster/056.jpg" alt="XXD Panel 056 · Negative-Space Memory Painting" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-056"><strong>056</strong> · Negative-Space Memory Painting</a><br><sub>Keeps one core image from your photo and repaints it in vast whitespace with naive brushwork and warm–cool colour jumps.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-057"><img src="./assets/roster/057.jpg" alt="XXD Panel 057 · Geometric Memory Field" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-057"><strong>057</strong> · Geometric Memory Field</a><br><sub>Rebuilds your photo as a quiet, warm modern collage of geometric blocks and ordered mosaic.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-058"><img src="./assets/roster/058.jpg" alt="XXD Panel 058 · Poetic Conceptual Scene" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-058"><strong>058</strong> · Poetic Conceptual Scene</a><br><sub>Reads what your photo implies and builds it, with rigorous geometry, into a poetic conceptual landscape.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-059"><img src="./assets/roster/059.jpg" alt="XXD Panel 059 · Hand-Drawn Fable Book" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-059"><strong>059</strong> · Hand-Drawn Fable Book</a><br><sub>Draws the story your photo leaves unsaid as a page from a warm, childlike and quietly clever fable book.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-060"><img src="./assets/roster/060.jpg" alt="XXD Panel 060 · Zen Minimalist Poem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-060"><strong>060</strong> · Zen Minimalist Poem</a><br><sub>Distils your photo into one to three black forms and vast whitespace, a quiet visual thought that lingers.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-061"><img src="./assets/roster/061.jpg" alt="XXD Panel 061 · Visual Memory Notebook" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-061"><strong>061</strong> · Visual Memory Notebook</a><br><sub>Reorganises your photo into a few scattered memory fragments that echo one another across the page.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-062"><img src="./assets/roster/062.jpg" alt="XXD Panel 062 · Clever Clumsy Line" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-062"><strong>062</strong> · Clever Clumsy Line</a><br><sub>Draws the one moment worth remembering in your photo with naive black lines and a single colour from the photo.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-063"><img src="./assets/roster/063.jpg" alt="XXD Panel 063 · Pixel Metaphor Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-063"><strong>063</strong> · Pixel Metaphor Journal</a><br><sub>Rebuilds your photo as a quiet metaphor made of one large pixel outline and a few soft colour blocks.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-064"><img src="./assets/roster/064.jpg" alt="XXD Panel 064 · Indie Collage Page" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-064"><strong>064</strong> · Indie Collage Page</a><br><sub>Turns a photo into a quiet, incomplete old-paper collage page that feels like a personal archive.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-065"><img src="./assets/roster/065.jpg" alt="XXD Panel 065 · Two-Line Editorial Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-065"><strong>065</strong> · Two-Line Editorial Journal</a><br><sub>Draws your photo with a black line skeleton and two photo colours that slip off-register like old two-colour printing.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-066"><img src="./assets/roster/066.jpg" alt="XXD Panel 066 · Innocent Narrative Line" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-066"><strong>066</strong> · Innocent Narrative Line</a><br><sub>Retells the action and relationship in your photo as a small childlike story in loose black lines and soft flat colour.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-067"><img src="./assets/roster/067.jpg" alt="XXD Panel 067 · Everyday Humor Drawing" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-067"><strong>067</strong> · Everyday Humor Drawing</a><br><sub>Records a funny moment from your photo as a private notebook page, drawn only in red and blue ink.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-068"><img src="./assets/roster/068.jpg" alt="XXD Panel 068 · Eastern Freehand Album" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-068"><strong>068</strong> · Eastern Freehand Album</a><br><sub>Repaints your photo the Eastern way, with freehand ink lines, light washes and generous blank paper.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-069"><img src="./assets/roster/069.jpg" alt="XXD Panel 069 · Vivid Smear Window" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-069"><strong>069</strong> · Vivid Smear Window</a><br><sub>Brushes a bold painted window with a few wide strokes and lets your subject step out of it in bright colour.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-070"><img src="./assets/roster/070.jpg" alt="XXD Panel 070 · Impasto Cozy Island" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-070"><strong>070</strong> · Impasto Cozy Island</a><br><sub>Paints the subject of your photo as a small, bright island resting in a wide field of warm white.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-071"><img src="./assets/roster/071.jpg" alt="XXD Panel 071 · Pastel Poetry Notebook" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-071"><strong>071</strong> · Pastel Poetry Notebook</a><br><sub>Turns your photo into a few pastel memory fragments floating on near-white paper, with a loose handwritten poem.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-072"><img src="./assets/roster/072.jpg" alt="XXD Panel 072 · Bright Color Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-072"><strong>072</strong> · Bright Color Journal</a><br><sub>Abstracts your photo into bright frosted-glass geometry, sharp in some places and hazy in others.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-073"><img src="./assets/roster/073.jpg" alt="XXD Panel 073 · Geometric City Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-073"><strong>073</strong> · Geometric City Journal</a><br><sub>Rebuilds your photo as a cutaway isometric miniature building wrapped in scaffolding.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-074"><img src="./assets/roster/074.jpg" alt="XXD Panel 074 · Mood Icon Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-074"><strong>074</strong> · Mood Icon Journal</a><br><sub>Distils the subject and mood of your photo into one front-facing, matte, layered rounded-square icon.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-075"><img src="./assets/roster/075.jpg" alt="XXD Panel 075 · Dark Crayon Sketch" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-075"><strong>075</strong> · Dark Crayon Sketch</a><br><sub>Leaves the one mark worth remembering from your photo in dark crayon on off-white handmade paper.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-076"><img src="./assets/roster/076.jpg" alt="XXD Panel 076 · Macaron Crayon" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-076"><strong>076</strong> · Macaron Crayon</a><br><sub>Draws your photo as a warm travel memory in rough dark crayon and bright macaron colour.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-077"><img src="./assets/roster/077.jpg" alt="XXD Panel 077 · Travel Magazine Illustration" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-077"><strong>077</strong> · Travel Magazine Illustration</a><br><sub>Turns your photo into a layered paper-cut travel magazine page with soft shadows and English type.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-078"><img src="./assets/roster/078.jpg" alt="XXD Panel 078 · Gold-Leaf Embossed Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-078"><strong>078</strong> · Gold-Leaf Embossed Journal</a><br><sub>Draws the defining outline of your photo in fine line and presses it deep into ivory cotton paper in champagne-gold foil.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-079"><img src="./assets/roster/079.jpg" alt="XXD Panel 079 · Pen-and-Wash Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-079"><strong>079</strong> · Pen-and-Wash Journal</a><br><sub>Draws your photo as a half-finished on-site sketch of geometric lines, free ink and a few light washes.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-080"><img src="./assets/roster/080.jpg" alt="XXD Panel 080 · Organic Gouache Field" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-080"><strong>080</strong> · Organic Gouache Field</a><br><sub>Places the mood of your photo and one small metaphor into wide whitespace, in soft organic shapes and botanical-coloured gouache.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-081"><img src="./assets/roster/081.jpg" alt="XXD Panel 081 · Colored-Thread Keepsake Album" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-081"><strong>081</strong> · Colored-Thread Keepsake Album</a><br><sub>Draws your photo in even-weight lines of two to four of its own colours, as a limited-ink personal keepsake poster.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-082"><img src="./assets/roster/082.jpg" alt="XXD Panel 082 · Watercolor Off the Page" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-082"><strong>082</strong> · Watercolor Off the Page</a><br><sub>Lets the one main subject of your photo stand up out of a loose watercolour patch as a naive little 3D world.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-083"><img src="./assets/roster/083.jpg" alt="XXD Panel 083 · Ugly-Cute Character Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-083"><strong>083</strong> · Ugly-Cute Character Journal</a><br><sub>Keeps one subject from your photo and draws its funniest trait deliberately ugly and clumsy, yet instantly recognisable.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-084"><img src="./assets/roster/084.jpg" alt="XXD Panel 084 · Stipple-and-Line Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-084"><strong>084</strong> · Stipple-and-Line Journal</a><br><sub>Draws your photo as a quiet city sketch in fine geometric lines and dots of varying density.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-085"><img src="./assets/roster/085.jpg" alt="XXD Panel 085 · Handmade Model Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-085"><strong>085</strong> · Handmade Model Journal</a><br><sub>Builds your photo into a tiny handmade stage of clay, felt, cut paper and string, set in wide whitespace.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-086"><img src="./assets/roster/086.jpg" alt="XXD Panel 086 · Negative-Space Print Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-086"><strong>086</strong> · Negative-Space Print Journal</a><br><sub>Keeps three to five key facts from your photo and presses them into a whitespace-led, limited-colour screen print.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-087"><img src="./assets/roster/087.jpg" alt="XXD Panel 087 · Red-Thread Relationship Map" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-087"><strong>087</strong> · Red-Thread Relationship Map</a><br><sub>Breaks your photo into pins and links them with vermilion string into a map of how its parts relate.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-088"><img src="./assets/roster/088.jpg" alt="XXD Panel 088 · Typographic Form Poem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-088"><strong>088</strong> · Typographic Form Poem</a><br><sub>Builds the subject of your photo out of words, punctuation and dots: an image from afar, all type up close.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-089"><img src="./assets/roster/089.jpg" alt="XXD Panel 089 · Everyday Vignette Notebook" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-089"><strong>089</strong> · Everyday Vignette Notebook</a><br><sub>Breaks your photo into one main vignette and a few small everyday fragments, laid out as a relaxed journal page.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-090"><img src="./assets/roster/090.jpg" alt="XXD Panel 090 · Visual Thinking Map" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-090"><strong>090</strong> · Visual Thinking Map</a><br><sub>Instead of drawing what is in your photo, maps the relationships and meaning behind it as visual thinking.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-091"><img src="./assets/roster/091.jpg" alt="XXD Panel 091 · Blue-Line Travel Album" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-091"><strong>091</strong> · Blue-Line Travel Album</a><br><sub>Draws your photo with a single blue pen as a travel sketch that stops once it has seen enough.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-092"><img src="./assets/roster/092.jpg" alt="XXD Panel 092 · Expressive Line Drawing Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-092"><strong>092</strong> · Expressive Line Drawing Journal</a><br><sub>Turns a photo into a black-and-white pen drawing of loose contours, layered hatching and open paper.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-093"><img src="./assets/roster/093.jpg" alt="XXD Panel 093 · Modern Geometric Painting" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-093"><strong>093</strong> · Modern Geometric Painting</a><br><sub>Compresses a photo into bright, matte, slightly hand-edged modernist blocks of geometric colour.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-094"><img src="./assets/roster/094.jpg" alt="XXD Panel 094 · Classic Two-Color Book" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-094"><strong>094</strong> · Classic Two-Color Book</a><br><sub>Turns a photo into an old book plate of fine ink lines, one spot colour and wide open paper.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-095"><img src="./assets/roster/095.jpg" alt="XXD Panel 095 · Red-and-Black Diagram Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-095"><strong>095</strong> · Red-and-Black Diagram Journal</a><br><sub>Explains what is in a photo with black technical lines, red spot colour and a few small diagrams.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-096"><img src="./assets/roster/096.jpg" alt="XXD Panel 096 · Folk Correspondence Card" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-096"><strong>096</strong> · Folk Correspondence Card</a><br><sub>Turns a photo into an old QSL card that looks typed, photocopied and actually posted.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-097"><img src="./assets/roster/097.jpg" alt="XXD Panel 097 · Retro Instruction Card" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-097"><strong>097</strong> · Retro Instruction Card</a><br><sub>Compresses a photo into a useful, slightly funny two-colour diagram, like an old instruction card.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-098"><img src="./assets/roster/098.jpg" alt="XXD Panel 098 · Naive Watercolor Book" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-098"><strong>098</strong> · Naive Watercolor Book</a><br><sub>Retells a photo as a bright, loose, deliberately imperfect picture-book page.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-099"><img src="./assets/roster/099.jpg" alt="XXD Panel 099 · Typeface Mascot" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-099"><strong>099</strong> · Typeface Mascot</a><br><sub>Redesigns the star of your photo as a memorable mascot in front of one line of giant type.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-100"><img src="./assets/roster/100.jpg" alt="XXD Panel 100 · Folk-Craft Narrative Painting" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-100"><strong>100</strong> · Folk-Craft Narrative Painting</a><br><sub>Turns a photo into a small, naive folk story with crayon grain and an everyday feel.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>101–150</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-101"><img src="./assets/roster/101.jpg" alt="XXD Panel 101 · Nine-Cell Memory Notebook" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-101"><strong>101</strong> · Nine-Cell Memory Notebook</a><br><sub>Breaks one photo into nine small doodled memories laid out like a personal journal page.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-102"><img src="./assets/roster/102.jpg" alt="XXD Panel 102 · Healing Geometry Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-102"><strong>102</strong> · Healing Geometry Journal</a><br><sub>Distils a photo into one calm, clear, quietly lively geometric figure.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-103"><img src="./assets/roster/103.jpg" alt="XXD Panel 103 · Vivid Abstract Assembly" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-103"><strong>103</strong> · Vivid Abstract Assembly</a><br><sub>Breaks a photo into bright colour blocks and rough hand-drawn lines, reassembled as an abstract picture.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-104"><img src="./assets/roster/104.jpg" alt="XXD Panel 104 · Halftone Zen Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-104"><strong>104</strong> · Halftone Zen Journal</a><br><sub>Distils a photo into a halftone-dot form, a few coloured lines and quiet open space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-105"><img src="./assets/roster/105.jpg" alt="XXD Panel 105 · Poetic Space Anthology" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-105"><strong>105</strong> · Poetic Space Anthology</a><br><sub>Picks the single most beautiful moment in a photo and turns it into a quiet, minimal paper collage.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-106"><img src="./assets/roster/106.jpg" alt="XXD Panel 106 · Pastel Pixel Memory" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-106"><strong>106</strong> · Pastel Pixel Memory</a><br><sub>Strips a photo down to two or three key shapes, then remembers it again in soft pastel pixels.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-107"><img src="./assets/roster/107.jpg" alt="XXD Panel 107 · Image-Word Poetry" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-107"><strong>107</strong> · Image-Word Poetry</a><br><sub>Draws a photo&#x27;s flowers, windows, roads and wind as small pictures that stand in for words in a short poem.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-108"><img src="./assets/roster/108.jpg" alt="XXD Panel 108 · New Folk Paper-Cut Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-108"><strong>108</strong> · New Folk Paper-Cut Journal</a><br><sub>Cuts the most recognisable shapes of a photo into a quiet, folk-flavoured coloured-paper collage.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-109"><img src="./assets/roster/109.jpg" alt="XXD Panel 109 · Soft Geometric Deconstruction" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-109"><strong>109</strong> · Soft Geometric Deconstruction</a><br><sub>Breaks a photo into a few large, whole blocks, then reassembles a recognisable figure in soft colours.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-110"><img src="./assets/roster/110.jpg" alt="XXD Panel 110 · Japanese-Style Everyday Scene Atlas" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-110"><strong>110</strong> · Japanese-Style Everyday Scene Atlas</a><br><sub>Arranges the small things worth remembering in a photo into an everyday map with routes and room to breathe.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-111"><img src="./assets/roster/111.jpg" alt="XXD Panel 111 · Textile Collage Chronicle" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-111"><strong>111</strong> · Textile Collage Chronicle</a><br><sub>Sews the most memorable relationship in a photo into a small, warm fabric collage.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-112"><img src="./assets/roster/112.jpg" alt="XXD Panel 112 · Gold-Line Paper Chronicle" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-112"><strong>112</strong> · Gold-Line Paper Chronicle</a><br><sub>Lets one irregular band of paper colour hold a small, quiet memory with a hint of gold.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-113"><img src="./assets/roster/113.jpg" alt="XXD Panel 113 · Shell-fragment Pixel Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-113"><strong>113</strong> · Shell-fragment Pixel Collage</a><br><sub>Builds the subject of a photo from fewer than two hundred shell tiles that slowly scatter into white space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-114"><img src="./assets/roster/114.jpg" alt="XXD Panel 114 · Retro Pastel Scrapbook Doodles" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-114"><strong>114</strong> · Retro Pastel Scrapbook Doodles</a><br><sub>Redraws a photo as a pastel scrapbook doodle collage on paper that can breathe.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-115"><img src="./assets/roster/115.jpg" alt="XXD Panel 115 · Pastel Stamp Collage Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-115"><strong>115</strong> · Pastel Stamp Collage Journal</a><br><sub>Draws the core memory of a photo as a small pastel doodle stamp on vintage paper.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-116"><img src="./assets/roster/116.jpg" alt="XXD Panel 116 · Pale-Paper Pastel Doodle Chronicle" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-116"><strong>116</strong> · Pale-Paper Pastel Doodle Chronicle</a><br><sub>Leaves the clear outline of a photo on very pale paper in thick, grainy coloured crayon.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-117"><img src="./assets/roster/117.jpg" alt="XXD Panel 117 · Fine-Line Pastel Whitespace Chronicle" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-117"><strong>117</strong> · Fine-Line Pastel Whitespace Chronicle</a><br><sub>Takes one visual anchor from a photo and recomposes it in fine lines and pale washes with lots of space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-118"><img src="./assets/roster/118.jpg" alt="XXD Panel 118 · Graphite Whitespace Sketch Chronicle" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-118"><strong>118</strong> · Graphite Whitespace Sketch Chronicle</a><br><sub>Keeps the relationships worth remembering in a photo, then recomposes them with pencil and open space.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-119"><img src="./assets/roster/119.jpg" alt="XXD Panel 119 · Hand-Sewn Textile &amp; Negative Space Chronicle" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-119"><strong>119</strong> · Hand-Sewn Textile &amp; Negative Space Chronicle</a><br><sub>Lets a few pieces of fabric and some stitches carry the warmest memory in a photo.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-120"><img src="./assets/roster/120.jpg" alt="XXD Panel 120 · Architectural Concept Sketch Chronicle" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-120"><strong>120</strong> · Architectural Concept Sketch Chronicle</a><br><sub>Turns the spatial memory in a photo into an architectural concept sketch with plenty of room.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-121"><img src="./assets/roster/121.jpg" alt="XXD Panel 121 · Lifestyle Doodle Editorial" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-121"><strong>121</strong> · Lifestyle Doodle Editorial</a><br><sub>Turns a small everyday emotion into a spacious lifestyle illustration where picture and words work together.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-122"><img src="./assets/roster/122.jpg" alt="XXD Panel 122 · Monochrome Halftone Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-122"><strong>122</strong> · Monochrome Halftone Journal</a><br><sub>Turns the subject of your photo into a small black-and-grey halftone print with a single line of red handwriting.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-123"><img src="./assets/roster/123.jpg" alt="XXD Panel 123 · Red–Blue Angular Pencil" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-123"><strong>123</strong> · Red–Blue Angular Pencil</a><br><sub>Redraws your photo&#x27;s subject in red and blue coloured pencil with angular, tense lines and lots of empty space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-124"><img src="./assets/roster/124.jpg" alt="XXD Panel 124 · Fabric Collage Whitespace" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-124"><strong>124</strong> · Fabric Collage Whitespace</a><br><sub>Pieces your photo&#x27;s subject together from a few large fabric patches and stitches, like a warm appliqué picture.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-125"><img src="./assets/roster/125.jpg" alt="XXD Panel 125 · Naïve Crayon Whitespace" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-125"><strong>125</strong> · Naïve Crayon Whitespace</a><br><sub>Draws your photo&#x27;s subject in childlike crayon and oil pastel, like a small picture-book stamp with one bright accent.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-126"><img src="./assets/roster/126.jpg" alt="XXD Panel 126 · Poetic Miniature Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-126"><strong>126</strong> · Poetic Miniature Collage</a><br><sub>Shrinks your photo into a postage-stamp-sized watercolour and torn-paper collage on a wide sheet of handmade paper.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-127"><img src="./assets/roster/127.jpg" alt="XXD Panel 127 · Mixed-media Architectural Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-127"><strong>127</strong> · Mixed-media Architectural Collage</a><br><sub>Turns your photo into a small collage like an architect&#x27;s study sheet, with a few structural lines and handwritten notes.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-128"><img src="./assets/roster/128.jpg" alt="XXD Panel 128 · Enamel Medallion Travel" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-128"><strong>128</strong> · Enamel Medallion Travel</a><br><sub>Presses your photo into a round enamel souvenir medallion with a few elegant serif lines, like a minimalist travel poster.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-129"><img src="./assets/roster/129.jpg" alt="XXD Panel 129 · Eastern Diffused Whitespace" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-129"><strong>129</strong> · Eastern Diffused Whitespace</a><br><sub>Turns your photo into an Eastern silhouette symbol beside one large block of colour with soft, glowing edges.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-130"><img src="./assets/roster/130.jpg" alt="XXD Panel 130 · Hard-edge Faceted Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-130"><strong>130</strong> · Hard-edge Faceted Collage</a><br><sub>Cuts your photo&#x27;s subject into hard-edged black, white and grey planes with one or two strong accent colours.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-131"><img src="./assets/roster/131.jpg" alt="XXD Panel 131 · Doodle Photo Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-131"><strong>131</strong> · Doodle Photo Collage</a><br><sub>Cuts your photo into a small cluster of pieces on white paper, then adds rough black frames and a few doodles.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-132"><img src="./assets/roster/132.jpg" alt="XXD Panel 132 · Pen-and-Wash Travel" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-132"><strong>132</strong> · Pen-and-Wash Travel</a><br><sub>Sketches your photo with wobbly pen lines and a few warm washes, as a postage-stamp-sized urban sketch.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-133"><img src="./assets/roster/133.jpg" alt="XXD Panel 133 · Stipple Transparent Overprint" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-133"><strong>133</strong> · Stipple Transparent Overprint</a><br><sub>Overprints your photo&#x27;s subject in layers of one translucent ink, darker where they overlap, with fine stippling for volume.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-134"><img src="./assets/roster/134.jpg" alt="XXD Panel 134 · Picture-book Colour-field Story" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-134"><strong>134</strong> · Picture-book Colour-field Story</a><br><sub>Empty space above, a small story subject in the middle and a broad band of mixed colour below, like a picture-book page.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-135"><img src="./assets/roster/135.jpg" alt="XXD Panel 135 · Street Spot-colour Zine" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-135"><strong>135</strong> · Street Spot-colour Zine</a><br><sub>Turns your photo into a street-zine poster with rough hand-drawn lines, a few clashing spot colours and print grain.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-136"><img src="./assets/roster/136.jpg" alt="XXD Panel 136 · Poetic Surrealist Whitespace" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-136"><strong>136</strong> · Poetic Surrealist Whitespace</a><br><sub>Rewrites your photo as a small naive surrealist painting on canvas, built around one absurd yet fitting idea.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-137"><img src="./assets/roster/137.jpg" alt="XXD Panel 137 · Etching Texture Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-137"><strong>137</strong> · Etching Texture Collage</a><br><sub>Draws a tiny subject in fine etching lines, then lays one or two rough printed colour blocks over it.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-138"><img src="./assets/roster/138.jpg" alt="XXD Panel 138 · Oriental Paper Relief" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-138"><strong>138</strong> · Oriental Paper Relief</a><br><sub>Folds, embosses and cuts handmade paper into a tiny shallow relief of your photo on a white page.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-139"><img src="./assets/roster/139.jpg" alt="XXD Panel 139 · Text-encoded Linear Fields" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-139"><strong>139</strong> · Text-encoded Linear Fields</a><br><sub>Encodes your photo as a small field of hairline horizontal and vertical lines: abstract from afar, faintly recognisable up close.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-140"><img src="./assets/roster/140.jpg" alt="XXD Panel 140 · Dry-media Visual Island" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-140"><strong>140</strong> · Dry-media Visual Island</a><br><sub>Distils your photo into a small gouache and oil-pastel island in the middle of a white page, like a kept memory.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-141"><img src="./assets/roster/141.jpg" alt="XXD Panel 141 · Minimal Hand-drawn Lines" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-141"><strong>141</strong> · Minimal Hand-drawn Lines</a><br><sub>Traces your photo&#x27;s subject in a few slim, slightly shaky hand-drawn lines, surrounded almost entirely by white space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-142"><img src="./assets/roster/142.jpg" alt="XXD Panel 142 · Extended Type–Image Masks" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-142"><strong>142</strong> · Extended Type–Image Masks</a><br><sub>Draws one word from your photo and masks the subject inside stretched, extended letterforms so type and image become one.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-143"><img src="./assets/roster/143.jpg" alt="XXD Panel 143 · Calligram Visual Poetry" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-143"><strong>143</strong> · Calligram Visual Poetry</a><br><sub>Builds your photo&#x27;s subject out of words taken from the photo: an image from afar, all text up close.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-144"><img src="./assets/roster/144.jpg" alt="XXD Panel 144 · Geometric Knockout Linework" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-144"><strong>144</strong> · Geometric Knockout Linework</a><br><sub>Redraws your photo&#x27;s subject in fine lines over one geometric colour block: knocked out in white inside it, back to line outside.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-145"><img src="./assets/roster/145.jpg" alt="XXD Panel 145 · Vintage Spot-colour Printmaking" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-145"><strong>145</strong> · Vintage Spot-colour Printmaking</a><br><sub>Prints your photo as a small vintage vignette in engraved hatching, stippling and halftone, overprinted in a few spot colours.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-146"><img src="./assets/roster/146.jpg" alt="XXD Panel 146 · Natural-history Scarf Illustration" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-146"><strong>146</strong> · Natural-history Scarf Illustration</a><br><sub>Draws your photo&#x27;s subject as a natural-history motif in fine engraved lines and a few bright flat colours, like a silk-scarf print.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-147"><img src="./assets/roster/147.jpg" alt="XXD Panel 147 · Bento Food Packaging" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-147"><strong>147</strong> · Bento Food Packaging</a><br><sub>Swaps everything in your photo for food, packs it into a clear convenience-store deli box and shoots it from above.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-148"><img src="./assets/roster/148.jpg" alt="XXD Panel 148 · Visual Journal Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-148"><strong>148</strong> · Visual Journal Collage</a><br><sub>Turns your photo into a private journal page of photo pieces, sticky notes, tape, tickets and handwriting, with lots of space.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-149"><img src="./assets/roster/149.jpg" alt="XXD Panel 149 · Textured Hand-drawn Flat Art" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-149"><strong>149</strong> · Textured Hand-drawn Flat Art</a><br><sub>Rebuilds your photo&#x27;s subject from large colour blocks with paper grain and pastel texture, like a cut-paper collage.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-150"><img src="./assets/roster/150.jpg" alt="XXD Panel 150 · Retro Modern Cut-paper" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-150"><strong>150</strong> · Retro Modern Cut-paper</a><br><sub>Cuts your photo into silhouettes and geometric and organic shapes of coloured paper, like a small mid-century modern collage.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>151–200</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-151"><img src="./assets/roster/151.jpg" alt="XXD Panel 151 · Naive Flat Hand Drawing" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-151"><strong>151</strong> · Naive Flat Hand Drawing</a><br><sub>Draws only the most characterful part of your photo in flat colour blocks and wobbly hand-drawn lines.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-152"><img src="./assets/roster/152.jpg" alt="XXD Panel 152 · Colour-field Paper Base" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-152"><strong>152</strong> · Colour-field Paper Base</a><br><sub>Cuts the subject of your photo into a few paper shapes and sets them on a solid colour band.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-153"><img src="./assets/roster/153.jpg" alt="XXD Panel 153 · Monochrome Journal Doodles" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-153"><strong>153</strong> · Monochrome Journal Doodles</a><br><sub>Draws the star of your photo as if with one green felt-tip pen on grid paper.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-154"><img src="./assets/roster/154.jpg" alt="XXD Panel 154 · Retro Pixel Whitespace" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-154"><strong>154</strong> · Retro Pixel Whitespace</a><br><sub>Turns the star of your photo into a small 16-bit-style pixel sprite surrounded by open space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-155"><img src="./assets/roster/155.jpg" alt="XXD Panel 155 · One-point Perspective Light Wash" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-155"><strong>155</strong> · One-point Perspective Light Wash</a><br><sub>Draws your photo as a one-point-perspective pen sketch with a very pale watercolour wash.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-156"><img src="./assets/roster/156.jpg" alt="XXD Panel 156 · Duotone Misregistered Illustration" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-156"><strong>156</strong> · Duotone Misregistered Illustration</a><br><sub>Prints the star of your photo in just two inks, as a small Risograph-style illustration slightly off register.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-157"><img src="./assets/roster/157.jpg" alt="XXD Panel 157 · Archaeological Ink Rubbing" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-157"><strong>157</strong> · Archaeological Ink Rubbing</a><br><sub>Turns the star of your photo into an ancient stone rubbing, patchy and worn, resting on a wide sheet of paper.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-158"><img src="./assets/roster/158.jpg" alt="XXD Panel 158 · Mixed-media Collage on Paper" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-158"><strong>158</strong> · Mixed-media Collage on Paper</a><br><sub>Builds the star of your photo from torn book pages, newspaper scraps and loose pencil lines.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-159"><img src="./assets/roster/159.jpg" alt="XXD Panel 159 · Post-digital Bitmap Typography" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-159"><strong>159</strong> · Post-digital Bitmap Typography</a><br><sub>Rebuilds the star of your photo from characters, dot matrix and halftone, with a bitmap title woven into it.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-160"><img src="./assets/roster/160.jpg" alt="XXD Panel 160 · Expressive Pen-and-wash Illustration" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-160"><strong>160</strong> · Expressive Pen-and-wash Illustration</a><br><sub>Sketches the star of your photo in loose ink lines with a few strokes of transparent watercolour.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-161"><img src="./assets/roster/161.jpg" alt="XXD Panel 161 · Frame-breaking Painted Colour Field" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-161"><strong>161</strong> · Frame-breaking Painted Colour Field</a><br><sub>Paints a small hand-brushed colour block on white paper as a second canvas, with the subject spilling just past its edge.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-162"><img src="./assets/roster/162.jpg" alt="XXD Panel 162 · Storybook Illustration on White Cutout" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-162"><strong>162</strong> · Storybook Illustration on White Cutout</a><br><sub>Draws the star of your photo as a crayon-textured picture-book figure on a hand-cut white paper backing.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-163"><img src="./assets/roster/163.jpg" alt="XXD Panel 163 · Centred Flat-colour Stamp Composition" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-163"><strong>163</strong> · Centred Flat-colour Stamp Composition</a><br><sub>Distils the star of your photo into a small emblem of clean flat colours, placed dead centre.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-164"><img src="./assets/roster/164.jpg" alt="XXD Panel 164 · Ink-wash Architectural Miniature" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-164"><strong>164</strong> · Ink-wash Architectural Miniature</a><br><sub>Turns your photo into a tiny architectural scene in a pale ink landscape, drawn like an architect&#x27;s sketch with one touch of orange.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-165"><img src="./assets/roster/165.jpg" alt="XXD Panel 165 · Central Torn-paper Reveal Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-165"><strong>165</strong> · Central Torn-paper Reveal Collage</a><br><sub>Tears a gap down the middle of a pale sheet of paper and reveals the star of your photo inside in geometric colour blocks.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-166"><img src="./assets/roster/166.jpg" alt="XXD Panel 166 · Sculptural Isometric Bas-relief Diorama" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-166"><strong>166</strong> · Sculptural Isometric Bas-relief Diorama</a><br><sub>Builds the star of your photo into an isometric miniature model that rises in layers like a low relief.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-167"><img src="./assets/roster/167.jpg" alt="XXD Panel 167 · Centred Wave-form Raised-ink Relief" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-167"><strong>167</strong> · Centred Wave-form Raised-ink Relief</a><br><sub>Sets the star of your photo on a centred abstract wave, printed as if in thick raised ink.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-168"><img src="./assets/roster/168.jpg" alt="XXD Panel 168 · Reserved-white Layered Painted Field" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-168"><strong>168</strong> · Reserved-white Layered Painted Field</a><br><sub>Brushes a layered warm colour field onto white paper, and the star of your photo is the white left unpainted.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-169"><img src="./assets/roster/169.jpg" alt="XXD Panel 169 · Warm Ochre Ink-line Spot Illustration" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-169"><strong>169</strong> · Warm Ochre Ink-line Spot Illustration</a><br><sub>Draws the star of your photo as a small, isolated ink sketch with ochre wash, stopping once the key part is down.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-170"><img src="./assets/roster/170.jpg" alt="XXD Panel 170 · Black and Rust-red Dry-media Spot" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-170"><strong>170</strong> · Black and Rust-red Dry-media Spot</a><br><sub>Draws the star of your photo as a tiny spot illustration in a few rough crayon strokes of charcoal black and a little rust red.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-171"><img src="./assets/roster/171.jpg" alt="XXD Panel 171 · Vertical Skeleton and Tiny Vignettes" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-171"><strong>171</strong> · Vertical Skeleton and Tiny Vignettes</a><br><sub>Stands a few faint vertical lines in wide warm white and scatters the people and things from your photo like tiny islands.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-172"><img src="./assets/roster/172.jpg" alt="XXD Panel 172 · Centred Subject with Translucent Geometry" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-172"><strong>172</strong> · Centred Subject with Translucent Geometry</a><br><sub>Places the star of your photo small and dead centre, with a few faint translucent geometric shapes floating behind it.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-173"><img src="./assets/roster/173.jpg" alt="XXD Panel 173 · Ivory Paper-text Miniature Landscape" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-173"><strong>173</strong> · Ivory Paper-text Miniature Landscape</a><br><sub>Compresses your photo into a tiny paper scene built from old book pages and text, floating in wide warm white.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-174"><img src="./assets/roster/174.jpg" alt="XXD Panel 174 · Naive Hand-drawn Sticker Assemblage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-174"><strong>174</strong> · Naive Hand-drawn Sticker Assemblage</a><br><sub>Breaks the star of your photo into chunky hand-drawn stickers and clusters them back into one figure in the centre.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-175"><img src="./assets/roster/175.jpg" alt="XXD Panel 175 · Amber-backlit Ivory Paper-cut Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-175"><strong>175</strong> · Amber-backlit Ivory Paper-cut Vignette</a><br><sub>Turns your photo into a small layered ivory paper sculpture with warm amber light glowing between the layers.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-176"><img src="./assets/roster/176.jpg" alt="XXD Panel 176 · Hand-drawn Ritual Diagram in Shallow Relief" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-176"><strong>176</strong> · Hand-drawn Ritual Diagram in Shallow Relief</a><br><sub>Seats the star of your photo at the centre of an intricate fine-line ritual diagram that rises in layers and opens outward.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-177"><img src="./assets/roster/177.jpg" alt="XXD Panel 177 · Irregular Silhouette Woodcut Micro-island" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-177"><strong>177</strong> · Irregular Silhouette Woodcut Micro-island</a><br><sub>Compresses the heart of your photo into one small, irregular print-style island in ink navy, grey-olive and a dot of vermilion.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-178"><img src="./assets/roster/178.jpg" alt="XXD Panel 178 · Diary Ink Mark" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-178"><strong>178</strong> · Diary Ink Mark</a><br><sub>Distils your photo into one small mark doodled in old ink, like a quick sketch in the corner of a diary.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-179"><img src="./assets/roster/179.jpg" alt="XXD Panel 179 · Ribbon-like Miniature Vignette Display" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-179"><strong>179</strong> · Ribbon-like Miniature Vignette Display</a><br><sub>Turns the heart of your photo into a few miniature exhibits spaced along a floating ivory ribbon.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-180"><img src="./assets/roster/180.jpg" alt="XXD Panel 180 · Vintage Circular Travel Stamp" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-180"><strong>180</strong> · Vintage Circular Travel Stamp</a><br><sub>Carves the star of your photo and one or two setting clues into a round vintage souvenir stamp on aged ivory paper.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-181"><img src="./assets/roster/181.jpg" alt="XXD Panel 181 · Literati Ink and Colour Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-181"><strong>181</strong> · Literati Ink and Colour Vignette</a><br><sub>Paints your photo as a small literati vignette, with ink as the backbone, light colour in support and plenty of empty space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-182"><img src="./assets/roster/182.jpg" alt="XXD Panel 182 · Miniature Pixel Graphic Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-182"><strong>182</strong> · Miniature Pixel Graphic Vignette</a><br><sub>Compresses the subject of a photo into a small hard-edged pixel graphic set quietly in wide whitespace.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-183"><img src="./assets/roster/183.jpg" alt="XXD Panel 183 · Dark Green Organic Corner Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-183"><strong>183</strong> · Dark Green Organic Corner Vignette</a><br><sub>Distils a photo&#x27;s subject into a small cluster of natural shapes in one corner, anchored by deep green.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-184"><img src="./assets/roster/184.jpg" alt="XXD Panel 184 · Hand-drawn Square Everyday Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-184"><strong>184</strong> · Hand-drawn Square Everyday Vignette</a><br><sub>Packs a photo&#x27;s everyday details into one small square scene in loose line and coloured-pencil wash.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-185"><img src="./assets/roster/185.jpg" alt="XXD Panel 185 · Monochrome Sticker with Pale Accent" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-185"><strong>185</strong> · Monochrome Sticker with Pale Accent</a><br><sub>Draws a photo&#x27;s subject as one small black-and-white hand-drawn sticker graphic with a single pale accent.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-186"><img src="./assets/roster/186.jpg" alt="XXD Panel 186 · Nine-cell Geometric Memory Grid" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-186"><strong>186</strong> · Nine-cell Geometric Memory Grid</a><br><sub>Breaks a photo into nine remembered fragments, arranged as a grid of soft flat geometric colour blocks.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-187"><img src="./assets/roster/187.jpg" alt="XXD Panel 187 · Archival Collage with Oversized Type" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-187"><strong>187</strong> · Archival Collage with Oversized Type</a><br><sub>Turns a photo&#x27;s subject into an archival collage of photo slices and drafting lines over oversized type.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-188"><img src="./assets/roster/188.jpg" alt="XXD Panel 188 · Warm Gold Architectural Archive" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-188"><strong>188</strong> · Warm Gold Architectural Archive</a><br><sub>Shrinks a photo&#x27;s subject to a small architectural specimen on old-paper whitespace with a sand-gold title.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-189"><img src="./assets/roster/189.jpg" alt="XXD Panel 189 · Double-frame Matchbox Label Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-189"><strong>189</strong> · Double-frame Matchbox Label Vignette</a><br><sub>Draws a photo as a small illustration on an old matchbox label, with double frames and a narrow side column.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-190"><img src="./assets/roster/190.jpg" alt="XXD Panel 190 · Naive Cool Pastel with Warm Accents" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-190"><strong>190</strong> · Naive Cool Pastel with Warm Accents</a><br><sub>Draws a photo as a small naive pastel vignette in cool greys, with only a touch of warm colour.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-191"><img src="./assets/roster/191.jpg" alt="XXD Panel 191 · Soft-edged Rectangular Pastel Field" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-191"><strong>191</strong> · Soft-edged Rectangular Pastel Field</a><br><sub>Paints a photo into a small frayed-edged rectangle of pastel colour floating in wide whitespace.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-192"><img src="./assets/roster/192.jpg" alt="XXD Panel 192 · Limited-colour Vintage Graphic Spot" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-192"><strong>192</strong> · Limited-colour Vintage Graphic Spot</a><br><sub>Compresses a photo into one small silhouette graphic printed on paper in two to four vintage colours.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-193"><img src="./assets/roster/193.jpg" alt="XXD Panel 193 · Muted Watercolour on a Low Base" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-193"><strong>193</strong> · Muted Watercolour on a Low Base</a><br><sub>Paints a photo as a few muted watercolour shapes resting on a pale low base, with bare paper around.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-194"><img src="./assets/roster/194.jpg" alt="XXD Panel 194 · Bright Axonometric Site-base Model" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-194"><strong>194</strong> · Bright Axonometric Site-base Model</a><br><sub>Turns a photo&#x27;s subject into a bright axonometric block model growing out of a flat site base.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-195"><img src="./assets/roster/195.jpg" alt="XXD Panel 195 · Archival Montage with One Bright Accent" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-195"><strong>195</strong> · Archival Montage with One Bright Accent</a><br><sub>Re-edits a photo into a black, white and warm-grey archival montage that keeps just one bright colour from it.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-196"><img src="./assets/roster/196.jpg" alt="XXD Panel 196 · Top-down Geometric Figure Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-196"><strong>196</strong> · Top-down Geometric Figure Vignette</a><br><sub>Looks down on the people in a photo and redraws them as flat geometric figures made of circles and capsules.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-197"><img src="./assets/roster/197.jpg" alt="XXD Panel 197 · Folk-art World Inside a Cage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-197"><strong>197</strong> · Folk-art World Inside a Cage</a><br><sub>Puts the theme of a photo inside a cage and draws it as a small world in flat, warm folk-art style.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-198"><img src="./assets/roster/198.jpg" alt="XXD Panel 198 · Limited-palette Floating Fashion Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-198"><strong>198</strong> · Limited-palette Floating Fashion Collage</a><br><sub>Draws a photo&#x27;s subject as a weightless fashion illustration in collage, halftone and a few colours.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-199"><img src="./assets/roster/199.jpg" alt="XXD Panel 199 · Bright Airy Miniature Fashion Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-199"><strong>199</strong> · Bright Airy Miniature Fashion Collage</a><br><sub>Shrinks a photo&#x27;s subject into small floating fashion figures set in wide, bright warm white.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-200"><img src="./assets/roster/200.jpg" alt="XXD Panel 200 · Blue-grey Monochrome Line Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-200"><strong>200</strong> · Blue-grey Monochrome Line Vignette</a><br><sub>Draws a photo as a small sketchy line vignette in relaxed lines of a single blue-grey.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>201–250</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-201"><img src="./assets/roster/201.jpg" alt="XXD Panel 201 · Cream-toned Handcrafted Miniature" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-201"><strong>201</strong> · Cream-toned Handcrafted Miniature</a><br><sub>Turns a photo&#x27;s subject into a small cream-toned handmade miniature, set quietly in wide whitespace.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-202"><img src="./assets/roster/202.jpg" alt="XXD Panel 202 · Geometric Line Diagram with Guide Axes" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-202"><strong>202</strong> · Geometric Line Diagram with Guide Axes</a><br><sub>Draws structural guide lines from a photo and hangs its subject on them as a blue-grey line diagram.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-203"><img src="./assets/roster/203.jpg" alt="XXD Panel 203 · Impasto Vignette Art Postcard" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-203"><strong>203</strong> · Impasto Vignette Art Postcard</a><br><sub>Paints a photo as a small impasto scene set in wide whitespace, like an art postcard.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-204"><img src="./assets/roster/204.jpg" alt="XXD Panel 204 · Soft-focus Light-memory Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-204"><strong>204</strong> · Soft-focus Light-memory Vignette</a><br><sub>Turns a photo&#x27;s subject into a small patch of soft-focus light, like a memory left by light.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-205"><img src="./assets/roster/205.jpg" alt="XXD Panel 205 · Warm Organic Photo and Line Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-205"><strong>205</strong> · Warm Organic Photo and Line Collage</a><br><sub>Crops a photo into a rounded organic shape with fine hand-drawn lines, warm tones and a terracotta accent.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-206"><img src="./assets/roster/206.jpg" alt="XXD Panel 206 · Soft-colour Layered Papercraft Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-206"><strong>206</strong> · Soft-colour Layered Papercraft Vignette</a><br><sub>Builds a photo&#x27;s subject as a small layered-paper relief scene in soft paper colours.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-207"><img src="./assets/roster/207.jpg" alt="XXD Panel 207 · Airy Blue Mixed-media Collage Insert" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-207"><strong>207</strong> · Airy Blue Mixed-media Collage Insert</a><br><sub>Turns a photo into a small centred photo-and-line collage, like a magazine insert on pale blue and white.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-208"><img src="./assets/roster/208.jpg" alt="XXD Panel 208 · Blue-pink Modernist Abstract Cluster" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-208"><strong>208</strong> · Blue-pink Modernist Abstract Cluster</a><br><sub>Distils a photo into a small modernist abstract cluster of blue and pink blocks with black line textures.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-209"><img src="./assets/roster/209.jpg" alt="XXD Panel 209 · Minimal Paper-based Image Archive" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-209"><strong>209</strong> · Minimal Paper-based Image Archive</a><br><sub>Shrinks a photo to a small image on a paper page with archive-style captions, like a photobook page.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-210"><img src="./assets/roster/210.jpg" alt="XXD Panel 210 · Cool Minimal Conceptual Photo Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-210"><strong>210</strong> · Cool Minimal Conceptual Photo Collage</a><br><sub>Shrinks a photo&#x27;s subject into a small photo collage with cool blue doodles, bubbles and symbols.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-211"><img src="./assets/roster/211.jpg" alt="XXD Panel 211 · Semantic-colour Geometric Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-211"><strong>211</strong> · Semantic-colour Geometric Vignette</a><br><sub>Compresses a photo into one small geometric colour-block graphic, with colours chosen for what the subject is.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-212"><img src="./assets/roster/212.jpg" alt="XXD Panel 212 · Near-monochrome Sculptural Form Study" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-212"><strong>212</strong> · Near-monochrome Sculptural Form Study</a><br><sub>Turns the subject of a photo into a small white conceptual model floating in a vast empty field.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-213"><img src="./assets/roster/213.jpg" alt="XXD Panel 213 · Cool Monochrome Concept on Warm Paper" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-213"><strong>213</strong> · Cool Monochrome Concept on Warm Paper</a><br><sub>Distils the mood and relationships in a photo into a tiny cool-toned line drawing on warm old paper.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-214"><img src="./assets/roster/214.jpg" alt="XXD Panel 214 · Rough Cut-out Spot with Local Colours" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-214"><strong>214</strong> · Rough Cut-out Spot with Local Colours</a><br><sub>Turns a photo into a small, rough cut-paper spot illustration in true colours on a wide white page.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-215"><img src="./assets/roster/215.jpg" alt="XXD Panel 215 · Grayscale Axonometric with Ochre Accent" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-215"><strong>215</strong> · Grayscale Axonometric with Ochre Accent</a><br><sub>Draws the subject of a photo as a small, precise white-and-grey axonometric diagram with one ochre accent.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-216"><img src="./assets/roster/216.jpg" alt="XXD Panel 216 · Tiny Print Island in Vast Negative Space" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-216"><strong>216</strong> · Tiny Print Island in Vast Negative Space</a><br><sub>Compresses a photo into one tiny single-colour print block on a wide field of warm paper.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-217"><img src="./assets/roster/217.jpg" alt="XXD Panel 217 · Bright Digital Mixed-Media Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-217"><strong>217</strong> · Bright Digital Mixed-Media Collage</a><br><sub>Cuts out the photo&#x27;s subject and builds a bright magazine collage around it with doodles and paper scraps.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-218"><img src="./assets/roster/218.jpg" alt="XXD Panel 218 · Minimal Needle-Felt Picture-Book Illustration" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-218"><strong>218</strong> · Minimal Needle-Felt Picture-Book Illustration</a><br><sub>Simplifies a photo into a tiny minimal picture-book scene, then makes it in soft handmade needle felt.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-219"><img src="./assets/roster/219.jpg" alt="XXD Panel 219 · Doodle Travel Sketch with Pencil Accents" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-219"><strong>219</strong> · Doodle Travel Sketch with Pencil Accents</a><br><sub>Turns a photo into a black ink travel-journal sketch with just a few touches of coloured pencil.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-220"><img src="./assets/roster/220.jpg" alt="XXD Panel 220 · Rounded Naïve Doodle Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-220"><strong>220</strong> · Rounded Naïve Doodle Vignette</a><br><sub>Turns a photo into a cute, rounded, loosely drawn doodle with colour dabbed in only a few places.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-221"><img src="./assets/roster/221.jpg" alt="XXD Panel 221 · New-Chinese Spot-Colour Print" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-221"><strong>221</strong> · New-Chinese Spot-Colour Print</a><br><sub>Condenses a photo into a small, seal-like New-Chinese spot-colour print in wide Eastern white space.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-222"><img src="./assets/roster/222.jpg" alt="XXD Panel 222 · Architectural Type Installation" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-222"><strong>222</strong> · Architectural Type Installation</a><br><sub>Turns the subject of a photo into a small colourful landmark built from letters and geometric blocks.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-223"><img src="./assets/roster/223.jpg" alt="XXD Panel 223 · Vintage Engraved Miniature Atlas" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-223"><strong>223</strong> · Vintage Engraved Miniature Atlas</a><br><sub>Breaks a photo into a set of separate tiny engraved motifs, like a page from an old field guide.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-224"><img src="./assets/roster/224.jpg" alt="XXD Panel 224 · Reassembled Porcelain Shards" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-224"><strong>224</strong> · Reassembled Porcelain Shards</a><br><sub>Rebuilds the subject from Chinese porcelain shards, keeping the gaps, cracks and wide porcelain white.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-225"><img src="./assets/roster/225.jpg" alt="XXD Panel 225 · Office-Object Hand-Drawn Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-225"><strong>225</strong> · Office-Object Hand-Drawn Collage</a><br><sub>Retells a photo as a visual diary page made of sticky notes, paper clips, tape and paper scraps.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-226"><img src="./assets/roster/226.jpg" alt="XXD Panel 226 · Iced Cookie Bas-Relief" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-226"><strong>226</strong> · Iced Cookie Bas-Relief</a><br><sub>Turns the subject and setting of a photo into one small, matte, rounded iced-cookie relief.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-227"><img src="./assets/roster/227.jpg" alt="XXD Panel 227 · Embroidered Mission Patch" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-227"><strong>227</strong> · Embroidered Mission Patch</a><br><sub>Condenses a photo into one machine-embroidered mission patch with a merrowed edge and satin-stitch lettering.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-228"><img src="./assets/roster/228.jpg" alt="XXD Panel 228 · Artist-Made Paper Object" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-228"><strong>228</strong> · Artist-Made Paper Object</a><br><sub>Remakes a photo as a handmade indie paper object: naive cut paper and a few spot colours.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-229"><img src="./assets/roster/229.jpg" alt="XXD Panel 229 · Folk-Modern Quiet Miniature" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-229"><strong>229</strong> · Folk-Modern Quiet Miniature</a><br><sub>Distils a photo into a small, rounded, pastel folk-modern illustration, quiet and nostalgic.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-230"><img src="./assets/roster/230.jpg" alt="XXD Panel 230 · Negative-Space Monument" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-230"><strong>230</strong> · Negative-Space Monument</a><br><sub>Leaves the subject as a huge white silhouette in dense hand-drawn dashes, with one tiny figure beside it.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-231"><img src="./assets/roster/231.jpg" alt="XXD Panel 231 · Neo-Naïve Hand Drawing" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-231"><strong>231</strong> · Neo-Naïve Hand Drawing</a><br><sub>Turns a photo into a small, loose colour drawing: wobbly outlines, marker and pencil, lots of space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-232"><img src="./assets/roster/232.jpg" alt="XXD Panel 232 · Horizontal Layered Folk-Modern" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-232"><strong>232</strong> · Horizontal Layered Folk-Modern</a><br><sub>Compresses a photo into quiet horizontal bands of landscape, with a person only as a tiny punctuation mark.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-233"><img src="./assets/roster/233.jpg" alt="XXD Panel 233 · Tufted Yarn Wall Hanging" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-233"><strong>233</strong> · Tufted Yarn Wall Hanging</a><br><sub>Remakes a photo as a few small, bright loop-pile yarn wall pieces scattered on a pale plain background.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-234"><img src="./assets/roster/234.jpg" alt="XXD Panel 234 · Digital Editorial Key Visual" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-234"><strong>234</strong> · Digital Editorial Key Visual</a><br><sub>Turns a photo into a youthful digital-editorial key visual: flat colour, rounded modules, fine lines.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-235"><img src="./assets/roster/235.jpg" alt="XXD Panel 235 · Mint Pixel Cooking Badge" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-235"><strong>235</strong> · Mint Pixel Cooking Badge</a><br><sub>Turns a photo into a pixel cooking badge in a mint-coloured dream: a crisp centre fading into white.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-236"><img src="./assets/roster/236.jpg" alt="XXD Panel 236 · Black-and-White Geometric Glyph" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-236"><strong>236</strong> · Black-and-White Geometric Glyph</a><br><sub>Compresses a photo into one tiny black-and-white geometric glyph at the centre of an unbroken white field.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-237"><img src="./assets/roster/237.jpg" alt="XXD Panel 237 · Y2K Sticker Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-237"><strong>237</strong> · Y2K Sticker Collage</a><br><sub>Breaks one subject into white-bordered stickers scattered across a pale grey-lavender neo-Y2K zine page.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-238"><img src="./assets/roster/238.jpg" alt="XXD Panel 238 · Gothic Picture-Book Miniature" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-238"><strong>238</strong> · Gothic Picture-Book Miniature</a><br><sub>Turns a photo into one tiny, fragile, slightly dark gouache picture-book figure on almost empty paper.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-239"><img src="./assets/roster/239.jpg" alt="XXD Panel 239 · Misregistered Spot-Colour Poster" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-239"><strong>239</strong> · Misregistered Spot-Colour Poster</a><br><sub>Turns a photo into an experimental spot-colour print poster with big type, halftone and misregistration.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-240"><img src="./assets/roster/240.jpg" alt="XXD Panel 240 · Crayon Visual Diary" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-240"><strong>240</strong> · Crayon Visual Diary</a><br><sub>Turns a photo into an unfinished crayon diary page: a small subject, warm earth tones and lots of blank paper.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-241"><img src="./assets/roster/241.jpg" alt="XXD Panel 241 · Poetic Specimen Study" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-241"><strong>241</strong> · Poetic Specimen Study</a><br><sub>Makes a poetic specimen page: part precise black-and-white photo, the missing part a fragile drawn contour.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-242"><img src="./assets/roster/242.jpg" alt="XXD Panel 242 · Naive Talisman Illustration" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-242"><strong>242</strong> · Naive Talisman Illustration</a><br><sub>Turns an everyday object in your photo into a centred naïve talisman on a deep matte ground.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-243"><img src="./assets/roster/243.jpg" alt="XXD Panel 243 · Blue Ballpoint on Lined Paper" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-243"><strong>243</strong> · Blue Ballpoint on Lined Paper</a><br><sub>Draws your photo in blue ballpoint on lined notebook paper, with uneven hatching and the process left in.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-244"><img src="./assets/roster/244.jpg" alt="XXD Panel 244 · Pen-Lift Notebook" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-244"><strong>244</strong> · Pen-Lift Notebook</a><br><sub>Turns your photo into a quick notebook sketch: a small subject, broken ink, a few thin watercolour washes.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-245"><img src="./assets/roster/245.jpg" alt="XXD Panel 245 · Memory in White Space" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-245"><strong>245</strong> · Memory in White Space</a><br><sub>Turns your photo into a quiet page of memory: a small, rounded, simplified subject in a wide field of paper.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-246"><img src="./assets/roster/246.jpg" alt="XXD Panel 246 · Neo-Constructivist Collage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-246"><strong>246</strong> · Neo-Constructivist Collage</a><br><sub>Turns one subject into a conceptual poster of geometric colour blocks, structural lines and white space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-247"><img src="./assets/roster/247.jpg" alt="XXD Panel 247 · Soft Storybook" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-247"><strong>247</strong> · Soft Storybook</a><br><sub>Turns one image from your photo into a small coloured-pencil and watercolour storybook vignette.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-248"><img src="./assets/roster/248.jpg" alt="XXD Panel 248 · Old Travel Journal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-248"><strong>248</strong> · Old Travel Journal</a><br><sub>Paints the impression your photo leaves, not everything in it: a travel-journal page in ink and watercolour.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-249"><img src="./assets/roster/249.jpg" alt="XXD Panel 249 · Atmospheric Pixel" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-249"><strong>249</strong> · Atmospheric Pixel</a><br><sub>Compresses a moment of your photo into a quiet retro-game scene: low resolution, soft colour, open space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-250"><img src="./assets/roster/250.jpg" alt="XXD Panel 250 · Architectural Geometry Poem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-250"><strong>250</strong> · Architectural Geometry Poem</a><br><sub>Turns your scene into abstract architectural outlines, geometric colour planes and quiet white space.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>251–300</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-251"><img src="./assets/roster/251.jpg" alt="XXD Panel 251 · Pixel Life Archive" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-251"><strong>251</strong> · Pixel Life Archive</a><br><sub>Compresses your subject into a pixel life-symbol on a grid, like a specimen kept by a future civilisation.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-252"><img src="./assets/roster/252.jpg" alt="XXD Panel 252 · Healing Sticker" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-252"><strong>252</strong> · Healing Sticker</a><br><sub>Turns the subject of your photo into one small, rounded, soft journal sticker inside quiet white space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-253"><img src="./assets/roster/253.jpg" alt="XXD Panel 253 · Flat Theme Key" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-253"><strong>253</strong> · Flat Theme Key</a><br><sub>Distils the theme of your photo into one flat symbol of clean colour, like a visual key with a story.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-254"><img src="./assets/roster/254.jpg" alt="XXD Panel 254 · Eastern Geometry Archive" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-254"><strong>254</strong> · Eastern Geometry Archive</a><br><sub>Takes the subject of your photo apart into translucent geometric slices floating in a vast empty field.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-255"><img src="./assets/roster/255.jpg" alt="XXD Panel 255 · Travel Keepsake Stamp" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-255"><strong>255</strong> · Travel Keepsake Stamp</a><br><sub>Seals a moment from your photo inside one small travel keepsake stamp, in a wide field of blank paper.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-256"><img src="./assets/roster/256.jpg" alt="XXD Panel 256 · Naive Folk Art" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-256"><strong>256</strong> · Naive Folk Art</a><br><sub>Turns your photo into a small centred naïve folk painting: one subject, one feeling, a touch of gold leaf.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-257"><img src="./assets/roster/257.jpg" alt="XXD Panel 257 · Silent Single Line" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-257"><strong>257</strong> · Silent Single Line</a><br><sub>Reduces the subject of your photo to one very thin, slightly imperfect line floating in wide white space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-258"><img src="./assets/roster/258.jpg" alt="XXD Panel 258 · Creamy Dreamscape" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-258"><strong>258</strong> · Creamy Dreamscape</a><br><sub>Remoulds the subject of your photo as a tiny soft cream sculpture floating in an open, cream-coloured space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-259"><img src="./assets/roster/259.jpg" alt="XXD Panel 259 · Classical Poem Manuscript" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-259"><strong>259</strong> · Classical Poem Manuscript</a><br><sub>Redraws your subject as a page of imperfect ink in a classical poem manuscript, as if from memory.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-260"><img src="./assets/roster/260.jpg" alt="XXD Panel 260 · Geometric Memory" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-260"><strong>260</strong> · Geometric Memory</a><br><sub>Turns your photo into a memory map made of geometric symbols, with a small subject and wide white space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-261"><img src="./assets/roster/261.jpg" alt="XXD Panel 261 · Crayon Memory" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-261"><strong>261</strong> · Crayon Memory</a><br><sub>Draws not the place itself but the feeling it left: a small memory in coloured pencil and wax pastel.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-262"><img src="./assets/roster/262.jpg" alt="XXD Panel 262 · Film Afterimage" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-262"><strong>262</strong> · Film Afterimage</a><br><sub>Saves the subject of your photo as one muted frame from an old film, hanging quietly in wide white space.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-263"><img src="./assets/roster/263.jpg" alt="XXD Panel 263 · Commemorative Seal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-263"><strong>263</strong> · Commemorative Seal</a><br><sub>Compresses your subject into one small commemorative seal, like a cultural keepsake put away.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-264"><img src="./assets/roster/264.jpg" alt="XXD Panel 264 · Sketchbook Doodle" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-264"><strong>264</strong> · Sketchbook Doodle</a><br><sub>Turns your photo into a naïve line drawing on a private sketchbook page: unfinished, but full of feeling.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-265"><img src="./assets/roster/265.jpg" alt="XXD Panel 265 · Botanical Emblem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-265"><strong>265</strong> · Botanical Emblem</a><br><sub>Turns your subject into a small emblem embraced by flowers and leaves, like a long-kept private mark.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-266"><img src="./assets/roster/266.jpg" alt="XXD Panel 266 · Symbol Mark" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-266"><strong>266</strong> · Symbol Mark</a><br><sub>Distils your subject into one small minimal symbol, like the mark of a cultural institution or brand.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-267"><img src="./assets/roster/267.jpg" alt="XXD Panel 267 · Fabric Badge" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-267"><strong>267</strong> · Fabric Badge</a><br><sub>Makes the subject of your photo into one small cloth badge: denim, stitching, patchwork and a frayed edge.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-268"><img src="./assets/roster/268.jpg" alt="XXD Panel 268 · Quiet Symbol" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-268"><strong>268</strong> · Quiet Symbol</a><br><sub>Compresses the subject of your photo into one tiny, quiet mark, like a stamp in a private collection.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-269"><img src="./assets/roster/269.jpg" alt="XXD Panel 269 · Experiment Notebook" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-269"><strong>269</strong> · Experiment Notebook</a><br><sub>Turns your subject into a small concept symbol in a lab notebook: ink line, halftone dots, a little colour.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-270"><img src="./assets/roster/270.jpg" alt="XXD Panel 270 · Eastern Totem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-270"><strong>270</strong> · Eastern Totem</a><br><sub>Distils the subject of your photo into a small Eastern seal-like totem, small and solemn in wide white space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-271"><img src="./assets/roster/271.jpg" alt="XXD Panel 271 · Private Emblem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-271"><strong>271</strong> · Private Emblem</a><br><sub>Turns your subject into a small folk-print private emblem: one outline, a few spot colours, ink on paper.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-272"><img src="./assets/roster/272.jpg" alt="XXD Panel 272 · Monochrome Soul" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-272"><strong>272</strong> · Monochrome Soul</a><br><sub>Turns the subject of your photo into one small black-and-white hand-drawn character with a hint of mood.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-273"><img src="./assets/roster/273.jpg" alt="XXD Panel 273 · Art Nouveau Crest" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-273"><strong>273</strong> · Art Nouveau Crest</a><br><sub>Condenses the subject of your photo into one fine-line Art Nouveau crest with a single colour accent.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-274"><img src="./assets/roster/274.jpg" alt="XXD Panel 274 · Night Crayon" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-274"><strong>274</strong> · Night Crayon</a><br><sub>Draws the subject of your photo as one small mark in glowing crayon lines on black paper.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-275"><img src="./assets/roster/275.jpg" alt="XXD Panel 275 · Naive Badge" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-275"><strong>275</strong> · Naive Badge</a><br><sub>Turns the subject of your photo into one small, rounded, slightly clumsy handmade badge.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-276"><img src="./assets/roster/276.jpg" alt="XXD Panel 276 · Spatial Archive" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-276"><strong>276</strong> · Spatial Archive</a><br><sub>Takes apart the structure in your photo and layers it into an unfinished fine-line spatial study.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-277"><img src="./assets/roster/277.jpg" alt="XXD Panel 277 · Geometric Mark" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-277"><strong>277</strong> · Geometric Mark</a><br><sub>Reduces the subject of your photo to one small modernist symbol of geometric silhouettes and flat colour.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-278"><img src="./assets/roster/278.jpg" alt="XXD Panel 278 · Cultural Silhouette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-278"><strong>278</strong> · Cultural Silhouette</a><br><sub>Cuts the subject of your photo into one small paper-cut seal of geometric colour with a screen-print feel.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-279"><img src="./assets/roster/279.jpg" alt="XXD Panel 279 · System Gene" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-279"><strong>279</strong> · System Gene</a><br><sub>Compresses the subject of your photo into one post-digital mark of modules, thin lines and a tiny number.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-280"><img src="./assets/roster/280.jpg" alt="XXD Panel 280 · Pixel Specimen" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-280"><strong>280</strong> · Pixel Specimen</a><br><sub>Turns the subject of your photo into one small low-res pixel emblem with a single signal colour.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-281"><img src="./assets/roster/281.jpg" alt="XXD Panel 281 · Living Pictograph" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-281"><strong>281</strong> · Living Pictograph</a><br><sub>Turns the subject of your photo into one small flat, dark, deadpan pictograph with a hint of life.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-282"><img src="./assets/roster/282.jpg" alt="XXD Panel 282 · Soft-focus Organic" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-282"><strong>282</strong> · Soft-focus Organic</a><br><sub>Softens the subject of your photo into one small abstract mark of translucent layers and milky pastels.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-283"><img src="./assets/roster/283.jpg" alt="XXD Panel 283 · Era Insignia" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-283"><strong>283</strong> · Era Insignia</a><br><sub>Issues the subject of your photo as one badge that looks officially released by a space-age institution.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-284"><img src="./assets/roster/284.jpg" alt="XXD Panel 284 · Civilisation Emblem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-284"><strong>284</strong> · Civilisation Emblem</a><br><sub>Frames the subject of your photo and prints it as a miniature monument in clashing cold and warm colours.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-285"><img src="./assets/roster/285.jpg" alt="XXD Panel 285 · Science Commemorative" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-285"><strong>285</strong> · Science Commemorative</a><br><sub>Prints the subject of your photo as one bold-outlined, halftone-inked commemorative stamp.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-286"><img src="./assets/roster/286.jpg" alt="XXD Panel 286 · Pastel Totem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-286"><strong>286</strong> · Pastel Totem</a><br><sub>Turns the one image in your photo most worth keeping into a light, slightly strange pastel totem.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-287"><img src="./assets/roster/287.jpg" alt="XXD Panel 287 · Little Note on Paper" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-287"><strong>287</strong> · Little Note on Paper</a><br><sub>Leaves the subject of your photo as one tiny, hand-drawn little creature on a wide sheet of blank paper.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-288"><img src="./assets/roster/288.jpg" alt="XXD Panel 288 · Codex Emblem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-288"><strong>288</strong> · Codex Emblem</a><br><sub>Reduces the subject of your photo to one small research emblem in fine engraved line on parchment tones.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-289"><img src="./assets/roster/289.jpg" alt="XXD Panel 289 · Folk Mark" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-289"><strong>289</strong> · Folk Mark</a><br><sub>Turns the subject of your photo into one small, hand-printed naive folk symbol with its key feature enlarged.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-290"><img src="./assets/roster/290.jpg" alt="XXD Panel 290 · Old Picture-book Sign" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-290"><strong>290</strong> · Old Picture-book Sign</a><br><sub>Turns the subject of your photo into one small old picture-book folk sign with trembling lines and faded colour.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-291"><img src="./assets/roster/291.jpg" alt="XXD Panel 291 · Gentle Totem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-291"><strong>291</strong> · Gentle Totem</a><br><sub>Condenses the subject of your photo into one rounded, soft little totem like a fairy-tale character mark.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-292"><img src="./assets/roster/292.jpg" alt="XXD Panel 292 · Journal Soul" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-292"><strong>292</strong> · Journal Soul</a><br><sub>Leaves the subject of your photo as one small emotional icon that looks quickly drawn from memory.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-293"><img src="./assets/roster/293.jpg" alt="XXD Panel 293 · Poetic Little Stamp" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-293"><strong>293</strong> · Poetic Little Stamp</a><br><sub>Presses the subject of your photo into one slightly clumsy poetic stamp on old paper, with a tiny expression.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-294"><img src="./assets/roster/294.jpg" alt="XXD Panel 294 · Tiny Private Sign" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-294"><strong>294</strong> · Tiny Private Sign</a><br><sub>Keeps just one tiny black-and-white private symbol from your photo, on a page that is almost entirely blank.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-295"><img src="./assets/roster/295.jpg" alt="XXD Panel 295 · Warm Clumsy Symbol" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-295"><strong>295</strong> · Warm Clumsy Symbol</a><br><sub>Reduces the subject of your photo to one rounded, slightly off-balance, warm and clumsy private symbol.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-296"><img src="./assets/roster/296.jpg" alt="XXD Panel 296 · Gestural Trace" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-296"><strong>296</strong> · Gestural Trace</a><br><sub>Leaves the subject of your photo as one charcoal or ink trace with speed and direction.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-297"><img src="./assets/roster/297.jpg" alt="XXD Panel 297 · Closure Cipher" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-297"><strong>297</strong> · Closure Cipher</a><br><sub>Leaves the subject of your photo as a broken-outline cipher that the viewer completes in their own mind.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-298"><img src="./assets/roster/298.jpg" alt="XXD Panel 298 · Charcoal Mark" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-298"><strong>298</strong> · Charcoal Mark</a><br><sub>Reduces the subject of your photo to one small semi-abstract mark left by charcoal, graphite and ink.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-299"><img src="./assets/roster/299.jpg" alt="XXD Panel 299 · Xerox Residue" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-299"><strong>299</strong> · Xerox Residue</a><br><sub>Turns the subject of your photo into a black-and-white trace that looks copied too often to be fully restored.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-300"><img src="./assets/roster/300.jpg" alt="XXD Panel 300 · Binary Seal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-300"><strong>300</strong> · Binary Seal</a><br><sub>Uses only pure black and pure white to cut the subject of your photo out of the blank as a small, fading seal.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>301–350</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-301"><img src="./assets/roster/301.jpg" alt="XXD Panel 301 · Digital Relic" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-301"><strong>301</strong> · Digital Relic</a><br><sub>Turns the strongest feature of your photo into one anonymous black-and-white totem left on an old computer.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-302"><img src="./assets/roster/302.jpg" alt="XXD Panel 302 · New Folk Emblem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-302"><strong>302</strong> · New Folk Emblem</a><br><sub>Keeps your photo and condenses the subject into one warm, slightly humorous neo-naive handmade emblem.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-303"><img src="./assets/roster/303.jpg" alt="XXD Panel 303 · Geometric Sign" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-303"><strong>303</strong> · Geometric Sign</a><br><sub>Keeps your photo and abstracts the subject into one geometric mark that still works without the picture.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-304"><img src="./assets/roster/304.jpg" alt="XXD Panel 304 · Constructivist Totem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-304"><strong>304</strong> · Constructivist Totem</a><br><sub>Keeps your photo and presses the subject&#x27;s mood into one abstract totem where organic and geometric pull at each other.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-305"><img src="./assets/roster/305.jpg" alt="XXD Panel 305 · Cut-Paper Totem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-305"><strong>305</strong> · Cut-Paper Totem</a><br><sub>Keeps your photo and cuts the subject into one screenprinted folk symbol that still reads when tiny.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-306"><img src="./assets/roster/306.jpg" alt="XXD Panel 306 · Folk Silhouette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-306"><strong>306</strong> · Folk Silhouette</a><br><sub>Keeps your photo and leaves only one very small folk silhouette on a wide empty page.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-307"><img src="./assets/roster/307.jpg" alt="XXD Panel 307 · Little Home Note" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-307"><strong>307</strong> · Little Home Note</a><br><sub>Keeps your photo and turns one remembered moment into a small, warm domestic symbol.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-308"><img src="./assets/roster/308.jpg" alt="XXD Panel 308 · Paper-Cut Badge" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-308"><strong>308</strong> · Paper-Cut Badge</a><br><sub>Keeps your photo and cuts the subject into one paper badge that feels brought home from a particular place.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-309"><img src="./assets/roster/309.jpg" alt="XXD Panel 309 · Concept Mini Mark" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-309"><strong>309</strong> · Concept Mini Mark</a><br><sub>Keeps your photo and turns the subject into a small emblem changed in just one place, with a twist you see on second look.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-310"><img src="./assets/roster/310.jpg" alt="XXD Panel 310 · Spirit Field" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-310"><strong>310</strong> · Spirit Field</a><br><sub>Keeps your photo and wraps one tiny bright focal point in a large organic shape to show the feeling behind it.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-311"><img src="./assets/roster/311.jpg" alt="XXD Panel 311 · Old-Book Pictogram" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-311"><strong>311</strong> · Old-Book Pictogram</a><br><sub>Keeps your photo and reduces the subject to one small pictogram, like a motif from an old book or a handmade seal.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-312"><img src="./assets/roster/312.jpg" alt="XXD Panel 312 · Picture-Book Memory" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-312"><strong>312</strong> · Picture-Book Memory</a><br><sub>Keeps your photo and turns the subject into one quiet memory stamp floating as in an old children&#x27;s book.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-313"><img src="./assets/roster/313.jpg" alt="XXD Panel 313 · Private Journal Mark" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-313"><strong>313</strong> · Private Journal Mark</a><br><sub>Keeps your photo and leaves the subject as a private symbol that looks redrawn many times in a notebook.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-314"><img src="./assets/roster/314.jpg" alt="XXD Panel 314 · Childhood Memory Seal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-314"><strong>314</strong> · Childhood Memory Seal</a><br><sub>Keeps your photo and leaves the subject as one small memory mark from an old picture book.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-315"><img src="./assets/roster/315.jpg" alt="XXD Panel 315 · Folk Identity Mark" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-315"><strong>315</strong> · Folk Identity Mark</a><br><sub>Keeps your photo and turns one outline, pose or fragment into a cut-paper, screenprinted folk identity mark.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-316"><img src="./assets/roster/316.jpg" alt="XXD Panel 316 · Tactile Mini Sculpture" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-316"><strong>316</strong> · Tactile Mini Sculpture</a><br><sub>Keeps your photo and turns the subject into one small collectible sculpture that looks hand-made from felt or soft clay.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-317"><img src="./assets/roster/317.jpg" alt="XXD Panel 317 · Round Naive Totem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-317"><strong>317</strong> · Round Naive Totem</a><br><sub>Keeps your photo and turns the subject into one rounded, slightly clumsy folk totem that looks long in use.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-318"><img src="./assets/roster/318.jpg" alt="XXD Panel 318 · Lived-In Mark" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-318"><strong>318</strong> · Lived-In Mark</a><br><sub>Keeps your photo and turns the feel of everyday life in it into one small, warm picture-book style mark.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-319"><img src="./assets/roster/319.jpg" alt="XXD Panel 319 · Poetic Mark" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-319"><strong>319</strong> · Poetic Mark</a><br><sub>Keeps your photo and leaves one small poetic symbol on white paper, with a faint second meaning.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-320"><img src="./assets/roster/320.jpg" alt="XXD Panel 320 · Character Silhouette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-320"><strong>320</strong> · Character Silhouette</a><br><sub>Keeps your photo and turns the subject into one silhouette-first character mark whose contour is allowed to break.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-321"><img src="./assets/roster/321.jpg" alt="XXD Panel 321 · Ink-Block Old Seal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-321"><strong>321</strong> · Ink-Block Old Seal</a><br><sub>Keeps your photo and inks the subject as one small plate from an old botanical manual or folk field guide.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-322"><img src="./assets/roster/322.jpg" alt="XXD Panel 322 · Geometric Composition" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-322"><strong>322</strong> · Geometric Composition</a><br><sub>Keeps your photo and rebuilds the subject as one mid-century modern geometric symbol that works as a shape before you recognise it.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-323"><img src="./assets/roster/323.jpg" alt="XXD Panel 323 · White-Line Emblem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-323"><strong>323</strong> · White-Line Emblem</a><br><sub>Keeps your photo and draws the subject in one white line on a textured ground, like the sign of a small shop.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-324"><img src="./assets/roster/324.jpg" alt="XXD Panel 324 · Miniature Mindscape" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-324"><strong>324</strong> · Miniature Mindscape</a><br><sub>Keeps your photo and folds a large feeling into one tiny object, like a talisman.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-325"><img src="./assets/roster/325.jpg" alt="XXD Panel 325 · Personal Myth Seal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-325"><strong>325</strong> · Personal Myth Seal</a><br><sub>Keeps your photo and seals the subject as one personal-myth totem with a sense of time.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-326"><img src="./assets/roster/326.jpg" alt="XXD Panel 326 · Raw Totem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-326"><strong>326</strong> · Raw Totem</a><br><sub>Keeps your photo and hangs one restrained, raw totem made with dry brush and chalk in empty space.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-327"><img src="./assets/roster/327.jpg" alt="XXD Panel 327 · Children&#x27;s Press Relic" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-327"><strong>327</strong> · Children&#x27;s Press Relic</a><br><sub>Keeps your photo and turns the subject into one small printed mark that looks clipped from an old children&#x27;s magazine.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-328"><img src="./assets/roster/328.jpg" alt="XXD Panel 328 · Retro Sticker Badge" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-328"><strong>328</strong> · Retro Sticker Badge</a><br><sub>Keeps your photo and turns the subject into one retro zine badge that looks like a die-cut sticker.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-329"><img src="./assets/roster/329.jpg" alt="XXD Panel 329 · Yuru Thin Line" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-329"><strong>329</strong> · Yuru Thin Line</a><br><sub>Keeps your photo and draws one quiet, easygoing little icon in a thin line that gently wobbles.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-330"><img src="./assets/roster/330.jpg" alt="XXD Panel 330 · Private Keepsake" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-330"><strong>330</strong> · Private Keepsake</a><br><sub>Keeps your photo and leaves one private little mark in the corner of a journal, as if it belonged to one person.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-331"><img src="./assets/roster/331.jpg" alt="XXD Panel 331 · Storybook Border" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-331"><strong>331</strong> · Storybook Border</a><br><sub>Keeps your photo and retells it as an old storybook page whose border tells the story while the centre stays quiet.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-332"><img src="./assets/roster/332.jpg" alt="XXD Panel 332 · Storybook Relic Emblem" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-332"><strong>332</strong> · Storybook Relic Emblem</a><br><sub>Reduces the subject of your photo to one small mark that looks like it was left behind by an old storybook.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-333"><img src="./assets/roster/333.jpg" alt="XXD Panel 333 · Sacred Tech Relic" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-333"><strong>333</strong> · Sacred Tech Relic</a><br><sub>Condenses the subject of your photo into a small circuit relief seal that looks left behind by a lost civilisation.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-334"><img src="./assets/roster/334.jpg" alt="XXD Panel 334 · Mythic Bookplate" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-334"><strong>334</strong> · Mythic Bookplate</a><br><sub>Turns the subject of your photo into a mythic bookplate: one central symbol ringed by matching ornament.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-335"><img src="./assets/roster/335.jpg" alt="XXD Panel 335 · Underground Stamp" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-335"><strong>335</strong> · Underground Stamp</a><br><sub>Cuts the subject of your photo into an underground street badge that still reads when shrunk very small.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-336"><img src="./assets/roster/336.jpg" alt="XXD Panel 336 · Axial Spirit Seal" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-336"><strong>336</strong> · Axial Spirit Seal</a><br><sub>Distils your photo into one quiet, mysterious seal set on a central axis of nested frames.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-337"><img src="./assets/roster/337.jpg" alt="XXD Panel 337 · Pixel Fragment" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-337"><strong>337</strong> · Pixel Fragment</a><br><sub>Compresses the subject of your photo into a lo-fi pixel fragment, framed like a specimen dug out of the old internet.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-338"><img src="./assets/roster/338.jpg" alt="XXD Panel 338 · Raster Relic Badge" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-338"><strong>338</strong> · Raster Relic Badge</a><br><sub>Compresses the subject of your photo into a raster badge: strong silhouette, little information, one anomaly.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-339"><img src="./assets/roster/339.jpg" alt="XXD Panel 339 · Future Relic" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-339"><strong>339</strong> · Future Relic</a><br><sub>Draws the character of your photo into one small low-relief medal from the future, worn by time.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-340"><img src="./assets/roster/340.jpg" alt="XXD Panel 340 · Visual Singularity" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-340"><strong>340</strong> · Visual Singularity</a><br><sub>Reduces your photo to one tiny black-and-white mark in a field that is almost entirely blank.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-341"><img src="./assets/roster/341.jpg" alt="XXD Panel 341 · Second World" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-341"><strong>341</strong> · Second World</a><br><sub>Lets the cleverest opening in your photo cross the midline and keep happening on paper.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-342"><img src="./assets/roster/342.jpg" alt="XXD Panel 342 · Punched Echo" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-342"><strong>342</strong> · Punched Echo</a><br><sub>Punches your photo with one repeated die shape, then regathers the punched-out pieces on a calm colour field.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-343"><img src="./assets/roster/343.jpg" alt="XXD Panel 343 · Floating Pixel Card" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-343"><strong>343</strong> · Floating Pixel Card</a><br><sub>Turns the subject of your photo into a small pastel pixel picture floating at the centre, with a soft shadow at the lower right.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-344"><img src="./assets/roster/344.jpg" alt="XXD Panel 344 · Miniature Plinth" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-344"><strong>344</strong> · Miniature Plinth</a><br><sub>Cuts out the subject of your photo with a patch of its ground and makes it a miniature model on a rounded plinth.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-345"><img src="./assets/roster/345.jpg" alt="XXD Panel 345 · Dark-Ground Silhouettes" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-345"><strong>345</strong> · Dark-Ground Silhouettes</a><br><sub>Presses the subject of your photo and a few nearby things into flat silhouettes, clustered on a dark ground.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-346"><img src="./assets/roster/346.jpg" alt="XXD Panel 346 · Fluted Glass Cover" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-346"><strong>346</strong> · Fluted Glass Cover</a><br><sub>Pushes the subject of your photo into a full-bleed close-up, like a magazine cover shot through fine fluted glass.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-347"><img src="./assets/roster/347.jpg" alt="XXD Panel 347 · Costumed Watercolour Figure" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-347"><strong>347</strong> · Costumed Watercolour Figure</a><br><sub>Stands the subject of your photo upright in a little costume, like a picture-book character about to set off.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-348"><img src="./assets/roster/348.jpg" alt="XXD Panel 348 · Field-Guide Stipple" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-348"><strong>348</strong> · Field-Guide Stipple</a><br><sub>Admits the subject of your photo to an old field guide, drawn dot by dot in a single ink.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-349"><img src="./assets/roster/349.jpg" alt="XXD Panel 349 · Block Island Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-349"><strong>349</strong> · Block Island Vignette</a><br><sub>Breaks the subject of your photo and its patch of ground into rounded blocks floating like a small island on white.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-350"><img src="./assets/roster/350.jpg" alt="XXD Panel 350 · Neon Spirits" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-350"><strong>350</strong> · Neon Spirits</a><br><sub>Draws your photo&#x27;s corner as a pale line drawing and turns the subject into a glowing, chubby rainbow spirit.</sub></td>
  </tr>
</table>

</details>

<details>
<summary><strong>351–354</strong></summary>

<table>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-351"><img src="./assets/roster/351.jpg" alt="XXD Panel 351 · Naive Marker Title" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-351"><strong>351</strong> · Naive Marker Title</a><br><sub>Writes your photo&#x27;s metaphor in wobbly bold marker and lets the subject tumble into the letters as a doodle.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-352"><img src="./assets/roster/352.jpg" alt="XXD Panel 352 · Cozy Line Vignette" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-352"><strong>352</strong> · Cozy Line Vignette</a><br><sub>Draws the subject of your photo and a few nearby things as a quiet black-line vignette under a big cloud.</sub></td>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-353"><img src="./assets/roster/353.jpg" alt="XXD Panel 353 · Stippled Light Cone" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-353"><strong>353</strong> · Stippled Light Cone</a><br><sub>Presses the subject of your photo into a small engraved silhouette beneath a huge stippled cone of light.</sub></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><a href="https://github.com/nevertoday/xxd-panel-354"><img src="./assets/roster/354.jpg" alt="XXD Panel 354 · Chunky Ink Doodle" width="100%"></a><br><a href="https://github.com/nevertoday/xxd-panel-354"><strong>354</strong> · Chunky Ink Doodle</a><br><sub>Draws the subject of your photo as stubby shapes in thick ink outlines, standing on one bold ground line.</sub></td>
  </tr>
</table>

</details>

<!-- xxd-soldier-roster:end -->

## FAQ

**Do I need to install every style?** No. Install the ones you like. Styles you haven't installed can still be described and recommended, marked as not installed; install one to make images with it.

**How does it decide which style fits?** It looks at what is in the photo (subject, scene, colour, text) and at the use and feel you describe, compares that with each style's description, and tells you why. It never guesses nationality or taste from someone's appearance.

**Will it mix styles together?** No. Each image goes to one style, painted with that style's own original prompt.

**Why not use a style directly?** If you already know which style you want, its own Skill is quickest. Use the catalog when you are undecided, want to compare, or have a whole folder.

**Do photos in a batch mix together?** No. Each photo is generated on its own and never borrows another photo's colours, text or layout. Settings are asked once for the whole batch.

**Where do my photos go?** Only to the image model your agent uses. The Skill uploads nothing elsewhere and never prints endpoints or keys.

## Setting up image generation

You need an OpenAI-compatible API that serves `gpt-image-2` (or a compatible model) and its API key. This creates a separate config and leaves your Codex settings alone:

```bash
mkdir -p ~/.xxd-imagegen
cat > ~/.xxd-imagegen/config.toml <<'EOF'
model_provider = "image"

[model_providers.image]
base_url = "https://api.openai.com/v1"   # or your compatible endpoint
env_key = "XXD_IMAGE_API_KEY"
EOF

# add to ~/.zshrc or ~/.bashrc so your agent can read them
echo 'export XXD_IMAGEGEN_CODEX_DIR=~/.xxd-imagegen' >> ~/.zshrc
echo 'export XXD_IMAGE_API_KEY=your-key' >> ~/.zshrc
```

Reopen your terminal and agent, then check once from this Skill's folder:

```bash
python3 scripts/canonical/configured_imagegen.py probe
```

`"ok":true` means it works. The check only reports readiness; it never prints the endpoint or key. If your Codex already generates images through a compatible API, skip this step.

## Parameters

The catalog takes the same image flags as a single style (`--mode` `--size` `--text` `--locale` `--wallpaper` `--out`) and passes them unchanged to each style; see "Parameters" in any style's README. It also takes `--prefs last|edit|new|off|clear` to reuse, edit or ignore last time's settings. Only layout, size, text mode and language are remembered, never photos, copy, chosen styles or keys.

## For maintainers

This repository also holds the rules and scripts shared by the whole family; every style repository carries copies of them.

| File | Purpose |
|---|---|
| `references/soldier-runtime.md` | image-making rules shared by every style, synced into each style repository |
| `references/panel-catalog.md` | numbered index for recommending and searching; not an image prompt |
| `references/readme-profile-guide.md` | how to write a style's `readme-profile.json` |
| `scripts/build_soldier_readme.py` | renders a style's five READMEs, SKILL description and `openai.yaml` from its profile |
| `scripts/build_general_readme.py` | renders this page and the style roster |
| `scripts/soldier_runtime.py` | syncs the shared rules and scripts to every style repository, and checks them |
| `scripts/readme_ads.py` | checks the advertising block in style READMEs |
| `scripts/brief_intake.py` | checks a new style's original prompt before it is built (reports only, never edits) |
| `scripts/unsplash_sample_sources.py` | picks Unsplash photos for samples |

<!-- xxd-general-ads:start -->
## Advertisement | Paid XXD services and membership

> **Advertising and commercial-information notice:** The QR code, membership, and paid-service links below are advertisements from Xiaoxiaodong. Scanning or purchasing is entirely optional and does not affect access to or use of this open-source project.


All General Skills are included in the CNY 699/year membership; no separate purchase is required. [WeChat](https://xiaoxiaodong.pages.dev/assets/wechat-qr.png)

## ZSXQ + member prompt library + all General Skills membership · CNY 699/year

[ZSXQ](https://wx.zsxq.com/group/15554814142882), the [Xiaoxiaodong member prompt library](https://vip.xiaoxiaodong.ai/), and membership for all General Skills are one combined benefit: **one annual payment activates all three; no duplicate payment is needed.** After joining through ZSXQ, contact Xiaoxiaodong on WeChat to receive a redemption code for the member prompt library. After joining through the member prompt library, contact Xiaoxiaodong on WeChat to enter the ZSXQ group and activate membership for all General Skills.
<!-- xxd-general-ads:end -->

## License

This project—including the Skill, prompts, scripts, documentation, and accompanying sample images—is licensed under the **PolyForm Noncommercial License 1.0.0**. See [LICENSE](LICENSE) for the full legal text and <https://polyformproject.org/licenses/noncommercial/1.0.0> for the official page.

In plain language:

- Individuals may use it for study, research, experimentation, testing, hobby projects, and private entertainment. Charities, educational institutions, public research, safety or health organisations, environmental organisations, and government institutions may also use it.
- For **noncommercial purposes**, you may use, copy, modify, create derivative works, and share it. When sharing, you must also provide this license (or the link above) and every `Required Notice:` statement supplied by the author.
- It may not be used in commercial products or services, paid delivery, sale of access or licences, or any use expected to lead to commercial application. Obtain separate written permission from the copyright holder before commercial use.
- The agreement grants only the copyright licence and limited patent licence expressly stated. It grants no trademarks, brand names, or other unstated rights, and you may not sublicense your licence to others.
- After written notice of a violation, you must return to compliance and take practical remedial steps within 32 days, or the licences terminate immediately. A written patent-infringement claim also terminates the patent licence.
- The material is provided “as is”, without warranty to the extent permitted by law. Users bear the risks and potential losses arising from its use.
