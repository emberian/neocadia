# Minigame Spec: Director's Cut

## Overview

### Telos
Director's Cut lets you become the storyteller. Arrange film strips to create coherent (or intentionally absurd) narratives. It's about understanding story structure—or delightfully subverting it.

### Ludos
Puzzle game: arrange story beats in correct order. Like a narrative jigsaw where you're assembling plot. Can be played "correctly" or for comedy.

---

## Core Loop

1. Receive shuffled film strips
2. Each strip shows a story moment
3. Arrange in logical order
4. Submit for review
5. Score based on narrative coherence
6. Bonus for speed and creativity

**Session Length**: 5-15 minutes typical

---

## Controls

### Mouse
- Drag strip → Move to position
- Click submit → Check answer

---

## Mechanics

### Film Strips
- Each strip: One story beat (image + caption)
- 4-8 strips per story
- Clear visual storytelling

### Story Types
| Type | Strips | Difficulty |
|------|--------|------------|
| Simple | 4 | Easy |
| Standard | 6 | Medium |
| Complex | 8 | Hard |
| Experimental | Variable | Expert |

### Scoring Modes

**Correct Order Mode**:
- One true sequence
- Points for proximity to correct
- Bonus for perfect order

**Creative Mode**:
- Multiple valid sequences
- Scored on coherence
- AI/rule-based evaluation

### Points
- Each strip in correct position: 100
- Adjacent pairs correct: +50
- Full sequence correct: +500
- Speed bonus: Up to 200

### Token Conversion
```
tokens = 20 + floor(score / 150)
```
Cap: 50 tokens per session

---

## Content

### Story Categories
- Classic tales (fairy tales, myths)
- Film parodies (famous movie plots)
- Original Neocadia stories
- Player-created (future feature)

### Examples
- "The Hero's Journey" - 6 strips
- "A Day at the Beach" - 4 strips
- "The Great Heist" - 8 strips

---

## Visual Style

- Film strip borders
- Sepia/vintage filtering
- Projector aesthetic
- Success: Film "plays"

---

## Asset List

### UI
| Asset | Description |
|-------|-------------|
| dc_strip_frame | Film strip border |
| dc_timeline | Arrangement area |
| dc_submit | Submit button |
| dc_result | Result display |

### Stories
| Asset | Description |
|-------|-------------|
| dc_story_* | Story strip images |

---

## Implementation Notes

### Story Data
```typescript
interface Story {
  id: string;
  title: string;
  strips: Strip[];
  correct_order: number[];
  alt_valid_orders?: number[][];
}

interface Strip {
  id: string;
  image: string;
  caption: string;
  correct_position: number;
}
```
