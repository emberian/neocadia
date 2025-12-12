# Minigame Spec: Wave Rider

## Overview

### Telos
Wave Rider is freedom. The endless wave, the wind, the simple joy of not falling off. It's Pixel Beach distilled into movement—no competition, just flow and the occasional spectacular wipeout.

### Ludos
Endless surfer with trick system. Balance on waves, perform tricks for points, avoid obstacles. Easy to play, satisfying to master, perfect for zone-out sessions.

---

## Core Loop

1. Automatically ride wave forward
2. Move up/down to adjust position on wave
3. Perform tricks when airborne
4. Land safely to continue
5. Avoid obstacles (jellyfish, rocks)
6. Survive as long as possible

**Session Length**: 2-8 minutes typical

---

## Controls

### Mouse (Primary)
- Move up/down → Surfer follows Y position
- Click in air → Perform trick
- Hold click → Charge spin trick

### Keyboard (Alternative)
- W/S or ↑/↓ → Move on wave
- Space → Perform trick (in air)
- Hold Space → Charge spin

---

## Mechanics

### The Wave
- Continuous wave scrolling left-to-right
- Wave height varies (creates jumps)
- Wave sections: Trough, Rise, Crest, Fall
- Speed increases over time (gradual)

### Surfing
| Position | Effect |
|----------|--------|
| Trough | Safe, slow, no tricks |
| Rise | Building speed |
| Crest | Launch point for air |
| Fall | Fast, risky |

### Jumping
- Hitting wave crest = automatic launch
- Height based on approach speed
- Air time = trick opportunity
- Must land on wave (not in trough) = safe landing

### Trick System
| Trick | Input | Points | Difficulty |
|-------|-------|--------|------------|
| Air Grab | Click once | 50 | Easy |
| Spin 180 | Hold briefly | 100 | Medium |
| Spin 360 | Hold longer | 200 | Hard |
| Flip | Double click | 150 | Medium |
| Super Spin | Hold max + click | 500 | Expert |

### Combos
- Chain tricks in one air: multiplier increases
- Land perfectly: bonus points
- Bail (miss landing): lose streak, respawn

### Obstacles
| Type | Behavior | Consequence |
|------|----------|-------------|
| Jellyfish | Floats at surface | Wipeout |
| Rock | Static in water | Wipeout |
| Seagull | Flies across | Lose points |
| Wave Gap | Missing wave section | Fall through = wipeout |

---

## Progression

### Speed Scaling
| Distance | Speed | Obstacles |
|----------|-------|-----------|
| 0-500m | 1.0x | Sparse |
| 500-1500m | 1.2x | Moderate |
| 1500-3000m | 1.4x | Dense |
| 3000m+ | 1.6x | Intense |

### Wave Patterns
- Simple: Regular crests, easy rhythm
- Rolling: Multiple peaks
- Choppy: Irregular, surprising
- Big Wave: Rare massive wave (high risk/reward)

### Milestones
| Distance | Event |
|----------|-------|
| 500m | "Getting the hang of it!" |
| 1000m | Scenery changes |
| 2500m | Big Wave incoming |
| 5000m | Achievement + Bonus |
| 10000m | Legendary status |

---

## Scoring

### Points
- Distance: 1 pt per meter
- Tricks: 50-500 per trick
- Combo: ×multiplier for chained tricks
- Perfect landing: +50% trick score
- Near miss (obstacle): +25 pts

### Multiplier
- Base: 1x
- Per trick in chain: +0.5x
- Max: 5x
- Wipeout: Reset to 1x

### Token Conversion
```
tokens = 20 + floor(distance / 100) + floor(trick_score / 50)
```
Cap: 50 tokens per session (casual cap)

---

## Visual Style

### Aesthetic
- Side-view pixel art
- Chunky 8-bit waves
- Bright turquoise water
- Pixel particle spray

### The Surfer
- Small character on board
- Pose changes by position
- Trick animations
- Wipeout animation (ragdoll)

### Environment
- Scrolling background islands
- Dynamic wave surface
- Sun reflecting on water
- Occasional pixel fish jumping

### Feedback
| Event | Visual |
|-------|--------|
| Good position | Subtle trail |
| Air | Character glows |
| Trick success | Sparkle burst |
| Perfect land | Wave rainbow |
| Wipeout | Splash + stars |

---

## Audio

### Music
- Upbeat lo-fi beach tune
- Tempo matches wave speed
- Chill but energetic

### Sound Effects
| Event | Sound |
|-------|-------|
| Wave riding | Constant water sound |
| Launch | Whoosh up |
| Air | Wind sound |
| Trick | Satisfying swoosh |
| Land | Splash down |
| Perfect land | Chime |
| Near miss | Quick whoosh |
| Wipeout | Splash + comedy sound |
| Milestone | Celebration jingle |

---

## Asset List

### Sprites
| Asset | Description | Variants |
|-------|-------------|----------|
| wr_surfer | Surfer character | 8 poses |
| wr_board | Surfboard | 1 |
| wr_wave | Wave tile segments | Rise/crest/fall/trough |
| wr_jellyfish | Jellyfish obstacle | Animation (bob) |
| wr_rock | Rock obstacle | 3 variants |
| wr_seagull | Seagull | Flight animation |
| wr_fish | Background fish | Jump animation |

### Environment
| Asset | Description | Notes |
|-------|-------------|-------|
| wr_bg_sky | Sky background | Parallax |
| wr_bg_islands | Distance islands | Parallax |
| wr_bg_water | Deep water | Below wave |

### Effects
| Asset | Description | Type |
|-------|-------------|------|
| fx_spray | Water spray | Particle |
| fx_trick_sparkle | Trick success | Particle burst |
| fx_wipeout_splash | Wipeout | Large particle |
| fx_rainbow | Perfect land | Sprite overlay |

### UI
| Asset | Description | Notes |
|-------|-------------|-------|
| wr_ui_distance | Distance counter | Top |
| wr_ui_score | Score display | Top |
| wr_ui_combo | Combo multiplier | Center-top |
| wr_ui_trick | Current trick | Center (brief) |

---

## Implementation Notes

### Wave Generation
```typescript
interface WaveSegment {
  type: 'trough' | 'rise' | 'crest' | 'fall';
  length: number;
  height: number;
}

function generateWave(difficulty: number): WaveSegment[] {
  // Procedural wave generation
  // Higher difficulty = more irregular
}
```

### Physics
- Gravity applies in air
- Wave surface collision
- Landing angle matters for success

### State Machine
```
states: title → surfing → airborne → landing → wiped_out → game_over
```

### Save Data
```typescript
interface WaveRiderSave {
  high_score: number;
  max_distance: number;
  max_combo: number;
  best_trick_score: number;
  total_wipeouts: number;
}
```
