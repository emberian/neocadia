# Onboarding & Tutorial System

## Overview

First impressions define the experience. A new player should understand Neocadia's core loop within 2 minutes and feel comfortable exploring independently within 5 minutes.

### Design Philosophy
- **Show, don't tell** - Actions teach better than text walls
- **Respect player intelligence** - Assume competence, don't over-explain
- **Allow skipping** - Veterans shouldn't be forced through basics
- **Contextual over front-loaded** - Teach mechanics when they become relevant

---

## First-Time User Experience (FTUE)

### The First 2 Minutes

#### 0:00 - Title Screen
- "New Game" only option for new players
- Simple, inviting, not overwhelming

#### 0:05 - The Flicker
> *Screen static. Brief glimpse of a vast, dim space. Then darkness.*

Player sees the arcade trying to exist. This creates curiosity, not confusion.

#### 0:15 - QWERTY Arrives
```
QWERTY: "OH! You're ACTUALLY here!"
[Keys clatter excitedly]
QWERTY: "I'm QWERTY. Welcome to Neocadia."
```

**What player learns**: They're welcome. Someone is happy to see them.

#### 0:30 - The Lobby Reveal
Camera pulls back to show the Lobby. QWERTY hovers near the player position.

**Visual teaching moment**:
- Dry fountain (clearly something is wrong)
- Dark doors (locked content)
- One glowing door (where to go)
- QWERTY's station (help is available)

#### 0:45 - First Interaction Prompt
```
QWERTY: "This is the Lobby. Click around - see what you find."
```

**Hotspot highlights appear briefly** on:
- Token Fountain (sparkle)
- QWERTY's station (glow)
- The one lit door (Pixel Beach)

Player is free to click anything. No wrong moves.

#### 1:00 - First Click Response
Whatever the player clicks, QWERTY responds contextually:

| Click | Response |
|-------|----------|
| Fountain | "The fountain... it used to flow. Maybe it will again." |
| QWERTY | "That's me! Click anytime you need help." |
| Lit Door | "That's Pixel Beach. The only zone still awake." |
| Dark Door | "That door's sleeping. We'll wake it up together." |
| Random Space | "Good exploring instinct! Everything here can be clicked." |

#### 1:30 - The Gentle Push
```
QWERTY: "Want to see what's still working? Pixel Beach is through that door."
[Arrow indicator appears on Pixel Beach door]
```

Player clicks the door. Transition plays.

#### 2:00 - Pixel Beach Introduction
Player arrives at Pixel Beach. PIXEL is present.

```
PIXEL: "...hey. new face."
PIXEL: "welcome to the beach. it's... quiet here."
PIXEL: "try the pier. fishing helps."
```

**Arrow indicator** points to the pier (Reel Deal minigame).

---

### The First 5 Minutes (continued)

#### 2:30 - First Minigame Tutorial

When player clicks the fishing station:

**Pre-Game Screen** (all minigames have this):
```
┌─────────────────────────────────────────────┐
│              REEL DEAL                       │
│           "Cast, wait, catch."              │
│                                              │
│  HOW TO PLAY:                               │
│  [Mouse icon] Click & hold to cast          │
│  [Mouse icon] Click when bobber dips        │
│  [Mouse icon] Click rhythm to reel in       │
│                                              │
│  [Skip Tutorial]      [Let's Fish!]         │
└─────────────────────────────────────────────┘
```

**First-time only**: Tutorial mode is ON by default.

#### 3:00 - In-Game Tutorial (Reel Deal example)

**Step 1: Casting**
- Overlay: "Hold to charge, release to cast"
- Power meter highlighted
- Player cannot fail (any cast works)
- Success: "Nice cast!"

**Step 2: Waiting**
- Overlay: "Watch the bobber..."
- Bobber is highlighted
- Wait time shortened for tutorial (5s max)
- When bite occurs: "NOW! Click!"

**Step 3: Hooking**
- Overlay: "Click when you see the dip!"
- Generous timing (2x normal window)
- Success: "Got it!"

**Step 4: Reeling**
- Overlay: "Click to reel. Match the rhythm!"
- Visual rhythm indicator shown
- Fish has 50% normal stamina
- Success: "You caught a fish!"

**Tutorial Complete**:
```
┌─────────────────────────────────────────────┐
│         YOU CAUGHT A PIXEL MINNOW!          │
│                                              │
│  That's the basics! You can:                │
│  - Keep fishing (collection + tokens)       │
│  - Explore other games                      │
│  - Return to the Lobby                      │
│                                              │
│  [Back]                 [Continue Fishing]  │
└─────────────────────────────────────────────┘
```

#### 4:00 - First Token Reward
Player earns their first tokens. HUD animates.

```
QWERTY (via thought bubble): "+25 tokens! These restore the arcade."
```

Brief, non-intrusive, dismisses automatically.

#### 5:00 - Freedom
Tutorial flags are set. Player is now in "normal" mode:
- Full timing windows
- No overlays unless requested
- QWERTY available but not intrusive

---

## Contextual Tutorials

### When They Appear
Tutorials trigger on **first encounter** with any of these:

| Trigger | Tutorial Content |
|---------|------------------|
| First visit to new zone | Brief zone introduction |
| First minigame launch | Game-specific controls |
| First token spend | Restoration explanation |
| First collection item | Collection system intro |
| First quest available | Quest log introduction |
| First NPC quest dialogue | Quest acceptance flow |

### Format
All contextual tutorials follow this pattern:

