# Minigame Spec: Void Breaker

## Overview

### Telos
Void Breaker is NEON's pride—the game that drew the biggest crowds in Neocadia's golden age. It's breakout refined, the satisfaction of smashing through barriers made physical. It represents what Neon Alley is about: precision, persistence, and the joy of destruction.

### Ludos
Smash neon bricks with a glowing paddle. Simple to understand, difficult to master. The bullet-hell elements add modern challenge without overwhelming the classic formula.

---

## Core Loop

1. Launch ball from paddle
2. Ball bounces, destroying bricks
3. Catch ball with paddle
4. Collect power-ups that drop
5. Clear all bricks to advance
6. Avoid losing all balls

**Session Length**: 3-10 minutes typical

---

## Controls

### Mouse (Primary)
- Move mouse left/right → Paddle follows
- Click → Launch ball (when attached)
- No scrolling or right-click needed

### Keyboard (Alternative)
- A/D or Arrow keys → Paddle movement
- Space → Launch ball
- P → Pause

### Touch (Future)
- Drag finger → Paddle follows
- Tap → Launch ball

---

## Mechanics

### The Paddle
- Width: 80px (default), 60px-120px (with power-ups)
- Speed: Matches mouse exactly (no acceleration)
- Position: Bottom of play area, 20px margin

### The Ball
- Size: 12px diameter
- Base speed: 400px/s
- Speed increase: +5% per level
- Max speed: 800px/s
- Angle: Varies based on paddle hit position (edges = steep angle)

### Bricks
| Type | Hits | Points | Color | Special |
|------|------|--------|-------|---------|
| Standard | 1 | 10 | Pink | None |
| Reinforced | 2 | 25 | Cyan | Cracks on first hit |
| Neon | 1 | 15 | Purple | Glows, pulses |
| Power | 1 | 20 | Gold | Always drops power-up |
| Explosive | 1 | 30 | Orange | Destroys adjacent bricks |
| Static | 3 | 50 | Gray | Flickering, rare |
| Boss | 10 | 200 | Multi | End of level 5, 10, 15... |

### Power-Ups
| Power-Up | Effect | Duration | Icon |
|----------|--------|----------|------|
| Wide Paddle | +50% paddle width | 20 seconds | ↔ |
| Multi-Ball | Split into 3 balls | Until lost | ×3 |
| Laser | Click to shoot (3 shots) | Until used | ⚡ |
| Slow | Ball speed -30% | 15 seconds | 🐢 |
| Magnet | Ball sticks to paddle | 10 seconds | 🧲 |
| Pierce | Ball goes through bricks | 10 seconds | → |

### Power-Downs (Rare, late levels)
| Power-Down | Effect | Duration | Icon |
|------------|--------|----------|------|
| Narrow | -30% paddle width | 15 seconds | ↔ |
| Fast | Ball speed +30% | 15 seconds | ⚡ |
| Invert | Controls reversed | 10 seconds | ⟲ |

---

## Progression

### Level Structure
- 20 levels total
- Levels 1-5: Tutorial difficulty
- Levels 6-10: Standard difficulty
- Levels 11-15: Hard difficulty
- Levels 16-20: Expert difficulty
- Boss battles at 5, 10, 15, 20

### Level Design
Each level is a unique brick arrangement:
- Level 1: Simple rows, all standard bricks
- Level 5: Boss battle (moving target)
- Level 10: First static bricks appear
- Level 15: Complex patterns, power-downs
- Level 20: Final challenge, all brick types

### Difficulty Scaling
| Levels | Ball Speed | Power-Up Frequency | Brick Types |
|--------|------------|-------------------|-------------|
| 1-5 | 400-450 | High | Standard, Reinforced, Power |
| 6-10 | 450-550 | Medium | + Neon, Explosive |
| 11-15 | 550-650 | Medium | + Static |
| 16-20 | 650-800 | Low | + Power-downs |

---

## Scoring

