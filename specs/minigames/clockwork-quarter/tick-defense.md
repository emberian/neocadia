# Minigame Spec: Tick Defense

## Overview

### Telos
Tick Defense protects the heart of the Clockwork Quarter. It's strategic thinking under pressure—building defenses, making choices, watching your plan either succeed brilliantly or teach you why it failed.

### Ludos
Tower defense with clockwork aesthetics. Place turrets along paths, upgrade them, defeat waves of invading Static. Resource management meets tactical placement.

---

## Core Loop

1. Wave announced (enemy types)
2. Placement phase (build/upgrade turrets)
3. Wave begins (enemies march)
4. Turrets attack automatically
5. Survive the wave
6. Earn resources, repeat

**Session Length**: 10-30 minutes typical

---

## Controls

### Mouse
- Click turret in menu → Select
- Click valid space → Place turret
- Click placed turret → Upgrade/sell
- Click "Start Wave" → Begin wave

---

## Mechanics

### Turrets
| Turret | Cost | Damage | Speed | Range | Special |
|--------|------|--------|-------|-------|---------|
| Gear Gun | 50 | 10 | Fast | Short | Basic |
| Steam Cannon | 100 | 30 | Medium | Medium | Splash |
| Tesla Coil | 150 | 15 | Fast | Medium | Chain lightning |
| Frost Pipe | 125 | 5 | Fast | Short | Slows enemies |
| Clockwork Knight | 200 | 50 | Slow | Melee | Blocks path |
| Temporal Tower | 300 | 0 | - | Medium | Stops time briefly |

### Upgrades (Per Turret)
- Level 1 → 2: 50% cost, +50% damage
- Level 2 → 3: 100% cost, +50% damage, +range
- Max level 3

### Enemies
| Enemy | HP | Speed | Reward | Special |
|-------|-----|-------|--------|---------|
| Static Sprite | 30 | Fast | 5 | None |
| Glitch Golem | 100 | Slow | 15 | High HP |
| Phaser | 50 | Medium | 10 | Teleports |
| Swarm | 10 each | Fast | 2 each | Groups of 5 |
| Boss (wave 10+) | 500+ | Slow | 100+ | Abilities |

### Wave Structure
| Wave | Enemies | Resources |
|------|---------|-----------|
| 1-5 | Sprites only | 100-200 |
| 6-10 | + Golems | 150-300 |
| 11-15 | + Phasers | 200-400 |
| 16-20 | + Swarms | 250-500 |
| 21+ | Boss waves | 500+ |

### Scoring
- Enemy killed: Value × wave multiplier
- Wave complete: 500 + (100 × wave)
- No leaks bonus: +25%
- Lives remaining: Points per life

### Lives
- Start with 20 lives
- Enemy reaching end: -1 to -5 lives
- Zero lives: Game over

### Token Conversion
```
tokens = 20 + floor(waves_cleared × 2.5) + floor(perfect_waves × 2)
```
Where `perfect_waves` = waves with no enemies reaching the end

**Scaling**:
- Waves 1-10: Full value (2.5 per wave)
- Waves 11-20: 75% value (1.875 per wave)
- Waves 21+: 50% value (1.25 per wave)

**Example Sessions**:
- Clear 10 waves (no perfects): 20 + 25 = 45 tokens
- Clear 10 waves (all perfect): 20 + 25 + 20 = 65 tokens
- Clear 20 waves (all perfect): 20 + 43 + 40 = 103 → capped at 100 tokens
- Clear 30+ waves: Still 100 tokens (cap reached)

Cap: 100 tokens per session

**Design Rationale**: Linear scaling created an infinite grind incentive. Diminishing returns after wave 10 rewards skill (perfect clears) over pure endurance while the hard cap prevents burnout farming.

---

## Visual Style

- Clockwork Quarter brass aesthetic
- Turrets have mechanical animations
- Enemies are glitchy/static-based
- Path is conveyor/gear track

---

## Asset List

### Turrets
| Asset | Description |
|-------|-------------|
| td_turret_gear | Gear Gun (3 levels) |
| td_turret_steam | Steam Cannon (3 levels) |
| td_turret_tesla | Tesla Coil (3 levels) |
| td_turret_frost | Frost Pipe (3 levels) |
| td_turret_knight | Clockwork Knight (3 levels) |
| td_turret_temporal | Temporal Tower (3 levels) |

### Enemies
| Asset | Description |
|-------|-------------|
| td_enemy_sprite | Static Sprite |
| td_enemy_golem | Glitch Golem |
| td_enemy_phaser | Phaser |
| td_enemy_swarm | Swarm unit |
| td_enemy_boss_* | Boss variants |

### Effects
| Asset | Description |
|-------|-------------|
| fx_bullet_* | Turret projectiles |
| fx_explosion | Enemy death |
| fx_slow | Frost effect |
| fx_temporal | Time stop |

---

## Implementation Notes

### Pathfinding
- Enemies follow pre-defined path
- Clockwork Knight can block (limited)
- Phasers teleport forward on path

### State Machine
```
states: build_phase → wave_active → wave_complete → game_over
```