1. **Notice** - Subtle indicator (QWERTY icon, sparkle)
2. **Optional expansion** - Click to see more
3. **Short explanation** - 2-3 sentences max
4. **Dismiss** - "Got it" or auto-dismiss after 5s

### Example: First Zone Unlock

When player has enough tokens to unlock Neon Alley:
```
[QWERTY icon pulses near Neon Alley door]

Click to expand:
"You have 500 tokens! That's enough to wake up Neon Alley.
Click the door and choose 'Unlock' to open it."

[Got it!]
```

---

## Skip & Replay Options

### Skipping Tutorials

**Global setting**: Settings > Gameplay > Show Tutorials (On/Off)

**Per-tutorial skip**: Every tutorial overlay has a subtle "Skip" button

**Skip confirmation** (first time only):
```
"Skip tutorials? You can always access help from QWERTY."
[Cancel] [Skip All] [Skip This One]
```

### Replaying Tutorials

**From QWERTY**:
```
Player: "How do I play [game name]?"
QWERTY: "Want me to walk you through it again?"
[Yes, show tutorial] [No, just remind me]
```

**From Pause Menu**:
Pause > How to Play > [Current Game Tutorial]

**From Settings**:
Settings > Gameplay > Reset Tutorial Progress

---

## Tutorial State Tracking

### Per-Player Flags
```typescript
interface TutorialState {
  // Core tutorials
  ftue_complete: boolean;
  lobby_intro_seen: boolean;
  first_zone_visited: boolean;
  first_minigame_played: boolean;
  first_tokens_earned: boolean;
  first_restoration_done: boolean;

  // Per-zone tutorials
  zone_intros: Record<ZoneId, boolean>;

  // Per-game tutorials
  game_tutorials: Record<GameId, boolean>;

  // System tutorials
  collection_intro_seen: boolean;
  quest_intro_seen: boolean;
  leaderboard_intro_seen: boolean;

  // Settings
  tutorials_enabled: boolean;
}
```

### Tutorial Gating
- Never show two tutorials simultaneously
- Queue tutorials if multiple triggers occur
- Minimum 30s between tutorial prompts
- Never interrupt active gameplay

---

## "Help Me" System

### QWERTY On-Demand Help

**Trigger**: Click QWERTY in HUD, press H, or click "?" icon

**Context-Aware Responses**:

| Location | Help Content |
|----------|--------------|
| Lobby | "This is home base. Doors lead to zones. Fountain tracks restoration." |
| Zone main | Zone-specific overview + game list |
| In minigame | Control reminder + current objective |
| In dialogue | "Click to advance. Choices are highlighted." |
| In menu | "Navigate with clicks or keyboard arrows." |

### Help Menu Structure
```
Help (from Pause menu)
├── Getting Started (FTUE recap)
├── Controls
│   ├── Navigation
│   ├── Current Game
│   └── Accessibility
├── Game Guides
│   ├── [Per-zone game list]
│   └── [Each game's how-to-play]
├── Economy
│   ├── Earning Tokens
│   └── Spending Tokens
├── Story
│   └── Recap So Far
└── Ask QWERTY
    └── [Opens dialogue with QWERTY]
```

---

## Accessibility in Onboarding

### First-Time Accessibility Check

On first launch (before FTUE):
```
┌─────────────────────────────────────────────┐
│  Before we begin, would you like to         │
│  adjust any accessibility settings?         │
│                                              │
│  [ ] Larger text                            │
│  [ ] High contrast                          │
│  [ ] Reduce motion                          │
│  [ ] Colorblind mode                        │
│                                              │
│  [Customize Now]    [Start with Defaults]   │
└─────────────────────────────────────────────┘
```

This respects player needs without assuming defaults work for everyone.

### Tutorial Accessibility

All tutorial content:
- Scales with text size setting
- Uses high-contrast mode colors when enabled
- Has reduced/no animation in reduce motion mode
- Is screen-reader compatible

---

## Measuring Onboarding Success

### Key Metrics

| Metric | Target | Meaning |
|--------|--------|---------|
| FTUE completion rate | >90% | Players finish tutorial |
| Time to first minigame | <3 min | Not too slow |
| Tutorial skip rate | 5-15% | Not too annoying |
| Return rate (day 2) | >50% | First session was good |
| Help menu access rate | <10% | Tutorials are sufficient |

### A/B Testing Opportunities
- Tutorial length variations
- QWERTY dialogue verbosity
- Hotspot highlight duration
- First-catch token amounts

---

## Common Confusion Points (and Solutions)

### "Where do I go?"
**Solution**: Hotspot highlights on first visit. Arrow indicators toward objectives. QWERTY's contextual suggestions.

### "What do tokens do?"
**Solution**: First token earn shows brief explanation. Restoration spending has preview before confirmation.

### "How do I unlock zones?"
**Solution**: Dark doors show unlock requirements on hover. QWERTY mentions it when player has enough tokens.

### "What's the goal?"
**Solution**: FTUE establishes restoration goal. HUD shows overall progress. QWERTY mentions next milestone.

### "How do I save?"
**Solution**: Autosave indicator in corner. "Your progress is automatically saved" message after FTUE.

---

## Implementation Checklist

- [ ] FTUE scripted sequence
- [ ] Per-game tutorial overlays (18 games)
- [ ] Context-sensitive QWERTY help
- [ ] Tutorial state persistence
- [ ] Skip/replay functionality
- [ ] Accessibility pre-check screen
- [ ] Help menu structure
- [ ] Tutorial queuing system
- [ ] Hotspot highlight system
- [ ] Arrow indicator system
