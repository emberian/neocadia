# Save System

## Overview

The save system preserves everything meaningful about a player's experience in Neocadia. It must be reliable, efficient, and support both local and cloud storage.

### Core Principles
1. **Never lose progress** - Save frequently, redundantly
2. **Minimal data** - Only store what's needed
3. **Fast loads** - Optimize for quick startup
4. **Cross-device** - Cloud sync when available

---

## Save Data Structure

### Master Save Object

```typescript
interface NeocadiaSave {
  // Metadata
  version: string;           // Save format version
  created_at: Date;
  updated_at: Date;
  playtime_seconds: number;
  session_count: number;

  // Core Systems
  economy: EconomyState;
  progression: ProgressionState;
  story: StoryState;

  // Per-Zone State
  zones: Record<ZoneId, ZoneState>;

  // Collections
  collections: CollectionsState;

  // Minigames
  minigames: MinigameState;

  // Player Customization
  player: PlayerState;

  // Settings (can also be separate)
  settings: SettingsState;
}
```

### Economy State

```typescript
interface EconomyState {
  tokens: number;
  tokens_earned_total: number;
  tokens_spent_total: number;

  daily: {
    date: string;  // ISO date for reset tracking
    login_claimed: boolean;
    fountain_spun: boolean;
    lost_found_claimed: boolean;
    challenge_completed: boolean;
    first_plays: ZoneId[];
  };

  weekly: {
    week_start: string;
    tournament_participated: boolean;
    featured_film_done: boolean;
  };
}
```

### Progression State

```typescript
interface ProgressionState {
  restoration: {
    overall_percent: number;
    zones: Record<ZoneId, number>;
  };

  unlocked_zones: ZoneId[];
  achievements: AchievementId[];

  milestones: {
    first_restoration: boolean;
    fifty_percent: boolean;
    all_zones_thriving: boolean;
    hundred_percent: boolean;
  };
}
```

### Story State

```typescript
interface StoryState {
  act: 1 | 2 | 3 | 4;
  prologue_complete: boolean;

  character_quests: Record<CharacterId, {
    current_quest: number;  // 0-5
    quest_states: QuestStepState[];
  }>;

  main_story_flags: string[];  // Flexible flag system
  choices: Choice[];
  ending: 'A' | 'B' | 'C' | null;

  dialogue_seen: string[];  // For skipping repeat dialogue
}
```

### Zone State

```typescript
interface ZoneState {
  restoration_percent: number;
  stage: 'flickering' | 'awakening' | 'thriving' | 'radiant';

  visited: boolean;
  first_visit_date: string | null;

  interactables: Record<string, boolean>;  // Which things have been clicked
  collectibles_found: string[];
  secrets_discovered: string[];
}
```

### Collections State

```typescript
interface CollectionsState {
  fish: {
    caught: Record<FishId, FishCatchData>;
    total_caught: number;
    largest_catch: { fish: FishId; size: number } | null;
  };

  film_reels: ReelId[];

  glitch_samples: GlitchSampleId[];

  blueprints: BlueprintId[];

  recipes: {
    collected: RecipeId[];
    ingredients: Record<IngredientId, number>;
  };
}
```

### Minigame State

```typescript
interface MinigameState {
  high_scores: Record<MinigameId, number>;
  play_counts: Record<MinigameId, number>;
  best_runs: Record<MinigameId, BestRunData>;

  // Specific minigame persistent data
  error_garden: ErrorGardenState;  // Idle game state
  // etc.
}
```

### Player State

```typescript
interface PlayerState {
  name: string | null;
  avatar: {
    body_type: number;
    skin_tone: string;
    hair_style: number;
    hair_color: string;
    // etc.
  };

  cosmetics: {
    owned: CosmeticId[];
    equipped: {
      outfit: CosmeticId | null;
      accessory_head: CosmeticId | null;
      accessory_hand: CosmeticId | null;
      aura: CosmeticId | null;
    };
  };

  cabinet: {
    decal: CosmeticId | null;
    interior_items: CosmeticId[];
    trophies: TrophyId[];
  };

  titles: {
    owned: TitleId[];
    equipped: TitleId | null;
  };
}
```