### Base Points
- Standard brick: 10 pts
- Reinforced brick: 25 pts
- Neon brick: 15 pts
- Power brick: 20 pts
- Explosive brick: 30 pts
- Static brick: 50 pts

### Multipliers
- Combo: +10% per consecutive hit without paddle touch
- Speed bonus: +20% if ball at max speed
- No power-up bonus: 1.5x for clearing level without power-ups
- Perfect clear: 2x for clearing with first ball

### Level Completion
- Base: 100 pts per level
- Time bonus: Up to 50 pts (faster = more)
- Lives remaining: 25 pts per life

### Token Conversion
```
tokens = 15 + floor(score / 100)
```
Cap: 100 tokens per session

---

## Visual Style

### Aesthetic
- Full synthwave/Neon Alley integration
- Black background with grid lines
- Neon-colored everything
- Bloom effects on all lights
- Screen shake on explosions

### Paddle
- Neon pink glow
- Motion blur when moving fast
- Flash on ball contact

### Ball
- Cyan core with pink trail
- Trail length increases with speed
- Explosion particle on brick hit

### Bricks
- Each type has distinct neon style
- Destruction animation (shatter + particles)
- Power bricks pulse before breaking

### UI Elements
- Score: Top left, cyan
- Lives: Top right, pink hearts
- Level: Top center
- Power-up indicator: Below paddle

---

## Audio

### Music
- Zone track continues (Neon Alley synthwave)
- Tempo increases with ball speed
- Drum fill on level clear

### Sound Effects
| Event | Sound |
|-------|-------|
| Ball launch | Synth whoosh |
| Paddle hit | Punchy click |
| Brick break | Satisfying shatter |
| Power-up collect | Rising chime |
| Power-down collect | Descending buzz |
| Multi-ball split | Triple arpeggio |
| Level clear | Fanfare burst |
| Ball lost | Descending tone |
| Game over | Dramatic synth drop |

---

## Asset List

### Sprites
| Asset | Description | Variants |
|-------|-------------|----------|
| vb_paddle | Player paddle | 3 sizes |
| vb_ball | Game ball | 1 (with trail effect) |
| vb_brick_standard | Pink brick | 1 |
| vb_brick_reinforced | Cyan brick | 2 (intact/cracked) |
| vb_brick_neon | Purple pulsing brick | Animation (4 frames) |
| vb_brick_power | Gold brick | Animation (pulse) |
| vb_brick_explosive | Orange brick | 1 |
| vb_brick_static | Gray flickering brick | Animation (flicker) |
| vb_brick_boss | Boss target | Multi-frame |
| vb_powerup_* | Power-up icons | 6 types |
| vb_powerdown_* | Power-down icons | 3 types |

### Effects
| Asset | Description | Type |
|-------|-------------|------|
| fx_brick_shatter | Brick destruction | Particle system |
| fx_ball_trail | Ball motion trail | Trail renderer |
| fx_paddle_hit | Contact flash | Sprite animation |
| fx_explosion | Explosive brick | Particle + screen shake |
| fx_powerup_collect | Collection effect | Particle burst |

### UI
| Asset | Description | Notes |
|-------|-------------|-------|
| vb_ui_score | Score display | Neon font |
| vb_ui_lives | Life hearts | Pink neon |
| vb_ui_level | Level indicator | Centered |
| vb_ui_powerup | Active power-up | Timer bar |

---

## Implementation Notes

### Physics
- Ball uses simple reflection physics
- Paddle hit angle based on contact point
- Brick collision: destroy on contact, reflect ball
- Multiple ball support (multi-ball power-up)

### State Machine
```
states: title → playing → paused → level_clear → game_over
```

### Save Data
```typescript
interface VoidBreakerSave {
  high_score: number;
  highest_level: number;
  total_bricks_broken: number;
  play_count: number;
}
```

### Performance
- Limit particles on screen (pool, recycle)
- Ball trail as fixed-length sprite array
- Brick destruction batched per frame
