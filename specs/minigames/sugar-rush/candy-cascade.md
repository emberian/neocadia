# Minigame Spec: Candy Cascade

## Overview

### Telos
Candy Cascade is instant gratification—the satisfying pop of matching candies, the chain reactions, the sugar rush of a massive combo. SUCRE loves it because joy should be easy sometimes.

### Ludos
Match-3 with modern polish. Swap candies to make matches of 3+, trigger cascades, complete objectives. The genre distilled to its most satisfying core.

---

## Core Loop

1. Board of candies displayed
2. Swap two adjacent candies
3. Match 3+ of same type
4. Candies disappear, new fall in
5. Cascades may trigger
6. Complete level objective

**Session Length**: 3-10 minutes typical

---

## Controls

### Mouse
- Click candy → Select
- Click adjacent → Swap
- Or: Click + drag → Swap direction

### Touch
- Tap + drag → Swap

---

## Mechanics

### Basic Candies (6 colors)
- Red (Cherry)
- Orange (Citrus)
- Yellow (Lemon)
- Green (Lime)
- Blue (Blueberry)
- Purple (Grape)

### Special Candies
| Match | Creates | Effect |
|-------|---------|--------|
| 4 in row | Striped | Clears row or column |
| 4 in square | Wrapped | Explodes 3×3 twice |
| 5 in row | Color Bomb | Clears all of one color |
| T or L shape | Wrapped | Same as square |

### Combo Effects
| Combination | Result |
|-------------|--------|
| Striped + Striped | Cross clear |
| Striped + Wrapped | 3-row clear |
| Wrapped + Wrapped | Large explosion |
| Color Bomb + Striped | All of color → Striped |
| Color Bomb + Wrapped | All of color → Wrapped |
| Color Bomb + Color Bomb | Clear entire board |

### Level Types
| Type | Objective |
|------|-----------|
| Score | Reach target score |
| Clear | Remove specific pieces |
| Collect | Gather falling items |
| Boss | Defeat candy boss |

### Scoring
- 3-match: 50 points
- 4-match: 100 points
- 5-match: 200 points
- Cascade: ×1.5 multiplier per cascade
- Special clear: 150-500 points

### Moves/Lives
- Limited moves per level
- 5 lives total
- Life lost on failed level
- Lives regenerate over time

### Token Conversion
```
tokens = 15 + floor(score / 500) + (level_stars × 5)
```
Cap: 50 tokens per session

---

## Visual Style

- Full Sugar Rush candy aesthetic
- Juicy, bouncy animations
- Particle explosions on matches
- Screen-filling combos

---

## Level Progression

### World Structure
- 100+ levels across worlds
- Each world: 20 levels
- Boss level every 10 levels
- New mechanics per world

### Star System
| Stars | Requirement |
|-------|-------------|
| 1 star | Complete level |
| 2 stars | 60% of max score |
| 3 stars | 90% of max score |

---

## Asset List

### Candies
| Asset | Description |
|-------|-------------|
| cc_candy_* | 6 basic colors |
| cc_striped_* | Striped variants |
| cc_wrapped_* | Wrapped variants |
| cc_bomb | Color Bomb |
| cc_boss_* | Boss candies |

### Effects
| Asset | Description |
|-------|-------------|
| fx_match | Match particles |
| fx_cascade | Cascade indicator |
| fx_special | Special candy effect |
| fx_combo | Big combo celebration |

### UI
| Asset | Description |
|-------|-------------|
| cc_ui_moves | Move counter |
| cc_ui_score | Score display |
| cc_ui_objective | Level goal |

---

## Implementation Notes

### Board Logic
- 8×8 or 9×9 grid typical
- Match detection after every move
- Cascade until no matches
- No valid moves = shuffle

### State Machine
```
states: idle → swapping → matching → cascading → level_end
```
