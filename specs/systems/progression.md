# Progression System

## Overview

Progression in Neocadia operates on multiple tracks simultaneously. Players always have something to work toward, and each track reinforces the others.

### Core Tracks
1. **Restoration** - Bringing the arcade back to life
2. **Story** - Uncovering narrative and making choices
3. **Collections** - Gathering items and achievements
4. **Personal** - Avatar and cabinet customization

---

## Track 1: Restoration

### The Central Metric
Restoration is the heartbeat of progression. Everything feeds into it:
- Spending tokens
- Completing quests
- Playing games

### Overall Restoration %
```
overall_restoration = weighted_average(
  lobby_restoration × 1.5,
  neon_alley_restoration × 1.0,
  pixel_beach_restoration × 1.0,
  glitch_garden_restoration × 1.0,
  starlight_cinema_restoration × 1.0,
  clockwork_quarter × 1.0,
  sugar_rush_restoration × 1.0
)
```

### Per-Zone Restoration Stages

Each zone has 4 stages:

| Stage | % Range | Visual State | Gameplay |
|-------|---------|--------------|----------|
| Flickering | 0-25% | Dim, damaged | Limited |
| Awakening | 25-50% | Functional | Normal |
| Thriving | 50-85% | Vibrant | Full + bonuses |
| Radiant | 85-100% | Spectacular | Special content |

### Restoration Triggers

**Automatic (from play)**:
- Every token earned adds 0.01% to zone played in
- Quest completion adds 0.5-2%

**Investment (spending tokens)**:
- Direct restoration purchases
- Each token spent adds 0.005% to target zone

### Visible Progress

Players see:
- Overall % in HUD
- Zone-specific % when in zone
- Visual changes as % increases
- Next milestone indicator

---

## Track 2: Story Progression

### Main Story

Gated by restoration milestones:

| Milestone | Restoration | Content Unlocked |
|-----------|-------------|------------------|
| Prologue | 0% | First login, meet QWERTY |
| Act 1 | 25% | All NPCs awakened |
| Act 2 | 50% | Deep NPC quests available |
| Act 3 | 75% | Glitch Garden secrets |
| Act 4 | 90% | Final choice available |

### Character Quests

Each character has 5 quests:

```
Quest 1: Available at NPC awakening (25% zone restoration)
Quest 2: Available after Quest 1 + time/progress
Quest 3: Available after Quest 2 + time/progress
Quest 4: Available after Quest 3 + main story progress
Quest 5: Available after Quest 4 + near-full restoration
```

### Quest Flow Example (QWERTY)
1. "Boot Sequence" - Find code (zone 25%)
2. "Memory Allocation" - Debug memories (zone 40%)
3. "Key Recovery" - Find keys across zones (zone 60%)
4. "First Memory" - Witness cutscene (zone 80%)
5. "The Question" - Make choice (zone 95%)

### Choice Tracking

```typescript
interface StoryState {
  main_act: 1 | 2 | 3 | 4;
  character_quests: Record<CharacterId, QuestProgress>;
  choices_made: Choice[];
  ending_path: 'A' | 'B' | 'C' | null;
}
```

---

## Track 3: Collections

### Collection Types

| Collection | Zone | Items | Completion Reward |
|------------|------|-------|-------------------|
| Fish | Pixel Beach | 50 | Title + Cabinet Trophy |
| Film Reels | Starlight Cinema | 7 (story) + 20 (bonus) | Title + CELIA cutscene |
| Glitch Samples | Glitch Garden | 30 | Title + Cosmetic effect |
| Blueprints | Clockwork Quarter | 15 | Title + Automaton pet |
| Recipes | Sugar Rush | 25 | Title + SUCRE transformation |
| High Scores | Neon Alley | Personal bests | Hall of Champions entry |

### Achievement System

Categories:
- **Milestones**: Restoration %, story progress
- **Mastery**: Game-specific accomplishments
- **Discovery**: Hidden content found
- **Social**: Community participation
- **Dedication**: Long-term engagement

Achievement Rewards:
- Tokens (50-500)
- Titles
- Cosmetics
- Cabinet decorations

### Display

Collections viewable in:
- Player's Cabinet (personal museum)
- Zone-specific NPCs (PIXEL shows fish, etc.)
- Achievement log

---

## Track 4: Personalization

### Avatar Progression

**Starting State**:
- Basic body options
- Limited colors
- No accessories

**Unlocks From**:
- Zone restoration (themed outfits)
- Story progress (narrative costumes)
- Achievements (special items)
- Direct purchase (general cosmetics)

### Cabinet Progression

**Starting State**:
- Basic cabinet shell
- Empty interior

**Unlocks**:
- Decals (purchase or earn)
- Interior items (achievements, collections)
- Trophies (completion rewards)
- Ambient effects (special achievements)

### Progression Philosophy

Cosmetics are:
- Earned through play (majority)
- Purchasable with tokens (never real money)
- Indicative of accomplishments
- Never gameplay-affecting

---

## Milestone Rewards

Major milestones come with celebration:

### Restoration Milestones
| Milestone | Reward |
|-----------|--------|
| First zone Awakening | Title: "First Light" |
| 50% overall | Cosmetic: Luminance Aura |
| All zones Thriving | Title: "Restorer" |
| 100% overall | Title: "Savior of Neocadia" |

### Story Milestones
| Milestone | Reward |
|-----------|--------|
| Complete Act 1 | Cosmetic: QWERTY Companion |
| Complete all character Quest 1s | Title: "Friend to All" |
| Reach Act 4 | Cosmetic: The Choice (glowing effect) |
| Complete game (any ending) | Exclusive ending-specific cosmetic |

### Collection Milestones
| Milestone | Reward |
|-----------|--------|
| Complete any collection | Cabinet Trophy |
| Complete 3 collections | Title: "Collector" |
| Complete all collections | Title: "Completionist", Unique aura |

---

## New Game Plus

After completing the game (any ending):

### What Carries Over
- All cosmetics and titles
- Collection progress
- Achievement progress
- High scores

### What Resets (Optionally)
- Story state (can replay)
- Token count (fresh start)
- Restoration % (can re-experience)

### NG+ Exclusive
- Harder game variants
- Developer commentary mode
- Hidden dialogue options
- Alternate cosmetics

---

## Data Structure

```typescript
interface ProgressionState {
  restoration: {
    overall: number;
    zones: Record<ZoneId, number>;
  };

  story: {
    main_act: number;
    quests: Record<QuestId, QuestState>;
    choices: Choice[];
    ending: EndingType | null;
  };

  collections: {
    fish: CollectionProgress;
    reels: CollectionProgress;
    glitches: CollectionProgress;
    blueprints: CollectionProgress;
    recipes: CollectionProgress;
  };

  achievements: AchievementId[];

  cosmetics: {
    owned: CosmeticId[];
    equipped: EquippedCosmetics;
  };

  cabinet: CabinetState;

  playtime: {
    total_seconds: number;
    sessions: number;
    first_played: Date;
    last_played: Date;
  };
}
```

---

## Progression UX

### Visual Feedback
- Progress bars are always visible
- Milestones clearly marked
- Celebration on achievement
- "Next reward" indicator

### Never Feel Lost
- QWERTY can always suggest next goals
- Quest log shows available quests
- Collection UI shows missing items (vague hints)

### Pacing
- Early game: Rapid unlocks, frequent rewards
- Mid game: Steady progress, story engagement
- Late game: Long-term goals, mastery focus
- Post-game: Completion, collection, replay
