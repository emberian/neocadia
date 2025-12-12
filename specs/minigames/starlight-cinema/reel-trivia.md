# Minigame Spec: Reel Trivia

## Overview

### Telos
Reel Trivia celebrates shared culture. It's the game for film buffs, music nerds, and trivia lovers—testing knowledge of movies, music, and pop culture across all eras. CELIA hosts, adding drama to every question.

### Ludos
Classic quiz game with multiple choice. Answer questions, earn points, climb leaderboards. Simple, endlessly replayable, satisfying for those who know things.

---

## Core Loop

1. Question appears with 4 answers
2. Timer counts down
3. Select answer before time expires
4. Reveal correct answer
5. Points based on speed and accuracy
6. Continue until out of lives

**Session Length**: 5-15 minutes typical

---

## Controls

### Mouse
- Click answer → Select

### Keyboard
- 1/2/3/4 → Select answer

---

## Mechanics

### Question Format
- 4 multiple choice answers
- 15 seconds per question (default)
- One correct answer

### Categories
| Category | Examples |
|----------|----------|
| Classic Film | Golden age movies |
| Modern Movies | Recent releases |
| TV Shows | Series knowledge |
| Music | Artists, songs, albums |
| Gaming | Video game culture |
| Internet | Memes, viral content |
| Neocadia | Lore questions |

### Difficulty
| Level | Timer | Points | Questions |
|-------|-------|--------|-----------|
| Easy | 20s | 100 | Obvious answers |
| Medium | 15s | 200 | Requires knowledge |
| Hard | 10s | 400 | Deep cuts |
| Expert | 8s | 800 | Obscure trivia |

### Lives System
- Start with 3 lives
- Wrong answer = lose 1 life
- Streak bonus: 5 correct = +1 life
- No lives = game over

### Scoring
- Base: Difficulty points
- Speed bonus: +50% if answered in first half of timer
- Streak: +10% per consecutive correct
- Category streak: Bonus for same category 3x

### Token Conversion
```
tokens = 20 + floor(score / 200)
```
Cap: 75 tokens per session

---

## Content

### Question Database
- 500+ questions at launch
- Community submission (moderated)
- Rotating featured questions
- Seasonal additions

### Daily Challenge
- 10 fixed questions per day
- Same for all players
- Leaderboard for daily scores

---

## Visual Style

- Cinema aesthetic
- Questions on movie screen
- CELIA reacts to answers
- Film transitions between questions

---

## Asset List

### UI
| Asset | Description |
|-------|-------------|
| rt_ui_question | Question display |
| rt_ui_answers | 4 answer buttons |
| rt_ui_timer | Time remaining |
| rt_ui_lives | Life indicators |
| rt_ui_score | Running score |

### Effects
| Asset | Description |
|-------|-------------|
| fx_correct | Correct answer effect |
| fx_wrong | Wrong answer effect |
| fx_streak | Streak indicator |

---

## Implementation Notes

### Question Data
```typescript
interface Question {
  id: string;
  category: Category;
  difficulty: Difficulty;
  question: string;
  answers: string[];
  correct_index: number;
  fun_fact?: string;
}
```

### Anti-Memorization
- Large question pool
- Random order of answers
- Variation in question phrasing
