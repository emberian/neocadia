# Scene Transitions

## Overview

Transitions connect Neocadia's spaces. They should feel magical—like stepping through a portal—not mechanical.

---

## Transition Types

### 1. Zone-to-Zone (Portal Transition)

**When**: Moving between zones via Lobby doors

**Animation Sequence**:
1. Player clicks door (0s)
2. Door opens/activates (0-0.3s)
3. Light/energy emerges from door (0.2-0.5s)
4. Screen fills with zone-colored light (0.4-0.7s)
5. Hold at full color (0.7-0.8s)
6. Fade into new zone (0.8-1.2s)
7. Zone ambient establishes (1.2-1.5s)

**Visual Elements**:
- Door animation specific to each zone
- Color matches destination zone
- Particle effects during transition
- Sound: Portal whoosh + destination ambient

### 2. Within-Zone Navigation

**When**: Moving between areas within same zone

**Animation**: Quick wipe or pan
- Horizontal wipe (most common)
- Directional based on layout
- Duration: 0.3-0.5s

**Visual**:
- Zone-colored wipe edge
- Subtle particle trail
- Maintains ambient continuity

### 3. Into Game

**When**: Launching a minigame

**Animation Sequence**:
1. Click cabinet/station (0s)
2. Zoom toward game (0-0.4s)
3. Game frame appears (0.3-0.6s)
4. Zone fades to black around game (0.5-0.8s)
5. Game UI fades in (0.7-1.0s)
6. Game ready (1.0s)

**Visual**:
- Maintains game cabinet aesthetic
- Frame styled to zone
- Smooth focus transition

### 4. Exit Game

**When**: Leaving a minigame

**Animation**:
- Reverse of entry
- Results displayed first
- Zoom out to zone
- Duration: 0.8-1.0s

### 5. Dialogue Start/End

**When**: Beginning or ending NPC conversation

**Animation**:
- Fade in dialogue box (0.2s)
- Character slides/fades in
- Fade out on exit (0.2s)
- No full-screen transition

### 6. Cutscene Transitions

**When**: Entering/exiting story cutscenes

**Animation**:
- Cinematic bars slide in (letterbox)
- Fade to scene
- Bars slide out on return
- Duration: 0.5s each way

---

## Zone-Specific Door Transitions

### Lobby → Neon Alley
- Door: Chrome frame pulses
- Light: Hot pink → Electric cyan
- Sound: Synth power-up
- Entry: Walk through neon corridor

### Lobby → Pixel Beach
- Door: Weathered wood creaks
- Light: Sky blue → Turquoise
- Sound: Wave crash
- Entry: Step onto warm sand

### Lobby → Glitch Garden
- Door: Frame glitches and phases
- Light: Shifting colors, unstable
- Sound: Digital corruption
- Entry: Colors normalize slowly

### Lobby → Starlight Cinema
- Door: Curtain parts
- Light: Spotlight yellow
- Sound: Orchestral swell
- Entry: Projector beam guides

### Lobby → Clockwork Quarter
- Door: Gears turn, unlocking
- Light: Warm brass glow
- Sound: Mechanical clicking
- Entry: Steam parts to reveal

### Lobby → Sugar Rush
- Door: Candy-stripe swings open
- Light: Bubblegum pink + mint
- Sound: Chime cascade
- Entry: Sugar sparkle shower

---

## Timing Guidelines

### Standard Durations
| Transition Type | Duration |
|----------------|----------|
| Zone-to-zone | 1.2-1.5s |
| Within-zone | 0.3-0.5s |
| Into game | 0.8-1.0s |
| Exit game | 0.8-1.0s |
| Dialogue | 0.2-0.3s |
| Cutscene | 0.5s each way |

### Pacing Principles
- Quick enough to not frustrate
- Long enough to be magical
- Skippable if needed (long transitions)
- Never abrupt

---

## Audio During Transitions

### Layering
1. **Fade Out**: Source zone ambient (0-0.4s)
2. **Transition Sound**: Whoosh/portal effect
3. **Fade In**: Destination ambient (0.6-1.0s)

### Music Handling
- Cross-fade between zone tracks
- Never cut abruptly
- Transition sounds don't conflict

---

## Loading Integration

### If Load Required
- Transition extends at "full screen" phase
- Loading indicator appears subtly
- Completes transition when ready

### Seamless Goal
- Most transitions should hide loading
- Pre-load adjacent zones when possible
- Stream assets during play

---

## Skip Functionality

### When Available
- Zone transitions (after first time)
- Cutscene transitions (always)
- Not available: Game enter/exit

### Skip UX
- "Press to skip" appears after 0.5s
- Click/key triggers quick fade
- Maintains sense of travel

---

## Accessibility

### Reduce Motion Mode
- Instant cuts replace animations
- Or simple fade (0.3s)
- No particles or movement

### Audio Cues
- Each transition type has distinct sound
- Helps orientation without visuals

---

## Technical Implementation

### Transition Manager
```typescript
interface Transition {
  type: TransitionType;
  from: SceneId;
  to: SceneId;
  duration: number;
  color?: string;
  skipAllowed: boolean;
}

async function executeTransition(t: Transition): Promise<void> {
  // Phase 1: Exit current
  await animateExit(t.from, t.duration * 0.4);

  // Phase 2: Loading (if needed)
  await loadScene(t.to);

  // Phase 3: Enter new
  await animateEnter(t.to, t.duration * 0.4);
}
```

### Animation System
- Tweening library for smooth motion
- Particle system for effects
- Shader support for color shifts

### Performance
- Precompute transition assets
- Simple geometry for effects
- Cap particles during transition
