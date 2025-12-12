# Collections System

## Overview

Collections give players long-term goals beyond story progression. Each collection tells its own micro-story, rewards curiosity, and provides satisfying completion.

---

## Collection Types

### 1. Fish Collection (Pixel Beach)
**Total**: 50 species
**Source**: Reel Deal minigame

**Categories**:
| Category | Count | Difficulty |
|----------|-------|------------|
| Shore Fish | 15 | Common |
| Mid Fish | 20 | Mixed |
| Deep Fish | 15 | Rare-heavy |

**Fish Data**:
```typescript
interface FishCatchData {
  fish_id: FishId;
  caught: boolean;
  first_caught: Date | null;
  times_caught: number;
  largest_size: number;  // 1-200 scale
  smallest_size: number;
}
```

**Display**: Aquarium in Pixel Beach Shack

**Completion Reward**:
- Title: "Master Angler"
- Cabinet Trophy: Golden Fish
- 500 tokens

---

### 2. Film Reels (Starlight Cinema)
**Total**: 27 reels (7 story + 20 bonus)
**Source**: Exploration, quests, achievements

**Categories**:
| Category | Count | Source |
|----------|-------|--------|
| Story Reels | 7 | CELIA's quest |
| Genre Reels | 12 | Hidden in zones |
| Rare Reels | 8 | Achievements |

**Reel Data**:
```typescript
interface ReelData {
  reel_id: ReelId;
  title: string;
  genre: 'action' | 'romance' | 'comedy' | 'drama' | 'horror' | 'musical';
  collected: boolean;
  location_hint: string;
  clip_url: string;  // Viewable once collected
}
```

**Display**: Film Archives in Starlight Cinema

**Completion Reward**:
- Title: "Film Historian"
- Cabinet Trophy: Golden Reel
- Watch CELIA's complete masterpiece

---

### 3. Glitch Samples (Glitch Garden)
**Total**: 30 samples
**Source**: Exploration, games, VERA's quest

**Categories**:
| Category | Count | Visual |
|----------|-------|--------|
| Color Glitches | 10 | Hue shifts |
| Form Glitches | 10 | Shape corruptions |
| Logic Glitches | 10 | Rule breaks |

**Glitch Data**:
```typescript
interface GlitchSample {
  glitch_id: GlitchId;
  name: string;
  category: 'color' | 'form' | 'logic';
  collected: boolean;
  effect_applicable: boolean;  // Can apply as cosmetic
  lore_text: string;
}
```

**Display**: VERA's Willow (floating around)

**Special**: Some glitches can be applied as cosmetic effects

**Completion Reward**:
- Title: "Error Collector"
- Cabinet Trophy: Contained Glitch
- Unlock all glitch cosmetic effects

---

### 4. Blueprints (Clockwork Quarter)
**Total**: 15 blueprints
**Source**: Quests, puzzles, exploration

**Categories**:
| Category | Count | Unlocks |
|----------|-------|---------|
| Automaton Parts | 5 | Pet pieces |
| Machine Designs | 5 | Lore |
| Secret Plans | 5 | Special content |

**Blueprint Data**:
```typescript
interface Blueprint {
  blueprint_id: BlueprintId;
  name: string;
  schematic_image: string;
  collected: boolean;
  associated_lore: string;
  unlocks: UnlockId | null;
}
```

**Display**: COG's Workshop boards

**Special**: Completing automaton blueprints = buildable clockwork pet

**Completion Reward**:
- Title: "Master Engineer"
- Cabinet Trophy: Miniature Engine
- Fully customizable clockwork companion

---

### 5. Recipes (Sugar Rush Boulevard)
**Total**: 25 recipes
**Source**: SUCRE's quest, exploration, Kitchen game

**Categories**:
| Category | Count | Effect |
|----------|-------|--------|
| Basic Recipes | 10 | Kitchen game content |
| Fancy Recipes | 10 | Kitchen game content |
| Secret Recipes | 5 | SUCRE transformations |

**Recipe Data**:
```typescript
interface Recipe {
  recipe_id: RecipeId;
  name: string;
  ingredients: IngredientId[];
  collected: boolean;
  available_in_kitchen: boolean;
  sucre_transformation: TransformId | null;
}
```

**Display**: Recipe Board in Grand Bakery

**Special**: Secret recipes transform SUCRE's appearance

**Completion Reward**:
- Title: "Confection Master"
- Cabinet Trophy: Golden Whisk
- Choose SUCRE's final form

---

### 6. Achievements
**Total**: 100+ achievements
**Source**: Everything

**Categories**:
| Category | Examples |
|----------|----------|
| Progress | Restoration milestones, story completion |
| Mastery | High scores, perfect runs |
| Discovery | Hidden content, secrets |
| Dedication | Playtime, streaks |
| Collection | Completing other collections |

**Achievement Data**:
```typescript
interface Achievement {
  achievement_id: AchievementId;
  name: string;
  description: string;
  category: AchievementCategory;
  unlocked: boolean;
  unlocked_date: Date | null;
  reward_tokens: number;
  reward_cosmetic: CosmeticId | null;
  hidden: boolean;  // Hidden until unlocked
}
```

**Display**: Achievement Log (accessible anywhere)

---

## Collection UI

### Overview Screen
- All collections visible
- Completion percentage per collection
- Quick view of recent acquisitions
- Links to detailed views

### Detailed View
- Grid/list of items
- Collected: Full display
- Not collected: Silhouette + hint
- Sorting options

### Hints System
- Vague hints for uncollected items
- More specific hints after 80% completion
- No exact locations (preserve discovery)

---

## Integration

### With Zones
- Each zone has primary collection
- Collection progress visible in zone
- NPCs comment on collection progress

### With Story
- Some collectibles tied to quests
- Completing collections unlocks dialogue
- Collections reveal lore

### With Economy
- Collectibles have token values (when found)
- Milestones award bonuses
- Completion awards significant tokens

---

## Collection Progress Tracking

```typescript
interface CollectionProgress {
  total_items: number;
  collected_items: number;
  completion_percentage: number;
  completion_reward_claimed: boolean;
  milestone_rewards_claimed: number[];  // 25%, 50%, 75%
}
```

### Milestones
| Percentage | Reward |
|------------|--------|
| 25% | 100 tokens |
| 50% | 250 tokens + cosmetic |
| 75% | 400 tokens |
| 100% | 500 tokens + title + trophy |

---

## Discovery Philosophy

### Make It Feel Good
- Every find is celebrated
- Visual + audio feedback
- "New!" indicator persists until viewed
- Log of recent discoveries

### Don't Make It Frustrating
- No permanently missable items
- Hints available after effort
- No real-money shortcuts
- Reasonable completion time

### Tell Stories
- Each item has description
- Items connect to characters
- Collections form narratives
- Completion reveals something
