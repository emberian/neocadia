# Minigame Spec: Spring Loaded

## Overview

### Telos
Spring Loaded is playful physics—the joy of launching things and watching them fly, bounce, and hopefully hit their target. Professor Cog considers it "applied ballistics education." Players consider it delightfully silly.

### Ludos
Physics puzzle like Angry Birds. Launch projectiles to hit targets, using springs, levers, and clockwork contraptions. Calculate angles, consider bounces, embrace chaos.

---

## Core Loop

1. See target(s) in level
2. Aim launcher (angle/power)
3. Fire projectile
4. Watch physics play out
5. Hit targets to clear level
6. Limited shots per level

**Session Length**: 5-15 minutes typical

---

## Controls

### Mouse
- Click + drag from launcher → Set angle and power
- Release → Fire
- Scroll → Zoom in/out

### Touch
- Drag → Aim
- Release → Fire

---

## Mechanics

### Launcher
- Fixed position per level
- Angle: Full 360° (some levels restrict)
- Power: 0-100% (affects distance)
- Visual trajectory preview (first part only)

### Projectiles
| Type | Behavior | Unlock |
|------|----------|--------|
| Brass Ball | Standard bounce | Start |
| Sticky Orb | Sticks to surfaces | Level 10 |
| Split Shot | Divides into 3 | Level 20 |
| Explosive | Destroys on impact | Level 30 |
| Ghost | Passes through 1 wall | Level 40 |

### Level Elements
| Element | Function |
|---------|----------|
| Target | Must hit to complete |
| Wall | Blocks projectiles |
| Bounce Pad | Extra bouncy surface |
| Spring | Launches projectile again |
| Lever | Activates on hit |
| Gate | Opens when lever hit |
| Portal | Teleports projectile |
| Gravity Zone | Alters trajectory |

### Scoring
- Target hit: 500 points
- Shots under par: 100 × remaining
- Speed bonus: Up to 200 for quick solve
- Trick shot: Bonus for complex paths

### Star System
| Stars | Requirement |
|-------|-------------|
| 1 star | Complete level |
| 2 stars | Under par shots |
| 3 stars | Perfect (minimum shots) |

### Token Conversion
```
tokens = 20 + floor(stars × 2) + floor(bonus / 100)
```
Cap: 60 tokens per session

---

## Visual Style

- Steampunk/clockwork aesthetic
- Brass projectiles
- Industrial level designs
- Satisfying impact effects

---

## Level Design

### Tutorial (1-10)
- Single target, clear path
- Introduce basic bouncing
- No obstacles

### Standard (11-30)
- Multiple targets
- Walls and bounce pads
- Springs introduced

### Advanced (31-50)
- Levers and gates
- Portals
- Complex multi-step solutions

### Expert (51+)
- All elements combined
- Minimal shots allowed
- Creative solutions required

---

## Asset List

### Projectiles
| Asset | Description |
|-------|-------------|
| sl_ball | Brass Ball |
| sl_sticky | Sticky Orb |
| sl_split | Split Shot |
| sl_explosive | Explosive |
| sl_ghost | Ghost ball |

### Level Elements
| Asset | Description |
|-------|-------------|
| sl_launcher | Launch mechanism |
| sl_target | Target indicator |
| sl_wall | Wall tiles |
| sl_bounce | Bounce pad |
| sl_spring | Spring launcher |
| sl_lever | Lever switch |
| sl_gate | Gate (open/closed) |
| sl_portal | Portal pair |

### Effects
| Asset | Description |
|-------|-------------|
| fx_launch | Launch effect |
| fx_bounce | Bounce impact |
| fx_hit_target | Target hit |
| fx_explosion | Explosive impact |

---

## Implementation Notes

### Physics
- Box2D or similar physics engine
- Consistent gravity
- Material-based bounce coefficients

### Trajectory Preview
- Show first 1-2 seconds of path
- Dotted line for projectile

### State Machine
```
states: aiming → flying → resolved → level_complete
```
