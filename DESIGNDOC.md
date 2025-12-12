# NEOCADIA Design Document

## High Concept

**Neocadia** is a browser-based arcade hub reminiscent of Neopets and early-2000s Flash game portals. Players explore a mysterious interdimensional arcade through point-and-click navigation, play diverse minigames to earn tokens, and gradually restore a fading digital world to its former glory.

**Tagline:** *"The arcade that exists everywhere, for everyone."*

---

## Core Fantasy

You've stumbled into **The Arcade Between Screens**—a pocket dimension that connects to every monitor, phone, and television in the world. Once a thriving hub where players from across reality gathered, Neocadia is now fading. Zones have gone dark. Characters have grown dormant. The games themselves are forgetting how to play.

You're one of the few who can still find the way in. By playing games and earning tokens, you restore power to the arcade, reawaken its inhabitants, and uncover the mystery of why Neocadia began to fade.

---

## World Structure

### Navigation System

Point-and-click exploration through illustrated 2D scenes. Each location has:
- **Clickable hotspots** for navigation (doors, paths, portals)
- **Interactive NPCs** with dialogue and quests
- **Arcade cabinets** that launch minigames
- **Collectible sparkles** (daily hidden items)
- **Ambient animations** bringing each zone to life

### The Seven Zones

```
                    ┌─────────────────┐
                    │  STARLIGHT      │
                    │  CINEMA         │
                    └────────┬────────┘
                             │
    ┌──────────────┐    ┌────┴────┐    ┌──────────────┐
    │ CLOCKWORK    ├────┤  THE    ├────┤ NEON         │
    │ QUARTER      │    │  LOBBY  │    │ ALLEY        │
    └──────────────┘    └────┬────┘    └──────────────┘
                             │
    ┌──────────────┐    ┌────┴────┐    ┌──────────────┐
    │ SUGAR RUSH   ├────┤ PIXEL   ├────┤ THE GLITCH   │
    │ BOULEVARD    │    │ BEACH   │    │ GARDEN       │
    └──────────────┘    └─────────┘    └──────────────┘
```

---

## Zone Details

### 1. THE LOBBY
**Theme:** Grand arcade entrance, art deco meets CRT glow
**Atmosphere:** Warm, welcoming, slightly dusty with potential
**State at Start:** Partially lit, echoing, most doors locked

The central hub connecting all zones. Features a massive token fountain (currently dry), a hall of high scores, and the **Registry Desk** where players manage their profile.

**Key Features:**
- Token Fountain (restoration milestone)
- Hall of Champions (leaderboards)
- The Lost & Found (daily mystery items)
- Portal doors to each zone (unlock progressively)

---

### 2. NEON ALLEY
**Theme:** 80s retro arcade, synthwave aesthetic
**Atmosphere:** Electric pink and blue, pulsing to music, nostalgic
**Unlock Cost:** 500 Tokens

A corridor of classic cabinet-style games bathed in neon light. The walls pulse with music. Highscores glow on every surface.

**Minigames:**
| Game | Genre | Description |
|------|-------|-------------|
| **Void Breaker** | Breakout clone | Smash neon bricks with a paddle, collect powerups, face geometric bosses |
| **Synth Racer** | Rhythm runner | Outrun-style racing where you hit notes on the beat to boost |
| **Pixel Invaders** | Space shooter | Classic fixed shooter with modern bullet-hell elements |

---

### 3. PIXEL BEACH
**Theme:** 8-bit tropical paradise, lo-fi summer vibes
**Atmosphere:** Chill, sunny, waves of static, chiptune ukulele
**Unlock Cost:** Free (starter zone)

A beach made of chunky pixels where the tide comes in as scanlines. Palm trees sway in 12fps animation. Perfect for relaxed play.

**Minigames:**
| Game | Genre | Description |
|------|-------|-------------|
| **Reel Deal** | Fishing sim | Cast into pixelated waters, time your catches, collect rare fish |
| **Wave Rider** | Endless surfer | Balance on waves, perform tricks, avoid jellyfish |
| **Shell Shocked** | Memory match | Flip shells on the beach to match pairs before tide comes in |

---

### 4. THE GLITCH GARDEN
**Theme:** Corrupted pastoral, beautiful errors, liminal beauty
**Atmosphere:** Unsettling yet serene, colors shift, reality stutters
**Unlock Cost:** 2000 Tokens

A garden where the code broke in beautiful ways. Flowers bloom in impossible colors. Paths loop back on themselves. Nothing here plays by normal rules.

