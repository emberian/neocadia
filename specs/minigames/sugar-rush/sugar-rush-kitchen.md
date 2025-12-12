# Minigame Spec: Sugar Rush Kitchen

## Overview

### Telos
Sugar Rush Kitchen is SUCRE's dream—a place where recipes come together, where timing matters, where the end result is sweet success (or caramelized failure). It's the zone's heart in game form.

### Ludos
Cooking time-management game. Follow recipes, time your actions, don't burn anything. Frantic at high levels, satisfying when you nail the timing.

---

## Core Loop

1. Orders appear (recipes)
2. Gather ingredients
3. Process at stations (chop, mix, bake)
4. Time each step correctly
5. Serve completed dishes
6. More orders come

**Session Length**: 5-15 minutes typical

---

## Controls

### Mouse
- Click ingredient → Pick up
- Click station → Use station (with ingredient)
- Click serving area → Serve dish

### Keyboard
- 1-4 → Quick-select ingredient
- Space → Interact with current station

---

## Mechanics

### Stations
| Station | Function | Time |
|---------|----------|------|
| Prep Table | Combine ingredients | Instant |
| Chopper | Dice/slice | 3-5s |
| Mixer | Blend/whip | 5-8s |
| Oven | Bake | 10-20s |
| Fryer | Fry | 8-12s |
| Freezer | Chill | 15-25s |

### Ingredients
- Basic: Sugar, Flour, Butter, Eggs
- Flavor: Chocolate, Vanilla, Fruit
- Special: Sprinkles, Cream, Caramel

### Recipes (Examples)
| Recipe | Steps | Time Limit |
|--------|-------|------------|
| Cupcake | Mix → Bake → Frost | 45s |
| Cookie | Mix → Shape → Bake | 40s |
| Ice Cream | Mix → Freeze → Serve | 50s |
| Cake Slice | Bake → Frost → Slice | 60s |
| Candy Bar | Chop → Mix → Freeze | 55s |

### Timing
- Each station has perfect timing
- Too early: Underdone (-points)
- Perfect: Full points + bonus
- Too late: Burnt (unusable)

### Scoring
- Dish served: 100-300 (by complexity)
- Perfect timing: +50%
- Speed bonus: Remaining time × 5
- Combo: Multiple dishes quick = multiplier

### Difficulty
| Level | Orders | Complexity | Stations |
|-------|--------|------------|----------|
| 1-3 | 1 at a time | Simple | 2 |
| 4-6 | 2 at a time | Medium | 3 |
| 7-9 | 3 at a time | Complex | 4 |
| 10+ | 4 at a time | All | All |

### Token Conversion
```
tokens = 15 + floor(score / 200)
```
Cap: 50 tokens per session

---

## Visual Style

- Sugar Rush kitchen aesthetic
- Candy-colored appliances
- Bouncy animations
- Steam, sparkles, frosting effects

---

## Asset List

### Stations
| Asset | Description |
|-------|-------------|
| sk_station_prep | Prep table |
| sk_station_chop | Chopping board |
| sk_station_mixer | Stand mixer |
| sk_station_oven | Candy oven |
| sk_station_fryer | Fryer |
| sk_station_freezer | Freezer |

### Ingredients
| Asset | Description |
|-------|-------------|
| sk_ingredient_* | All ingredients |

### Dishes
| Asset | Description |
|-------|-------------|
| sk_dish_* | Completed dishes |

### UI
| Asset | Description |
|-------|-------------|
| sk_ui_orders | Order queue |
| sk_ui_timer | Station timers |
| sk_ui_recipe | Recipe hint |

---

## Implementation Notes

### Multi-Tasking
- Multiple stations can run simultaneously
- Player must track all timers
- Audio cues for nearly-done

### Recipe System
```typescript
interface Recipe {
  name: string;
  ingredients: Ingredient[];
  steps: Step[];
  time_limit: number;
  points: number;
}

interface Step {
  station: Station;
  duration: number;
  perfect_window: [number, number];
}
```
