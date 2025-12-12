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

**Performance Multiplier Formula**:
- Score 0-50% of par: 0.5× (floor)
- Score 50-100% of par: 0.5× + ((score% - 50)/50 × 0.5) → scales from 0.5× at 50% to 1.0× at 100%
- Score 100-150% of par: 1.0× + ((score% - 100)/50 × 0.5) → scales from 1.0× at 100% to 1.5× at 150%
- Score 150%+ of par: 1.5× (cap)

**Score Bonus Range by Zone** (varies by minigame, see individual specs):
- Action games: 10-85 tokens (high variance, skill-based)
- Relaxed games: 5-55 tokens (low variance, time-based)
- Puzzle games: 15-50 tokens (solution-based)
- Narrative games: 10-30 tokens (engagement-based)
- Logic games: 10-80 tokens (complexity-based)
- Casual games: 5-35 tokens (accessibility-focused)

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

| Zone | Session Cap | Rationale |
|------|-------------|-----------|
| Neon Alley | 100 | High-skill competitive play rewards dedication |
| Pixel Beach | 75 | Relaxed but not infinitely farmable |
| Glitch Garden | 75 | Puzzle solutions are finite per session |
| Starlight Cinema | 50 | Narrative content is limited |
| Clockwork Quarter | 100 | Complex logic games deserve payout |
| Sugar Rush Boulevard | 50 | Quick casual sessions |

- No hard limit on sessions per day
- **Diminishing Returns**: After 45 minutes on a single game, token earn rate drops to 50%. After 90 minutes, drops to 25%. Timer resets after 2 hours away from that specific game.
- **Daily Soft Cap**: After earning 500 tokens from gameplay in one day, all rates drop to 50%. Bonuses (daily, weekly, quest) are unaffected.

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
| Tournament top 50% | 75 | Weekly |
| Tournament top 25% | 125 | Weekly |
| Tournament top 10% | 200 | Weekly |
| Tournament top 10 players | 300 | Weekly |
| Tournament #1 | 500 + exclusive cosmetic | Weekly |
| Featured film completion | 75 | Weekly |
| Featured film perfect score | 150 | Weekly |
| 7-day login streak | 200 | Weekly |

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
| Pixel Beach | Free | None (starter zone) |
| Neon Alley | 500 | Complete tutorial |
| Sugar Rush Boulevard | 750 | 25% overall restoration |
| Clockwork Quarter | 1000 | 35% overall restoration |
| Starlight Cinema | 1500 | 45% overall restoration |
| Glitch Garden | 2000 | 60% overall restoration |

**How Zone Prerequisites Work**:
- Overall restoration is a weighted average (see Progression spec)
- Players can reach 25% overall by restoring Lobby (1.5× weight) + starter zones
- Token cost AND restoration prerequisite must both be met
- Players cannot "skip" by just having tokens—engagement with restoration is required
- Example path to Glitch Garden unlock:
  - Lobby at 50% (contributes ~11% weighted)
  - Pixel Beach at 100% (contributes ~14%)
  - Neon Alley at 75% (contributes ~11%)
  - Sugar Rush at 50% (contributes ~7%)
  - Clockwork Quarter at 50% (contributes ~7%)
  - Starlight Cinema at 75% (contributes ~11%)
  - **Total: ~61% overall** → Glitch Garden unlockable

### Restoration Spending
Each zone has restoration tiers requiring cumulative tokens:

| Tier | Lobby | Other Zones | Total to Radiant |
|------|-------|-------------|------------------|
| Flickering → Awakening (25%) | 500 | 300 | - |
| Awakening → Thriving (50%) | 1500 | 800 | - |
| Thriving → Radiant (100%) | 3000 | 1500 | - |
| **Per Zone Total** | **5000** | **2600** | - |

**Full Restoration Cost Breakdown**:
- Lobby: 5,000 tokens
- 6 Other Zones: 6 × 2,600 = 15,600 tokens
- **Total to 100% Restoration**: 20,600 tokens

**Note**: Tokens spent on restoration are *invested*, not lost. They become part of the world. Restoration also gains passively: every token earned adds 0.05% to the zone played in, and every token spent adds 0.025% to the target zone.

**Passive Restoration Math**:
- Casual player (175 tokens/day) → 8.75% zone restoration/day from passive alone
- This means passive restoration is a nice bonus (~10-15% of total progress) rather than the primary driver
- Investing tokens directly in restoration remains the main progression method
- Example: A player earning 1,000 tokens in Neon Alley gains +50% passive restoration there, but needs 2,600 tokens invested to fully restore the zone

### Cosmetics
| Category | Range | Examples |
|----------|-------|----------|
| Avatar outfits | 100-500 | Zone-themed costumes |
| Accessories | 50-200 | Hats, glasses, effects |
| Cabinet decals | 100-300 | Personal cabinet skins |
| Emotes | 50-100 | Reaction animations |
| Titles | 150-500 | Display names |

### Consumables (Optional Helps)
| Item | Cost | Effect | Max Held | Daily Purchase Limit |
|------|------|--------|----------|---------------------|
| Hint Token | 25 | One hint in puzzle games | 5 | 3 |
| Extra Life | 50 | +1 life in applicable games | 3 | 2 |
| Score Boost | 100 | 1.5× next game score | 2 | 1 |
| Bait (fishing) | 10-50 | Better fish chances | 10 per type | 5 per type |

**Consumable Philosophy**:
- Consumables help struggling players, not optimize grinding
- Can't stockpile forever (inventory limits)
- Can't buy unlimited per day (purchase limits)
- Never required for progression (purely optional assists)
- Reset: Inventory persists, purchase limits reset daily at midnight UTC

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

**Casual Player Path** (30 min/day, ~175 tokens/day average):

