# Minigame Spec: Loop Garden

## Overview

### Telos
Loop Garden embodies the Glitch Garden's reality-bending nature. The maze doesn't play fair—paths loop, rules change, up becomes down. It's disorienting in the best way, teaching players that sometimes you have to think differently.

### Ludos
Maze navigation where the rules keep changing. Each screen might wrap differently, gravity might shift, doors might lead back to start. Figure out the pattern, escape the garden.

---

## Core Loop

1. Enter maze screen
2. Navigate toward exit
3. Rules change as you progress
4. Some paths loop back
5. Find the true exit
6. Advance to more complex mazes

**Session Length**: 5-20 minutes typical

---

## Controls

### Keyboard (Primary)
- WASD or Arrows → Move
- Space → Interact with objects

### Mouse (Alternative)
- Click → Move toward click point
- Click objects → Interact

---

## Mechanics

### Rule Modifiers
| Modifier | Effect | Indicator |
|----------|--------|-----------|
| Screen Wrap | Walking off wraps to other side | Edge glow |
| Gravity Shift | Controls rotate 90° | Arrow overlay |
| Mirror | Movements reversed | Reflection effect |
| Loop Point | Certain paths return you | Subtle shimmer |
| Invisible Walls | Blocked paths not visible | None (discovery) |
| Phasing | Walk through certain walls | Walls flicker |

### Level Structure
- Each level: 3-7 connected screens
- One true exit, multiple loops
- Hints hidden in environment
- Wrong paths teach patterns

### Scoring
- Base: 500 points per level
- Speed bonus: Up to 500 additional
- Mistakes: -50 per wrong path taken
- Hints: -100 per hint used

### Difficulty Progression
| Level | Screens | Modifiers | Complexity |
|-------|---------|-----------|------------|
| 1-3 | 3 | 1 | Tutorial |
| 4-7 | 4-5 | 2 | Standard |
| 8-12 | 5-6 | 3 | Complex |
| 13+ | 7 | 4 | Expert |

### Token Conversion
```
tokens = 25 + floor(level × 10) + floor(bonus / 100)
```
Cap: 75 tokens per session

---

## Visual Style

- Glitch Garden pathways
- Impossible geometry suggestions
- Each modifier has visual tell
- Found paths light up

---

## Asset List

### Environment
| Asset | Description |
|-------|-------------|
| lg_tile_path | Walkable path tile |
| lg_tile_wall | Wall/blocked tile |
| lg_tile_exit | Exit indicator |
| lg_indicator_* | Modifier indicators (6) |

### Effects
| Asset | Description |
|-------|-------------|
| fx_screen_wrap | Edge transition |
| fx_gravity_shift | Direction change |
| fx_mirror_flip | Reversal indicator |

---

## Implementation Notes

### Level Design
- Levels pre-designed (not procedural)
- Each screen has connection data
- Loop logic: some exits return to previous

### State Machine
```
states: intro → navigating → transitioning → level_complete → game_over
```
