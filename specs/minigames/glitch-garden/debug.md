# Minigame Spec: Debug

## Overview

### Telos
Debug is about seeing what others miss—finding the glitches in a corrupted image. It's VERA's game in spirit, a meditation on imperfection and attention. What's wrong becomes beautiful when you look closely enough.

### Ludos
Spot-the-difference with a glitch aesthetic. Find visual errors in corrupted scenes before time runs out. Relaxed pace with growing complexity, rewarding the observant eye.

---

## Core Loop

1. Two images displayed side by side
2. One is "correct," one has glitches
3. Click on glitches to mark them
4. Find all glitches before time expires
5. Advance to harder scenes

**Session Length**: 5-15 minutes typical

---

## Controls

### Mouse (Primary)
- Click → Mark a glitch location
- Hover → Magnifying effect (optional)

### Touch
- Tap → Mark a glitch

---

## Mechanics

### Glitch Types
| Type | Visual | Difficulty |
|------|--------|------------|
| Color Shift | Wrong hue on object | Easy |
| Missing Element | Object removed | Easy |
| Duplicate | Object copied | Medium |
| Position Shift | Object moved | Medium |
| Tiling | Section repeats | Medium |
| Inversion | Colors inverted | Hard |
| Transparency | Semi-visible | Hard |
| Micro-Glitch | Single pixel change | Expert |

### Scoring
- Correct click: +100 points
- Wrong click: -25 points, -5 seconds
- Speed bonus: Points × (time_remaining / total_time)
- Hints available: -50 points per use

### Difficulty Progression
| Level | Glitches | Time | Types |
|-------|----------|------|-------|
| 1-5 | 3 | 60s | Easy only |
| 6-10 | 5 | 90s | Easy + Medium |
| 11-15 | 7 | 120s | All except Micro |
| 16+ | 10 | 150s | All types |

### Token Conversion
```
tokens = 25 + floor(score / 150)
```
Cap: 75 tokens per session

---

## Visual Style

- Glitch Garden aesthetic throughout
- Images are scenes from Neocadia
- Corrupted versions use glitch effects
- Found glitches get circled with sparkle

---

## Asset List

### Images (Scene Pairs)
- 20+ base scenes from various zones
- Each has pre-generated glitch version
- Glitch positions stored in data

### UI
| Asset | Description |
|-------|-------------|
| db_ui_timer | Time remaining |
| db_ui_found | Glitches found counter |
| db_ui_hint | Hint button |
| db_marker | Found glitch circle |

---

## Implementation Notes

### Glitch Generation
- Scenes pre-authored or procedurally modified
- Glitch positions stored as coordinates
- Hit detection radius around each glitch

### State Machine
```
states: intro → playing → level_complete → game_over
```