| Milestone | Tokens Needed | Days | Week |
|-----------|---------------|------|------|
| Neon Alley unlock | 500 | 3 | Week 1 |
| Sugar Rush unlock (25% resto) | 750 + ~500 resto | 7 | Week 1-2 |
| Clockwork Quarter unlock | 1000 + ~700 resto | 10 | Week 2 |
| Starlight Cinema unlock | 1500 + ~900 resto | 14 | Week 2-3 |
| Glitch Garden unlock | 2000 + ~1200 resto | 18 | Week 3 |
| All zones Awakening (25%) | ~3000 resto | 25 | Week 4 |
| All zones Thriving (50%) | ~8000 resto | 45 | Week 6-7 |
| 100% Restoration | ~20,600 total | 90-120 | Month 3-4 |

**Validation Math**:
- Zone unlocks total: 500 + 750 + 1000 + 1500 + 2000 = 5,750 tokens
- Restoration total: 20,600 tokens
- Cosmetics (optional): ~3,000 tokens for decent collection
- **Grand Total to "Complete"**: ~29,350 tokens
- At 175 tokens/day casual: 168 days (~5.5 months)
- At 350 tokens/day regular: 84 days (~3 months)
- At 600 tokens/day dedicated: 49 days (~7 weeks)

**Collection Reward Offset** (tokens earned back during play):
- Fish Collection (Pixel Beach): 750 tokens (25%: 100, 50%: 150, 75%: 200, 100%: 300)
- Arcade Legends (Neon Alley): 750 tokens
- Film Reels (Starlight Cinema): 750 tokens
- Glitch Samples (Glitch Garden): 750 tokens
- Blueprints (Clockwork Quarter): 750 tokens
- Recipes (Sugar Rush): 750 tokens
- Achievements: ~1,000 tokens (meta-collection, larger scope)
- **Total Collection Rewards**: 5,500 tokens
- **Net Cost after Collections**: ~23,850 tokens (reduces timeline by ~18%)

This pacing ensures casual players can see credits in 3-4 months while dedicated players reach endgame in under 2 months.

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

---

## System Integration

### The Core Loop: Tokens → Restoration → Unlocks → Content → Tokens

```
┌─────────────────────────────────────────────────────────────┐
│                         PLAY                                 │
│   ┌─────────────┐    ┌──────────────┐    ┌─────────────┐   │
│   │  Minigames  │───▶│   Tokens     │───▶│ Restoration │   │
│   └─────────────┘    └──────────────┘    └─────────────┘   │
│         ▲                   │                    │          │
│         │                   │                    ▼          │
│         │                   │            ┌─────────────┐   │
│         │                   │            │Zone Unlocks │   │
│         │                   │            └─────────────┘   │
│         │                   │                    │          │
│         │                   ▼                    ▼          │
│   ┌─────────────┐    ┌──────────────┐    ┌─────────────┐   │
│   │  New Games  │◀───│  Cosmetics   │◀───│   Story     │   │
│   └─────────────┘    └──────────────┘    └─────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Dead End Prevention

**Identified Risk**: Player spends all tokens on cosmetics early, can't afford zone unlocks.
**Solution**: Zone unlocks and restoration are separate "investment" transactions that feel different from "spending" on cosmetics. UI distinction: "Invest" vs "Purchase".

**Identified Risk**: Player focuses only on one zone, doesn't see restoration progress elsewhere.
**Solution**: Passive restoration (0.05% per token earned in zone played) and first-play-of-day bonuses encourage variety.

**Identified Risk**: New player overwhelmed by token sinks, doesn't know what to prioritize.
**Solution**: QWERTY provides gentle guidance: "The Lobby fountain could use some attention..." / "Neon Alley is calling to you!"

### Cross-System Hooks

| Trigger | System A | System B | Effect |
|---------|----------|----------|--------|
| Token earned | Economy | Restoration | +0.05% to zone played |
| Token spent | Economy | Restoration | +0.025% to target zone |
| Zone unlock | Economy | Progression | New quests available |
| Restoration 25% | Restoration | Story | NPC awakens |
| Restoration 50% | Restoration | Story | Deep quests unlock |
| Collection complete | Collections | Economy | 750 token reward (300 final + 450 milestones) |
| Character quest done | Story | Economy | 100-500 token reward |
| Daily challenge done | Daily | Economy | 100 tokens |
| Tournament entry | Weekly | Economy | 50+ tokens |
| First-play bonus | Daily | Economy | 1.5× multiplier per zone |
| 7-day streak | Weekly | Economy | 200 tokens + streak multiplier |

### Exploit Watchlist

| Potential Exploit | Mitigation | Status |
|-------------------|------------|--------|
| Fishing infinite farm | Session cap of 75 tokens, first-catch bypass limited to 3/session | Mitigated |
| Idle game AFK farm | 8-hour offline cap, 100 daily cap, resources uncapped but tokens capped | Mitigated |
| Multi-account tournaments | Account age requirements (7 days) for ranked rewards | Mitigated |
| Consumable stockpiling | Max held limits (2-10), daily purchase limits (1-5) | Mitigated |
| Token sinks exhausted late-game | New Game Plus resets restoration, cosmetics expand with updates | Designed |
| Tower defense endless grinding | Diminishing returns after wave 10, perfect wave bonus rewards skill | Mitigated |
| First-play bonus farming | First-play 1.5× limited to once per zone per day | Designed |
| Score Boost stacking | Max 2 held, 1/day purchase, doesn't stack with other multipliers | Mitigated |
| Zone restoration via passive only | Passive rate (0.05%) is supplementary; direct investment still primary method | Designed |
| Daily soft cap evasion | 500 token daily soft cap affects all gameplay, bonuses exempt but limited | Designed |
