# Navigation System

## Overview

Navigation in Neocadia uses a point-and-click model. Players click on hotspots to move between areas, interact with objects, and launch activities.

### Core Principles
1. **Always know where you can go** - Clickable areas clearly indicated
2. **Never feel lost** - Consistent back/home options
3. **Smooth transitions** - No jarring cuts
4. **Context preserved** - Remember where player came from

---

## Navigation Hierarchy

```
Main Menu
    └─→ The Lobby (Hub)
            ├─→ Token Fountain
            ├─→ Registry Desk (QWERTY)
            ├─→ Hall of Champions
            ├─→ Lost & Found
            ├─→ Player Cabinet
            ├─→ Zone Doors (7)
            │       ├─→ Neon Alley
            │       │       ├─→ Stage (NEON)
            │       │       ├─→ Tournament Board
            │       │       ├─→ Game Cabinets (3) → Games
            │       │       └─→ Loser's Lounge
            │       ├─→ Pixel Beach
            │       │       ├─→ Shack (PIXEL)
            │       │       ├─→ Pier → Fishing
            │       │       ├─→ Surfboard → Surfing
            │       │       ├─→ Shell Shore → Memory
            │       │       └─→ Sandcastle
            │       ├─→ Glitch Garden
            │       ├─→ Starlight Cinema
            │       ├─→ Clockwork Quarter
            │       └─→ Sugar Rush Boulevard
            └─→ Exit (Leave Neocadia)
```

---

## Interaction Model

### Hotspot Types

| Type | Visual Indicator | Click Action |
|------|-----------------|--------------|
| Door/Portal | Glow + destination hint | Travel to area |
| NPC | Character present | Open dialogue |
| Object | Subtle sparkle | Interact/collect |
| Game | Cabinet/station glow | Launch game |
| UI Element | Standard button style | Open interface |

### Hotspot Feedback

**On Hover**:
- Cursor changes to pointer
- Hotspot brightens
- Label appears (optional)
- Soft sound cue

**On Click**:
- Click sound
- Brief visual pulse
- Action initiates

---

## Scene Transitions

### Between Zones
1. Click door in Lobby
2. Door opens animation (0.3s)
3. Fade to black (0.3s)
4. Load destination
5. Fade in (0.3s)
6. Ambient establishes

**Total transition**: ~1 second

### Within Zones
1. Click navigation point
2. Quick wipe/fade (0.2s)
3. New view appears

**Total**: ~0.5 seconds

### Into Games
1. Click game cabinet/station
2. Zoom/focus on game area (0.5s)
3. Game UI fades in
4. Game starts

### Exit Games
1. Exit button clicked
2. Score/results shown
3. Confirmation
4. Zoom out to zone (0.5s)

---

## Back Navigation

### Always Available
- Back button in top-left corner
- Keyboard shortcut: ESC / Backspace
- Goes to previous location

### Context-Aware
| Current Location | Back Goes To |
|-----------------|--------------|
| Zone | Lobby |
| Sub-area of zone | Zone main |
| Game | Zone main |
| Dialogue | Remains in place |
| Menu | Close menu |

### Home Button
- Always returns to Lobby
- Confirmation if in game (lose progress)
- Accessible from anywhere

---

## Cursor States

| State | Visual | Meaning |
|-------|--------|---------|
| Default | Arrow | Can click UI |
| Pointer | Hand | Clickable hotspot |
| Wait | Hourglass | Loading |
| Talk | Speech bubble | NPC interaction |
| Move | Footsteps | Navigation point |
| Play | Play icon | Game start |
| Collect | Sparkle | Collectible |
| Locked | Lock | Unavailable |

---

## Waypoint System

### Automatic Waypoints
- Clicking far destination auto-paths
- Character walks there (if character visible)
- Transitions happen at path end

### Manual Navigation
- Click directly on adjacent areas
- Instant response

---

## Accessibility

### Keyboard Navigation
- Tab cycles through hotspots
- Enter activates selected
- Arrow keys for directional selection
- Number keys for quick slots

### Visual Aids
- Optional: Highlight all hotspots on key press
- Optional: Label all interactive elements
- Colorblind-friendly indicators

### Screen Reader Support
- All hotspots have aria labels
- Navigation announced
- State changes verbalized

---

## State Persistence

### Remember Position
- On zone exit, save last position
- On return, start at same spot
- Exception: Games always exit to zone entry

### Remember Context
- Dialogue progress saved
- Collection state preserved
- Game unlocks retained

---

## Loading States

### Short Loads (<0.5s)
- No indicator
- Instant feel

### Medium Loads (0.5-2s)
- Subtle loading indicator
- Progress if measurable

### Long Loads (>2s)
- Full loading screen
- Tip display
- Progress bar

---

## Technical Implementation

### Scene Management
```typescript
interface Scene {
  id: SceneId;
  type: 'zone' | 'subarea' | 'game' | 'menu';
  parent: SceneId | null;
  hotspots: Hotspot[];
  ambient: AmbientConfig;
}

interface Hotspot {
  id: string;
  bounds: Rectangle;
  type: HotspotType;
  action: Action;
  enabled: boolean;
  label?: string;
}
```

### Navigation Stack
```typescript
const navigationStack: SceneId[] = [];

function navigate(to: SceneId): void {
  navigationStack.push(currentScene);
  loadScene(to);
}

function goBack(): void {
  const previous = navigationStack.pop();
  if (previous) loadScene(previous);
}
```

### Transition Manager
```typescript
async function transition(from: Scene, to: Scene): Promise<void> {
  await fadeOut(0.3);
  unloadScene(from);
  await loadScene(to);
  await fadeIn(0.3);
}
```
