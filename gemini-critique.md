<file name="neocadia-specs/CRITIQUE.md"># Design Critique: Round 2 (The Gloves Are Off)

**Critic**: Lead Design Director (Simulated)
**Date**: 2025-12-12
**Status**: **CRITICAL**

---

## The "Mean" Summary

Neocadia is currently a beautiful corpse. It looks pretty, the prose is purple and evocative, but the **math is broken**, the **core loops contradict the narrative**, and the **scope is lying to itself**. You are building a "cozy" game with "competitive" mechanics and "mobile F2P" restrictions. It doesn't know what it is.

Here are the four highest-leverage hypervectors you need to fix immediately or this game dies on launch.

---

## Hypervector 1: The Economy is Hyper-Inflationary Garbage

**The Problem**: You have designed an economy that solves itself in 4 hours of gameplay.

**The Math**:
- **Passive Restoration**: `systems/economy.md` says "every token earned adds 0.05% to the zone".
- **The Math**: To get 100% restoration (0 to 100), you need `100 / 0.05 = 2000` tokens earned.
- **Earning Rate**: A "Dedicated" player earns 700 tokens/day.
- **Result**: A dedicated player restores a zone fully in **3 days** purely by *accident*, without spending a single token on the actual "Restoration" sink.
- **Consequence**: The "Restoration Spending" mechanic is obsolete. Why spend 5,000 tokens to restore the Lobby when I can just play *Void Breaker* for a week and get it for free?

**The Fix**:
1. **Nuke Passive Restoration**: Change 0.05% to 0.001% or remove it entirely. Make players *choose* to fix the world, don't let it happen as a side effect.
2. **Remove Session Caps**: `minigames/README.md` caps tokens per session (e.g., 100). This is hostile design. If I'm in a flow state in *Synth Racer*, don't punish me. Cap the *rate*, not the *session*.
3. **Endgame Sinks**: Once restoration is 100%, tokens are worthless. You need infinite sinks (consumable buffs, temporary events, prestige) immediately, not in Phase 3.

---

## Hypervector 2: The Ludonarrative Dissonance of "The Static"

**The Problem**: You can't decide if The Static is "Entropy" or "Bowser".

**The Contradiction**:
- `characters/the-static.md`: "Not a villain... can never be destroyed... simply what happens when things are forgotten."
- `minigames/neon-alley/pixel-invaders.md`: "**Boss: Static Queen (HP 2000)**".
- `minigames/clockwork-quarter/tick-defense.md`: "**Enemy: Static Sprite**".

**The Critique**: You are writing poetry about "the gentle fade of memory" and then asking the player to shoot it in the face with a laser. If the Static is inevitable entropy, I shouldn't be able to kill a "Queen" of it.

**The Fix**:
1. **Rename Enemies**: Change "Static Queen" to "Corruption Core" or "Glitch Construct". Make them *symptoms* of the Static, not the Static itself.
2. **Mechanics**: The Static should be an *environmental hazard* (slowing you down, obscuring vision), not an HP bar.

---

## Hypervector 3: The "Eighth Zone" is Vaporware

**The Problem**: `lore.md` teases an "Eighth Zone". `asset-list.md` has zero assets for it.

**The Critique**: This is the "Peter Molyneux" trap. You are teasing a mystery box that is empty. If players hit 100% restoration (which they will, in 3 days, see Hypervector 1) and nothing happens, they will review-bomb you.

