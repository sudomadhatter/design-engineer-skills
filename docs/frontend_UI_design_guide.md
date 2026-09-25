# Frontend & UI/UX Design Guide

**The house standard for world-class, fluid, production-ready interfaces.** This procedural guide establishes how agents and operators design, build, animate, and audit user interfaces across all projects.

Consolidates the seven pillars of house UI craft:
1. **Design System & Visual Intelligence**: [`skills/ui-ux-pro-max`](../skills/ui-ux-pro-max/SKILL.md) — 67 styles, 96 color palettes, 57 font pairings, 99 UX heuristics, and stack guidelines via `search.py`.
2. **Master Motion Engine & Fluid Interactions**: [`skills/emil-design-eng`](../skills/emil-design-eng/SKILL.md) — Consolidated Emil Kowalski motion craft, Apple 2-parameter spring physics, 4-gate opportunity filter, sub-300ms budget, and Before/After review tables.
3. **WebGPU Shader Engine**: [`skills/vgpu`](../skills/vgpu/SKILL.md) — `vercel-labs/vgpu`, typed WGSL shaders, fullscreen fluid meshes, interactive plasma backdrops, particle compute, ~25KB bundle, and zero-GPU headless CI test adapters.
4. **Mobile-First Apple Glass & Materials**: [`skills/apple-glass`](../skills/apple-glass/SKILL.md) — Apple HIG frosted glass (CSS/Tailwind with 180% saturation boost), optical liquid glass refraction over live DOM ([`@samasante/liquid-glass`](https://github.com/samasante/liquid-glass)), and native mobile bridges (React Native and SwiftUI iOS 26).
5. **3D Spatial Models & Geometry**: [`skills/visual-fx-3d`](../skills/visual-fx-3d/SKILL.md) — Complete Poimandres suite ([`pmndrs/react-three-fiber`](https://github.com/pmndrs/react-three-fiber), Drei, Postprocessing, Rapier), glTF product models (`gltfjsx`), and 3D spatial transmission meshes.
6. **Rich Media & Platform Specialists**: [`skills/webm-alpha-video`](../skills/webm-alpha-video/SKILL.md) (green-screen to alpha WebM), [`skills/animate-expo`](../skills/animate-expo/SKILL.md) (React Native / Expo), [`skills/write-swift`](../skills/write-swift/SKILL.md) (iOS native).
7. **Border Beam & Optical Glows Engine**: [`skills/border-beam`](../skills/border-beam/SKILL.md) — 3-tier sub-pixel stroke (`::after` with `mask-composite: exclude` / `-webkit-mask-composite: xor`), hugging inner glow (`::before`; on the `pulse-outside` halo that slot is the out glow instead), 32px Gaussian bloom (`[data-beam-bloom]`), Ocean/Sunset tokens, ~30fps `requestAnimationFrame` pulse driver (zero 120Hz CSS `@keyframes` throttling), and AI Thinking Indicators (Thinking Orb 2D canvas, Cosmic Nebula, Plasma Reactor). Vocabulary and interactive catalog: [`docs/development_diagrams/ui_effects_and_thinking_icons.html`](development_diagrams/ui_effects_and_thinking_icons.html).

Front door: **`/smh-designer`** ([`commands/smh-designer.md`](../commands/smh-designer.md)) — activates **🦋 Caterpillar** with the Two-Phase Creative Vision Lock lifecycle.

---

## 0. The Shared Vocabulary — how the operator talks about UI, and how you answer

**Two documents, one set of words.** The operator reads the
[UI vocabulary page](development_diagrams/ui_effects_and_thinking_icons.html) (HTML, with drawings
and live demos). Agents read this guide. This section is the page's vocabulary in agent form. When
either one changes, change both in the same commit.

**Speak these words to the operator.** Use the on-screen names below, never the code names. Translate to code
yourself. Code names go in plans and diffs only.

### The request formula — five slots

Every UI change requested fits one sentence: **WHERE** (device, theme, state) · **WHAT** (screen,
then component) · **WHICH LAYER** · **WHICH KNOB** · **HOW MUCH** (direction and amount).

- **When a request leaves a slot empty, ask for that slot in these words** before you plan, and
  offer your best reading. Example: "Which layer: the edge ring, or the out glow?"
- **Anchor every percent.** "Cut it in half" at 70% today could mean 35% or 50%. Ask the operator "half of
  today, or 50% strength?".
- **The worked case.** The operator asks to "cut the size-pulse-outside in half". That names the
  whole effect, not a layer. The request as executed:
  "On a phone, in dark mode, on the chat window: edge ring to 50%
  strength; out glow to 50% strength and 60% reach; outer bloom back to 100%."

### The layers of a glow — operator words and the code

| Operator says | What they see | Where it sits | Border Beam code |
|---|---|---|---|
| **Edge ring** | the thin bright line on the border | on the border, 1px | `::after` · `--beam-stroke-opacity` |
| **Out glow** | the colored glow hugging the border | behind the element: ~14px past the edge and shining in through the glass | **`pulse-outside` only:** `::before`, which the code calls "core" · `--beam-inner-opacity` · `--beam-glow-reach` · `--beam-core-blur` |
| **Outer bloom** | the wide soft haze | ~42px past the edge, onto the page | `[data-beam-bloom]` · `--beam-bloom-opacity` · `--beam-bloom-blur` |
| **Inner glow** | light pooled just inside the edge | inside only | `size="pulse-inner"`, and the `::before` of the traveling beams (`sm`, `md`, `line`) |
| **Glass** | the see-through surface | the element itself | background alpha (tint) · `backdrop-filter: blur()` (frost) |
| **Halo** | all of the above breathing together | the whole effect | `size="pulse-outside"` |

⛔ **The misnomer that costs time.** On the `pulse-outside` halo, `::before` is "core" and its
strength hook is `--beam-inner-opacity`, yet it is the **out glow**, outside the edge. Never call it an
inner glow to the operator. On a phone a chat window fills the screen, so the bloom and the outer half of the out
glow are off-screen: what is visible there is the edge ring and the out glow's reach inward.

### The six knobs

| Knob | Means | Code | Operator words |
|---|---|---|---|
| **Strength** | how visible, 0–100% | opacity, alpha | dimmer, brighter, half as strong |
| **Reach** | how far it extends, out or in | size, spread, scale | smaller, pull it in, reach 60% |
| **Softness** | how fuzzy the edge | blur | softer, crisper |
| **Speed** | seconds per cycle; bigger is slower | duration | slower, calmer |
| **Color** | hue, saturation (vivid), brightness, palette | palette, hue-rotate, saturate | more blue, less vivid, use Sunset |
| **Motion** | the kind of movement | preset, travel | breathe, orbit, sweep, shimmer, drift |

"Bigger" can mean strength or reach, and "calmer" usually means speed. Ask which.

### Pairs that get mixed up

`size="…"` names the effect; how big it is lives under reach · padding (inside), margin (outside), gap
(between) · border (takes space) vs outline (takes none) vs focus ring · shadow (dark, below) vs glow
(light, around) · blur (the thing) vs frost (what's behind the glass) · opacity (see-through) vs
brightness (darker, still solid) · modal (blocks, center) vs drawer (from a side) vs sheet (from the
bottom, phones) vs popover (beside its trigger) · toast (leaves) vs banner (stays) vs tooltip (hover) ·
hover (mouse) vs focus (keyboard or cursor) vs pressed (the tap) · transition (once, on change) vs
animation (on its own, often looping) · viewport (the screen) vs window (a panel in the app).

### Screen sizes

Mobile first: the phone is the base, and wider sizes add to it. Phone is 0–639px, then `sm` 640+,
tablet `md` 768+, desktop `lg` 1024+, `xl` 1280+. Say "on a phone", "on a tablet" and "on desktop" to the operator.

The full dictionary (layout, surfaces, edges, depth, color, type, motion, states, feedback, theme),
the thinking spinners and the live Border Beam catalog are on the
[page](development_diagrams/ui_effects_and_thinking_icons.html).

---

## 1. The Seven Pillars of UI Excellence

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       HOUSE FRONTEND DESIGN ARCHITECTURE                     │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ 1. VISUAL SYSTEM & TOKENS    │ 2. FLUID MOTION & CRAFT      │ 3. WEBGPU     │
│ • ui-ux-pro-max              │ • emil-design-eng            │ • vgpu        │
│   (styles, palettes, fonts,  │   (Apple springs, sub-300ms, │   (WGSL, 25KB,│
│    heuristics, search)       │    review audit tables)      │    fluid mesh)│
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 4. MOBILE APPLE GLASS        │ 5. 3D SPATIAL MODELS         │ 6. SPECIALISTS│
│ • apple-glass                │ • visual-fx-3d               │ • webm-alpha  │
│   (HIG frosted 180% saturate,│   (R3F 3D spatial scenes,    │ • animate-expo│
│    live DOM liquid refraction│    glTF models, Rapier)      │ • write-swift │
├──────────────────────────────┴──────────────────────────────┴───────────────┤
│ 7. BORDER BEAM & OPTICAL GLOWS ENGINE (border-beam)                         │
│ • 3-tier sub-pixel stroke (mask-composite), inner/out glow, Gaussian bloom  │
│ • ~30fps rAF pulse driver, Ocean/Sunset tokens, AI Thinking Indicators      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Mobile First, Always (The Foundation)

### The Invariant
- **Design, build, and REVIEW the phone render before desktop.** Base CSS rule is the phone viewport (375px); `min-width` / Tailwind `sm:`, `md:`, `lg:` enhance OUT.
- ⛔ **NEVER write `max-width` media queries** that subtract from a desktop baseline. Subtractive desktop CSS almost always introduces responsive glitches on intermediate mobile screens.
- **Budget expensive effects for mobile hardware:** Mobile GPUs are thermally constrained and memory-bandwidth bound. Expensive CSS/GPU effects (e.g. `backdrop-filter: blur()`, `mix-blend-mode`, complex SVG filters like `feTurbulence`, or multiple layered canvas passes) must take a reduced count and lower values in the mobile base rule, enhanced only at desktop breakpoints.
- **Screenshot mobile first:** Always present the mobile render first when handing work back for review.
- **Dual-Viewport Layout Verification:** A layout suite that measures only one viewport has a blind spot. Any automated spec or manual QA asserting geometry, overflow, or element positioning must run at **BOTH** a phone (e.g. 375x667) and a desktop viewport.

---

## 3. Motion & Animation Standards ([`emil-design-eng`](../skills/emil-design-eng/SKILL.md))

Motion should communicate physical weight and momentum, not decorate:

- **The Sub-300ms UI Budget:** Standard UI transitions (modals, dropdowns, drawer expansions, card reveals) must complete within $\le 300\text{ms}$. Longer animations make interfaces feel sluggish.
- **Never Use `ease-in`:** Never use `ease-in` curves for enter transitions. Ease-in delays initial movement, creating perceptual lag. Always use custom spring physics or crisp `ease-out`.
- **Never Animate from `scale(0)`:** Zooming elements from zero looks unnatural. Enter scale should start at `scale(0.95)` with opacity `0` and spring into `scale(1)`.
- **GPU Transform Rules:** Only animate `transform` (`translate3d`, `scale`) and `opacity`. Never trigger browser layout reflows by animating `width`, `height`, `top`, `left`, `margin`, or `padding`.
- **Interruptible Physics:** Gestures (sheet pulls, pan dismissals) must update 1:1 with pointer coordinates and hand off velocity smoothly on release via spring physics.

---

## 4. Advanced Visual FX, 3D & Shaders

Three dedicated engines govern visual craft beyond flat CSS:

### 1. Mobile-First Apple Frosted & Liquid Glass ([`apple-glass`](../skills/apple-glass/SKILL.md))
- **Tier 1 (95% of UI):** Hardware-composited Apple HIG frosted glass via CSS `backdrop-filter: blur(20px) saturate(180%)`, subtle neutral border, and specular highlight. Runs on the GPU compositor at locked 60/120fps with zero JavaScript overhead.
- **Tier 2 (Physical Lenses):** Liquid glass with true optical refraction and chromatic dispersion via `@samasante/liquid-glass` (WebKit-hardened SVG Signed Distance Field displacement over live interactive DOM).
- **Tier 3 (Native Mobile):** `@callstack/liquid-glass` for React Native and iOS 26 SwiftUI `.glassEffect()`.
- ⛔ **Strict Ban on Canvas Hacks:** Never use `html2canvas` or 3D WebGL canvases for 2D UI elements.

### 2. WebGPU Shaders ([`vgpu`](../skills/vgpu/SKILL.md))
- Typed WGSL modules for fullscreen ambient fluid meshes, audio-reactive ripples, and particle compute.
- Always implement the **WebGPU Fallback Guard**: verify `navigator.gpu` and render CSS gradient backdrops on unsupported devices.

### 3. 3D Spatial Models & R3F ([`visual-fx-3d`](../skills/visual-fx-3d/SKILL.md))
- High-end 3D product models, interactive spatial cards, and physics via React Three Fiber ([`pmndrs/react-three-fiber`](https://github.com/pmndrs/react-three-fiber)), Drei, and Rapier.
- **On-Demand Rendering Invariant:** Always configure `<Canvas frameloop="demand" dpr={[1, 1.5]}>` to avoid draining mobile battery while idle.
- Reserved strictly for 3D meshes and spatial scenes, never HTML DOM cards.

### 4. Border Beam & Optical Glows Engine ([`border-beam`](../skills/border-beam/SKILL.md))
- **3-Tier Separation:** Tier 1 razor stroke (`::after` with `mask-composite: exclude`), Tier 2 inner/out glow (`::before`), Tier 3 Gaussian bloom (`[data-beam-bloom]`).
- **Presets:**
  - `size="line"` / `travel="sweep"`: Bottom Rim Sweep with anti-phase flicker (search inputs, chat input bars).
  - `size="line"` / `travel="loop"`: Full perimeter traveling laser line (interactive cards, modals).
  - `size="circle"` / `travel="orbit"`: Continuous 360° hairline laser orbit (avatars, round action buttons).
  - `size="edge-shimmer"`: Single boundary edge rim shimmer (drawers, dividers).
  - `size="pulse-outside"`: The halo (edge ring, out glow ~14px past edge, outer bloom).
  - `size="sm"`: Compact action pill highlight.
- **Shared Pulse Driver (~30fps):** Drive pulses through a shared ~30fps `requestAnimationFrame` pulse driver rather than unthrottled 120Hz CSS keyframes.
- **AI Thinking Indicators:** 2D Canvas Thinking Orb (3 orbital particle rings, 0 WebGL overhead), Cosmic Nebula, Plasma Reactor.
- **Interactive Visual Studio:** [`docs/development_diagrams/ui_effects_and_thinking_icons.html`](development_diagrams/ui_effects_and_thinking_icons.html).

---

## 5. Rich Media & Transparent Video ([`webm-alpha-video`](../skills/webm-alpha-video/SKILL.md))

When user interfaces require floating video elements (mascots, holographic badges, voice reaction avatars):
- Convert green-screen MP4 videos to transparent WebM (`VP9` with `yuva420p`):
  ```bash
  ffmpeg -i input_greenscreen.mp4 -vf "colorkey=0x00FF00:0.3:0.1,format=yuva420p" -c:v libvpx-vp9 -b:v 2M output_alpha.webm
  ```
- Embed cleanly with `<video autoPlay loop muted playsInline className="pointer-events-none ...">`.

---

## 6. The Two-Phase Creative Vision Lock Lifecycle ([`smh-designer`](../commands/smh-designer.md))

Front-end design is sensory. To avoid coding the wrong visual aesthetic, [`/smh-designer`](../commands/smh-designer.md) enforces a two-phase gate:

```
Phase 1: Creative Discovery & Vision Lock
  ↳ Interview on aesthetic mood, physics, and materials
  ↳ Deliver Creative Vision Brief (palette, typography, layout, motion curves, shaders)
  ↳ ⛔ STOP FOR APPROVAL: Operator confirms "Approved"

Phase 2: Technical Translation
  ↳ Deliver formal implementation_plan.md (components, props, bundle budget, test plan)
  ↳ ⛔ STOP FOR APPROVAL: Operator confirms "Approved"

Hand-off to Build Lane
  ↳ Hand approved implementation_plan.md to your build workflow or agent
```

---

## 7. Agent Skill Routing Matrix

| Task | Primary Skill | Supporting Resources / Capabilities |
|---|---|---|
| Complete design systems, color palettes, font pairings, styles | [`skills/ui-ux-pro-max`](../skills/ui-ux-pro-max/SKILL.md) | `search.py --design-system` |
| Motion craft, animations, easings, spring physics, review tables, toasts | [`skills/emil-design-eng`](../skills/emil-design-eng/SKILL.md) | `RECIPES.md` · Apple 2-parameter springs · Before/After tables |
| WebGPU shaders, fullscreen ambient fluid meshes, interactive plasma, particle compute | [`skills/vgpu`](../skills/vgpu/SKILL.md) | typed WGSL · @vgpu/adapter-mock · mobile CSS fallback |
| Apple frosted glass, optical liquid glass refraction, mobile-first glassmorphism | [`skills/apple-glass`](../skills/apple-glass/SKILL.md) | Apple HIG frosted glass · @samasante/liquid-glass live DOM refraction · 180% saturation · locked 120fps mobile |
| 3D spatial scenes, glTF models, geometric cards, 3D physics | [`skills/visual-fx-3d`](../skills/visual-fx-3d/SKILL.md) | [`pmndrs/react-three-fiber`](https://github.com/pmndrs/react-three-fiber) · Drei · Postprocessing · Rapier |
| Border beam optical glows, sub-pixel strokes, Gaussian blooms, AI thinking indicators | [`skills/border-beam`](../skills/border-beam/SKILL.md) | 3-tier optical architecture · ~30fps rAF pulse driver · Ocean/Sunset palettes · Thinking Orb 2D canvas |
| Mobile gestures & animations (React Native / Expo Reanimated) | [`skills/animate-expo`](../skills/animate-expo/SKILL.md) | Worklets & reanimated recipes |
| Apple platform UI & native Swift motion | [`skills/write-swift`](../skills/write-swift/SKILL.md) | Native SwiftUI springs & gestures |
| Converting green-screen assets to transparent WebM video overlays | [`skills/webm-alpha-video`](../skills/webm-alpha-video/SKILL.md) | ffmpeg colorkey scripts |
| End-to-end design engineering persona with Two-Phase Vision Lock | [`commands/smh-designer.md`](../commands/smh-designer.md) | 🦋 Caterpillar — Brainstorm, Audit, Scaffold & Build |

---

## 8. Pre-Delivery UI Quality Checklist

Before completing any frontend feature, chore, or UI refactor, verify against this checklist:

### Visual Quality
- [ ] **No Emoji Icons:** Use consistent SVG icon sets (Lucide, Heroicons, Simple Icons) instead of emoji characters.
- [ ] **Stable Hover States:** Use color/background/shadow transitions on hover; never use scale transforms that cause layout shifts on sibling elements.
- [ ] **High Contrast Text:** Minimum 4.5:1 contrast ratio in both Light and Dark modes.
- [ ] **Border Visibility:** In dark mode, borders use subtle white opacity (`rgba(255, 255, 255, 0.1)`); in light mode, clean neutral borders (`#E2E8F0`).

### Motion & Interaction
- [ ] **Press Feedback:** All clickable cards, buttons, and list items have `cursor: pointer` and `:active` scale feedback (`scale(0.97)`).
- [ ] **GPU Acceleration:** Only animate `transform` and `opacity`. Never animate `height`, `width`, `padding`, or `margin` directly.
- [ ] **No `ease-in` on Enters:** All enter transitions use `ease-out` or custom spring physics.
- [ ] **Animation Duration Budget:** All UI transitions complete in $\le 300\text{ms}$.
- [ ] **Interruptibility:** Gesture-driven components (sheets, drawers, sliders) update 1:1 with pointer events and hand off velocity smoothly on release.
- [ ] **Accessibility:** All animations respect `@media (prefers-reduced-motion: reduce)` by falling back to gentle crossfades or static states.

### Responsive & Mobile-First Quality
- [ ] **Mobile-First Layout:** Base styles (`default`) target mobile viewports (375px–390px); progressive enhancements use `md:` / `lg:` breakpoints. Never design desktop first and patch mobile after.
- [ ] **Zero Horizontal Overflow:** No horizontal scrollbar on mobile viewports. All text containers use `break-words` or `truncate` with visible limits.
- [ ] **Adaptive Wrap & Stacking:** Horizontal chips, filter pills, and button groups wrap cleanly (`flex-wrap`) or switch to vertical stacks / touch carousels on narrow screens without collision or truncation.
- [ ] **Touch Target Geometry:** All interactive touch targets are at least $44 \times 44\text{px}$ with adequate touch spacing (minimum 8px gap).
- [ ] **Performance Budget on Mobile:** Heavy backdrop-blur filters (`backdrop-blur-xl`), massive gradients, or complex SVG overlays are simplified or disabled on low-power mobile devices.
- [ ] **Dual-Viewport Verification:** Explicitly tested and verified at both mobile (375×667 / 390×844) and desktop (1280×800 / 1440×900) resolutions before sign-off.
- [ ] **WebGPU Fallback Guard:** Any component utilizing `vgpu` verifies `navigator.gpu` and renders a CSS gradient or SVG fallback on unsupported devices (iOS $\le 17$, legacy Android).
- [ ] **Border Beam & Glow Invariants:** Optical glows use 3-tier separation (razor stroke mask, inner/out glow, Gaussian bloom) driven by the ~30fps rAF pulse driver. No single-layer box shadows or unthrottled 120Hz CSS keyframe animations.
