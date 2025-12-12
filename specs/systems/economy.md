# Economy System

## Overview

Neocadia's economy is designed to feel generous while maintaining meaningful progression. Players should always feel rewarded for playing, never like they're grinding against a wall.

### Core Principle
*"Every game should feel worth playing. Every token should feel worth earning."*

---

## Currency: Tokens

### What Are Tokens?
Tokens are crystallized Luminance—the residue of enjoyment condensed into transferable form. They're not abstract currency; they're proof that someone played and enjoyed.

### Visual Representation
- Golden coin shape with arcade token aesthetic
- Subtle glow indicating Luminance
- Stacking animation when collected
- Satisfying "clink" sound

---

## Earning Tokens

### Minigame Rewards
Every minigame awards tokens based on a formula:

```
tokens = base_award + (score_bonus × performance_multiplier)
```

#### Base Awards by Zone
| Zone | Base | Rationale |
|------|------|-----------|
| Neon Alley | 15 | Competitive, skill-based |
| Pixel Beach | 20 | Relaxed, time-based |
| Glitch Garden | 25 | Puzzle, thinking-based |
| Starlight Cinema | 20 | Narrative, engagement-based |
| Clockwork Quarter | 20 | Logic, solution-based |
| Sugar Rush Boulevard | 15 | Casual, quick sessions |

#### Session Caps
To prevent burnout and maintain balance:
- Most games: 50-100 tokens per session
- No hard limit on sessions per day
- Diminishing returns after ~1 hour on single game

### Daily Bonuses
| Source | Amount | Reset |
|--------|--------|-------|
| First login | 50 | Daily |
| Token Fountain spin | 10-100 (random) | Daily |
| Lost & Found | 5-50 (random item value) | Daily |
| Daily challenge | 100 | Daily |
| Zone first play | 1.5× multiplier | Daily |

### Weekly Bonuses
| Source | Amount | Reset |
|--------|--------|-------|
| Tournament participation | 50 | Weekly |
| Tournament top 10 | 200 | Weekly |
| Featured film completion | 75 | Weekly |
| Collection milestone | Variable | On achieve |

### Quest Rewards
| Quest Type | Range |
|------------|-------|
| Character quest step | 100-500 |
| Main story milestone | 500-1000 |
| Achievement unlock | 50-500 |
| Hidden discovery | 25-100 |

### Special Events
- Seasonal events: Bonus multipliers
- Community goals: Shared rewards
- Anniversary: All players receive tokens

---

## Spending Tokens

### Zone Unlocks
| Zone | Cost | Prerequisite |
|------|------|--------------|
| Pixel Beach | Free | None (starter) |
| Neon Alley | 500 | Complete tutorial |
| Sugar Rush Boulevard | 750 | 25% restoration |
| Clockwork Quarter | 1000 | 35% restoration |
| Starlight Cinema | 1500 | 45% restoration |
| Glitch Garden | 2000 | 60% restoration |

### Restoration Spending
Each zone has restoration tiers requiring cumulative tokens:

| Tier | Lobby | Other Zones |
|------|-------|-------------|
| Flickering → Awakening | 1000 | 500 |
| Awakening → Thriving | 2500 | 1500 |
| Thriving → Radiant | 5000 | 3000 |

**Note**: Tokens spent on restoration are *invested*, not lost. They become part of the world.

### Cosmetics
| Category | Range | Examples |
|----------|-------|----------|
| Avatar outfits | 100-500 | Zone-themed costumes |
| Accessories | 50-200 | Hats, glasses, effects |
| Cabinet decals | 100-300 | Personal cabinet skins |
| Emotes | 50-100 | Reaction animations |
| Titles | 150-500 | Display names |

### Consumables (Optional Helps)
| Item | Cost | Effect |
|------|------|--------|
| Hint Token | 25 | One hint in puzzle games |
| Extra Life | 50 | +1 life in applicable games |
| Score Boost | 100 | 1.5× next game score |
| Bait (fishing) | 10-50 | Better fish chances |

---

## Balance Philosophy

### Earning Rates

**Target**: A casual player (30 min/day) should progress steadily.

| Playstyle | Daily Tokens | Weekly | Monthly |
|-----------|--------------|--------|---------|
| Casual (30 min) | 150-200 | 1000-1400 | 4000-6000 |
| Regular (1 hour) | 300-400 | 2000-2800 | 8000-12000 |
| Dedicated (2+ hours) | 500-700 | 3500-5000 | 15000-20000 |

### Progression Timeline

**Casual Player Path**:
- Week 1: Pixel Beach fully explored, Neon Alley unlocked
- Week 2-3: Two more zones unlocked
- Month 1: All zones accessible, 50% restoration
- Month 2-3: 75% restoration, most cosmetics available
- Month 3-4: Full restoration achievable

### Anti-Grind Measures
- Base awards are substantial (not dependent on high scores)
- Daily bonuses are significant portion of income
- Restoration milestones visible and satisfying
- No token purchases with real money (no pay-to-win)

---

## Economy Sinks

### Where Tokens Go
1. **Zone Unlocks** - One-time large purchases
2. **Restoration** - Cumulative investment
3. **Cosmetics** - Optional personalization
4. **Consumables** - Optional helpers

### Preventing Inflation
- Token caps per game session
- Restoration acts as permanent sink
- New content adds new sinks
- No token trading between players

---

## Token UI

### Display
- Always visible in HUD corner
- Shows current total
- Recent change indicator (+50 recent!)
- Animated on earn

### Transaction Feedback
- Earn: Coins fly to counter, satisfying sound
- Spend: Investment animation, positive sound
- Milestone: Celebration effect, progress indicator

---

## Data Structure

```typescript
interface EconomyState {
  tokens_current: number;
  tokens_lifetime_earned: number;
  tokens_lifetime_spent: number;

  daily_state: {
    login_claimed: boolean;
    fountain_spun: boolean;
    lost_found_claimed: boolean;
    challenge_completed: boolean;
    first_plays_remaining: ZoneId[];
  };

  weekly_state: {
    tournament_participated: boolean;
    featured_film_completed: boolean;
  };

  purchase_history: PurchaseRecord[];
}
```

---

## Tuning Notes

### If Players Progress Too Fast
- Reduce daily bonuses
- Increase restoration costs
- Lower session caps

### If Players Feel Stuck
- Increase base awards
- Add catch-up mechanics
- Create bonus events

### Monitoring
- Track median time to milestones
- Watch for frustration patterns
- Survey player satisfaction
