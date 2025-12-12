# Minigame Spec: Synth Racer

## Overview

### Telos
Synth Racer captures the feel of arcade racing—the endless road, the setting sun, the speed—combined with rhythm game precision. It's Outrun meets Guitar Hero, the most "synthwave" game in Neocadia.

### Ludos
Race down a neon highway, hitting notes on the beat to boost your speed. Miss notes and slow down. The better your rhythm, the further you go. It's about flow state—finding the groove and riding it.

---

## Core Loop

1. Car automatically drives forward
2. Notes approach in 3 lanes
3. Hit correct key when note reaches line
4. Perfect timing = boost, Good timing = maintain, Miss = slow
5. Survive as long as possible
6. Score based on distance + accuracy

**Session Length**: 2-5 minutes typical

---

## Controls

### Keyboard (Primary)
- A / S / D → Hit notes in left / center / right lane
- Alternative: ← / ↓ / → arrow keys
- Hold keys for sustained notes

### Mouse (Alternative)
- Click three zones at bottom of screen
- Less precise but accessible

### Touch (Future)
- Tap three zones

---

## Mechanics

### The Road
- Pseudo-3D perspective (Mode 7 style)
- Three lanes with note receptors at bottom
- Endless procedural generation
- Scenery: neon palm trees, buildings, mountains

### Notes
| Type | Input | Points | Visual |
|------|-------|--------|--------|
| Single | Tap | 100 | Neon circle |
| Sustained | Hold | 50/beat | Neon bar |
| Chord | Multiple lanes | 150 | Connected circles |

### Timing Windows
| Window | Range | Score | Effect |
|--------|-------|-------|--------|
| Perfect | ±30ms | 100% | Speed boost |
| Great | ±60ms | 75% | Maintain speed |
| Good | ±100ms | 50% | Slight slow |
| Miss | >100ms | 0% | Speed penalty |

### Speed System
- Base speed: 100 km/h (visual)
- Perfect hits: +5 km/h (stacks)
- Max speed: 300 km/h
- Miss: -20 km/h
- Below 50 km/h: Game over

### Combo System
- Combo counter for consecutive Perfect/Great hits
- Combo multiplier: 1x → 2x → 3x → 4x (at 10/25/50 combo)
- Miss resets combo to 0

---

## Progression

### Difficulty Modes
| Mode | Note Density | BPM Range | Note Types |
|------|--------------|-----------|------------|
| Easy | Low | 100-120 | Singles only |
| Normal | Medium | 120-140 | Singles, Sustained |
| Hard | High | 140-160 | All types |
| Expert | Extreme | 160-180 | All + patterns |

### Song/Segment Structure
Game is procedurally generated but follows patterns:
- Intro: 30 seconds, simple patterns
- Build: Note density increases
- Drop: High density, fast patterns
- Breakdown: Sustained notes, recovery
- Climax: Maximum intensity
- Cycle repeats with escalation

### Milestone Bonuses
| Distance | Bonus | Event |
|----------|-------|-------|
| 1 km | 500 pts | Scenery change (city) |
| 5 km | 1000 pts | Night falls |
| 10 km | 2000 pts | Neon storm begins |
| 25 km | 5000 pts | Approaching horizon |
| 50 km | 10000 pts | Achievement unlock |

---

## Scoring

### Base Points
- Perfect: 100 × combo multiplier
- Great: 75 × combo multiplier
- Good: 50 × combo multiplier
- Sustained: 50 per beat held × multiplier

### Bonus Points
- Distance: 100 pts per km
- Max combo bonus: combo count × 10
- Speed bonus: Distance traveled at 250+ km/h × 2

### Token Conversion
```
tokens = 15 + floor(distance / 2) + floor(max_combo / 10)
```
Cap: 100 tokens per session

---

## Visual Style

### Aesthetic
- Peak synthwave: sunset gradient, neon grids, chrome
- Horizon line with setting sun (orange/pink/purple gradient)
- Road: Black with cyan lane dividers
- Note receptors: Three neon circles at bottom

### The Car
- Stylized sports car silhouette
- Color matches current speed (cyan → pink → white)
- Motion blur at high speed
- Trail effects

### Environment
- Neon palm trees (pink)
- Distant city skyline (cyan)
- Grid pattern on ground
- Stars appear as speed increases

### Notes
- Circles with outer glow
- Color by lane: Pink / White / Cyan
- Pulsing to the beat
- Shatter effect on hit

### Feedback
| Event | Visual |
|-------|--------|
| Perfect | Note explodes, rainbow streak |
| Great | Note shatters, small particles |
| Good | Note fades, minimal effect |
| Miss | Note falls through, screen flash red |

---

## Audio

### Music
- Original synthwave track (or multiple tracks)
- Notes correspond to actual musical elements
- Hit sounds blend with music
- Miss creates brief dissonance

### Sound Effects
| Event | Sound |
|-------|-------|
| Perfect hit | Satisfying synth note (in key) |
| Great hit | Softer synth |
| Good hit | Muted tone |
| Miss | Discordant buzz |
| Speed boost | Whoosh + arpeggio up |
| Speed loss | Engine stutter |
| Combo milestone | Fanfare burst |
| Game over | Music winds down |

### Dynamic Music
- Base track always playing
- Intensity layers added with combo
- Filter sweep during speed changes
- Beat drop on milestone distances

---

## Asset List

### Sprites
| Asset | Description | Variants |
|-------|-------------|----------|
| sr_car | Player vehicle | 1 (color shifts) |
| sr_note_single | Single hit note | 3 (by lane color) |
| sr_note_sustained | Hold note | 3 + end cap |
| sr_note_chord | Multi-lane connector | 1 |
| sr_receptor | Lane receptors | 3 |

### Environment
| Asset | Description | Notes |
|-------|-------------|-------|
| sr_bg_sky | Gradient sky | Procedural or sprite |
| sr_bg_sun | Setting sun | Animated glow |
| sr_road | Road surface | Scrolling |
| sr_lane_dividers | Lane markings | Scrolling |
| sr_palm_* | Palm tree variants | 3 types |
| sr_building_* | Skyline buildings | 5 types |

### Effects
| Asset | Description | Type |
|-------|-------------|------|
| fx_note_perfect | Perfect hit explosion | Particle burst |
| fx_note_hit | Standard hit | Particle |
| fx_note_miss | Miss indicator | Flash + fade |
| fx_speed_lines | Motion blur | Screen effect |
| fx_combo_fire | High combo visual | Particle trail |

### UI
| Asset | Description | Notes |
|-------|-------------|-------|
| sr_ui_speed | Speedometer | Visual gauge |
| sr_ui_combo | Combo counter | Large, flashy |
| sr_ui_distance | Distance traveled | Top center |
| sr_ui_multiplier | Score multiplier | Near combo |

---

## Implementation Notes

### Rhythm System
- Audio timestamp tracking essential
- Pre-load note positions from "song" data
- Hit detection based on audio time, not visual
- Visual sync to audio (compensate for latency)

### Procedural Generation
```typescript
interface SongSegment {
  bpm: number;
  duration: number;
  pattern_type: 'intro' | 'build' | 'drop' | 'breakdown' | 'climax';
  note_density: number;
}

function generateSong(difficulty: Difficulty): SongSegment[] {
  // Generate sequence of segments
  // Each segment has appropriate note patterns
}
```

### State Machine
```
states: title → countdown → playing → paused → game_over
```

### Save Data
```typescript
interface SynthRacerSave {
  high_score: number;
  max_distance: number;
  max_combo: number;
  perfect_percentage_best: number;
  play_count: number;
}
```
