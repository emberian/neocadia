# Minigame Spec: Pixel Invaders

## Overview

### Telos
Pixel Invaders honors the granddaddy of arcade games while bringing modern depth. It's the game NEON remembers from the very beginning—the one that proved games could be art, competition, and joy all at once.

### Ludos
Fixed-position shooter with modern bullet-hell elements. Shoot waves of enemies, dodge patterns, defeat bosses. Simple controls, deep mastery, high score glory.

---

## Core Loop

1. Ship at bottom, can move left/right
2. Enemies descend in formations
3. Shoot enemies before they reach bottom
4. Dodge enemy projectiles
5. Collect power-ups
6. Survive waves, defeat bosses

**Session Length**: 5-15 minutes typical

---

## Controls

### Keyboard (Primary)
- A/D or ←/→ → Move ship
- Space → Shoot (auto-fire available)
- Shift → Focus mode (slow, precise movement)

### Mouse (Alternative)
- Mouse horizontal position → Ship follows
- Left click → Shoot
- Right click → Focus mode

### Touch (Future)
- Drag → Ship follows
- Auto-shoot enabled

---

## Mechanics

### The Ship
- Width: 32px
- Speed (normal): 300px/s
- Speed (focus): 120px/s
- Hitbox: 8px circle (center, visible in focus mode)

### Weapons
| Level | Type | Fire Rate | Damage | Visual |
|-------|------|-----------|--------|--------|
| 1 | Single shot | 5/s | 10 | Small pink bolt |
| 2 | Double shot | 5/s | 10×2 | Twin pink bolts |
| 3 | Triple spread | 5/s | 8×3 | Triangle pattern |
| 4 | Wide spread | 6/s | 8×5 | Fan pattern |
| 5 | Beam + spread | Continuous + 4/s | 5/tick + 8×3 | Central beam |

### Enemies
| Type | HP | Points | Behavior | Shots |
|------|-----|--------|----------|-------|
| Grunt | 10 | 50 | March down | 1 straight |
| Swooper | 15 | 75 | Sine wave descent | None |
| Shooter | 20 | 100 | Stationary, aims | 3-way spread |
| Tank | 50 | 200 | Slow, center | Bullet ring |
| Elite | 30 | 150 | Erratic, fast | Aimed shots |

### Boss Enemies
| Boss | HP | Points | Wave | Patterns |
|------|-----|--------|------|----------|
| Command Ship | 500 | 2000 | 5 | Sweeping laser, grunt spawn |
| Void Core | 1000 | 5000 | 10 | Bullet spirals, shield phases |
| Static Queen | 2000 | 10000 | 15 | All patterns, corruption zones |

### Power-Ups
| Type | Effect | Duration | Drop Rate |
|------|--------|----------|-----------|
| Weapon Up | +1 weapon level | Permanent (until death) | 10% |
| Shield | Absorbs 3 hits | Until depleted | 5% |
| Bomb | Screen clear | Instant | 3% |
| Score | +1000 points | Instant | 15% |
| Speed | +20% ship speed | 20 seconds | 8% |

---

## Progression

### Wave Structure
- Waves 1-5: Tutorial, basic enemies
- Waves 6-10: Mixed formations
- Waves 11-15: Bullet hell introduction
- Waves 16-20: Full intensity
- Endless mode after Wave 20

### Formation Types
| Type | Layout | Behavior |
|------|--------|----------|
| Classic | Grid rows | March left-right-down |
| V-Formation | Arrow shape | Dive attack |
| Circle | Ring pattern | Spiral inward |
| Random | Scattered | Unpredictable entry |
| Boss | Single large | Pattern-based |

### Difficulty Scaling
| Wave | Enemy HP | Bullet Speed | Spawn Rate |
|------|----------|--------------|------------|
| 1-5 | ×1.0 | ×1.0 | ×1.0 |
| 6-10 | ×1.2 | ×1.2 | ×1.1 |
| 11-15 | ×1.5 | ×1.4 | ×1.2 |
| 16-20 | ×2.0 | ×1.6 | ×1.3 |
| 21+ | ×2.5 | ×1.8 | ×1.5 |

---

## Scoring

### Base Points
- Grunt: 50
- Swooper: 75
- Shooter: 100
- Tank: 200
- Elite: 150
- Bosses: 2000/5000/10000

