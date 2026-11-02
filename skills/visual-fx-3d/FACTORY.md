# The 7-Layer 3D & Motion Production Factory (Spline + Higgsfield + R3F + Gauntlet Loop)

This companion architecture manual turns [`SKILL.md`](./SKILL.md) and [`../living-site/SKILL.md`](../living-site/SKILL.md) into a deterministic, 7-layer production factory for Awwwards-tier 3D scrollytelling apps, interactive 3D book/passport spines, Higgsfield scroll films, and 60fps real-time viseme voice avatars.

## Contents
- [1. Locked Gold Standard Benchmarks & Reference Cloning](#1-locked-gold-standard-benchmarks--reference-cloning)
- [2. Layer 1: Core Application Framework, Aesthetic Tokens & Transient State](#2-layer-1-core-application-framework-aesthetic-tokens--transient-state)
- [3. Layer 2: Styling, Layout & Live `/design-system` X-Ray Director Drawer](#3-layer-2-styling-layout--live-design-system-x-ray-director-drawer)
- [4. Layer 3: 3D WebGL / WebGPU Rendering Engine & Interactive 3D Book Engine](#4-layer-3-3d-webgl--webgpu-rendering-engine--interactive-3d-book-engine)
- [5. Layer 4: Scroll Choreography & Camera Physics (`useScrollCameraDirector`)](#5-layer-4-scroll-choreography--camera-physics-usescrollcameradirector)
- [6. Layer 5: Generative AI Media & Deterministic Motion (`@higgsfield/cli`)](#6-layer-5-generative-ai-media--deterministic-motion-higgsfieldcli)
- [7. Layer 6: Real-Time Audio, Voice Agent & 60FPS Viseme Avatar (`VisemeCanvasEngine`)](#7-layer-6-real-time-audio-voice-agent--60fps-viseme-avatar-visemecanvasengine)
- [8. Layer 7: The 4-Gate Gauntlet Loop (`/design-loop`) & Anti-Slop Enforcement](#8-layer-7-the-4-gate-gauntlet-loop-design-loop--anti-slop-enforcement)
- [9. Complete GitHub Repository & MCP Directory + One-Shot Bootstrap](#9-complete-github-repository--mcp-directory--one-shot-bootstrap)

---

## 1. Locked Gold Standard Benchmarks & Reference Cloning

Before writing a single line of 3D or motion code, lock the structural and spatial reference sites during the planning phase (`design.md` / `implementation_plan.md`). Every 3D scrollytelling build inherits two non-negotiable Gold Standard benchmarks plus any domain-specific references supplied by the operator:

| Benchmark | Reference URL | What to Clone |
|---|---|---|
| **3D Book & Spine Mechanics** | [`https://press.stripe.com`](https://press.stripe.com) | Tactile 3D hardcover/passport spine geometry, realistic foil/emboss normal maps, physics-damped cover opening, and sequential page-turn rigging. |
| **Spatial Z-Axis Scrollytelling** | [`https://www.apple.com/iphone-18-pro/`](https://www.apple.com/iphone-18-pro/) | Deep Z-axis camera dolly choreography, scroll-scrubbed keyframe sequences, studio rim lighting, and razor-sharp dark-mode glass UI overlays. |
| **Living 3-Level Layout** | [`../living-site/SKILL.md`](../living-site/SKILL.md) | Level 1 interactive 3D showpiece, Level 2 continuous single-shot Higgsfield scroll film (`split-film.html`), and Level 3 self-drawing motion diagrams (`living-pipeline.js`). |

---

## 2. Layer 1: Core Application Framework, Aesthetic Tokens & Transient State

### Next.js App Router & SSR Isolation
- **Framework:** Next.js 15+ (App Router), React 19+, TypeScript 5+ (`strict: true`).
- **SSR Isolation Rule:** Every Three.js / WebGL / WebGPU / Spline component MUST carry `'use client'` at line 1 and be imported via `next/dynamic` with `{ ssr: false }` so server rendering never evaluates `window`, `WebGLRenderingContext`, or `AudioContext`.

### Dual-Theme CSS Token Foundation (`globals.css`)
```css
:root, [data-theme="dark"] {
  --bg-obsidian: #0B0C10;
  --bg-surface: rgba(20, 23, 31, 0.65);
  --bg-glass-border: rgba(255, 255, 255, 0.10);
  --text-primary: #F4F5F8;
  --text-secondary: #9BA1B0;
  --accent-primary: #D4AF37;   /* Metallic Gold / Brand Primary */
  --accent-secondary: #10B981; /* Verification Emerald */
}

[data-theme="light"] {
  --bg-obsidian: #F9F9FB;
  --bg-surface: rgba(255, 255, 255, 0.78);
  --bg-glass-border: rgba(11, 12, 16, 0.08);
  --text-primary: #111318;
  --text-secondary: #525866;
  --accent-primary: #0F2537;   /* Deep Editorial Navy */
  --accent-secondary: #B48A28; /* Warm Burnished Brass */
}
```

### Transient 60FPS State Store (`src/store/use3DDirectorStore.ts`)
Never drive 60fps scroll progress, page-turn angles, or audio viseme weights through React `useState`. Use `zustand` and read `use3DDirectorStore.getState()` directly inside R3F's `useFrame`:

```ts
// src/store/use3DDirectorStore.ts
import { create } from 'zustand';

export type VisemeId = 'sil' | 'aa' | 'ee' | 'oo';
export type FontPresetId = 'editorial' | 'grotesque' | 'technical';
export type ThemeMode = 'dark' | 'light';

interface DirectorState {
  scrollProgress: number;       // 0.0 -> 1.0
  activeChapter: number;        // 0..N
  bookOpenProgress: number;     // 0.0 (closed) -> 1.0 (open & docked left)
  activeViseme: VisemeId;
  isAgentSpeaking: boolean;
  fontPreset: FontPresetId;
  themeMode: ThemeMode;
  xrayEnabled: boolean;
  setScrollProgress: (progress: number, chapter: number, bookOpen: number) => void;
  setViseme: (viseme: VisemeId, speaking: boolean) => void;
  setFontPreset: (preset: FontPresetId) => void;
  setThemeMode: (mode: ThemeMode) => void;
  toggleXray: () => void;
}

export const use3DDirectorStore = create<DirectorState>((set) => ({
  scrollProgress: 0,
  activeChapter: 0,
  bookOpenProgress: 0,
  activeViseme: 'sil',
  isAgentSpeaking: false,
  fontPreset: 'editorial',
  themeMode: 'dark',
  xrayEnabled: false,
  setScrollProgress: (scrollProgress, activeChapter, bookOpenProgress) =>
    set({ scrollProgress, activeChapter, bookOpenProgress }),
  setViseme: (activeViseme, isAgentSpeaking) =>
    set({ activeViseme, isAgentSpeaking }),
  setFontPreset: (fontPreset) => set({ fontPreset }),
  setThemeMode: (themeMode) => set({ themeMode }),
  toggleXray: () => set((s) => ({ xrayEnabled: !s.xrayEnabled })),
}));
```

---

## 3. Layer 2: Styling, Layout & Live `/design-system` X-Ray Director Drawer

Pair [`.agents/skills/apple-glass`](../apple-glass/SKILL.md) (180% saturation frost + specular 1px borders) and [`.agents/skills/border-beam`](../border-beam/SKILL.md) with a live **`XRayDirectorDrawer`** mounted on `/design-system` (or toggled via `Cmd+Shift+D`). This lets the operator switch typography pairings, flip Dark/Light luxury themes, and inspect live 3D/Media badges (`[3D ENGINE: R3F + SPLINE]`, `[VIDEO: HIGGSFIELD SEEDANCE]`, `[VOICE: VISEME 60FPS]`) in real time:

```tsx
// src/components/design-system/XRayDirectorDrawer.tsx
'use client';

import React, { useEffect } from 'react';
import { use3DDirectorStore, FontPresetId, ThemeMode } from '@/store/use3DDirectorStore';

const FONT_PRESETS: Record<FontPresetId, { label: string; heading: string; body: string }> = {
  editorial: { label: 'Editorial Classic (Instrument Serif + Plus Jakarta)', heading: '"Instrument Serif", serif', body: '"Plus Jakarta Sans", sans-serif' },
  grotesque: { label: 'Neo-Swiss Grotesque (Syne + Inter)', heading: '"Syne", sans-serif', body: '"Inter", sans-serif' },
  technical: { label: 'Spatial Technical (Space Grotesk + JetBrains Mono)', heading: '"Space Grotesk", sans-serif', body: '"JetBrains Mono", monospace' },
};

export function XRayDirectorDrawer() {
  const { fontPreset, themeMode, xrayEnabled, setFontPreset, setThemeMode, toggleXray } = use3DDirectorStore();

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', themeMode);
    document.documentElement.style.setProperty('--font-heading', FONT_PRESETS[fontPreset].heading);
    document.documentElement.style.setProperty('--font-body', FONT_PRESETS[fontPreset].body);
  }, [fontPreset, themeMode]);

  return (
    <aside className="fixed bottom-4 right-4 z-50 rounded-2xl border border-white/15 bg-black/75 p-4 text-xs text-white backdrop-blur-xl shadow-2xl space-y-3 max-w-xs">
      <div className="flex items-center justify-between gap-4">
        <span className="font-semibold tracking-wider uppercase text-amber-400">Director X-Ray</span>
        <button onClick={toggleXray} className="px-2 py-1 rounded bg-white/10 hover:bg-white/20">
          {xrayEnabled ? 'X-Ray: ON' : 'X-Ray: OFF'}
        </button>
      </div>
      <div className="space-y-1">
        <label className="block text-white/60">Typography Pairing</label>
        <select
          value={fontPreset}
          onChange={(e) => setFontPreset(e.target.value as FontPresetId)}
          className="w-full rounded bg-white/10 px-2 py-1 text-white"
        >
          {(Object.keys(FONT_PRESETS) as FontPresetId[]).map((key) => (
            <option key={key} value={key} className="bg-neutral-900">
              {FONT_PRESETS[key].label}
            </option>
          ))}
        </select>
      </div>
      <div className="flex gap-2">
        {(['dark', 'light'] as ThemeMode[]).map((mode) => (
          <button
            key={mode}
            onClick={() => setThemeMode(mode)}
            className={`flex-1 py-1 rounded capitalize ${themeMode === mode ? 'bg-amber-500 text-black font-semibold' : 'bg-white/10'}`}
          >
            {mode}
          </button>
        ))}
      </div>
    </aside>
  );
}
```

---

## 4. Layer 3: 3D WebGL / WebGPU Rendering Engine & Interactive 3D Book Engine

### The 3-Stage Scrollytelling Book / Passport Rig (`Interactive3DBookEngine.tsx`)
Combines Apple's Z-axis spatial camera fly-in with Stripe Press's 3D spine rotation and sequential page-flip choreography:
- **Stage 1 (`0% -> 20%` Scroll — Hero Z-Axis Dolly):** The closed 3D book/passport floats at center screen under studio rim lighting while the camera dollies forward along the Z-axis.
- **Stage 2 (`20% -> 35%` Scroll — Spine Unfold & Left Dock):** The 3D book translates smoothly to the left desktop column (`x = -1.6`), rotates its spine open (`coverRotationY: 0 -> -Math.PI * 0.88`), and exposes page 1 while the right column reveals glassmorphic story cards.
- **Stage 3 (`35% -> 100%` Scroll — Sequential Page Turns & Stamp Verification):** Each chapter milestone (`activeChapter`) flips the corresponding page mesh (`0 -> -Math.PI * 0.85`) with vertex-bent curvature and triggers metallic foil/emerald stamp highlights.

```tsx
// src/components/3d/Interactive3DBookEngine.tsx
'use client';

import React, { useRef } from 'react';
import * as THREE from 'three';
import { useFrame } from '@react-three/fiber';
import { RoundedBox } from '@react-three/drei';
import { use3DDirectorStore } from '@/store/use3DDirectorStore';

const PAGE_COUNT = 5;

export function Interactive3DBookEngine() {
  const bookGroupRef = useRef<THREE.Group>(null);
  const frontCoverPivotRef = useRef<THREE.Group>(null);
  const pagePivotRefs = useRef<(THREE.Group | null)[]>([]);

  useFrame((_, delta) => {
    const { scrollProgress, bookOpenProgress, activeChapter } = use3DDirectorStore.getState();
    const damp = 1 - Math.exp(-8 * delta);

    if (bookGroupRef.current) {
      // Stage 1 -> 2: Dock book to left column as it opens
      const targetX = THREE.MathUtils.lerp(0, -1.45, bookOpenProgress);
      const targetRotationY = THREE.MathUtils.lerp(0.28, 0.12, bookOpenProgress);
      const targetRotationX = THREE.MathUtils.lerp(0.10, 0.04, scrollProgress);

      bookGroupRef.current.position.x = THREE.MathUtils.lerp(bookGroupRef.current.position.x, targetX, damp);
      bookGroupRef.current.rotation.y = THREE.MathUtils.lerp(bookGroupRef.current.rotation.y, targetRotationY, damp);
      bookGroupRef.current.rotation.x = THREE.MathUtils.lerp(bookGroupRef.current.rotation.x, targetRotationX, damp);
    }

    if (frontCoverPivotRef.current) {
      // Open front cover around the left spine hinge (-Math.PI * 0.88)
      const targetCoverAngle = THREE.MathUtils.lerp(0, -Math.PI * 0.88, bookOpenProgress);
      frontCoverPivotRef.current.rotation.y = THREE.MathUtils.lerp(
        frontCoverPivotRef.current.rotation.y,
        targetCoverAngle,
        damp
      );
    }

    // Sequential page turns driven by activeChapter
    for (let i = 0; i < PAGE_COUNT; i++) {
      const pivot = pagePivotRefs.current[i];
      if (!pivot) continue;
      const isFlipped = activeChapter > i;
      const targetPageAngle = isFlipped ? -Math.PI * (0.84 - i * 0.015) : -0.02 * i;
      pivot.rotation.y = THREE.MathUtils.lerp(pivot.rotation.y, targetPageAngle, damp);
    }
  });

  return (
    <group ref={bookGroupRef} position={[0, 0, 0]}>
      {/* Back Cover */}
      <mesh position={[0.9, 0, -0.08]}>
        <RoundedBox args={[1.8, 2.5, 0.06]} radius={0.02} smoothness={4}>
          <meshStandardMaterial color="#0F2537" roughness={0.35} metalness={0.25} />
        </RoundedBox>
      </mesh>

      {/* Spine Hinge */}
      <mesh position={[0, 0, 0]}>
        <cylinderGeometry args={[0.09, 0.09, 2.5, 24]} />
        <meshStandardMaterial color="#D4AF37" roughness={0.25} metalness={0.85} />
      </mesh>

      {/* Interior Pages Hinged at Spine (x = 0) */}
      {Array.from({ length: PAGE_COUNT }).map((_, i) => (
        <group
          key={i}
          ref={(el) => { pagePivotRefs.current[i] = el; }}
          position={[0.02, 0, -0.04 + i * 0.015]}
        >
          <mesh position={[0.86, 0, 0]}>
            <boxGeometry args={[1.72, 2.4, 0.008, 24, 1, 1]} />
            <meshStandardMaterial color="#F8F6F0" roughness={0.65} metalness={0.05} />
          </mesh>
        </group>
      ))}

      {/* Front Cover Hinged at Spine (x = 0) */}
      <group ref={frontCoverPivotRef} position={[0, 0, 0.08]}>
        <mesh position={[0.9, 0, 0]}>
          <RoundedBox args={[1.8, 2.5, 0.06]} radius={0.02} smoothness={4}>
            <meshStandardMaterial color="#0F2537" roughness={0.3} metalness={0.4} />
          </RoundedBox>
        </mesh>
      </group>
    </group>
  );
}
```

### Spline MCP, Blender MCP & GLB Draco Compression Pipeline
- **Spline MCP (`https://mcp.spline.design/mcp`):** Use for rapid interactive 3D hero props and characters. Always place `runtime/spline-shield.js` (`living-site`) over embedded Spline iframes so mouse wheel events never trap page scroll.
- **Blender MCP (`ahujasid/mcp-for-blender`):** Use to generate custom embossed crests, rigid-body props, and UV-unwrapped `.glb` assets directly from Claude Code.
- **Mandatory GLTF Compression & Typing:**
  ```bash
  npx @gltf-transform/cli optimize raw-model.glb public/models/model-draco.glb --compress draco --texture-compress webp
  npx gltfjsx public/models/model-draco.glb --transform --types -o src/components/3d/ModelGenerated.tsx
  ```

---

## 5. Layer 4: Scroll Choreography & Camera Physics (`useScrollCameraDirector`)

Synchronize `Lenis` smooth inertial scrolling with GSAP `ScrollTrigger` (`scrub: 1.2`) so scroll progress updates `use3DDirectorStore` transiently without triggering React component re-renders:

```tsx
// src/hooks/useScrollCameraDirector.ts
'use client';

import { useEffect } from 'react';
import Lenis from 'lenis';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { use3DDirectorStore } from '@/store/use3DDirectorStore';

gsap.registerPlugin(ScrollTrigger);

export function useScrollCameraDirector(totalChapters = 5) {
  useEffect(() => {
    const lenis = new Lenis({ lerp: 0.08, smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);

    const ticker = (time: number) => lenis.raf(time * 1000);
    gsap.ticker.add(ticker);
    gsap.ticker.lagSmoothing(0);

    const trigger = ScrollTrigger.create({
      trigger: '#scrollytelling-track',
      start: 'top top',
      end: 'bottom bottom',
      scrub: 1.2,
      onUpdate: (self) => {
        const p = self.progress; // 0.0 -> 1.0
        const bookOpen = gsap.utils.clamp(0, 1, (p - 0.18) / 0.17);
        const chapterProg = gsap.utils.clamp(0, 0.999, (p - 0.35) / 0.65);
        const activeChapter = p < 0.35 ? 0 : Math.floor(chapterProg * totalChapters) + 1;
        use3DDirectorStore.getState().setScrollProgress(p, activeChapter, bookOpen);
      },
    });

    return () => {
      trigger.kill();
      gsap.ticker.remove(ticker);
      lenis.destroy();
    };
  }, [totalChapters]);
}
```

---

## 6. Layer 5: Generative AI Media & Deterministic Motion (`@higgsfield/cli`)

### Pilot Generation Protocol (Credit Protection Rule)
Never batch-render 10 video clips blind. Generate **1 Pilot Keyframe (`nano_banana_2`)** and **1 Pilot Motion Clip (`seedance_2_5` or `seedance_2_0`)**, verify lighting, soul-id character lock, and continuity, and log every credit in `ledger.tsv` (`living-site` Stage 3).

```bash
# 1. Verify Higgsfield CLI authentication & credit balance
npx @higgsfield/cli account status < /dev/null

# 2. Lock persistent avatar character identity (Soul ID)
npx @higgsfield/cli soul-id create --name "avatar_anchor" --images ./refs/anchor-01.png,./refs/anchor-02.png

# 3. Generate 4K studio keyframe with transparent/clean dark backdrop
npx @higgsfield/cli generate image nano_banana_2 \
  --prompt "Editorial portrait, studio rim lighting, neutral head pose, obsidian background #0B0C10, 85mm lens" \
  --soul-id "avatar_anchor" \
  --output ./public/media/avatar-base.png

# 4. Generate continuous single-shot scroll film clip or locked-head avatar idle loop
npx @higgsfield/cli generate video seedance_2_5 \
  --image ./public/media/avatar-base.png \
  --prompt "One continuous single shot, no cuts. Subtle breathing and natural eye blinks, head remains steady." \
  --duration 5 \
  --output ./raw-avatar-idle.mp4

# 5. Strip audio track & compress to web-ready MP4 + WebM
ffmpeg -y -i ./raw-avatar-idle.mp4 -an -c:v libx264 -crf 22 -pix_fmt yuv420p ./public/media/avatar-idle.mp4
```

### Deterministic Code-Driven Motion (`window.seek(t)`)
For Level 3 product architecture animations (`howseen-ai/claude-motion-design` and `living-site/recipes/living-pipeline.js`), expose `window.seek = (t: number) => ...` so headless Playwright/Puppeteer scripts can step frame-by-frame or verify motion determinism at any timestamp `t`.

---

## 7. Layer 6: Real-Time Audio, Voice Agent & 60FPS Viseme Avatar (`VisemeCanvasEngine`)

Never swap full-frame `<video>` tags on every spoken syllable (which causes black-frame flicker and uncanny head jumps). Use a **2-Layer Composited 60FPS HTML5 `<canvas>` Engine**:
1. **Base Spine Layer:** A continuously looping, locked-head `<video>` (`avatar-idle.mp4`) providing natural blinks, micro-nods, and breathing.
2. **Feathered Mouth Viseme Overlay:** An offscreen `<canvas>` that draws the active mouth viseme sprite (`sil`, `aa`, `ee`, `oo`) and masks it with a soft radial gradient (`globalCompositeOperation = 'source-in'`) over the lower face region, driven at 60fps by a Web Audio API `AnalyserNode` (`fftSize = 512`) or `wawa-lipsync`.

```tsx
// src/components/avatar/VisemeCanvasEngine.tsx
'use client';

import React, { useEffect, useRef } from 'react';
import { use3DDirectorStore, VisemeId } from '@/store/use3DDirectorStore';

interface VisemeCanvasEngineProps {
  idleVideoSrc: string;
  visemeSpritePaths: Record<VisemeId, string>;
  audioElement?: HTMLAudioElement | null;
  width?: number;
  height?: number;
}

export function VisemeCanvasEngine({
  idleVideoSrc,
  visemeSpritePaths,
  audioElement,
  width = 512,
  height = 640,
}: VisemeCanvasEngineProps) {
  const mainCanvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = mainCanvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // Offscreen canvas for soft radial-gradient feathering of the mouth region
    const mouthCanvas = document.createElement('canvas');
    mouthCanvas.width = width;
    mouthCanvas.height = height;
    const mouthCtx = mouthCanvas.getContext('2d')!;

    // Base idle video spine
    const video = document.createElement('video');
    video.src = idleVideoSrc;
    video.muted = true;
    video.loop = true;
    video.playsInline = true;
    video.play().catch(() => {});

    // Preload viseme mouth sprites
    const sprites: Partial<Record<VisemeId, HTMLImageElement>> = {};
    (Object.keys(visemeSpritePaths) as VisemeId[]).forEach((id) => {
      const img = new Image();
      img.src = visemeSpritePaths[id];
      sprites[id] = img;
    });

    // Optional Web Audio API formant analyser
    let analyser: AnalyserNode | null = null;
    let freqData: Uint8Array<ArrayBuffer> | null = null;
    if (audioElement) {
      const audioCtx = new AudioContext();
      const source = audioCtx.createMediaElementSource(audioElement);
      analyser = audioCtx.createAnalyser();
      analyser.fftSize = 512;
      analyser.smoothingTimeConstant = 0.65;
      source.connect(analyser);
      analyser.connect(audioCtx.destination);
      freqData = new Uint8Array(analyser.frequencyBinCount);
    }

    let rafId = 0;
    const render = () => {
      if (analyser && freqData) {
        analyser.getByteFrequencyData(freqData);
        // Low (vowels/oo: bins 2..10), Mid (open aa: bins 11..28), High (sibilant/ee: bins 29..64)
        const low = freqData.slice(2, 10).reduce((a, b) => a + b, 0) / 8;
        const mid = freqData.slice(11, 28).reduce((a, b) => a + b, 0) / 17;
        const high = freqData.slice(29, 64).reduce((a, b) => a + b, 0) / 35;

        let nextViseme: VisemeId = 'sil';
        const energy = Math.max(low, mid, high);
        if (energy > 28) {
          if (mid >= low && mid >= high) nextViseme = 'aa';
          else if (high > mid) nextViseme = 'ee';
          else nextViseme = 'oo';
        }
        use3DDirectorStore.getState().setViseme(nextViseme, energy > 28);
      }

      // 1. Draw base looping idle video frame
      if (video.readyState >= 2) {
        ctx.drawImage(video, 0, 0, width, height);
      }

      // 2. Composite feathered mouth sprite when speaking
      const { activeViseme } = use3DDirectorStore.getState();
      const sprite = sprites[activeViseme];
      if (activeViseme !== 'sil' && sprite && sprite.complete) {
        mouthCtx.clearRect(0, 0, width, height);
        mouthCtx.globalCompositeOperation = 'source-over';
        mouthCtx.drawImage(sprite, 0, 0, width, height);

        // Radial feather mask centered on the mouth coordinates (cx = 0.5, cy = 0.66)
        mouthCtx.globalCompositeOperation = 'destination-in';
        const cx = width * 0.5;
        const cy = height * 0.66;
        const radius = width * 0.18;
        const grad = mouthCtx.createRadialGradient(cx, cy, radius * 0.35, cx, cy, radius);
        grad.addColorStop(0, 'rgba(0,0,0,1)');
        grad.addColorStop(1, 'rgba(0,0,0,0)');
        mouthCtx.fillStyle = grad;
        mouthCtx.beginPath();
        mouthCtx.arc(cx, cy, radius, 0, Math.PI * 2);
        mouthCtx.fill();

        ctx.drawImage(mouthCanvas, 0, 0);
      }

      rafId = requestAnimationFrame(render);
    };

    rafId = requestAnimationFrame(render);
    return () => {
      cancelAnimationFrame(rafId);
      video.pause();
    };
  }, [idleVideoSrc, visemeSpritePaths, audioElement, width, height]);

  return (
    <canvas
      ref={mainCanvasRef}
      width={width}
      height={height}
      className="w-full h-auto rounded-2xl border border-white/10 shadow-2xl"
    />
  );
}
```

---

## 8. Layer 7: The 4-Gate Gauntlet Loop (`/design-loop`) & Anti-Slop Enforcement

Never declare a 3D or motion frontend complete on code compile alone. Run the **4-Gate Gauntlet Loop** (`MAX_ITERATIONS = 4`):

1. **Gate 1 — Multi-Viewport Scroll & Spatial Inspection:**
   - Boot the dev server in the background and capture headless Playwright/Puppeteer screenshots ([`living-site/tools/shots.js`](../living-site/tools/shots.js) or headless Playwright) at **Desktop (`1440x900`)** and **Mobile (`390x844`)** across **`0%`, `33%`, `66%`, and `100%` scroll depth**.
   - Verify two shots taken 1 second apart at the hero and Level 3 sections differ visually (proving live animation is ticking).
2. **Gate 2 — Runtime Telemetry & Continuity Gate:**
   - Zero console errors, zero uncaught page exceptions, zero WebGL context loss warnings.
   - Draw calls `< 100` and frame time `< 16.6ms` (`60fps`) verified via `r3f-perf` or `<PerformanceMonitor>`.
   - Run `python3 .agents/skills/living-site/check.py <entry.html>` (or verify `prefers-reduced-motion` + `runtime/spline-shield.js`), `python3 .agents/skills/living-site/tools/cutscan.py` on every Higgsfield clip, and `zsh .agents/skills/living-site/tools/continuity-gate.sh` on any joined scroll film.
3. **Gate 3 — Anti-Slop Design & Copy Audit (`taste-skill` + `humanizer`):**
   - Reject default Tailwind indigo/violet gradients, glowing neon AI boxes, centered 3-card SaaS clichés, and unrequested floating chat bubbles.
   - Reject AI copy tells (`delve`, `tapestry`, `elevate`, `seamless`, `unlock`, `revolutionary`, and em/en dashes) per [`../living-site/references/copy.md`](../living-site/references/copy.md).
4. **Gate 4 — Autonomous Remediation or Graduation:**
   - If any gate fails, fix the highest-severity visual, shader, camera-clipping, or copy defect first and re-run Gates 1–3 before presenting the build to the operator.

---

## 9. Complete GitHub Repository & MCP Directory + One-Shot Bootstrap

### The 14 Production Repositories & MCP Servers
| Layer | Repository / Tool | Role |
|---|---|---|
| **3D Engine** | [`pmndrs/react-three-fiber`](https://github.com/pmndrs/react-three-fiber) · [`pmndrs/drei`](https://github.com/pmndrs/drei) · [`pmndrs/react-postprocessing`](https://github.com/pmndrs/react-postprocessing) | Declarative React Three.js scene graph, cameras, materials, and post-processing. |
| **3D Telemetry** | [`utsuboco/r3f-perf`](https://github.com/utsuboco/r3f-perf) | Real-time WebGL draw-call, triangle, texture memory, and FPS monitor (`< 100` draw calls gate). |
| **GLTF Pipeline** | [`pmndrs/gltfjsx`](https://github.com/pmndrs/gltfjsx) · [`donmccurdy/glTF-Transform`](https://github.com/donmccurdy/glTF-Transform) | Converts and Draco-compresses `.glb` models into typed React components. |
| **3D MCPs** | [`https://mcp.spline.design/mcp`](https://mcp.spline.design/mcp) · [`ahujasid/mcp-for-blender`](https://github.com/ahujasid/mcp-for-blender) | Direct agent creation of interactive Spline scenes and custom Blender `.glb` geometry. |
| **Scroll & Motion** | [`darkroomengineering/lenis`](https://github.com/darkroomengineering/lenis) · [`greensock/GSAP`](https://github.com/greensock/GSAP) · [`theatre-js/theatre`](https://github.com/theatre-js/theatre) | Inertial smooth scrolling, `ScrollTrigger` camera scrubbing, and keyframe timelines. |
| **Generative Media** | [`higgsfield-ai/higgsfield-cli`](https://github.com/higgsfield-ai/higgsfield-cli) · [`howseen-ai/claude-motion-design`](https://github.com/howseen-ai/claude-motion-design) | CLI generation for Nano Banana 2, Seedance 2.0/2.5, Kling 3.0, Soul ID, and deterministic `window.seek(t)` motion graphics. |
| **Voice & Visemes** | [`wass08/wawa-lipsync`](https://github.com/wass08/wawa-lipsync) | Real-time browser Web Audio API phoneme/viseme detection paired with `VisemeCanvasEngine`. |
| **Anti-Slop QA** | [`Leonxlnx/taste-skill`](https://github.com/Leonxlnx/taste-skill) · [`blader/humanizer`](https://github.com/blader/humanizer) | Layout taste enforcement and AI copywriting tell removal. |

### One-Shot Project Bootstrap (`setup-3d-factory.sh`)
```bash
#!/usr/bin/env bash
set -euo pipefail

# 1. Core 3D, Scroll, State & Audio Viseme Dependencies (React 19 + R3F 9)
npm i three @react-three/fiber@^9 @react-three/drei@^10 @react-three/postprocessing@^3 postprocessing \
  lenis gsap zustand lucide-react wawa-lipsync

# 2. Dev & Asset Optimization Tooling
npm i -D @types/three r3f-perf gltfjsx @gltf-transform/cli @higgsfield/cli @playwright/test

# 3. Prepare Public Media & Draco Model Directories
mkdir -p public/models public/media/visemes public/media/frames src/components/3d src/components/avatar src/store src/hooks
```
