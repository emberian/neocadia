# Zone Spec: The Lobby

## Overview

### Telos
The Lobby is home. It's the first place you see and the place you return to. It should feel like the entrance to a grand old building—once magnificent, now worn, but still dignified. The Lobby teaches players that Neocadia was something special, and could be again.

### Ludos
The Lobby is the central hub. All navigation flows through it. Players check progress, access their cabinet, exchange tokens, and travel to all other zones from here.

---

## Visual Description

### First Impression Prompt
```
An art deco arcade lobby in soft decay. Marble checkerboard floors (cream and charcoal) stretch toward a grand dry fountain. A chandelier of brass and clouded glass hangs from a vaulted ceiling lost in shadow. Dust motes drift through shafts of amber light from unseen windows. Portal doors line the walls—some dark, some flickering, one or two glowing warmly. The aesthetic is 1920s theater lobby meets retro arcade. Warm, inviting, slightly dusty, full of potential.
```

### Detailed Environment

**Floor**: Checkerboard marble, cream (#F5F0E6) and charcoal (#3A3A3A). Some tiles cracked, revealing faint circuitry glow beneath. Small pixel-sparkle collectibles occasionally appear in corners.

**Walls**: Deep burgundy (#8B2942) wallpaper with subtle geometric patterns (interlocking circles, art deco sunbursts). Gold (#D4AF37) trim at ceiling and floor. Faded posters in gilded frames advertise zones and events from Neocadia's past.

**Ceiling**: Vaulted, disappearing into soft darkness. The chandelier hangs on a brass chain, its bulbs a mix of warm amber and cold static-flicker. At full restoration, all bulbs glow steadily.

**Token Fountain**: Center of the room. Black marble basin (5 meters diameter) with a bronze statue in the center—an abstract figure holding a token aloft. When dry: tarnished, silent, a single dull token in the basin. When restored: luminous water arcs upward, the token gleams gold, soft music emanates.

**Portal Doors**: Seven doors arranged around the lobby perimeter. Each door is styled to hint at its destination:
- Neon Alley: Chrome frame, pink/cyan neon trim
- Pixel Beach: Weathered wood, pixel-wave pattern carved
- Glitch Garden: Frame shifts colors, slightly out of phase
- Starlight Cinema: Velvet curtains, tiny marquee lights
- Clockwork Quarter: Brass gears visible in frame, ticking
- Sugar Rush Boulevard: Candy-stripe frame, sweet colors

**QWERTY's Station**: Near the entrance, a raised platform with the Registry Desk—an old wooden counter with a brass lamp and scattered papers. QWERTY hovers here when not accompanying the player.

**Hall of Champions**: An alcove with glass display cases showing trophies, high score plaques (most blank/faded), and a few mysterious artifacts. At full restoration, scores populate and glow.

**The Lost & Found**: A cabinet near the back corner, labeled in art deco lettering. Opens daily to reveal a random collectible.

**Player's Cabinet**: Along one wall, a row of arcade cabinets. One is yours—customizable exterior, clickable to access inventory/stats/cosmetics.

---

## Color Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| Primary | Warm Gold | #D4AF37 | Trim, accents, restored elements |
| Secondary | Cream | #F5F0E6 | Marble light tiles, paper |
| Tertiary | Charcoal | #3A3A3A | Marble dark tiles, shadows |
| Accent 1 | Burgundy | #8B2942 | Wallpaper, drapery |
| Accent 2 | Amber | #FFBF00 | Light shafts, chandelier |
| Decay | Dust Gray | #9C9C9C | Faded elements |
| Restored | Luminous White | #FFFEF0 | Fountain water, active elements |

---

## Restoration States

### Stage 1: Flickering (0-25%)
- Chandelier: 2 of 12 bulbs lit, others flicker
- Fountain: Completely dry, tarnished
- Walls: Visible dust, cobwebs in corners
- Doors: Only Pixel Beach glows; others dark or barely flickering
- Ambient: Occasional crackle of static, distant echoes

### Stage 2: Awakening (25-50%)
- Chandelier: 6 bulbs lit steadily
- Fountain: Basin cleaned, faint glow from beneath
- Walls: Dust reduced, posters more visible
- Doors: 3-4 doors active
- Ambient: Soft background music begins

### Stage 3: Thriving (50-85%)
- Chandelier: 10 bulbs lit, warm glow
- Fountain: Water flowing gently, soft splash sounds
- Walls: Clean, patterns vivid
- Doors: All doors active
- Ambient: Full music, occasional NPC visitors

### Stage 4: Radiant (85-100%)
- Chandelier: All bulbs blazing, prismatic sparkles
- Fountain: Full arcs of luminous water, statue gleams
- Walls: Gilding actually glints
- Doors: All doors pulsing invitingly
- Ambient: Rich, layered soundscape, Hall of Champions populated

---

## Key Landmarks

### Token Fountain
- **Function**: Visual restoration milestone, daily spin (free token chance)
- **Interaction**: Click to spin once per day; animation plays, token reward revealed
- **Art Needs**: 4 states (dry/filling/flowing/radiant), spin animation, token burst particles

### Registry Desk
- **Function**: Tutorial delivery, NPC home base, help menu
- **Interaction**: Click to talk to QWERTY, access tutorials, view progress
- **Art Needs**: Desk with lamp, papers, brass fixtures; QWERTY hover position

### Hall of Champions
- **Function**: Leaderboards, achievement display, lore breadcrumbs
- **Interaction**: Click to view leaderboards; individual cases are clickable for details
- **Art Needs**: Glass cases (3), trophies (5 types), high score plaques, mysterious artifacts (4)

### Lost & Found Cabinet
- **Function**: Daily reward dispenser
- **Interaction**: Click once per day; cabinet opens, item floats out
- **Art Needs**: Wooden cabinet with glass door, open animation, sparkle effect

### Player Cabinet
- **Function**: Personal space access, inventory, stats, cosmetics
- **Interaction**: Click to open cabinet interface
- **Art Needs**: Arcade cabinet exterior (customizable decals), interior scene for customization UI

### Portal Doors (7)
- **Function**: Zone navigation
- **Interaction**: Click active door to travel; inactive doors prompt restoration
- **Art Needs**: Each door unique style, 4 states (locked/unlocked/active/inviting)

---

## Ambient Details

### Background Animations
- Dust motes drifting through light shafts
- Chandelier crystals slowly rotating
- Fountain water ripples (when restored)
- Occasional flicker in not-fully-restored elements
- Papers on Registry Desk occasionally rustling

### Background Characters (Post-Restoration)
- Occasionally, silhouettes of other "players" cross the background
- Not interactive—just atmosphere
- Suggests Neocadia is coming back to life

### Environmental Sounds
- Baseline: Low ambient hum, distant arcade sounds
- Chandelier: Subtle chime when player passes beneath
- Fountain: Trickling to rushing as restoration increases
- Doors: Soft hum from active portals
- Papers: Occasional rustle
- Footsteps: Player movement on marble (click-clack echo)

---

## Navigation Hotspots

| Hotspot | Destination/Action | Visual Indicator |
|---------|-------------------|------------------|
| Token Fountain | Daily spin interface | Sparkle when available |
| Registry Desk | QWERTY dialogue | QWERTY waves/bobs |
| Hall of Champions | Leaderboard interface | Soft glow |
| Lost & Found | Daily reward | Glow when unclaimed |
| Player Cabinet | Personal space interface | Your custom decal |
| Neon Alley Door | Travel to Neon Alley | Pink/cyan glow |
| Pixel Beach Door | Travel to Pixel Beach | Wavering blue light |
| Glitch Garden Door | Travel to Glitch Garden | Color shifts |
| Starlight Cinema Door | Travel to Starlight Cinema | Spotlight flicker |
| Clockwork Quarter Door | Travel to Clockwork Quarter | Gear tick visible |
| Sugar Rush Boulevard Door | Travel to Sugar Rush | Sweet color pulse |
| Exit (Back of lobby) | Leave Neocadia | Faint real-world static |

---

## Sound Design

### Ambient Loop
- Low frequency hum (electrical)
- Distant, muffled arcade sounds
- Soft reverb suggesting large space
- Occasional creak (old building settling)

### Dynamic Elements
| Restoration % | Audio Changes |
|--------------|---------------|
| 0-25% | Echo heavier, static crackle, silence gaps |
| 25-50% | Soft piano melody fades in, warmer tone |
| 50-85% | Full ambient track, more "present" arcade sounds |
| 85-100% | Rich orchestral undertone, chimes, life sounds |

### Sound Effects Needed
- Footsteps on marble (click-clack)
- Fountain: dry/trickle/flow/rush
- Chandelier chime
- Door portal hum (7 variants, one per zone)
- Paper rustle
- Cabinet open/close
- Daily reward reveal (magical chime)
- QWERTY typing sounds

---

## Asset List

### Environment
| Asset | Description | States |
|-------|-------------|--------|
| lobby_bg_floor | Checkerboard marble floor | 1 |
| lobby_bg_walls | Burgundy wallpaper with trim | 4 (decay levels) |
| lobby_bg_ceiling | Vaulted ceiling, fading to dark | 1 |
| lobby_chandelier | Brass/glass chandelier | 4 (restoration levels) |
| lobby_fountain | Central token fountain | 4 (restoration levels) |
| lobby_statue | Bronze figure with token | 2 (tarnished/gleaming) |
| lobby_desk | Registry desk | 1 |
| lobby_lamp | Brass desk lamp | 2 (dim/bright) |
| lobby_papers | Scattered desk papers | 1 |
| lobby_cabinet_row | Row of arcade cabinets | 1 |
| lobby_player_cabinet | Customizable player cabinet | Base + decals |
| lobby_hall_cases | Glass display cases | 3 |
| lobby_trophy_* | Trophy variants | 5 types |
| lobby_plaque_* | High score plaques | 10 (blank + populated) |
| lobby_lost_found | Lost & Found cabinet | 2 (closed/open) |

### Doors
| Asset | Description | States |
|-------|-------------|--------|
| door_neon | Chrome frame, neon trim | 4 (locked/unlocked/active/inviting) |
| door_pixel | Weathered wood, wave carving | 4 |
| door_glitch | Phase-shifting frame | 4 |
| door_cinema | Velvet curtains, marquee | 4 |
| door_clockwork | Brass gears frame | 4 |
| door_sugar | Candy-stripe frame | 4 |
| door_exit | Faint static threshold | 1 |

### Effects
| Asset | Description | Type |
|-------|-------------|------|
| fx_dust_motes | Floating dust particles | Particle system |
| fx_light_shaft | Amber light beam | Sprite |
| fx_fountain_water | Luminous water arcs | Animation (4 states) |
| fx_sparkle | Collectible indicator | Particle |
| fx_portal_glow | Door activation glow | Per-door variant |
| fx_token_burst | Token reward effect | Particle |

### UI Elements
| Asset | Description | Notes |
|-------|-------------|-------|
| ui_restoration_bar | Progress indicator | Shows in lobby HUD |
| ui_daily_spin | Fountain spin interface | Overlay |
| ui_leaderboard | Hall of Champions display | Overlay |
| ui_cabinet_interior | Player cabinet customization | Full interface |

---

## Implementation Notes

### Navigation Flow
```
Entry → Lobby (central)
       ├─→ Token Fountain (daily)
       ├─→ Registry Desk (QWERTY)
       ├─→ Hall of Champions (leaderboards)
       ├─→ Lost & Found (daily)
       ├─→ Player Cabinet (personal space)
       ├─→ Neon Alley Door → Neon Alley
       ├─→ Pixel Beach Door → Pixel Beach
       ├─→ Glitch Garden Door → Glitch Garden
       ├─→ Starlight Cinema Door → Starlight Cinema
       ├─→ Clockwork Quarter Door → Clockwork Quarter
       ├─→ Sugar Rush Door → Sugar Rush Boulevard
       └─→ Exit → Title Screen / Close
```

### Data Required
```typescript
interface LobbyState {
  restoration_percent: number;  // 0-100
  fountain_spun_today: boolean;
  lost_found_claimed_today: boolean;
  doors_unlocked: ZoneId[];
  hall_of_champions_data: LeaderboardEntry[];
}
```

### Restoration Triggers
- Fountain visual: 15%, 40%, 70%, 95%
- Chandelier bulbs: every 8.33%
- Music layer: 25%, 50%, 75%
- Background characters: 60%+