### Multipliers
- Chain kills (kills within 0.5s): +10% cumulative
- No-damage wave clear: ×2 wave score
- Boss no-hit: ×3 boss score
- Graze (near miss): +10 pts per bullet

### Wave Completion
- Base: 500 pts per wave
- Time bonus: Up to 300 pts (faster = more)
- Lives remaining: 100 pts per life

### Token Conversion
```
tokens = 15 + floor(score / 500) + floor(wave / 2)
```
Cap: 100 tokens per session

---

## Visual Style

### Aesthetic
- Classic arcade meets modern neon
- Black background with star field
- Purple/pink dominant palette
- CRT scanline filter (optional)

### Player Ship
- Neon purple chassis
- Engine glow (pink)
- Banking animation on movement
- Focus mode: visible hitbox glow

### Enemies
- Geometric neon designs
- Each type distinct silhouette
- Damage states (flicker, color shift)
- Death explosions (type-specific)

### Bullets
- Player: Pink/magenta bolts
- Enemy: Cyan/white projectiles
- Boss: Gold/orange special attacks
- All with glow effects

### Environment
- Scrolling star field
- Occasional neon grid lines
- Zone elements visible at edges
- Screen shake on boss attacks

---

## Audio

### Music
- Intense synthwave/chiptune hybrid
- Building intensity with wave progression
- Boss themes (unique per boss)
- Victory fanfare on boss defeat

### Sound Effects
| Event | Sound |
|-------|-------|
| Player shoot | Pew pew (8-bit style) |
| Enemy hit | Impact thud |
| Enemy destroy | Explosion (varies by type) |
| Player hit | Shield break or damage buzz |
| Power-up collect | Rising arpeggio |
| Bomb activate | Deep boom + sweep |
| Boss appear | Dramatic sting |
| Wave clear | Fanfare |
| Game over | Descending tones |

---

## Asset List

### Player
| Asset | Description | Variants |
|-------|-------------|----------|
| pi_ship | Player ship | Base + 2 bank angles |
| pi_ship_hitbox | Focus mode hitbox | Glow effect |
| pi_shot_* | Player projectiles | 5 weapon levels |
| pi_shield | Shield overlay | 3 damage states |

### Enemies
| Asset | Description | Variants |
|-------|-------------|----------|
| pi_grunt | Basic enemy | 1 + destroyed |
| pi_swooper | Sine wave enemy | 1 + destroyed |
| pi_shooter | Aiming enemy | 1 + destroyed |
| pi_tank | Heavy enemy | 2 damage states + destroyed |
| pi_elite | Fast enemy | 1 + destroyed |
| pi_boss_1 | Command Ship | Multiple segments |
| pi_boss_2 | Void Core | Phase variants |
| pi_boss_3 | Static Queen | Corruption states |

### Projectiles
| Asset | Description | Notes |
|-------|-------------|-------|
| pi_bullet_enemy | Enemy shots | Multiple colors |
| pi_bullet_boss | Boss special shots | Larger, glowing |
| pi_laser | Boss laser beam | Animated |

### Effects
| Asset | Description | Type |
|-------|-------------|------|
| fx_explosion_small | Small enemy death | Particle |
| fx_explosion_large | Boss/tank death | Particle |
| fx_graze | Near miss indicator | Brief flash |
| fx_bomb | Screen clear | Full screen |
| fx_power_collect | Power-up get | Particle burst |

### UI
| Asset | Description | Notes |
|-------|-------------|-------|
| pi_ui_score | Score display | Top left |
| pi_ui_lives | Life indicators | Top right |
| pi_ui_wave | Wave counter | Top center |
| pi_ui_weapon | Weapon level | Bottom |
| pi_ui_boss_health | Boss HP bar | Top (during boss) |

---

## Implementation Notes

### Bullet System
- Object pooling for projectiles (100+ on screen)
- Collision: Circle-based for all
- Separate player vs enemy bullet layers
- Graze detection: slightly larger collision check

### Pattern System
For bullet-hell patterns:
```typescript
interface BulletPattern {
  type: 'spread' | 'spiral' | 'aimed' | 'random';
  count: number;
  speed: number;
  angle_start: number;
  angle_spread: number;
  delay_between: number;
}
```

### State Machine
```
states: title → wave_start → playing → wave_end → boss → game_over
```

### Save Data
```typescript
interface PixelInvadersSave {
  high_score: number;
  max_wave: number;
  bosses_defeated: number[];
  total_kills: number;
  play_count: number;
}
```
