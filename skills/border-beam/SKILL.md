---
name: border-beam
description: "Multi-tiered optical border beam engine, hairline razor edge strokes, inner and out glows, outer atmospheric aurora halos, and AI thinking indicators. Based on Jakub Antalík's Libraries.dev open-source architecture with custom 9-point radial gradient coordinates, SVG mask-composite sub-pixel precision, and 20px 2D canvas 3D-projected Thinking Orbs. Use when designing or implementing glowing border cards, buttons, drawers, inputs, or reasoning indicators."
---

# Border Beam & Optical Glows Engine

The single source of truth for **multi-tiered optical glows**, **boundary edge shimmers**, **aurora halos**, and **AI reasoning indicators** across the command center and projects.

Based on Jakub Antalík's open-source `Libraries.dev` architecture, this engine decouples illumination into three distinct optical tiers to achieve Apple-grade visual depth without pixel bleeding, crude conic gradient wheels, or mobile GPU thermal throttling.

Interactive visual catalog & live studio: [`docs/development_diagrams/ui_effects_and_thinking_icons.html`](../../docs/development_diagrams/ui_effects_and_thinking_icons.html).
Dedicated AI Thinking Indicators catalog: [`THINKING_INDICATORS.md`](THINKING_INDICATORS.md).

---

## 1. The Three-Tier Optical Architecture

Standard CSS borders or single-layer `box-shadow` effects appear flat and synthetic. Authentic optical presence requires three separate hardware-composited layers:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      BORDER BEAM THREE-TIER HIERARCHY                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ TIER 1: HAIRLINE EDGE STROKE (DOM: ::after, z-index: 2)                     │
│ • 1px razor-sharp sub-pixel stroke                                          │
│ • Cut via mask-composite: intersect, exclude (or webkit-mask-composite: xor)│
│ • Renders 9-point radial-gradient coordinates with zero corner fuzziness   │
├─────────────────────────────────────────────────────────────────────────────┤
│ TIER 2: GLOW LAYER (DOM: ::before, z-index: 1) - the code calls it "core"   │
│ • Traveling beams and pulse-inner: the INNER GLOW, inset: 0, inside the edge│
│ • pulse-outside (the halo): the OUT GLOW, inset: -14px, behind the element, │
│   past the edge and in through the glass (strength: --beam-inner-opacity)   │
│ • Say "inner glow" or "out glow" to the operator, never "core"              │
├─────────────────────────────────────────────────────────────────────────────┤
│ TIER 3: OUTER ATMOSPHERIC BLOOM (DOM: [data-beam-bloom], z-index: 0)        │
│ • Soft 28px–36px Gaussian-dispersed aurora field                            │
│ • Spills volumetric light into dark backgrounds                             │
│ • Driven by a shared ~30fps requestAnimationFrame cosine pulse loop         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Presets Decision Matrix

| Preset Code | Prop Key | Primary Target Surfaces | Optical Behavior |
|:---:|---|---|---|
| **[Bottom Rim Sweep]** *(★ Operator Favorite)* | `size="line"` / `travel="sweep"` | Chat input bars, search inputs, docked headers | Oscillating back-and-forth glide along the bottom edge with anti-phase flicker and edge fading |
| **[Perimeter Shimmer Loop]** | `size="line"` / `travel="loop"` | Interactive focal cards, modal frames, feature cards | Continuous 360° perimeter travel with slender Northern Lights curtain rays and multi-color auroral flicker |
| **[Circle Orbit]** *(★ Operator Favorite)* | `size="circle"` / `travel="orbit"` | Agent avatar halos, round CTA buttons, audio dials | Continuous 1px hairline laser beam traveling 360° around circular shapes |
| **[Edge Shimmer]** | `size="edge-shimmer"` | Docked drawer top rims, panel dividers, search inputs | Sweeps along a single horizontal border edge without enclosing the container |
| **[Halo]** | `size="pulse-outside"` | Specialist chat dialogs, hero spotlight cards | Edge ring, out glow (~14px past the edge, seen through the glass) and outer bloom (~42px) spilling onto the page |
| **[Pill]** | `size="sm"` | Action pills, launcher buttons, high-priority CTAs | Compact 1px perimeter highlight with hugging inner luminance |
| **[Inner]** | `size="pulse-inner"` | Secondary cards, inactive panels, telemetry gauges | Breaths slowly (6.0s) strictly inside container boundaries |
| **[Glass]** | `fx-smoked-glass` | Specialist chat backdrop, login gates, modals | 72% obsidian smoked glass pane over statically blurred brand emblem watermark |

### Code Recipes: Traveling Line (Loop & Ping-Pong) & Circle Orbit

