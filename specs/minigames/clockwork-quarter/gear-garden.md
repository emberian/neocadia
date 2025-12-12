# Minigame Spec: Gear Garden

## Overview

### Telos
Gear Garden is pure puzzle satisfaction—the joy of things fitting together, the click of gears meshing, the hum of a machine coming to life. Professor Cog built it to teach mechanical thinking, but it became art.

### Ludos
Connection puzzle: place gears to transfer rotation from source to target. Physics-based, increasingly complex, deeply satisfying when solved.

---

## Core Loop

1. See power source (spinning gear)
2. See target (needs to spin)
3. Place gears from inventory
4. Gears must mesh correctly
5. Power transfers through chain
6. Target spins = success

**Session Length**: 5-20 minutes typical

---

## Controls

### Mouse
- Click gear in inventory → Select
- Click on board → Place gear
- Right-click/drag → Rotate gear
- Double-click placed gear → Remove

---

## Mechanics

### Gear Types
| Gear | Teeth | Size | Special |
|------|-------|------|---------|
| Small | 8 | 1 unit | Fast spin |
| Medium | 16 | 2 units | Standard |
| Large | 24 | 3 units | Slow spin |
| Corner | Variable | 2 units | 90° redirect |
| Split | Variable | 2 units | Powers 2 outputs |
| Locked | Any | Any | Can't be moved |

### Physics Rules
- Adjacent gears spin opposite directions
- Size determines speed (smaller = faster)
- Power diminishes over long chains
- Target needs minimum power to activate

### Puzzle Elements
| Element | Function |
|---------|----------|
| Source | Provides power (spinning) |
| Target | Needs power (goal) |
| Obstacle | Blocks placement |
| Pipe | Pre-placed gear |
| Boost | Adds power to chain |
| Brake | Slows power (obstacle) |

### Scoring
- Solve: 500 points
- Efficiency bonus: +points for fewer gears used
- Speed bonus: +points for quick solve
- Par bonus: Extra if under par gear count

### Difficulty Progression
| Level | Board Size | Gears Given | Elements |
|-------|-----------|-------------|----------|
| 1-10 | 5×5 | Exact needed | Basic |
| 11-20 | 7×7 | +2 extra | + Obstacles |
| 21-30 | 9×9 | +3 extra | + Corners |
| 31+ | 10×10 | Limited | All elements |

### Token Conversion
```
tokens = 20 + floor(level × 3) + floor(bonus / 100)
```
Cap: 80 tokens per session

---

## Visual Style

- Brass/copper gear aesthetics
- Satisfying rotation animation
- Meshing gears click together
- Power visualization (glow transfer)

---

## Asset List

### Gears
| Asset | Description |
|-------|-------------|
| gg_gear_small | 8-tooth gear |
| gg_gear_medium | 16-tooth gear |
| gg_gear_large | 24-tooth gear |
| gg_gear_corner | 90° redirect |
| gg_gear_split | Power splitter |

### UI
| Asset | Description |
|-------|-------------|
| gg_board | Puzzle board |
| gg_inventory | Gear inventory |
| gg_source | Power source indicator |
| gg_target | Target indicator |

---

## Implementation Notes

### Physics Simulation
```typescript
function simulatePower(source: Gear): void {
  // BFS from source
  // Each connected gear gets opposite direction
  // Power reduces over distance
  // Check if target receives minimum power
}
```

### Gear Meshing
- Gears mesh if adjacent and teeth align
- Visual feedback for valid/invalid placement