**The Fix**:
1. **Cut it or Spec it**: Either delete the reference or spec a "Victory Lap" zone (e.g., The Developer's Terminal) that unlocks. Do not leave it as "Rumors".

---

## Hypervector 4: Input Schizophrenia

**The Problem**: Your accessibility goals conflict with your genre choices.

**The Contradiction**:
- `accessibility.md`: "One-button mode where possible."
- `minigames/neon-alley/pixel-invaders.md`: "A/D to move, Space to shoot, Shift to focus." (3 simultaneous inputs).
- `minigames/neon-alley/synth-racer.md`: "A / S / D hit notes in lanes." (3 spatial inputs).

**The Critique**: A "One-Button Mode" for *Synth Racer* isn't accessibility, it's an auto-player. A one-button *Pixel Invaders* is impossible without fundamentally changing the game (e.g., auto-move?). You are promising accessibility you haven't designed.

**The Fix**:
1. **Spec the Assists**: Don't just say "Simplified Controls". Spec exactly how *Pixel Invaders* works with one button. (e.g., "Ship auto-moves back and forth; press to change direction; auto-shoot always on").

---

## Specific File Nitpicks (The "Mean" Part)

### `systems/economy.md`
> "Passive restoration (0.05% per token earned)"
**CHANGE TO**: `0.005%`. You are off by an order of magnitude.

### `minigames/README.md`
> "Endless escalation"
**CRITIQUE**: Most of your games have "Levels" (Void Breaker 1-20). Only *Wave Rider* is truly endless. Don't promise endless if you built levels.

### `characters/vera.md`
> "Age appearance: Early 20s (frozen in time)"
**CRITIQUE**: She was a lead programmer in 1987. She'd be mid-30s minimum. "Frozen in time" implies she froze *then*. Why is she 20? Did she code herself younger? If so, say that. It adds character (vanity? nostalgia?).

### `zones/05-clockwork-quarter.md`
> "Master tick rate: 120 BPM"
**CRITIQUE**: Have you ever listened to a clock ticking at 120 BPM? That's 2 ticks per second. That is frantic, not "methodical". A grandfather clock is 60 BPM. Slow it down or the zone will feel like a techno rave, not a workshop.

---

## Final Verdict

The "Cozy Melancholy" vibe is strong, but the systems underneath are fighting it. The economy wants me to speed-run, the narrative wants me to cry, and the minigames want me to sweat.

**Align the vectors.** Make the economy slower. Make the Static scarier (mechanically). Make the controls tighter.

**Priority Order:**
1.  **Fix the Economy Math** (`systems/economy.md`) - **IMMEDIATE**
2.  **Reconcile Static Combat** (`characters/the-static.md` vs Minigames) - **HIGH**
3.  **Define Accessibility Implementation** (`systems/accessibility.md`) - **HIGH**
</file>

<file name="neocadia-specs/systems/economy.md"># Economy System

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

#### Session Caps (Soft Caps via Diminishing Returns)
To prevent burnout and maintain balance, token generation slows down after extended play in a single session, rather than hitting a hard wall.

- **Diminishing Returns**:
  - First 30 minutes in a single game: **100% earn rate**
  - 30-60 minutes: **50% earn rate**
  - 60+ minutes: **10% earn rate** (token generation slows to a trickle)
- **Reset**: Timer resets after 1 hour of not playing that specific game.
- **Daily Soft Cap**: After earning 1,000 tokens from gameplay in one day, all gameplay earn rates drop to 25% globally. Bonuses (daily, weekly, quest) are unaffected.

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

**Note**: Tokens spent on restoration are *invested*, not lost. They become part of the world. Restoration also gains passively, but slowly.

**Passive Restoration Math (CRITICAL UPDATE)**:
- Every token earned adds **0.005%** to the zone played in.
- This is a *trace amount* of luminance. Earning 2,000 tokens results in +10% restoration.
- Passive restoration cannot advance a zone beyond its current Tier cap (e.g., cannot go from Flickering to Awakening purely via passive). You *must* pay the token cost to break the tier ceiling.
- **Why?** To prevent grinding from bypassing the investment mechanic.

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
- Zone unlocks total: 5,750 tokens
- Restoration total: 20,600 tokens
- Cosmetics (optional): ~3,000 tokens for decent collection
- **Grand Total to "Complete"**: ~29,350 tokens
- At 175 tokens/day casual: 168 days (~5.5 months)
- At 350 tokens/day regular: 84 days (~3 months)
- At 600 tokens/day dedicated: 49 days (~7 weeks)

This pacing ensures casual players can see credits in 3-4 months while dedicated players reach endgame in under 2 months.

---

## Economy Sinks

### Where Tokens Go
1. **Zone Unlocks** - One-time large purchases
2. **Restoration** - Cumulative investment
3. **Cosmetics** - Optional personalization
4. **Consumables** - Optional helpers

### Preventing Inflation
- **Restoration Tiers**: Require explicit token dumps to advance stages.
- **Endgame Sink**: After 100% restoration, tokens can be spent on "Luminance Festivals" (temporary zone boosts) or "Legacy Status" (prestige ranks).
- **No Trading**: No token trading between players.

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
    tokens_earned_today: number; // For soft cap tracking
  };

  weekly_state: {
    tournament_participated: boolean;
    featured_film_completed: boolean;
  };

  session_state: {
    game_start_time: Record<GameId, number>; // Track diminishing returns
  }

  purchase_history: PurchaseRecord[];
}
```

---

## Tuning Notes

### If Players Progress Too Fast
- Reduce daily bonuses
- Increase restoration costs
- Tighten diminishing returns curve

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

### Cross-System Hooks

| Trigger | System A | System B | Effect |
|---------|----------|----------|--------|
| Token earned | Economy | Restoration | +0.005% to zone played (capped by tier) |
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
| Fishing infinite farm | Soft cap via diminishing returns after 30 mins | Mitigated |
| Idle game AFK farm | 8-hour offline cap, 100 daily cap, resources uncapped but tokens capped | Mitigated |
| Multi-account tournaments | Account age requirements (7 days) for ranked rewards | Mitigated |
| Consumable stockpiling | Max held limits (2-10), daily purchase limits (1-5) | Mitigated |
| Token sinks exhausted late-game | Prestige ranks ("Legacy Status") added as infinite sink | Designed |
| Tower defense endless grinding | Diminishing returns after wave 10, perfect wave bonus rewards skill | Mitigated |
| First-play bonus farming | First-play 1.5× limited to once per zone per day | Designed |
| Zone restoration via passive only | Passive rate slashed to 0.005%; Tier caps require payment | Fixed |
| Daily soft cap evasion | 1000 token daily soft cap affects all gameplay | Designed |
</file>

<file name="neocadia-specs/systems/accessibility.md"># Accessibility System

## Overview

Neocadia should be playable by everyone. Accessibility isn't an afterthought—it's a core design principle. Every player deserves to experience the arcade.

### Guiding Principles
1. **Options, not compromises** - Accessibility settings enhance, never subtract
2. **Clear defaults, easy changes** - Work out of the box, customize when needed
3. **Multiple input methods** - Mouse, keyboard, and touch all supported
4. **No penalty for using assists** - Full game, full achievements, full experience

---

## Accessibility Settings

### Location
- Settings > Accessibility (dedicated section)
- Also prompted on first launch (optional quick setup)

### Visual Settings

| Setting | Options | Default | Description |
|---------|---------|---------|-------------|
| **Text Size** | Normal / Large / Extra Large | Normal | Scales all UI text (125% / 150%) |
| **High Contrast** | On / Off | Off | Solid backgrounds, bolder colors |
| **Colorblind Mode** | None / Deuteranopia / Protanopia / Tritanopia | None | Adjusts palette for color vision |
| **Reduce Motion** | On / Off | Off | Minimizes animations, removes particles |
| **Screen Shake** | On / Off | On | Disables camera shake effects |
| **Flash Effects** | On / Off | On | Reduces/removes flashing |
| **UI Opacity** | 50-100% | 80% | Transparency of HUD elements |
| **Hotspot Highlights** | Auto / Always / Off | Auto | Visibility of clickable areas |

### Audio Settings

| Setting | Options | Default | Description |
|---------|---------|---------|-------------|
| **Master Volume** | 0-100 | 100 | Overall audio level |
| **Music Volume** | 0-100 | 80 | Background music |
| **SFX Volume** | 0-100 | 100 | Sound effects |
| **Voice Volume** | 0-100 | 100 | Character dialogue (future) |
| **Audio Cues** | On / Off | On | Sound indicators for visual events |
| **Mute When Unfocused** | On / Off | On | Silence when tabbed away |

### Gameplay Settings

| Setting | Options | Default | Description |
|---------|---------|---------|-------------|
| **Auto-Fire** | On / Off | Off | Automatic shooting in action games |
| **Extended Timers** | Off / +50% / +100% | Off | More time for timed events |
| **Simplified Controls** | On / Off | Off | Maps complex inputs to single/simple actions |
| **Tutorial Mode** | On / Off | On | In-game guidance (can toggle) |
| **Pause in Menus** | On / Off | On | Game pauses when menu open |
| **Skip Animations** | On / Off | Off | Faster transitions |

### Input Settings

| Setting | Options | Default | Description |
|---------|---------|---------|-------------|
| **Primary Input** | Mouse / Keyboard / Touch | Auto-detect | Preferred control method |
| **Mouse Sensitivity** | 0.5-2.0× | 1.0× | Cursor speed |
| **Click Assistance** | Off / Sticky / Magnetic | Off | Helps with precise clicking |
| **Key Repeat Delay** | 100-500ms | 200ms | Delay before key repeats |
| **Hold Duration** | 100-500ms | 200ms | Required time for "hold" actions |

---

## Simplified Controls Implementation (Per-Game)

When "Simplified Controls" is enabled, minigame mechanics adjust as follows:

| Game | Standard | Simplified |
|------|----------|------------|
| **Pixel Invaders** | A/D Move, Space Shoot, Shift Focus | **Mouse/Touch**: Ship auto-moves to cursor, auto-fires constantly. **Keyboard**: Arrow keys move, auto-fire on. Focus mode toggles instead of hold. |
| **Synth Racer** | 3 Lanes (A/S/D keys) | **One Button**: Press Space/Click anywhere to hit ANY note in ANY lane. Timing still matters, lane selection is auto. |
| **Void Breaker** | Paddle Move + Click Launch | **Auto-Launch**: Ball launches automatically. Paddle magnetizes slightly to ball trajectory. |
| **Reel Deal** | Hold/Release Cast, Rhythm Click Reel | **One Click**: Click once to cast (max power). Auto-hook on bite. Hold mouse to reel (no rhythm clicking). |
| **Tick Defense** | Drag/Drop Turrets | **Tap to Place**: Select turret -> Tap valid slot. Game auto-pauses during placement. |
| **Scene Stealer** | Directional Arrows + Action Keys | **Single Key**: Press ANY key when prompt hits marker. Direction doesn't matter, only timing. |

---

## Visual Accessibility Details

### High Contrast Mode

**What changes**:
- HUD backgrounds: Transparent → Solid dark
- Text: Soft glow → Bold outline
- Buttons: Gradient → Solid colors with borders
- Interactive elements: Subtle glow → Strong outline

**Zone palettes in high contrast**:
| Zone | Standard | High Contrast |
|------|----------|---------------|
| Lobby | Warm gold | Bright yellow on black |
| Neon Alley | Soft neon | Bold magenta/cyan |
| Pixel Beach | Soft pastels | Strong blue/yellow |
| Glitch Garden | Shifting colors | Stable magenta/green |
| Starlight Cinema | Deep purples | Purple/gold borders |
| Clockwork Quarter | Warm brass | Orange/brown outlines |
| Sugar Rush | Soft pinks | Bright pink/white |

### Colorblind Modes

**Deuteranopia (red-green, most common)**:
- Red → Orange/yellow
- Green → Blue/cyan
- Enemy indicators use shape + color

**Protanopia (red-blind)**:
- Similar to deuteranopia adjustments
- Enhanced brightness for former-red elements

**Tritanopia (blue-yellow)**:
- Blue → Cyan/green
- Yellow → Pink/magenta

**Universal design rule**: Never rely on color alone. All important information has shape, icon, or text backup.

### Reduce Motion Mode

**What changes**:
- Scene transitions: Animated → Instant fade
- Particle effects: Full → Minimal or none
- Character animations: Full → Key frames only
- Background animations: Moving → Static
- Screen shake: Disabled
- Bobbing/floating: Disabled

**What stays**:
- Essential gameplay feedback
- Progress indicators
- UI state changes (still visible, just faster)

### Text Scaling

**Normal (100%)**:
- Body: 14px
- Headers: 18-24px
- HUD: 12-14px

**Large (125%)**:
- Body: 17px
- Headers: 22-30px
- HUD: 15-17px
- UI reflows as needed

**Extra Large (150%)**:
- Body: 21px
- Headers: 27-36px
- HUD: 18-21px
- Some UI elements simplify to fit

---

## Audio Accessibility Details

### Audio Cues

Visual events that get audio equivalents:
| Visual Event | Audio Cue |
|--------------|-----------|
| Hotspot available | Soft chime when cursor nears |
| New notification | Bell tone |
| Quest progress | Rising note |
| Token earned | Coin clink |
| Error/invalid action | Low buzz |
| Timer warning | Ticking accelerates |
| Success | Triumphant chord |
| Failure | Descending tones |

### Subtitles & Captions

All dialogue has text display (default: ON).

Caption options:
- **Speaker labels**: "QWERTY: Hello!"
- **Background sounds**: [Keys clacking]
- **Music cues**: [Tense music begins]
- **Caption size**: Scales with text size setting

---

## Input Accessibility Details

### Keyboard Navigation

Full keyboard control is possible throughout the game:

**Universal Keys**:
| Key | Action |
|-----|--------|
| Tab | Cycle through interactive elements |
| Enter/Space | Activate focused element |
| Escape | Back/Close/Pause |
| Arrow keys | Navigate within menus |
| H | Open help |
| M | Toggle mute |
| F11 | Toggle fullscreen |

**Minigame Keys**:
Each minigame has documented keyboard alternatives (see individual specs).

### Click Assistance

**Sticky Clicking**:
- Click to select, click again to confirm
- Reduces need for precision
- Helpful for motor difficulties

**Magnetic Targeting**:
- Cursor "snaps" slightly toward clickable elements
- Subtle assistance, doesn't override player intent
- Adjustable strength

---

## Screen Reader Support

### ARIA Implementation

All interactive elements include:
- `aria-label`: Descriptive name
- `aria-describedby`: Detailed description when needed
- `aria-live`: Announcements for state changes
- `role`: Proper element identification

### Navigation Announcements

Screen readers hear:
- Current location: "The Lobby. Token Fountain, Registry Desk, Hall of Champions, 6 Zone Doors"
- Focus changes: "Token Fountain, sparkle available"
- State changes: "Tokens: 1,234. Increased by 50"
- Actions: "Door to Pixel Beach. Press Enter to travel"

### Game Compatibility

| Game Type | Screen Reader Experience |
|-----------|-------------------------|
| Exploration | Full audio description of areas |
| Dialogue | Complete text access |
| Trivia | Questions read aloud |
| Action | Limited (primarily visual) |
| Puzzle | Depends on puzzle type |

**Honest limitation**: Some minigames are inherently visual. We provide audio cues where possible but acknowledge limits.

---

## Testing & Compliance

### Testing Checklist

- [ ] All features keyboard-accessible
- [ ] All text scales properly
- [ ] Colorblind modes tested with simulators
- [ ] Screen reader tested with NVDA/VoiceOver
- [ ] No flashing >3Hz (seizure safety)
- [ ] All audio has visual alternative
- [ ] All visual feedback has audio alternative
- [ ] Touch targets minimum 44px
- [ ] Focus indicators visible
- [ ] Motion can be disabled

### WCAG 2.1 Targets

**Level AA compliance** for all UI elements:
- 4.5:1 contrast ratio for normal text
- 3:1 for large text and UI components
- Focus visible
- Resize to 200% without loss
- Consistent navigation
- Error identification

---

## Implementation Notes

### Settings Persistence
```typescript
interface AccessibilitySettings {
  visual: {
    text_size: 'normal' | 'large' | 'extra_large';
    high_contrast: boolean;
    colorblind_mode: ColorblindMode | null;
    reduce_motion: boolean;
    screen_shake: boolean;
    flash_effects: boolean;
    ui_opacity: number;
    hotspot_highlights: 'auto' | 'always' | 'off';
  };
  audio: {
    master_volume: number;
    music_volume: number;
    sfx_volume: number;
    audio_cues: boolean;
    mute_unfocused: boolean;
  };
  gameplay: {
    auto_fire: boolean;
    extended_timers: 'off' | '50' | '100';
    simplified_controls: boolean;
    tutorials_enabled: boolean;
  };
  input: {
    primary_input: 'mouse' | 'keyboard' | 'touch' | 'auto';
    mouse_sensitivity: number;
    click_assistance: 'off' | 'sticky' | 'magnetic';
    key_repeat_delay: number;
    hold_duration: number;
  };
}
```

### CSS Custom Properties

Accessibility-affected values use CSS variables:
```css
:root {
  --text-scale: 1;
  --motion-reduce: 0;
  --contrast-boost: 0;
  --ui-opacity: 0.8;
}

.high-contrast {
  --contrast-boost: 1;
  --ui-opacity: 1;
}

.reduce-motion {
  --motion-reduce: 1;
}
```

### Testing Tools

- Color contrast: Stark / Colour Contrast Analyser
- Colorblind simulation: Sim Daltonism / Color Oracle
- Screen reader: NVDA (Windows) / VoiceOver (Mac)
- Keyboard testing: Unplug mouse, use Tab
- Motion sensitivity: User testing with vestibular disorders
</file>
