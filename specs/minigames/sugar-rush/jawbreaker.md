# Minigame Spec: Jawbreaker

## Overview

### Telos
Jawbreaker is destruction made delicious—smashing candy structures with bouncing gumballs. It's Breakout wearing a candy costume, pure arcade satisfaction with Sugar Rush flair.

### Ludos
Brick breaker with candy theming. Break candy structures with bouncing gumballs, collect power-ups, clear levels. Simple, addictive, endlessly satisfying.

---

## Core Loop

1. Launch gumball from paddle
2. Gumball bounces, breaks candy
3. Catch gumball with paddle
4. Clear all breakable candy
5. Advance to next level
6. Don't lose all gumballs

**Session Length**: 5-15 minutes typical

---

## Controls

### Mouse
- Move → Paddle follows
- Click → Launch gumball

### Keyboard
- A/D → Move paddle
- Space → Launch

---

## Mechanics

### Paddle
- Width: 80px (default)
- Can be widened/narrowed by power-ups
- Position: Bottom of play area

### Gumball
- Standard bounce physics
- Angle affected by paddle hit location
- Speed increases slightly over time

### Candy Types
| Candy | Hits | Points | Visual |
|-------|------|--------|--------|
| Gumdrop | 1 | 10 | Colored dome |
| Hard Candy | 2 | 25 | Wrapped |
| Chocolate | 1 | 15 | Brown block |
| Candy Cane | 3 | 40 | Striped |
| Jawbreaker | 5 | 100 | Rainbow sphere |
| Explosive | 1 | 50 | Fizzy candy (explodes) |

### Power-Ups
| Power-Up | Effect | Duration |
|----------|--------|----------|
| Wide Paddle | +50% width | 20s |
| Multi-Gum | 3 gumballs | Until lost |
| Sticky | Gumball sticks | 15s |
| Fire Gum | Burns through | 10s |
| Slow Motion | Slower ball | 15s |
| Extra Life | +1 life | Permanent |

### Scoring
- Break candy: Points per type
- Combo: +10% per uninterrupted hit
- Level clear: 500 + (100 × level)
- Time bonus: Remaining time × 10

### Lives
- Start with 3 gumballs
- Lose one when ball falls
- Zero = game over

### Token Conversion
```
tokens = 15 + floor(score / 100)
```
Cap: 75 tokens per session

---

## Visual Style

- Sugar Rush candy aesthetic
- Colorful candy blocks
- Bouncy, juicy feedback
- Sweet particle explosions

---

## Level Design

### Progression
- Levels 1-10: Basic patterns
- Levels 11-20: + Hard candies
- Levels 21-30: + Candy canes
- Levels 31-40: + Jawbreakers
- Levels 41+: All types, complex patterns

### Level Themes
- Layer Cake (rows)
- Candy Castle (structure)
- Gumball Machine (circles)
- Chocolate Bar (grid)
- Party Piñata (shaped)

---

## Asset List

### Sprites
| Asset | Description |
|-------|-------------|
| jb_paddle | Candy paddle |
| jb_gumball | Bouncing ball |
| jb_candy_* | All candy types |
| jb_powerup_* | Power-up items |

### Effects
| Asset | Description |
|-------|-------------|
| fx_candy_break | Break particles |
| fx_explosion | Explosive candy |
| fx_fire_trail | Fire gum effect |
| fx_multi_split | Multi-gum spawn |

### UI
| Asset | Description |
|-------|-------------|
| jb_ui_score | Score display |
| jb_ui_lives | Life counter |
| jb_ui_level | Level indicator |
| jb_ui_powerup | Active power-up |

---

## Implementation Notes

### Physics
- Standard breakout physics
- Ball speed: 300-500 px/s
- Paddle hit angle calculation
- Wall bounces

### State Machine
```
states: ready → playing → ball_lost → level_clear → game_over
```

### Level Data
```typescript
interface Level {
  layout: CandyType[][]; // Grid
  background: string;
  music_variant?: string;
}
```
