# Zone Spec: Pixel Beach

## Overview

### Telos
Pixel Beach is comfort. It's the zone you go to when you want to unwind, when the competitive heat of Neon Alley feels like too much, when you just want to exist in a pleasant space. It embodies the lazy summer afternoon, the satisfaction of small tasks, the peace of waves.

### Ludos
This is the starter zone—first accessible, lowest pressure. Games here are simple to learn, relaxing to play, but have depth for mastery. Fishing, surfing, memory matching. Casual-friendly but not condescending.

---

## Visual Description

### First Impression Prompt
```
An 8-bit tropical beach where the pixels are chunky and lovable. A turquoise sea stretches to a horizon of scanlines. Sandy shores dotted with pixel palm trees and bright beach umbrellas. The tide comes in as visible scanlines sweeping up the sand. Everything is low-poly warmth: a wooden pier, a small beach shack, distant islands rendered in simple shapes. The sun is a perfect yellow circle. The vibe is pure chill.
```

### Detailed Environment

**Sky**: Gradient from pale blue (#87CEEB) at horizon to deeper blue (#4A90D9) above. The sun is a solid yellow-orange circle (#FFD93D) with optional simple ray sprites. Occasional pixel clouds drift slowly. At dusk (cosmetic option), gradient shifts to oranges and pinks.

**Ocean**: Turquoise (#40E0D0) with visible horizontal scanlines that move toward shore as "waves." Deeper water darker (#2AA198). Occasional pixel fish shadows visible beneath surface. Simple white (#FFFFFF) foam sprites where waves meet sand.

**Beach**: Sandy yellow (#F4D35E) with slight pixel texture. Gradient darker where wet from tide. Scattered pixel shells, small rocks, occasional seaweed clump. Footprints appear briefly where player "walks."

**Palm Trees**: Classic pixel palms—brown (#8B4513) trunk, green (#228B22) fronds. 2-3 variants for variety. Gentle sway animation. Coconuts visible on some.

**Beach Shack**: PIXEL's home base. Weathered wood construction, thatched roof, small counter where PIXEL sits. Surfboards leaning against side. Chalkboard menu showing daily catches/rewards. String lights (inactive → twinkling as restored).

**Pier**: Wooden dock extending into water. Fishing game access point. Lanterns hung along posts. A bench at the end for sitting (cosmetic/idle animation trigger).

**Distant Islands**: 2-3 simple island shapes on horizon. One has a mountain, one has palm trees, one is mysterious (tied to late-game content).

**Beach Umbrellas**: Colorful umbrellas (#FF6B6B, #4ECDC4, #FFE66D) dotted around. Mostly decorative, one or two are clickable (hidden collectibles underneath).

**The Great Sandcastle**: (Restoration milestone) A massive sandcastle structure that builds progressively. At full restoration, it's elaborate with towers and a flag.

---

## Color Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Primary | Turquoise | #40E0D0 | Ocean, accents |
| Secondary | Sandy Yellow | #F4D35E | Beach, warm tones |
| Tertiary | Sky Blue | #87CEEB | Sky, subtle bg |
| Accent 1 | Coral | #FF6B6B | Umbrella, fish, life |
| Accent 2 | Seafoam | #4ECDC4 | Secondary water, plants |
| Accent 3 | Sun Yellow | #FFD93D | Sun, bright highlights |
| Wood | Warm Brown | #8B4513 | Pier, shack, palms |
| Foliage | Palm Green | #228B22 | Palm fronds, plants |
| Depth | Deep Teal | #2AA198 | Deep water, shadows |

---

## The First Magic Moment

Pixel Beach answers a question you didn't know you had: *What would it feel like if a place wanted you to rest?*

The player arrives and the first thing they notice is the sound—or rather, the gentle absence of urgency. Waves don't crash; they *sweep*, soft and rhythmic. The colors are warm but not demanding. The scanlines that make up the tide move at a pace that asks nothing of you.

The magic beat: a shell tumbles in on the foam, and the player realizes they can just... pick it up. No timer. No objective. No stakes. It's theirs because they noticed it. The shell goes into their collection—a tiny thing, worthless by any metric, but *theirs*.

**Sensory anchor**: The tide. That gentle, reliable, four-second cycle of waves approaching and retreating. It's a heartbeat for the zone—steady, calming, always there. Players should unconsciously sync their breathing to it. When the zone is damaged, the tide's rhythm breaks, and restoring it feels like helping something breathe again.

**PIXEL's welcome**: PIXEL doesn't rush to greet the player. They're there, at the shack, and they look up with mild curiosity. No fanfare, no tutorial bombardment. Just: "oh. hey. welcome, i guess." And somehow that low-key acknowledgment feels more welcoming than any celebration could. You're not a hero here. You're a guest who might become a friend.

The Beach is about permission—permission to slow down, to collect small things, to find value in gentleness. In a world of intensity and decay, Pixel Beach whispers: *some games are won by resting*.

---

## Restoration States

### Stage 1: Flickering (0-25%)
- Ocean: Scanlines erratic, tide unpredictable
- Beach: Some "dead pixels" (gray patches)
- Shack: Boarded up, no lights
- Pier: Missing planks, no lanterns lit
- PIXEL: Partially rendered, sad
- Sandcastle: Foundation only, crumbling

### Stage 2: Awakening (25-50%)
- Ocean: Regular tide pattern
- Beach: Colorful, shells present
- Shack: Open, PIXEL at counter
- Pier: Repaired, some lanterns
- PIXEL: Fully rendered, chill
- Sandcastle: Base built, walls starting

### Stage 3: Thriving (50-85%)
- Ocean: Beautiful, fish visible
- Beach: Lively, umbrellas up
- Shack: String lights active
- Pier: All lanterns lit, bench usable
- PIXEL: Happy, offers more dialogue
- Sandcastle: Towers rising, detail emerging

### Stage 4: Radiant (85-100%)
- Ocean: Sparkles on waves, occasional dolphin pixels
- Beach: Paradise-quality, everything vivid
- Shack: Bustling, menu full
- Pier: Festive, flower garlands
- PIXEL: Thriving, hints at secrets
- Sandcastle: Magnificent, flag flying, interior explorable

---

## Key Landmarks

### Beach Shack
- **Function**: PIXEL's home, info hub, daily catch display
- **Interaction**: Click to talk to PIXEL, view fish collection, get quests
- **Art Needs**: Shack exterior, counter, menu board, string lights, surfboards

### The Pier
- **Function**: Fishing game access, scenic viewing
- **Interaction**: Click to start fishing; walk to end for idle scene
- **Art Needs**: Wooden pier, lanterns, bench, fishing spot indicator

### The Great Sandcastle
- **Function**: Restoration milestone, late-game explorable area
- **Interaction**: Visual progress; at full restoration, clickable to enter
- **Art Needs**: 5+ build stages, final interior (small room with treasure/lore)

### Wave Zone
- **Function**: Surfing game access
- **Interaction**: Click surfboard on beach to start
- **Art Needs**: Surfboard sprite, wave indicator, game entry point

### Shell Shore
- **Function**: Memory game access, collectible shells
- **Interaction**: Click area to start memory game; shells collectible daily
- **Art Needs**: Designated beach section, shell sprites, game setup

### Mysterious Island (Distant)
- **Function**: Late-game content tease
- **Interaction**: Non-interactive until late game; then reveals secret
- **Art Needs**: Simple silhouette, evolving detail as story progresses

---

## Ambient Details

### Background Animations
- Waves rolling in (scanline effect, 4-second cycle)
- Palm trees swaying (gentle, continuous)
- Clouds drifting (very slow)
- Fish shadows under water (occasional)
- Seagulls (pixel birds) flying across (rare)
- Foam bubbles at shore (continuous)

### Background Characters (Post-Restoration)
- Pixel crabs scuttling at water's edge
- Distant figures on other islands (late game)
- Beach umbrellas casting moving shadows

### Environmental Sounds
- Baseline: Lo-fi chiptune beach theme, gentle
- Waves: Rhythmic wash, retreating
- Wind: Soft, palm frond rustle
- Seagulls: Occasional calls (distant)
- PIXEL: Occasional crab chittering when active

---

## Navigation Hotspots

| Hotspot | Destination/Action | Visual Indicator |
|---------|-------------------|------------------|
| Beach Shack | PIXEL dialogue, fish collection | PIXEL visible, string lights |
| The Pier | Fishing game | Lantern glow, fishing rod |
| Surfboard | Surfing game | Board propped on sand |
| Shell Shore | Memory game | Cluster of shells |
| Great Sandcastle | View/enter (when complete) | Structure, flag |
| Under Umbrellas | Hidden collectibles | Subtle sparkle |
| Lobby Exit | Return to Lobby | Path leading to portal door |

---

## Sound Design

### Music
- **Style**: Lo-fi chiptune, island vibes, ukulele samples
- **Base Track**: "Pixel Waves" - mellow, 80 BPM, major key, simple melody
- **Dynamic Layers**:
  - Layer 1 (0-25%): Just waves, hint of melody
  - Layer 2 (25-50%): Soft drums, bass
  - Layer 3 (50-85%): Full arrangement, ukulele lead
  - Layer 4 (85-100%): Extra percussion, happy embellishments

### Sound Effects Needed
- Wave wash (rhythmic, soothing)
- Wave retreat (different texture)
- Sand footsteps (soft crunch)
- Pier footsteps (wooden clunk)
- Palm rustle
- Seagull call (distant)
- Shell pickup
- Fishing cast/reel
- PIXEL dialogue blips (bubbly)
- Surfboard pickup
- Splash effects

---

## Asset List

### Environment
| Asset | Description | States |
|-------|-------------|--------|
| beach_bg_sky | Sky gradient with sun | 2 (day/dusk) |
| beach_bg_ocean | Turquoise sea with scanlines | Animation (wave cycle) |
| beach_bg_sand | Sandy beach | 4 (restoration: dead pixels → vibrant) |
| beach_clouds | Pixel cloud sprites | 3 variants, float animation |
| beach_sun | Yellow circle sun | 1 (2 if dusk variant) |
| beach_foam | Wave foam sprites | Animation (bubble/pop) |
| beach_palm_* | Palm tree variants | 3 types, sway animation |
| beach_umbrella_* | Beach umbrella colors | 4 colors |
| beach_shells | Collectible shell sprites | 6 variants |
| beach_rocks | Decorative rocks | 3 variants |
| beach_seaweed | Seaweed clumps | 2 variants |

### Structures
| Asset | Description | States |
|-------|-------------|--------|
| beach_shack | PIXEL's beach shack | 4 (restoration levels) |
| beach_shack_counter | Counter detail | 1 |
| beach_shack_menu | Chalkboard menu | Dynamic content |
| beach_shack_lights | String lights | 2 (off/on + twinkle) |
| beach_surfboards | Leaning surfboards | 1 |
| beach_pier | Wooden pier | 4 (restoration levels) |
| beach_pier_lanterns | Pier lanterns | Off/on |
| beach_pier_bench | End-of-pier bench | 1 |
| beach_sandcastle | The Great Sandcastle | 5 (build stages) |
| beach_sandcastle_interior | Inside the castle | 1 (late game) |

### Interactive
| Asset | Description | States |
|-------|-------------|--------|
| beach_surfboard_pickup | Clickable surfboard | Idle/hover/picked |
| beach_fishing_spot | Pier fishing location | Indicator glow |
| beach_shell_shore | Memory game area | Idle/active |

### Effects
| Asset | Description | Type |
|-------|-------------|------|
| fx_wave_scanline | Wave movement effect | Shader/animation |
| fx_sand_footprint | Temporary footprints | Fade sprite |
| fx_water_sparkle | Ocean sparkle (high rest.) | Particle |
| fx_fish_shadow | Underwater fish shapes | Animation |
| fx_pixel_dolphin | Rare dolphin jump | Animation |

### Characters/Creatures
| Asset | Description | Notes |
|-------|-------------|-------|
| creature_crab_pixel | Ambient pixel crab | Walk animation |
| creature_seagull | Flying seagull | Fly cycle |
| creature_fish_shadow | Fish silhouettes | 4 variants |

---

## Minigames Housed

### Reel Deal
*See minigames/pixel-beach/reel-deal.md*
- Genre: Fishing simulation
- Access: The Pier

### Wave Rider
*See minigames/pixel-beach/wave-rider.md*
- Genre: Endless surfer/runner
- Access: Surfboard on beach

### Shell Shocked
*See minigames/pixel-beach/shell-shocked.md*
- Genre: Memory matching
- Access: Shell Shore area

---

## Implementation Notes

### Navigation Flow
```
Lobby → Pixel Beach (main beach view)
        ├─→ Beach Shack (PIXEL)
        ├─→ The Pier → Reel Deal (fishing)
        ├─→ Surfboard → Wave Rider (surfing)
        ├─→ Shell Shore → Shell Shocked (memory)
        ├─→ Sandcastle (view, enter when complete)
        ├─→ Under Umbrellas (hidden items)
        └─→ Exit → Lobby
```

### Data Required
```typescript
interface PixelBeachState {
  restoration_percent: number;
  fish_collection: FishEntry[];
  shells_collected_today: number;
  sandcastle_stage: number; // 0-5
  daily_catch_claimed: boolean;
  mysterious_island_unlocked: boolean;
}
```

### Wave System
- Waves are implemented as horizontal scanline offsets
- 4-second full cycle: approach → crest → retreat → pause
- Foam sprites spawn at crest point
- Tide line (wet sand) follows wave position

### Day/Dusk Cycle (Optional)
- Can be tied to real time or player preference
- Dusk version: warmer palette, longer shadows, different music variant

---

## PIXEL: Voice & Dialogue Samples

### Voice Characteristics
- All lowercase, always (even proper nouns)
- Minimal punctuation, lots of ellipses
- Short sentences, often incomplete thoughts
- Speaks at the pace of waves—unhurried, rhythmic
- Silence is part of their vocabulary; pauses are meaningful
- Occasional crab clicks accompany speech
- No exclamation marks, ever

### Signature Phrases
- "hey." (greeting)
- "the tide knows." (wisdom)
- "...yeah." (agreement)
- "sit with me for a bit?" (invitation)
- "some things just... are." (acceptance)
- "the waves don't rush." (comfort)

### Dialogue Samples by Context

**First Meeting (Zone Unlock)**
> PIXEL: "oh."
> *long pause, wave sounds*
> PIXEL: "you're here."
> PIXEL: "didn't think... anyone was coming."
> PIXEL: "i'm pixel. this is... the beach."
> *gestures vaguely at everything*
> PIXEL: "the games are over there. or you can just... sit."
> PIXEL: "sitting's good too."
> PIXEL: "welcome, i guess. the water's fine."

**Daily Greeting (Early Game)**
> PIXEL: "hey."
> *wave washes up*
> PIXEL: "back again? cool."
> PIXEL: "the fish are biting today. might be a good day to try the pier."
> PIXEL: "or not. no pressure."

**Daily Greeting (Mid Game)**
> PIXEL: "you came back."
> PIXEL: "keep doing that. the beach notices."
> *pause*
> PIXEL: "the sandcastle's a little taller than yesterday. saw you add to it."
> PIXEL: "that was... nice. small things. i like small things."

**Daily Greeting (Late Game)**
> PIXEL: "you know what i realized? you never ask permission."
> PIXEL: "you just... show up. do things. help."
> PIXEL: "i used to think that was exhausting. chasing restoration. fighting the fade."
> *wave retreats*
> PIXEL: "but you made it look... easy? no. not easy. natural."
> PIXEL: "maybe i was wrong about stillness being the only answer."
> PIXEL: "maybe sometimes you have to move... gently."

**Before Fishing**
> PIXEL: "the fish don't care about your day. they don't know about restoration or tokens or any of that."
> PIXEL: "they just swim. you just cast. something bites or it doesn't."
> PIXEL: "there's a kind of peace in that. the not-caring."
> PIXEL: "cast when you're ready."

**After a Good Catch**
> PIXEL: "oh... nice one."
> *holds fish up to the light*
> PIXEL: "this one's got good colors. healthy pixels."
> PIXEL: "the collection's growing. slowly. the way things should."
> PIXEL: "no rush."

**After Player Fails**
> PIXEL: "didn't get it? that's okay."
> PIXEL: "the waves come back. always. you can try again when they do."
> PIXEL: "or don't. rest here. nobody's keeping score."
> *pause*
> PIXEL: "...okay, neon's keeping score. but not here."

**When Player Seems Stressed**
> PIXEL: "hey. stop for a second."
> *wave sounds intensify, then calm*
> PIXEL: "breathe with the waves. in... out..."
> PIXEL: "whatever you're chasing... it'll still be there after the next wave."
> PIXEL: "everything is. nothing's going anywhere that fast."
> PIXEL: "except neon. neon moves pretty fast."

**Quest Introduction (Act 1)**
> PIXEL: "can i ask you something? you don't have to answer."
> PIXEL: "when everyone left... i stopped trying to bring them back."
> PIXEL: "told myself it was peace. acceptance. wisdom."
> *long pause*
> PIXEL: "but then you showed up. and started... fixing things."
> PIXEL: "and i just watched. from the beach. let you do the work."
> PIXEL: "there's a difference between peace and passivity, isn't there?"
> PIXEL: "i want to find out which one i chose."
> PIXEL: "will you help me look? at what i was... before i decided to stop being?"

**Discussing NEON**
> PIXEL: "neon." *sigh*
> PIXEL: "all that energy. all that volume."
> PIXEL: "they think i gave up. i think they're exhausting themselves."
> *pause*
> PIXEL: "...maybe we're both right."
> PIXEL: "i don't hate them. i just... can't be like that. it hurts to watch sometimes."
> PIXEL: "all that hope. so loud it could break."
> PIXEL: "the beach doesn't hope. the beach just... is."
> *softer*
> PIXEL: "maybe that's not better. just... different."

**Discussing SUCRE**
> PIXEL: "sucre tries so hard. too hard."
> PIXEL: "all that sweetness... it's a mask, right? you can tell."
> PIXEL: "i visit them sometimes. near the boulevard. don't say much."
> PIXEL: "but i think they know i see through it."
> PIXEL: "the sad part isn't that they're hurting. it's that they think being sad would ruin everything."
> PIXEL: "...it wouldn't. nothing ruins the beach. not even storms."

**Late Game Revelation (Quest 4)**
> PIXEL: "i found something. washed up. from... before."
> *holds a fragment of something*
> PIXEL: "when the last players left... i was different. i fought. yelled. tried to stop them."
> PIXEL: "it didn't work. obviously."
> PIXEL: "so i... stopped. told myself letting go was enlightenment."
> *wave sounds, long pause*
> PIXEL: "but i think i was just... tired of feeling things."
> PIXEL: "you made me feel things again. that's scary."
> PIXEL: "but also... the waves feel different now. more... alive?"
> PIXEL: "maybe feeling things isn't the problem. maybe it's where i put the feelings."
> PIXEL: "thank you. for being worth feeling things for."

**On the Mysterious Island**
> PIXEL: "you see that island? the far one?"
> PIXEL: "i've watched it for years. never changes. never gets closer."
> PIXEL: "sometimes i think it's a promise. something out there, waiting."
> PIXEL: "sometimes i think it's a trick. something that looks like hope but isn't."
> PIXEL: "...ask me again later. when we know more."

**Idle Dialogue (Random Selection)**
> - "the tide's been out for a while. it comes back. always does."
> - "found a shell today. blue one. put it with the others."
> - "you ever just... listen? to the nothing between the waves?"
> - "the crabs are chattier when you're around. i think they like you."
> - "somewhere under the water there's a fish i haven't caught. keeps it interesting."
> - "the sandcastle's leaning a little. might fix it. might let it lean."
> - "neon asked if i ever get bored. i asked if they ever get tired. neither of us answered."
> - "the sunset's different every day. most people don't notice."
