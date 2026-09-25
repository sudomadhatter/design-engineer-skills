# Credits

This pack is a **composition**. The MIT licence in [LICENSE](LICENSE) covers the way these skills are
assembled, worded and wired together — not the underlying craft, libraries or teaching they draw on.
Those belong to the people below, and are worth going to directly.

## Emil Kowalski — motion & design engineering

[`skills/emil-design-eng`](skills/emil-design-eng/SKILL.md) encodes design-engineering philosophy
taught by **Emil Kowalski**: the opportunity filter for when *not* to animate, Apple's 2-parameter
spring model, the sub-300ms budget, the ban on `ease-in` for entrances, and the Before/After audit
table format.

- Course: **[animations.dev](https://animations.dev/)**
- Site: **[emilkowal.ski](https://emilkowal.ski/)**

If this skill is useful to you, take the course. It is the source.

## Poimandres (`pmndrs`) — the React 3D ecosystem

[`skills/visual-fx-3d`](skills/visual-fx-3d/SKILL.md), its
[`CATALOG.md`](skills/visual-fx-3d/CATALOG.md) and [`RECIPES.md`](skills/visual-fx-3d/RECIPES.md)
document and recommend the **Poimandres** open-source collective's libraries:

- [`pmndrs/react-three-fiber`](https://github.com/pmndrs/react-three-fiber) — React renderer for three.js
- [`pmndrs/drei`](https://github.com/pmndrs/drei) — helpers and abstractions
- [`pmndrs/postprocessing`](https://github.com/pmndrs/postprocessing) — effect composer
- [`pmndrs/react-three-rapier`](https://github.com/pmndrs/react-three-rapier) — physics
- [`pmndrs/gltfjsx`](https://github.com/pmndrs/gltfjsx) — glTF to JSX compiler
- [`pmndrs/leva`](https://github.com/pmndrs/leva) — GUI controls

All are MIT licensed by their respective authors. This pack ships **documentation and recipes only** —
no Poimandres source code is vendored here.

## Vercel Labs — WebGPU

[`skills/vgpu`](skills/vgpu/SKILL.md) documents patterns for
[`vercel-labs/vgpu`](https://github.com/vercel-labs/vgpu) and raw WebGPU / WGSL. Again:
documentation, not vendored source.

## Sam Asante & Callstack — optical liquid glass for web and mobile

[`skills/apple-glass`](skills/apple-glass/SKILL.md) and its
[`RECIPES.md`](skills/apple-glass/RECIPES.md) document and recommend:

- [`@samasante/liquid-glass`](https://github.com/samasante/liquid-glass) by **Sam Asante** — live-DOM optical refraction via WebKit-hardened SVG Signed Distance Field (SDF) displacement filters.
- [`@callstack/liquid-glass`](https://github.com/callstack/liquid-glass) by **Callstack** — React Native bridge to native Apple glass materials.

Both libraries are open source under their respective licences. This pack ships documentation, architecture standards, and component recipes only.

## Jakub Antalík (`Libraries.dev`) — optical border beam & glows engine

[`skills/border-beam`](skills/border-beam/SKILL.md) and its
[`THINKING_INDICATORS.md`](skills/border-beam/THINKING_INDICATORS.md) build upon the open-source optical architecture created by **Jakub Antalík** on [`Libraries.dev`](https://libraries.dev/):
- Three-tier optical hierarchy: 1px razor hairline edge stroke via CSS `mask-composite: exclude`, hugging inner/out glow, and 32px Gaussian bloom.
- 9-point radial gradient sub-pixel precision and ~30fps `requestAnimationFrame` pulse driver avoiding mobile GPU thermal throttling.

## Archify (`tt-a1i/archify`) — interactive workflow diagrams

The interactive diagrams in `docs/development_diagrams/` are authored and compiled with **Archify** ([`tt-a1i/archify`](https://github.com/tt-a1i/archify)) by **tt-a1i**, generating standalone SVG/HTML interactive walkthroughs with light/dark theme adaptation and state inspection.

## Everything else

`ui-ux-pro-max` (design-system data and search scripts), `border-beam`, `webm-alpha-video`, `animate-expo`,
`write-swift`, the `/smh-designer` command, interactive visual studio, and the frontend design guide were assembled for this
pack and are covered by the MIT licence above.

---

**If you own work referenced here and want the attribution changed or the material removed, open an
issue — it will be handled promptly.**
