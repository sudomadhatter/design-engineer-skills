# AI Reasoning & Thinking Indicators Reference Catalog

The single source of truth for **AI reasoning modes**, **canvas-based thinking animations**, and **interactive cognitive indicators** across the command center and client projects.

Interactive visual studio & live animation preview: [`docs/development_diagrams/ui_effects_and_thinking_icons.html`](../../docs/development_diagrams/ui_effects_and_thinking_icons.html).

---

## 1. Mathematical 2D Canvas Engine Architecture

All reasoning indicators run on an ultra-lightweight mathematical 3D projection engine built directly on HTML5 Canvas 2D (`CanvasRenderingContext2D`):
- **Zero WebGL Context Overhead:** Renders 100% via trigonometric matrix math ($x, y, z \to x', y'$) into standard 2D canvas sub-pixel strokes. Avoids mobile browser WebGL context allocation limits (iOS Safari drops WebGL after 8–16 contexts).
- **Lightweight Footprint:** Full 9-state math engine is under 55KB uncompressed, with zero third-party 3D engine dependencies (no Three.js, Babylon, or glMatrix).
- **60 FPS Hardware Compositing:** Driven by standard `requestAnimationFrame` with sub-pixel anti-aliasing (`devicePixelRatio = 2` retina scaling).
- **Off-Screen Throttling:** Automatically pauses render loops when scrolled out of viewport using `IntersectionObserver`.

---

## 2. The 9 Reasoning States Decision Matrix

| State Key | Display Name | Visual Behavior | Primary Usage Surfaces |
|---|---|---|---|
| **`solving`** | 🎲 **Rubik's Cube** | 3D cubie bands scramble, rotate across orthogonal axes, and click back into alignment | Complex problem solving, code debugging, algorithmic synthesis, test generation |
| **`connecting`** | ✨ **Constellation** | Dynamic neural star cluster drifting in 3D with traveling pulse signals and connecting vector lines | Multi-agent coordination, knowledge graph traversal, associative reasoning, router dispatch |
| **`working`** | 🪐 **Orbits** | Tilted orbital particle rings revolving smoothly around a central glowing core | Standard reasoning bubbles, background tool execution, long-running agent workflows |
| **`searching`** | 🌐 **Globe** | Meridian scanning lines sweeping across a rotating dotted 3D globe | Web searches, repository codebase indexing, vector database retrieval |
| **`listening`** | 🌊 **Wave** | Concentric harmonic waveform rings undulating rhythmically | Multimodal audio input, live microphone listening, voice streaming |
| **`weaving`** | 🧬 **Braid** | Three intertwined helical strands plaiting rhythmically around a spherical volume | Cross-lane git diff integration, merge conflict resolution, multi-file refactoring |
| **`composing`** | 🎗️ **Ribbon** | Undulating multi-band harmonic sash floating with spatial depth | Technical writing, PRD authoring, copy editing, walkthrough generation |
| **`breathing`** | ⭕ **Ring** | Face-on harmonic ring slowly pulsing and morphing perimeter radii | Idle standby, listening for user input, background heartbeat |
| **`shaping`** | 📐 **Morph** | Smooth continuous geometric polygon transition: circle $\to$ triangle $\to$ square | Dynamic layout adaptation, viewport resizing, component geometry recalculation |

---

## 3. Scale Standards & Implementation Targets

### A. 64px Avatar Scale (`<ThinkingIndicator size="lg" />`)
- **Resolution:** 128x128 physical pixels (`style="width: 64px; height: 64px;"`).
- **Target Surfaces:**
  - Agent profile hero headers in chat dialogs.
  - Full-screen modal loading states.
  - Active specialist status cards in team rosters.
- **Styling:** Nested inside a rounded-3xl dark container (`#090d16`) with an ambient outer glow blur (`w-28 h-28 blur-2xl`).

### B. 20px Inline Stream Scale (`<ThinkingIndicator size="sm" />`)
- **Resolution:** 40x40 physical pixels (`style="width: 20px; height: 20px;"`).
- **Target Surfaces:**
  - Markdown streaming chat bubbles (`ThinkingBubble.tsx`).
  - Search bar input status badges.
  - Inline agent reasoning indicators preceding token stream output.
- **Styling:** Clean transparent background with high-contrast monochrome or cyan/emerald primary points.

---

## 4. Drop-In React Component Usage

```tsx
import { ThinkingIndicator } from '@/components/common/ThinkingIndicator';

// 1. Complex Algorithmic Reasoning in Chat Bubble
<ThinkingIndicator 
  mode="solving" 
  size="sm" 
  speed={1.0} 
  aria-label="Agent solving logic" 
/>

// 2. Multi-Agent Network Routing in Header
<ThinkingIndicator 
  mode="connecting" 
  size="lg" 
  speed={1.0} 
  aria-label="Connecting agent network" 
/>
```

