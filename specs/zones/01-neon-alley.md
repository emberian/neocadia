# Zone Spec: Neon Alley

## Overview

### Telos
Neon Alley is the heart of competitive play—the electric pulse of the arcade. It embodies the 80s dream of arcade mastery: initials on the high score board, crowds gathered around your cabinet, the thrill of one more quarter. It should feel like stepping into a synthwave music video.

### Ludos
This zone houses the action-heavy minigames: shooters, rhythm games, high-score chasers. Players come here to compete against themselves and leaderboards. Weekly tournaments add a community element.

---

## Visual Description

### First Impression Prompt
```
A neon-drenched arcade corridor stretching into electric infinity. Hot pink and electric cyan light everything. Classic arcade cabinets line both walls, their screens flickering with attract modes. The floor is black mirror-polished, reflecting the neon into doubled infinity. Posters of stylized game heroes cover the walls between cabinets. The ceiling is a grid of light strips that pulse to an unheard beat. The air itself seems to hum with competitive energy.
```

### Detailed Environment

**Floor**: Black polished surface (#0A0A0A) so reflective it doubles every light source. Neon strips embedded at regular intervals create a runway effect leading deeper into the alley.

**Walls**: Dark charcoal (#1A1A1A) covered with:
- Arcade cabinet sides (visible between games)
- Posters in neon frames (game advertisements, tournament announcements)
- Graffiti-style high scores painted directly on walls
- Subtle grid pattern that glows faintly

**Ceiling**: Industrial grid structure with:
- Neon tube lights (pink, cyan, purple)
- Hanging geometric shapes (triangles, hexagons) that rotate slowly
- Occasional burst of fog/haze effect

**Arcade Cabinets**: Classic upright cabinet designs with modern styling:
- Each game has a unique cabinet design
- Screens show attract modes when not in play
- Side art visible, themed to each game
- Some cabinets are dark (not yet restored)

**The Stage**: At the far end, a raised platform with a massive screen—this is where tournaments are broadcast. NEON's home base. Currently has one spotlight; at full restoration, multiple lights and animated backdrop.

**Tournament Board**: A massive digital display showing current rankings, upcoming events, and legendary high scores. Flickers at low restoration; blazes at full.

**The Loser's Lounge**: A small alcove with a beaten-up couch, a few chairs, screens showing game replays. Where players go to watch and learn (or lick wounds).

---

## Color Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Primary | Hot Pink | #FF1493 | Primary neon, accents |
| Secondary | Electric Cyan | #00FFFF | Secondary neon, highlights |
| Tertiary | Neon Purple | #BF40FF | Accent neon, gradients |
| Background | Pure Black | #0A0A0A | Floor, deep shadows |
| Surface | Charcoal | #1A1A1A | Walls, cabinet bodies |
| Highlight | White | #FFFFFF | Brightest reflections |
| Grid | Dark Grid | #2D2D2D | Background pattern |
| Warning | Neon Orange | #FF6600 | Alerts, fail states |

---

## Restoration States

### Stage 1: Flickering (0-25%)
- Lights: Sporadic, some tubes buzzing/dead
- Cabinets: Only 1 game active, others dark
- Floor: Dull, minimal reflection
- NEON: Glitchy, unstable form
- Sound: Crackling, intermittent music

### Stage 2: Awakening (25-50%)
- Lights: Steady but not full brightness
- Cabinets: All 3 games active
- Floor: Reflective, some strips lit
- NEON: Stable, enthusiastic
- Sound: Music consistent, good bass

### Stage 3: Thriving (50-85%)
- Lights: Vibrant, pulsing to music
- Cabinets: All active, attract modes playing
- Floor: Full mirror effect, light show
- Tournament Board: Active, showing rankings
- Sound: Full synthwave soundtrack, crowd ambiance

### Stage 4: Radiant (85-100%)
- Lights: Spectacular, reactive to player movement
- Stage: Full light rig, animated backdrops
- Floor: Prismatic rainbow effects
- Loser's Lounge: Comfortable, active screens
- Sound: Concert-quality audio, cheering crowd samples

---

## Key Landmarks

### The Stage
- **Function**: Tournament viewing, NEON's home, special events
- **Interaction**: Click to talk to NEON, view tournament info, enter events
- **Art Needs**: Stage with screen, light rig, NEON position, crowd silhouettes (restored)

### Tournament Board
- **Function**: Leaderboards, event schedule, rankings
- **Interaction**: Click to view detailed leaderboards, upcoming tournaments
- **Art Needs**: Large digital display, 4 restoration states, animated number effects

### Game Cabinets (3)
- **Function**: Access minigames
- **Interaction**: Click cabinet to launch game
- **Art Needs**: Unique cabinet per game, attract mode animation, side art

### Loser's Lounge
- **Function**: Optional social area, replay viewing
- **Interaction**: Click to enter smaller scene, watch replays
- **Art Needs**: Couch, chairs, mounted screens, dim lighting

### Back to Lobby
- **Function**: Zone exit
- **Interaction**: Click arrow/door at entrance
- **Art Needs**: Exit indicator with lobby preview

---

## Ambient Details

### Background Animations
- Neon lights pulsing to beat (4/4 tempo, ~120 BPM)
- Ceiling shapes rotating slowly
- Fog/haze drifting through light beams
- Floor reflections shimmering
- Attract mode screens cycling
- Occasional "firework" burst when high score achieved anywhere

### Background Characters (Post-Restoration)
- Silhouettes gathered around popular cabinets
- Shadow of someone celebrating a win
- Suggests competitive community

### Environmental Sounds
- Baseline: Synthwave track, muffled
- Neon: Constant subtle buzz/hum
- Cabinets: Attract mode sounds blending
- Stage: NEON's energetic commentary when active
- Crowd: Murmur, occasional cheer (at high restoration)

---

## Navigation Hotspots

| Hotspot | Destination/Action | Visual Indicator |
|---------|-------------------|------------------|
| The Stage | NEON dialogue, tournaments | Spotlight, NEON presence |
| Tournament Board | Leaderboard interface | Glow, number animation |
| Void Breaker Cabinet | Launch Void Breaker | Cabinet attract mode |
| Synth Racer Cabinet | Launch Synth Racer | Cabinet attract mode |
| Pixel Invaders Cabinet | Launch Pixel Invaders | Cabinet attract mode |
| Loser's Lounge | Enter viewing area | Dim glow, couch visible |
| Lobby Exit | Return to Lobby | Arrow, faint gold glow |

---

## Sound Design

### Music
- **Style**: Synthwave, chiptune fusion
- **Base Track**: "Neon Dreams" - driving beat, nostalgic pads, chippy arpeggios
- **Dynamic Layers**:
  - Layer 1 (0-25%): Muffled, distant, occasional drop-out
  - Layer 2 (25-50%): Clear bass and drums
  - Layer 3 (50-85%): Full track with pads
  - Layer 4 (85-100%): Extra lead synth, crowd energy samples

### Sound Effects Needed
- Neon buzz (constant, subtle)
- Light flicker
- Cabinet attract mode (per game)
- Step sounds on reflective floor
- Tournament fanfare
- High score achieved
- NEON dialogue blips
- Crowd cheer variants (3-4)
- Lose sound (sympathetic but not harsh)

---

## Asset List

### Environment
| Asset | Description | States |
|-------|-------------|--------|
| neon_bg_floor | Black mirror floor | 4 (restoration levels) |
| neon_bg_walls | Charcoal walls with posters | 4 |
| neon_bg_ceiling | Grid with lights/shapes | 4 |
| neon_lights_main | Primary neon tubes | Animation (pulse) |
| neon_lights_accent | Secondary accent lights | Animation (pulse) |
| neon_ceiling_shapes | Rotating geometric shapes | Animation (rotate) |
| neon_fog | Haze/fog effect | Particle system |
| neon_stage | Tournament stage platform | 4 |
| neon_stage_screen | Large backdrop screen | Animation (patterns) |
| neon_stage_lights | Light rig | 4 |
| neon_tournament_board | Digital ranking display | 4 + number animation |
| neon_lounge_bg | Loser's Lounge background | 2 (dim/active) |
| neon_lounge_couch | Beaten-up couch | 1 |
| neon_lounge_screens | Replay monitors | Animation |

### Cabinets
| Asset | Description | States |
|-------|-------------|--------|
| cabinet_void_breaker | Void Breaker machine | Dark/attract/playing |
| cabinet_synth_racer | Synth Racer machine | Dark/attract/playing |
| cabinet_pixel_invaders | Pixel Invaders machine | Dark/attract/playing |
| cabinet_side_art_* | Side panel art per game | 3 variants |

### Posters
| Asset | Description | Notes |
|-------|-------------|-------|
| poster_void_breaker | Game promo poster | Neon frame |
| poster_synth_racer | Game promo poster | Neon frame |
| poster_pixel_invaders | Game promo poster | Neon frame |
| poster_tournament | Tournament announcement | Dynamic content |
| poster_legend | "AAA" legendary player | Mysterious, partially obscured |

### Effects
| Asset | Description | Type |
|-------|-------------|------|
| fx_neon_glow | Bloom effect for neons | Shader/overlay |
| fx_floor_reflection | Floor mirror effect | Shader |
| fx_high_score_burst | Celebration particles | Particle system |
| fx_light_beam | Volumetric light rays | Sprite animation |

---

## Minigames Housed

### Void Breaker
*See minigames/neon-alley/void-breaker.md*
- Genre: Breakout clone with bullet-hell elements
- Cabinet Style: Angular, aggressive, pink dominant

### Synth Racer
*See minigames/neon-alley/synth-racer.md*
- Genre: Rhythm runner (Outrun + beat matching)
- Cabinet Style: Sleek, curved, cyan dominant

### Pixel Invaders
*See minigames/neon-alley/pixel-invaders.md*
- Genre: Fixed shooter with modern twists
- Cabinet Style: Classic upright, purple dominant

---

## Implementation Notes

### Navigation Flow
```
Lobby → Neon Alley (main corridor)
        ├─→ The Stage (NEON)
        ├─→ Tournament Board (leaderboards)
        ├─→ Void Breaker Cabinet → Game
        ├─→ Synth Racer Cabinet → Game
        ├─→ Pixel Invaders Cabinet → Game
        ├─→ Loser's Lounge (optional area)
        └─→ Exit → Lobby
```

### Data Required
```typescript
interface NeonAlleyState {
  restoration_percent: number;
  high_scores: {
    void_breaker: LeaderboardEntry[];
    synth_racer: LeaderboardEntry[];
    pixel_invaders: LeaderboardEntry[];
  };
  tournament_active: boolean;
  tournament_end_time?: Date;
  player_tournament_rank?: number;
}
```

### Music Sync
- Ambient lights pulse to music beat
- Beat detection should drive:
  - Ceiling shape rotation speed
  - Floor light strip pulses
  - Fog density variation