**Minigames:**
| Game | Genre | Description |
|------|-------|-------------|
| **Debug** | Puzzle | Find and fix visual glitches in corrupted scenes |
| **Loop Garden** | Maze escape | Navigate a garden that wraps and shifts, rules change each screen |
| **Error Garden** | Idle/clicker | Plant glitch seeds, harvest corrupted but valuable resources |

---

### 5. STARLIGHT CINEMA
**Theme:** Golden age Hollywood meets vaporwave
**Atmosphere:** Dreamy, dramatic, film grain and lens flares
**Unlock Cost:** 1500 Tokens

An abandoned movie palace where the films developed personalities. The seats are dusty velvet, the screen still flickers with half-remembered stories.

**Minigames:**
| Game | Genre | Description |
|------|-------|-------------|
| **Scene Stealer** | Quick-time sequences | Recreate famous movie scenes with timed inputs |
| **Reel Trivia** | Quiz game | Answer questions about films, music, pop culture of all eras |
| **Director's Cut** | Narrative puzzle | Rearrange film strips to create coherent (or absurd) stories |

---

### 6. CLOCKWORK QUARTER
**Theme:** Steampunk meets circuit board, mechanical precision
**Atmosphere:** Ticking, clicking, brass and copper, steam vents
**Unlock Cost:** 1000 Tokens

A zone of gears and logic gates where everything runs on mechanical precision. The puzzles here require thinking, timing, and patience.

**Minigames:**
| Game | Genre | Description |
|------|-------|-------------|
| **Gear Garden** | Puzzle | Connect gears to power machines, increasing complexity |
| **Tick Defense** | Tower defense | Place clockwork turrets to protect the central mechanism |
| **Spring Loaded** | Physics puzzle | Launch objects to hit targets using springs and levers |

---

### 7. SUGAR RUSH BOULEVARD
**Theme:** Candy land chaos, saccharine overload
**Atmosphere:** Hyper, colorful, everything is edible (and slightly threatening)
**Unlock Cost:** 750 Tokens

A street paved with hard candy where buildings are made of cake. Cheerful on the surface, but play too long and you'll notice the teeth.

**Minigames:**
| Game | Genre | Description |
|------|-------|-------------|
| **Candy Cascade** | Match-3 | Classic matching with combo chains and special candies |
| **Sugar Rush Kitchen** | Cooking sim | Follow recipes under time pressure, don't burn the caramel |
| **Jawbreaker** | Brick breaker variant | Break candy structures with bouncing gumballs |

---

## Characters

### Main Cast

#### QWERTY (The Lobby)
**Appearance:** A sentient mechanical keyboard with expressive keys, hovers slightly, types responses into the air
**Personality:** Helpful, slightly anxious, speaks in keyboard shortcuts ("CTRL yourself! Let me SHIFT your attention...")
**Role:** Tutorial guide, token exchange, restoration progress tracker
**Backstory:** The first program ever written for Neocadia. Has watched everything since the beginning.

#### NEON (Neon Alley)
**Appearance:** A humanoid figure made entirely of flickering neon tubes, constantly changing between pink and cyan
**Personality:** Enthusiastic, competitive, speaks in arcade callouts ("PLAYER ONE READY! HIGH SCORE INCOMING!")
**Role:** Manages Neon Alley games, runs weekly tournaments
**Quest Line:** Help them remember the legendary high scores that were lost in the fade

#### PIXEL (Pixel Beach)
**Appearance:** A friendly crab rendered in chunky 8-bit style, occasionally drops pixels when moving
**Personality:** Laid-back, speaks slowly, offers beach wisdom
**Role:** Beach guide, fishing expert, collectible tracker
**Quest Line:** Help restore the great sandcastle that was washed away by static

#### VERA (The Glitch Garden)
**Appearance:** A young girl whose form constantly corrupts—half her face might tile, her arm might duplicate
**Personality:** Mysterious, speaks in fragmented sentences, oddly peaceful about her condition
**Role:** Guardian of the Glitch Garden, sells rare corrupted items
**Quest Line:** Piece together her memories to learn what she was before the corruption
**Secret:** May be the original creator of Neocadia, or what's left of them

#### CELIA (Starlight Cinema)
**Appearance:** A 1920s film projector with a face in the light beam, wears a tiny director's beret
**Personality:** Dramatic, speaks in movie quotes, nostalgic for the golden age
**Role:** Runs the cinema games, provides narrative context for the world
**Quest Line:** Help her complete her unfinished masterpiece film

