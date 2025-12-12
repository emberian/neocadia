# Minigame Spec: Shell Shocked

## Overview

### Telos
Shell Shocked is a memory game with pressure. The tide is coming in—match the shells before they're washed away. It's PIXEL's game, the one they play to pass the time, and it rewards the attentive mind.

### Ludos
Classic memory match with a twist: the tide is your timer, and special shells add complications. Simple to understand, satisfying to complete, brutal at higher difficulties.

---

## Core Loop

1. Grid of face-down shells revealed
2. Brief preview of all shells
3. Flip two shells to find matches
4. Matching pairs stay revealed
5. Beat the tide timer
6. Clear board to advance

**Session Length**: 5-15 minutes typical

---

## Controls

### Mouse (Primary)
- Click shell → Flip it
- That's it. Pure simplicity.

### Keyboard (Alternative)
- Arrow keys → Move cursor
- Space → Flip selected

### Touch
- Tap → Flip shell

---

## Mechanics

### The Board
| Level | Grid Size | Pairs | Preview Time |
|-------|-----------|-------|--------------|
| 1-3 | 4×3 | 6 | 5 seconds |
| 4-6 | 4×4 | 8 | 4 seconds |
| 7-9 | 5×4 | 10 | 3 seconds |
| 10-12 | 6×4 | 12 | 2 seconds |
| 13+ | 6×5 | 15 | 1 second |

### Shell Types
| Shell | Visual | Special |
|-------|--------|---------|
| Scallop | Pink fan | None |
| Conch | Spiral cream | None |
| Clam | Purple oval | None |
| Starfish | Orange star | None |
| Sand Dollar | White circle | None |
| Coral | Red branch | None |
| Pearl | White glow | Worth 2x points |
| Mystery | ? pattern | Random effect when matched |
| Crab | Red pincher | Moves to new position if not matched |

### The Tide
- Timer bar shows tide approaching
- When tide fills, unmatched shells wash away
- Each washed shell = -100 points
- All washed = game over
- Match grants +time extension

### Scoring
| Action | Points |
|--------|--------|
| Match | 100 |
| First-try match | 200 |
| Pearl match | 200 |
| Speed match (<1s between flips) | +50 |
| Full board clear | 500 × level |

### Power-Ups (Found in Mystery Shells)
| Effect | Description |
|--------|-------------|
| Tide Pause | Stop tide for 5 seconds |
| Reveal | Show all shells for 2 seconds |
| Magnet | Highlight one matching pair |
| Double Points | Next 3 matches worth 2x |

### Hazards (Also in Mystery Shells)
| Effect | Description |
|--------|-------------|
| Shuffle | Unmatched shells swap positions |
| Tide Rush | Tide speeds up for 10 seconds |
| Fog | Shells harder to see for 5 seconds |

---

## Progression

### Difficulty Curve
- Levels 1-3: Tutorial pace, long preview
- Levels 4-6: Standard difficulty
- Levels 7-9: Crab shells introduced
- Levels 10-12: Mystery shells, faster tide
- Levels 13+: Maximum pressure

### Endless Mode
- After Level 15, difficulty plateaus
- Boards randomized
- High score chase

### Challenge Mode
- Fixed difficult boards
- No preview
- Leaderboard specific

---

## Scoring & Rewards

### Level Completion
- Base: 500 × level number
- Time bonus: Remaining tide % × 100
- No-mistake bonus: +50%
- Perfect (all first-try): +100%

### Token Conversion
```
tokens = 20 + floor(score / 200)
```
Cap: 75 tokens per session

### Collection Integration
- New shell types unlock as collection items
- Rare shells collected from gameplay
- Display in Pixel Beach shack

---

## Visual Style

### Aesthetic
- Beach sand background
- Pixel art shells
- Tide visually creeping up
- Water effects at board edges

### Board
- Shells arranged on sand
- Each shell has "down" and "up" state
- Matched shells stay revealed and sparkle
- Unmatched shells flip back with wobble

### Tide
- Water visible at bottom
- Rises as timer decreases
- Reaches shells when time critical
- Washes over with wave animation

### Feedback
| Event | Visual |
|-------|--------|
| Flip | Shell rotates in place |
| Match | Shells sparkle, stay up |
| Mismatch | Shells shake, flip back |
| Time low | Screen edges turn blue |
| Clear | Celebration particles |
| Wash away | Shell tumbles off screen |

---

## Audio

### Music
- Soft beach ambient
- Tempo increases as tide rises
- Triumph on level clear

### Sound Effects
| Event | Sound |
|-------|-------|
| Shell flip | Soft click |
| Match | Satisfying chime |
| Mismatch | Soft buzz |
| Pearl match | Special sparkle |
| Mystery reveal | Surprise sound |
| Crab move | Scuttling |
| Tide warning | Rushing water |
| Shell wash | Wave splash |
| Level clear | Fanfare |
| Game over | Sad wave |

---

## Asset List

### Sprites
| Asset | Description | Variants |
|-------|-------------|----------|
| ss_shell_back | Face-down shell | 1 |
| ss_shell_scallop | Scallop shell | Face up |
| ss_shell_conch | Conch shell | Face up |
| ss_shell_clam | Clam shell | Face up |
| ss_shell_starfish | Starfish | Face up |
| ss_shell_dollar | Sand dollar | Face up |
| ss_shell_coral | Coral piece | Face up |
| ss_shell_pearl | Pearl shell | Face up + glow |
| ss_shell_mystery | Mystery shell | Face up |
| ss_shell_crab | Crab shell | Face up + move anim |

### Environment
| Asset | Description | Notes |
|-------|-------------|-------|
| ss_bg_sand | Sand background | Base |
| ss_tide | Rising water | Animation |
| ss_wave | Washing wave | Animation |
| ss_foam | Edge foam | Animation |

### Effects
| Asset | Description | Type |
|-------|-------------|------|
| fx_shell_flip | Flip animation | Rotation |
| fx_match_sparkle | Match celebration | Particle |
| fx_wash_away | Shell washing | Animation |
| fx_fog | Fog hazard | Overlay |

### UI
| Asset | Description | Notes |
|-------|-------------|-------|
| ss_ui_tide | Tide timer bar | Filling water |
| ss_ui_score | Score display | Top |
| ss_ui_level | Level indicator | Top |
| ss_ui_matches | Pairs remaining | Counter |

---

## Implementation Notes

### Board Generation
```typescript
function generateBoard(level: number): Shell[][] {
  const size = getBoardSize(level);
  const pairs = (size.width * size.height) / 2;

  // Select shell types
  const shells = selectShellTypes(pairs, level);

  // Duplicate and shuffle
  const allShells = [...shells, ...shells];
  shuffle(allShells);

  // Arrange in grid
  return arrangeGrid(allShells, size);
}
```

### Match Detection
- Track currently flipped shells (max 2)
- Compare on second flip
- Delay before flip-back (let player see)
- Crab shells check position after mismatch

### Tide System
- Timer independent of gameplay speed
- Visual sync to timer value
- Warning thresholds: 50%, 25%, 10%

### State Machine
```
states: preview → playing → level_complete → game_over
```

### Save Data
```typescript
interface ShellShockedSave {
  high_score: number;
  max_level: number;
  shells_collected: ShellId[];
  perfect_levels: number;
  total_matches: number;
}
```
