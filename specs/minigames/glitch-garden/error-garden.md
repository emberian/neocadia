# Minigame Spec: Error Garden

## Overview

### Telos
Error Garden asks: what if bugs were features? It's an idle game where you cultivate glitches, harvest corruption, and somehow create beauty. It's the chill game of the Glitch Garden—low pressure, weirdly satisfying.

### Ludos
Idle/clicker with glitch theming. Plant corrupted seeds, wait for them to grow into impossible flora, harvest for resources. Check in periodically, optimize your garden, watch the chaos bloom.

---

## Core Loop

1. Plant glitch seeds in plots
2. Seeds grow over real time
3. Harvest mature glitches
4. Use resources to unlock more plots/seeds
5. Discover rare glitch combinations
6. Garden grows while you're away

**Session Length**: 2-5 minutes per check-in

---

## Controls

### Mouse
- Click plot → Plant/Harvest
- Click seed menu → Select seed
- Drag → Water (speeds growth)

---

## Mechanics

### Seed Types
| Seed | Grow Time | Yield | Unlock |
|------|-----------|-------|--------|
| Static Sprout | 1 min | 5 glitch | Start |
| Color Bloom | 5 min | 15 glitch | 50 glitch |
| Tile Vine | 15 min | 40 glitch | 200 glitch |
| Loop Flower | 1 hour | 150 glitch | 500 glitch |
| Void Fruit | 4 hours | 500 glitch | 2000 glitch |
| Error Blossom | 24 hours | 2000 glitch | 10000 glitch |

### Garden Plots
- Start with 4 plots
- Expand with glitch resources
- Max 16 plots
- Each plot independent

### Watering
- Click repeatedly to water
- Speeds growth by 10% per water
- Cooldown per plot
- Auto-water unlockable

### Special Events
- Random mutation: Plant becomes rare variant
- Glitch storm: All plants grow 2x for 5 min
- Corruption spread: Adjacent plants share bonus

### Resources
- Glitch (main currency)
- Spend to: Unlock seeds, expand plots, buy upgrades

### Upgrades
| Upgrade | Cost | Effect |
|---------|------|--------|
| Bigger Plot | 100 | +1 plot |
| Fast Water | 500 | Water cooldown -50% |
| Auto-Water | 2000 | Plots water themselves |
| Growth Boost | 5000 | All growth +25% |
| Rare Chance | 10000 | +10% mutation rate |

### Token Conversion
```
tokens = floor(glitch_harvested / 20)
```

**Token Limits**:
- Per-harvest cap: 75 tokens (matches Glitch Garden zone cap)
- Daily cap: 100 tokens (idle games should reward check-ins, not replace active play)
- Offline cap: Maximum 8 hours of offline growth converted to tokens (prevents "set and forget" exploits)

**Glitch-to-Token Math**:
- At 4 starting plots with Static Sprouts (5 glitch/min each): 20 glitch/min = 1 token/min
- Optimal mid-game (8 plots, mixed seeds): ~60 glitch/5min = 3 tokens/5min
- Late-game (16 plots, all Error Blossoms): 2000 × 16 / 24 hours = ~1333 glitch/hour = ~67 tokens/hour
- This makes idle play supplementary income, not the primary farm

---

## Visual Style

- Corrupted garden plots
- Each plant type unique glitch visual
- Growth stages visible
- Harvest animation (sparkle burst)

---

## Asset List

### Plants
| Asset | Description |
|-------|-------------|
| eg_plant_static | Static Sprout (4 stages) |
| eg_plant_color | Color Bloom (4 stages) |
| eg_plant_tile | Tile Vine (4 stages) |
| eg_plant_loop | Loop Flower (4 stages) |
| eg_plant_void | Void Fruit (4 stages) |
| eg_plant_error | Error Blossom (4 stages) |

### UI
| Asset | Description |
|-------|-------------|
| eg_ui_plot | Garden plot frame |
| eg_ui_seed_menu | Seed selector |
| eg_ui_resources | Resource display |

---

## Implementation Notes

### Offline Progress
- Calculate growth based on time away
- Cap offline earnings (prevent exploitation)
- Show "while you were away" summary

### Save Data
```typescript
interface ErrorGardenSave {
  plots: PlotState[];
  resources: number;
  upgrades: UpgradeId[];
  total_harvested: number;
  last_visit: timestamp;
}
```