#### PROFESSOR COG (Clockwork Quarter)
**Appearance:** A Victorian automaton with visible clockwork through a glass chest, monocle, magnificent mustache
**Personality:** Proper, intellectual, obsessed with efficiency and elegance
**Role:** Puzzle master, teaches advanced mechanics, sells precision tools
**Quest Line:** Help rebuild the Great Engine that once powered all of Neocadia

#### SUCRE (Sugar Rush Boulevard)
**Appearance:** A golem made of stacked sweets—gumdrop eyes, licorice arms, cake body, changes based on what you feed them
**Personality:** Excitable, hungry, speaks in food puns, secretly melancholic
**Role:** Recipe keeper, sweetness dealer, party coordinator
**Quest Line:** Help them recover the Original Recipe that gave them consciousness

---

### Antagonist (Late Game)

#### THE STATIC
**Appearance:** Not a character but a force—manifests as TV static creeping at the edges, consuming color and sound
**Nature:** The entropy eating Neocadia, the forgetting, the end of all games
**Revelation:** Not evil, but inevitable—what happens when no one plays anymore
**Resolution:** Cannot be defeated, only held back through continuous play and community

---

## Economy & Metagame

### Currency: TOKENS

**Earning Tokens:**
- Completing minigames: 10-100 tokens based on score
- Daily login: 50 tokens
- Finding hidden sparkles: 5 tokens each
- Quest completion: 100-500 tokens
- Achievements: One-time bonuses

**Spending Tokens:**
- Unlock new zones: 500-2000 tokens
- Purchase cosmetics: 50-500 tokens
- Buy power-ups: 10-50 tokens
- Restore landmarks: 200-1000 tokens

### Restoration System

The core progression mechanic. As players earn and spend tokens, they restore Neocadia:

**Stage 1: Flickering**
- Zones are dim, games have limited features
- NPCs speak in fragments
- Basic rewards only

**Stage 2: Awakening**
- Full lighting returns
- NPCs fully conversational
- Standard rewards available

**Stage 3: Thriving**
- Special events become possible
- Rare rewards unlock
- Zone-specific bonuses activate

**Stage 4: Radiant**
- Maximum restoration
- Secret games unlock
- Legendary items become available

### Collectibles

**Fish Collection** (Pixel Beach)
- 50 species ranging from common to legendary
- Display in your personal aquarium
- Some fish only appear at certain times

**Film Reels** (Starlight Cinema)
- Fragments of lost movies
- Collect all pieces to watch complete shorts
- Some contain world lore

**Glitch Samples** (Glitch Garden)
- Captured visual bugs
- Can be applied as cosmetic effects
- Rare ones change game rules temporarily

**Blueprints** (Clockwork Quarter)
- Designs for clockwork companions
- Build your own following automaton
- Upgrade with better parts

**Recipes** (Sugar Rush Boulevard)
- Unlock cooking minigame variants
- Feed Sucre for transformation effects
- Trade with other players

### Daily & Weekly Systems

**Daily:**
- One free spin at the Token Fountain
- Hidden sparkle spawns refresh
- Daily challenge (bonus rewards for specific game)
- Shop inventory refreshes

**Weekly:**
- Tournament in Neon Alley (compete for ranking)
- New "Featured Film" in Starlight Cinema
- Seasonal event progress

**Seasonal:**
- Themed events (Halloween Glitch Garden, Winter Wonderzone, etc.)
- Limited cosmetics
- Special storylines

---

## Player Customization

### Avatar System

Players create an avatar to represent them in Neocadia:

**Base Options:**
- Body shape (5 types)
- Skin tone (full spectrum)
- Hair styles (30+)
- Face features

**Unlockable Cosmetics:**
- Outfits themed to each zone
- Accessories (hats, glasses, wings)
- Auras and particle effects
- Walking animations

### Personal Space: THE CABINET

Every player has their own arcade cabinet somewhere in the lobby. Customization includes:
- Exterior decal/skin
- Interior decoration
- Trophy display
- Pet display (clockwork companions)
- Jukebox (collected music)

---

## Narrative Arc

### Act 1: Arrival
Player stumbles into Neocadia through a glitching screen. QWERTY explains the situation—the arcade is fading. Most zones are dark. The Token Fountain is dry. Player must play games to generate tokens and restore power.

### Act 2: Restoration
As zones reawaken, each NPC shares fragments of the past:
- Neocadia was created by a group of programmers who loved games
- It was meant to be a place where anyone could play forever
- Something went wrong—people stopped coming
- The STATIC began to creep in

