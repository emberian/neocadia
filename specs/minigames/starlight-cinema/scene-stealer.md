# Minigame Spec: Scene Stealer

## Overview

### Telos
Scene Stealer lets you be the star. Recreate famous movie moments through timed inputs—feel the drama, nail the timing, become the hero. It's CELIA's favorite because it proves that stories live in the doing.

### Ludos
Quick-time event sequences set to film scenes. Press the right buttons at the right time to successfully perform iconic moments. Rhythm meets narrative.

---

## Core Loop

1. Scene intro plays (sets context)
2. Action sequence begins
3. Prompts appear for timed inputs
4. Match prompts to succeed
5. Scene plays out based on performance
6. Score based on accuracy

**Session Length**: 3-10 minutes typical

---

## Controls

### Keyboard (Primary)
- W/A/S/D → Direction prompts
- Space → Action prompt
- Timing: Hit when prompt reaches marker

### Mouse
- Click zones → Match prompt direction

---

## Mechanics

### Prompt Types
| Type | Visual | Input |
|------|--------|-------|
| Direction | Arrow pointing | WASD |
| Action | Circle | Space |
| Hold | Bar filling | Hold key |
| Rapid | Multiple flashes | Button mash |

### Timing Windows
| Window | Range | Score |
|--------|-------|-------|
| Perfect | ±50ms | 100% |
| Great | ±100ms | 75% |
| Good | ±200ms | 50% |
| Miss | >200ms | 0% |

### Scene Structure
- Intro: 5-10s (no input)
- Action: 30-60s (prompts)
- Outro: Based on performance

### Scene Categories (by Genre)
- **Action**: Fast prompts, combat moments
- **Romance**: Slower, emotional timing
- **Comedy**: Unexpected rhythms
- **Drama**: Tension building, key moments
- **Musical**: Actually rhythmic

### Scoring
- Per prompt: 100 × timing multiplier
- Combo: +10% per consecutive hit
- Scene completion: Up to 500 bonus
- Perfect scene: 2x all points

### Token Conversion
```
tokens = 20 + floor(score / 100)
```
Cap: 50 tokens per session

---

## Visual Style

- Film aesthetics per scene
- Prompts styled to genre
- Performance affects scene visuals
- Miss = comedic fails

---

## Content: Scenes

### Starter Scenes
1. "The Great Escape" - Action, running sequence
2. "Love at Last" - Romance, slow dance
3. "Sword Duel" - Action, combat
4. "The Speech" - Drama, building tension
5. "Dance Number" - Musical, choreography

### Unlock Scenes (10+ total)
- Varied genres and difficulties
- Higher difficulty = better rewards
- Some tied to CELIA's quest

---

## Asset List

### UI
| Asset | Description |
|-------|-------------|
| ss_prompt_arrow | Direction prompt (4) |
| ss_prompt_action | Action prompt |
| ss_prompt_hold | Hold bar |
| ss_prompt_target | Timing marker |

### Scenes
| Asset | Description |
|-------|-------------|
| ss_scene_* | Scene video/animation |
| ss_scene_fail_* | Fail variants |

---

## Implementation Notes

### Scene Data
```typescript
interface Scene {
  id: string;
  name: string;
  genre: Genre;
  duration: number;
  prompts: Prompt[];
  video_success: string;
  video_fail: string;
}
```

### Timing System
- Audio-synced prompts
- Latency compensation
- Visual cue before audio hit