### Settings State

```typescript
interface SettingsState {
  audio: {
    master_volume: number;    // 0-100
    music_volume: number;
    sfx_volume: number;
    mute_when_unfocused: boolean;
  };

  display: {
    fullscreen: boolean;
    resolution: string;
    quality: 'low' | 'medium' | 'high';
    show_fps: boolean;
  };

  gameplay: {
    auto_fire: boolean;       // For relevant games
    show_tutorials: boolean;
    colorblind_mode: boolean;
    screen_shake: boolean;
  };

  accessibility: {
    reduce_motion: boolean;
    high_contrast: boolean;
    text_size: number;
  };
}
```

---

## Save Triggers

### Automatic Saves
- After every minigame completion
- After token transaction
- After dialogue completion
- After collectible found
- On zone change
- Every 60 seconds during active play
- On window close/unfocus

### Save Indicator
- Small icon appears briefly on save
- Never interrupts gameplay
- Shows error state if save fails

---

## Storage Backends

### Local Storage (Primary)

```typescript
const SAVE_KEY = 'neocadia_save';
const BACKUP_KEY = 'neocadia_save_backup';

function saveLocal(data: NeocadiaSave): void {
  // Keep previous save as backup
  const current = localStorage.getItem(SAVE_KEY);
  if (current) {
    localStorage.setItem(BACKUP_KEY, current);
  }

  localStorage.setItem(SAVE_KEY, JSON.stringify(data));
}

function loadLocal(): NeocadiaSave | null {
  const saved = localStorage.getItem(SAVE_KEY);
  if (!saved) return null;

  try {
    return JSON.parse(saved);
  } catch {
    // Try backup
    const backup = localStorage.getItem(BACKUP_KEY);
    if (backup) {
      return JSON.parse(backup);
    }
    return null;
  }
}
```

### IndexedDB (Large Data)

For data that exceeds localStorage limits:
- Collection images
- Replay data
- Large state objects

### Cloud Sync (Future)

```typescript
interface CloudSyncConfig {
  enabled: boolean;
  provider: 'firebase' | 'custom' | null;
  last_sync: Date | null;
  conflict_resolution: 'local' | 'cloud' | 'newest';
}

async function syncToCloud(data: NeocadiaSave): Promise<void> {
  // Compare timestamps
  // Upload if local is newer
  // Handle conflicts
}

async function syncFromCloud(): Promise<NeocadiaSave | null> {
  // Download if cloud is newer
  // Merge if needed
}
```

---

## Version Migration

When save format changes:

```typescript
const CURRENT_VERSION = '1.0.0';

function migrateSave(oldSave: unknown): NeocadiaSave {
  const version = (oldSave as any).version || '0.0.0';

  let data = oldSave as any;

  // Apply migrations in order
  if (semver.lt(version, '0.1.0')) {
    data = migrate_0_0_to_0_1(data);
  }
  if (semver.lt(version, '1.0.0')) {
    data = migrate_0_1_to_1_0(data);
  }

  data.version = CURRENT_VERSION;
  return data as NeocadiaSave;
}
```

---

## Error Handling

### Save Failures
1. Retry 3 times
2. If still failing, alert user
3. Offer export option
4. Continue play (queue saves)

### Corrupted Saves
1. Try backup
2. If backup fails, offer partial recovery
3. Last resort: fresh start with apology bonus

### Recovery Features
- Manual export/import (JSON)
- Support code for recovery assistance
- Automatic backup rotation (keep last 3)

---

## Performance

### Save Size Targets
- Initial save: < 10KB
- Full completion: < 100KB
- Compression optional for cloud

### Load Times
- Target: < 100ms for local load
- Show loading state if > 200ms

### Optimization
- Only save changed data (diff-based)
- Batch rapid changes
- Compress collections (ID lists, not full objects)

---

## Privacy

### Data Collection
- No personal data stored in save
- Player name is local only
- No tracking or analytics in save

### Export
- Players can export full save
- Human-readable JSON
- Can import on any device