### Act 3: The Memory
Restoring the Glitch Garden reveals VERA's true nature—she's the echo of the original creator, fragmented when they tried to fix the decay alone. Her memories contain the truth: Neocadia isn't dying because people forgot. It's dying because the original creator tried to close it, believing it was time to let go.

### Act 4: The Choice
Players must make a choice:
- **Restore Fully:** Complete the Great Engine to permanently power Neocadia independent of players
- **Accept Entropy:** Allow the STATIC to peacefully claim zones, making what remains more precious
- **Merge:** Help VERA become whole, letting the creator return to guide Neocadia's future

Each ending changes the endgame, but all allow continued play.

---

## Technical Implementation Notes

### Target Platform
- Web browser (modern JS, Canvas/WebGL)
- Mobile-responsive design
- Offline-capable for played minigames

### Framework Considerations
- Phaser 3 for minigames
- React/Preact for UI chrome and navigation
- IndexedDB for local save state
- Optional cloud sync for cross-device

### Minigame Architecture
Each minigame is a self-contained module:
```
/games
  /void-breaker
    index.ts       # Entry point
    config.ts      # Game settings, difficulty curves
    scenes/        # Phaser scenes
    assets/        # Sprites, audio
```

### Save System
```typescript
interface PlayerSave {
  tokens: number;
  zones: Record<ZoneId, ZoneState>;
  collections: Collections;
  avatar: AvatarConfig;
  cabinet: CabinetConfig;
  questProgress: QuestLog;
  achievements: Achievement[];
  statistics: GameStats;
}
```

---

## Art Direction

### Overall Style
- **Clean vector illustrations** with subtle texture
- **Limited color palettes per zone** that harmonize when combined
- **Smooth animations** at 30fps for navigation, 60fps for games
- **Consistent character proportions** (chibi-adjacent, ~3 heads tall)

### Zone Color Keys

| Zone | Primary | Secondary | Accent |
|------|---------|-----------|--------|
| Lobby | Gold | Cream | Warm white |
| Neon Alley | Hot pink | Electric cyan | Purple |
| Pixel Beach | Sky blue | Sand yellow | Coral |
| Glitch Garden | Corrupted green | Error pink | Static gray |
| Starlight Cinema | Deep purple | Silver | Spotlight yellow |
| Clockwork Quarter | Brass | Copper | Steam white |
| Sugar Rush Boulevard | Bubblegum pink | Mint green | Cherry red |

---

## Audio Direction

### Music
- Each zone has a distinct genre/style
- Dynamic mixing based on game state
- 2-3 tracks per zone that rotate

| Zone | Style |
|------|-------|
| Lobby | Ambient arcade sounds, gentle piano |
| Neon Alley | Synthwave, chiptune fusion |
| Pixel Beach | Lo-fi chiptune, island vibes |
| Glitch Garden | Glitch hop, ambient drone |
| Starlight Cinema | Jazz, orchestral swells |
| Clockwork Quarter | Mechanical rhythms, baroque influences |
| Sugar Rush Boulevard | Hyperpop, bubblegum bass |

### Sound Design
- Satisfying UI feedback (clicks, whooshes, chimes)
- Each minigame has cohesive sound palette
- Ambient background loops for exploration
- Character voice clips (non-verbal expressions)

---

## Scope Tiers

### Tier 1: Minimum Viable Arcade (MVP)
- The Lobby + 2 zones (Pixel Beach, Neon Alley)
- 6 minigames total (3 per zone)
- Basic token economy
- Avatar creation (limited options)
- Local save only

### Tier 2: Full Experience
- All 7 zones
- 21 minigames
- Complete restoration system
- All NPCs with dialogue
- Quest system
- Cloud save
- Achievements

### Tier 3: Living Arcade
- Seasonal events
- Community features (leaderboards, trading)
- Regular new minigame additions
- Expanded story content
- Mobile apps

---

## Success Metrics

- **Retention:** 30% day-7 return rate
- **Session length:** Average 15+ minutes
- **Completion:** 20% reach full restoration
- **Breadth:** Players engage with 5+ minigames regularly

---

## Open Questions

1. **Monetization:** Free-to-play with cosmetics? Premium one-time purchase? Hybrid?
2. **Multiplayer:** Any real-time competitive modes, or purely async (leaderboards)?
3. **User Content:** Allow players to create and share levels/minigames?
4. **Narrative Depth:** How much lore is too much? Optional vs. required?

---

*"Every screen is a door. Every game is a memory. Welcome home, Player One."*
