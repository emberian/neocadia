# Neocadia Specifications

This directory contains the complete specifications for Neocadia, structured for both **art generation** and **development**.

## Directory Structure

```
specs/
├── README.md                 # This file
├── world/
│   ├── lore.md              # World history, mythology, the fade
│   ├── narrative.md         # Story beats, act structure, endings
│   └── tone.md              # Voice, humor, emotional beats
├── zones/
│   ├── 00-lobby.md          # The Lobby (hub)
│   ├── 01-neon-alley.md     # Neon Alley (retro arcade)
│   ├── 02-pixel-beach.md    # Pixel Beach (starter zone)
│   ├── 03-glitch-garden.md  # The Glitch Garden (corrupted)
│   ├── 04-starlight-cinema.md # Starlight Cinema (film)
│   ├── 05-clockwork-quarter.md # Clockwork Quarter (steampunk)
│   └── 06-sugar-rush.md     # Sugar Rush Boulevard (candy)
├── characters/
│   ├── qwerty.md            # QWERTY - Lobby guide
│   ├── neon.md              # NEON - Arcade master
│   ├── pixel.md             # PIXEL - Beach crab
│   ├── vera.md              # VERA - Glitch guardian
│   ├── celia.md             # CELIA - Cinema projector
│   ├── professor-cog.md     # PROFESSOR COG - Clockwork inventor
│   ├── sucre.md             # SUCRE - Candy golem
│   └── the-static.md        # THE STATIC - Antagonist force
├── minigames/
│   ├── README.md            # Minigame design philosophy
│   ├── neon-alley/          # 3 games
│   ├── pixel-beach/         # 3 games
│   ├── glitch-garden/       # 3 games
│   ├── starlight-cinema/    # 3 games
│   ├── clockwork-quarter/   # 3 games
│   └── sugar-rush/          # 3 games
├── systems/
│   ├── economy.md           # Tokens, spending, earning
│   ├── progression.md       # Restoration, unlocks, milestones
│   ├── collections.md       # Collectibles per zone
│   ├── daily-weekly.md      # Recurring content systems
│   ├── save-system.md       # Data structures, sync
│   ├── accessibility.md     # Accessibility options [P3]
│   └── onboarding.md        # Tutorial and new player flow [MVP]
├── art/
│   ├── direction.md         # Overall art philosophy
│   ├── color-palettes.md    # Zone palettes with hex codes
│   ├── characters.md        # Character art specs
│   ├── environments.md      # Environment art specs
│   ├── ui-assets.md         # UI element specs
│   └── asset-list.md        # Complete asset manifest
└── ui/
    ├── navigation.md        # Point-and-click flow
    ├── hud.md               # In-game HUD elements
    ├── menus.md             # Menu screens
    └── transitions.md       # Scene transitions
```

## Spec Format

Each spec follows a consistent format:

### For Zones & Environments
- **Overview**: Telos (why it exists) + Ludos (how it plays)
- **Visual Description**: Detailed prose for art generation
- **Color Palette**: Primary, secondary, accent with hex codes
- **Key Landmarks**: Named locations within the zone
- **Ambient Details**: Background elements, animations
- **Sound Design**: Audio cues and music style
- **Navigation Hotspots**: Clickable areas and destinations
- **Asset List**: Every sprite/image needed

### For Characters
- **Overview**: Role, personality, speech patterns
- **Visual Description**: Detailed appearance for art generation
- **Expression Sheet**: Required emotional states
- **Animation States**: Idle, talking, happy, sad, special
- **Dialogue Samples**: Example lines showing voice
- **Quest Line**: Their story contribution
- **Asset List**: All character assets needed

### For Minigames
- **Overview**: Telos (why play) + Ludos (how it works)
- **Core Loop**: The 30-second experience
- **Controls**: Input scheme
- **Mechanics**: Detailed rules with numbers
- **Progression**: How difficulty scales
- **Scoring**: Point values and multipliers
- **Visual Style**: Art direction specific to game
- **Audio Cues**: Sound effects needed
- **Asset List**: All game assets

## Art Generation Notes

When generating assets with image AI, use the **Visual Description** sections as prompts, combined with:
- The zone's **Color Palette**
- The **Art Direction** style guide
- Specific **Asset List** item descriptions

## Development Notes

Implementation should reference:
- **Systems** specs for core mechanics
- **Minigames** specs for game logic
- **UI** specs for interface implementation
- **Save System** for data structures

## Priorities & MVP Scope

Throughout these specs, content is marked as follows:
- **[MVP]** - Required for Phase 1 launch
- **[P2]** - Phase 2 expansion content
- **[P3]** - Phase 3 polish/future content

### Phase 1 (MVP)
**Zones**: Lobby, Pixel Beach, Neon Alley
**Characters**: QWERTY, PIXEL, NEON
**Minigames** (6 total):
- Pixel Beach: Reel Deal, Wave Rider, Shell Shocked
- Neon Alley: Pixel Invaders, Synth Racer, Void Breaker

**Systems**:
- Core economy (tokens, spending)
- Basic restoration (Lobby + 2 starter zones)
- Save system
- Tutorial flow

**Story**: Act 1 complete, Act 2 hooks

### Phase 2 (Expansion)
**Zones**: Starlight Cinema, Clockwork Quarter, Sugar Rush Boulevard, Glitch Garden
**Characters**: CELIA, COG, SUCRE, VERA
**Minigames**: 12 additional (3 per new zone)
**Systems**: Collections, Daily/Weekly challenges

### Phase 3 (Polish)
**Story**: Full narrative (Acts 2-4), all three endings
**Features**: New Game Plus, seasonal events, accessibility assists
**Content**: Developer commentary, alternate cosmetics
