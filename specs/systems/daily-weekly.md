# Daily & Weekly Systems

## Overview

Recurring content systems give players reasons to return. Done well, they feel like rewards for loyalty, not obligations. Neocadia's daily/weekly systems are opt-in bonuses, never required for progression.

---

## Daily Systems

### Daily Login Bonus
**Reset**: Midnight UTC

**Reward**: 50 tokens

**Presentation**:
- Warm welcome message from QWERTY
- Token animation
- Quick, no interruption

### Token Fountain Spin
**Location**: The Lobby
**Reset**: Midnight UTC

**Mechanics**:
- Click fountain when available
- Wheel spin animation
- Random reward:
  - 10 tokens (40%)
  - 25 tokens (30%)
  - 50 tokens (20%)
  - 100 tokens (10%)

**Visual**: Fountain sparkles when spin available

### Lost & Found
**Location**: The Lobby
**Reset**: Midnight UTC

**Mechanics**:
- Click cabinet when available
- Random collectible OR token bonus
- Contents rotate through a pool

**Possible Rewards**:
- Small token bonus (5-25)
- Cosmetic items (common pool)
- Lore fragments (rare)
- Collection items (very rare)

### Daily Challenge
**Reset**: Midnight UTC

**Structure**:
- One featured minigame
- Specific objective (score target, achievement)
- Completion reward: 100 tokens

**Example Challenges**:
- "Score 5000 in Void Breaker"
- "Catch 3 uncommon fish in Reel Deal"
- "Complete 5 levels in Candy Cascade"
- "Achieve 80% accuracy in Scene Stealer"

**Display**: Banner in relevant zone, QWERTY mentions it

### First Play Bonus
**Reset**: Midnight UTC

**Mechanics**:
- First game in each zone: 1.5× token multiplier
- Encourages variety
- Resets for all zones daily

---

## Weekly Systems

### Neon Alley Tournament
**Reset**: Sunday midnight UTC
**Duration**: Full week

**Structure**:
1. Featured game rotates weekly
2. Play anytime during week
3. Best score recorded
4. Leaderboard ranking

**Rewards**:
- Participation: 50 tokens
- Top 50%: 75 tokens
- Top 25%: 125 tokens
- Top 10%: 200 tokens
- Top 10: 300 tokens + Title
- #1: 500 tokens + Exclusive cosmetic

**Presentation**:
- NEON announces tournament
- Special UI for tournament mode
- Live leaderboard visible
- End-of-week results ceremony

### Featured Film (Starlight Cinema)
**Reset**: Sunday midnight UTC

**Structure**:
- One "film" (Scene Stealer sequence or Director's Cut puzzle)
- Special content not in regular rotation
- Complete for bonus

**Rewards**:
- Completion: 75 tokens
- Perfect score: 150 tokens
- First completion: Reel collectible

**Presentation**:
- CELIA announces "This week's feature"
- Special marquee in Cinema
- Limited availability feeling

### Weekly Quest Recap
**Reset**: Sunday midnight UTC

**Structure**:
- Summary of week's progress
- Bonus for active play
- Streak tracking

**Rewards**:
| Days Played | Bonus |
|-------------|-------|
| 3 days | 50 tokens |
| 5 days | 100 tokens |
| 7 days | 200 tokens + streak bonus |

### Streak System
**Mechanics**:
- Login on consecutive days builds streak
- Streak multiplies weekly bonus
- Missing a day breaks streak (no punishment, just reset)

**Streak Rewards**:
| Week Streak | Bonus Multiplier |
|-------------|------------------|
| 2 weeks | 1.1× weekly reward |
| 4 weeks | 1.25× weekly reward |
| 8 weeks | 1.5× weekly reward |
| 12 weeks | 1.75× weekly reward + cosmetic |

---

## Monthly/Seasonal Systems

### Monthly Highlights
**Reset**: First of month

**Content**:
- Recap of achievements
- Special monthly cosmetic (play on X days)
- Community milestones (total tokens earned by all)

### Seasonal Events (4 per year)

**Example: Autumn Harvest (October)**
- Special zone decorations
- Limited-time minigame variant
- Exclusive cosmetics
- Bonus collectibles
- Themed quests

**Duration**: 3-4 weeks

**Rewards**:
- Event currency → Event shop
- Participation cosmetics
- Completion titles

---

## Calendar Display

### In-Game Calendar
**Location**: Accessible from Lobby, Player Cabinet

**Shows**:
- Daily reset countdown
- Weekly reset countdown
- Current daily challenge
- Tournament standings
- Event schedule
- Upcoming content

### Notifications
**Types**:
- Daily reset: "A new day in Neocadia!"
- Weekly reset: "Tournament results are in!"
- Event start: "The [Event Name] has begun!"

**Settings**:
- All optional
- In-game only (no push notifications)

---

## Implementation

### Reset Logic

```typescript
interface DailyState {
  date: string;  // YYYY-MM-DD format, UTC
  login_claimed: boolean;
  fountain_spun: boolean;
  lost_found_claimed: boolean;
  challenge_completed: boolean;
  first_plays: ZoneId[];
}

function checkDailyReset(state: DailyState): DailyState {
  const today = new Date().toISOString().split('T')[0];

  if (state.date !== today) {
    return {
      date: today,
      login_claimed: false,
      fountain_spun: false,
      lost_found_claimed: false,
      challenge_completed: false,
      first_plays: [],
    };
  }

  return state;
}
```

### Weekly Content Selection

```typescript
interface WeeklyContent {
  tournament_game: MinigameId;
  featured_film: FilmId;
  special_rewards: RewardId[];
}

function getWeeklyContent(weekNumber: number): WeeklyContent {
  // Deterministic selection based on week
  // Ensures same content for all players
  // Rotates through catalog
}
```

---

## Balance Considerations

### Not Punishing
- Missing days has NO negative consequence
- Streaks add bonus, don't gate content
- All content achievable without daily play

### Encouraging But Not Addictive
- Rewards are nice, not essential
- No FOMO-inducing exclusive missables
- Seasonal items return (eventually)

### Respecting Time
- Daily tasks completable in < 10 minutes
- Weekly goals achievable with moderate play
- No "log in every 4 hours" mechanics
