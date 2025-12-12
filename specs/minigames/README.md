# Minigame Design Philosophy

## Core Principles

### 1. Telos + Ludos
Every minigame must answer two questions:
- **Telos**: Why does this game exist in Neocadia? What does it add to the world?
- **Ludos**: What is the play? What makes it fun moment-to-moment?

### 2. The 30-Second Loop
Each game's core loop should be engaging within 30 seconds. Players should understand the basics immediately and find depth over time.

### 3. Skill + Luck Balance
Games should reward skill but include enough variance that new players can occasionally succeed. Mastery = consistency, not impossibility.

### 4. Token Integration
All games award tokens based on performance. The economy should feel:
- Generous enough to progress
- Challenging enough to value high scores
- Fair across all game types

### 5. Accessibility
- Simple controls (mouse-only primary, keyboard optional)
- Clear visual feedback
- Colorblind-friendly palettes
- Adjustable difficulty where appropriate

---

## Game Categories

### Action (Neon Alley)
Fast-paced, reflex-based, score-chasing. These are the competitive games.
- Void Breaker (Breakout)
- Synth Racer (Rhythm Runner)
- Pixel Invaders (Shooter)

### Relaxed (Pixel Beach)
Low-pressure, satisfaction-focused, zen-like. Play to unwind.
- Reel Deal (Fishing)
- Wave Rider (Surfing)
- Shell Shocked (Memory)

### Puzzle (Glitch Garden)
Rule-bending, perspective-shifting, thoughtful. Embrace the weird.
- Debug (Spot-the-difference)
- Loop Garden (Changing-rules maze)
- Error Garden (Idle/clicker)

### Narrative (Starlight Cinema)
Story-driven, culture-connected, dramatic. For people who love stories.
- Scene Stealer (QTE sequences)
- Reel Trivia (Quiz)
- Director's Cut (Narrative puzzle)

### Logic (Clockwork Quarter)
Systematic, satisfying, elegant. For puzzle lovers.
- Gear Garden (Connection puzzle)
- Tick Defense (Tower defense)
- Spring Loaded (Physics puzzle)

### Casual (Sugar Rush Boulevard)
Pure fun, instant gratification, everyone welcome. The crowd-pleasers.
- Candy Cascade (Match-3)
- Sugar Rush Kitchen (Cooking sim)
- Jawbreaker (Brick breaker)

---

## Universal Game Elements

### Start Screen
- Game title
- High score display
- Control hints
- Start button
- Back to zone button

### Pause Menu
- Continue
- Restart
- Controls
- Quit to zone

### End Screen
- Final score
- Tokens earned
- Personal best indicator
- Leaderboard position (if applicable)
- Play again / Return options

### Difficulty Scaling
Games should scale in one of these ways:
- **Level-based**: Clear stages of increasing difficulty
- **Endless escalation**: Gets harder the longer you survive
- **Player choice**: Easy/Medium/Hard selection

---

## Token Awards

Base formula:
```
tokens = base_award + (score_bonus × performance_multiplier)
```

### By Category
| Category | Base Award | Score Bonus Range |
|----------|-----------|-------------------|
| Action | 15 | 10-85 |
| Relaxed | 20 | 5-30 |
| Puzzle | 25 | 15-75 |
| Narrative | 20 | 10-30 |
| Logic | 20 | 10-80 |
| Casual | 15 | 5-35 |

### Multipliers
- First play of day: 1.5x
- Personal best: 1.25x
- Zone restoration bonus: up to 1.2x (at max restoration)
- Weekly tournament: Variable

---

## Leaderboard System

### Scope
- Personal best (always tracked)
- Daily leaderboard (resets at midnight UTC)
- Weekly leaderboard (resets Sunday)
- All-time leaderboard (permanent)

### Display
- Top 10 shown
- Player's position always shown
- Friends only option (future feature)

---

## Art Direction Per Game

Each game spec includes:
- **Visual style**: How it fits the zone aesthetic
- **UI skin**: Zone-specific UI elements
- **Sound palette**: Genre-appropriate audio
- **Victory/defeat states**: Zone-consistent feedback

---

## Technical Spec Format

Each game spec follows this structure:
1. Overview (Telos + Ludos)
2. Core Loop
3. Controls
4. Mechanics (with numbers)
5. Progression/Difficulty
6. Scoring
7. Visual Style
8. Audio
9. Asset List
10. Implementation Notes

---

## Game Index

### Neon Alley
1. [Void Breaker](neon-alley/void-breaker.md) - Breakout with bullet-hell
2. [Synth Racer](neon-alley/synth-racer.md) - Outrun meets rhythm
3. [Pixel Invaders](neon-alley/pixel-invaders.md) - Classic shooter evolved

### Pixel Beach
4. [Reel Deal](pixel-beach/reel-deal.md) - Fishing simulation
5. [Wave Rider](pixel-beach/wave-rider.md) - Endless surfer
6. [Shell Shocked](pixel-beach/shell-shocked.md) - Memory matching

### Glitch Garden
7. [Debug](glitch-garden/debug.md) - Spot the visual glitch
8. [Loop Garden](glitch-garden/loop-garden.md) - Rule-changing maze
9. [Error Garden](glitch-garden/error-garden.md) - Glitch idle game

### Starlight Cinema
10. [Scene Stealer](starlight-cinema/scene-stealer.md) - QTE movie scenes
11. [Reel Trivia](starlight-cinema/reel-trivia.md) - Pop culture quiz
12. [Director's Cut](starlight-cinema/directors-cut.md) - Story sequencing

### Clockwork Quarter
13. [Gear Garden](clockwork-quarter/gear-garden.md) - Gear connection
14. [Tick Defense](clockwork-quarter/tick-defense.md) - Clockwork tower defense
15. [Spring Loaded](clockwork-quarter/spring-loaded.md) - Physics launcher

### Sugar Rush Boulevard
16. [Candy Cascade](sugar-rush/candy-cascade.md) - Match-3
17. [Sugar Rush Kitchen](sugar-rush/sugar-rush-kitchen.md) - Cooking time management
18. [Jawbreaker](sugar-rush/jawbreaker.md) - Candy brick breaker