```css
/* Shared Angle Property & Rotation Keyframes */
@property --beam-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}
@keyframes beam-travel-rotate {
  0% { --beam-angle: 0deg; }
  100% { --beam-angle: 360deg; }
}

/* Option 1: Traveling Perimeter Line (Full 360° Loop) */
.beam-travel-line {
  position: relative;
}
.beam-travel-line::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  pointer-events: none;
  padding: 1.5px;
  background: conic-gradient(
    from var(--beam-angle, 0deg) at 50% 50%,
    transparent 0deg,
    transparent 270deg,
    var(--beam-secondary, #0072ff) 305deg,
    var(--beam-primary, #00c2ff) 345deg,
    #ffffff 360deg
  );
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: beam-travel-rotate var(--beam-speed, 6.0s) linear infinite;
  z-index: 2;
}

/* Option 2: Back & Forth Ping-Pong Line (Horizontal Sweep) */
.beam-pingpong-line {
  position: relative;
}
.beam-pingpong-line::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  pointer-events: none;
  padding: 1.5px;
  background: radial-gradient(
    ellipse 130px 45px at var(--pingpong-x, 50%) 50%,
    #ffffff 0%,
    var(--beam-primary, #00c2ff) 30%,
    var(--beam-secondary, #0072ff) 65%,
    transparent 85%
  );
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  z-index: 2;
}

/* Full Circle Orbit Beam (Avatars, Round CTAs) */
.beam-circle-orbit {
  position: relative;
  border-radius: 50%;
}
.beam-circle-orbit::after {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: 50%;
  pointer-events: none;
  padding: 1.5px;
  background: conic-gradient(
    from var(--beam-angle, 0deg) at 50% 50%,
    transparent 0deg,
    transparent 270deg,
    var(--beam-secondary, #0072ff) 305deg,
    var(--beam-primary, #00c2ff) 345deg,
    #ffffff 360deg
  );
  -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  animation: beam-travel-rotate var(--beam-speed, 6.0s) linear infinite;
  z-index: 2;
}
```

---

## 3. Approved Design Tokens & Palettes

All presets integrate with the design tokens in `/smh-designer`:

### Ocean Palette (`colorVariant="ocean"`) — Signature
- **Atmosphere:** High-altitude aeronautical cockpit, deep night sky, electric aurora.
- **Tokens:**
  - Electric Cyan: `#00C2FF` (Primary spike / highlight)
  - Aero Blue: `#0072FF` (Mid-tone core luminance)
  - Violet Indigo: `#6B00FF` (Deep atmospheric roll-off)

### Sunset Palette (`colorVariant="sunset"`) — Warm Horizon
- **Atmosphere:** Sunset approach, golden hour horizon, active warning/alert engagement.
- **Tokens:**
  - Sunset Coral: `#FF4B4B`
  - Radiant Amber: `#FF8533`
  - Luminous Gold: `#FFC700`

### Default Motion & Strength Tokens
- **Default Speed:** `6.0s` (Slow / Calm) — prevents distraction during focused reading.
- **Normal Interaction Speed:** `3.1s` — for active buttons or modal entrances.
- **Default Strength:** `90%` (`0.9`) opacity.

---

## 4. AI Thinking & Reasoning Indicators

When models or agents are actively processing, pair border effects with the dedicated thinking indicators:

1. **Thinking Orb (`<ThinkingOrb />`)**:
   - 20px 2D canvas mathematical projection of 3 projected 3D orbital particle rings.
   - Zero WebGL context overhead (eliminates `CONTEXT_LOST_WEBGL` crashes on mobile Safari).
   - Embedded inside chat message bubbles (`ThinkingBubble.tsx`).
2. **Socratic Progress Arc (`<SocraticDial />`)**:
   - Concentric circular milestone arc tracking step progression (Questioning → Hinting → Synthesizing → Mastery).
3. **6-Lane Citation Seal (`<VerificationBadge />`)**:
   - Hermetic source lock indicator showing verified FAA regulations (14 CFR) and aeronautical manuals.

---

## 5. Performance & Mobile Invariants

1. **Shared Pulse Driver:** Outward-blooming breathing pulses must be driven by a shared `requestAnimationFrame` loop capped at ~30fps (`pulseDriver.ts`). This avoids running 15+ CSS `@property` keyframe animations per element at 120Hz display refresh rates, saving 50–75% of GPU memory bandwidth.
2. **Sub-Pixel Mask Compositing:** Always use native CSS masking (`mask-composite: exclude` / `-webkit-mask-composite: xor`) for hairline borders instead of thick SVG elements.
3. **Accessibility:** Always provide `@media (prefers-reduced-motion: reduce)` fallbacks that freeze animation cycles into static, tasteful 1px borders.

