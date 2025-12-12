# Complete Asset List

## Overview

This document catalogues all visual assets needed for Neocadia. Organized by category, with priority tiers for production planning.

### Priority Tiers
- **P1**: MVP required (Lobby, Pixel Beach, Neon Alley)
- **P2**: Full release required
- **P3**: Polish/expansion

---

## Characters

### QWERTY (P1)
| Asset | Type | Variants |
|-------|------|----------|
| qwerty_base | Sprite | 1 |
| qwerty_glow | Overlay | 6 colors |
| qwerty_expressions | Overlay | 6 emotions |
| qwerty_idle | Animation | 8 frames |
| qwerty_talk | Animation | 12 frames |
| qwerty_celebrate | Animation | 16 frames |
| qwerty_float_text | Font | Retro terminal |

### NEON (P1)
| Asset | Type | Variants |
|-------|------|----------|
| neon_body_layers | Sprite | 3 (pink/cyan/purple) |
| neon_face | Overlay | 6 emotions |
| neon_idle | Animation | 12 frames |
| neon_talk | Animation | 8 frames |
| neon_announce | Animation | 10 frames |
| neon_victory | Animation | 16 frames |
| neon_glow | Effect | Bloom shader |

### PIXEL (P1)
| Asset | Type | Variants |
|-------|------|----------|
| pixel_body | Sprite | 1 (pixelated) |
| pixel_expressions | Overlay | 5 emotions |
| pixel_idle | Animation | 4 frames |
| pixel_talk | Animation | 4 frames |
| pixel_walk | Animation | 4 frames |
| pixel_wave | Animation | 6 frames |
| pixel_sparkle | Effect | Particle |

### VERA (P2)
| Asset | Type | Variants |
|-------|------|----------|
| vera_base | Sprite | 1 |
| vera_corruption | Overlay | 5 types |
| vera_expressions | Overlay | 6 emotions |
| vera_idle_early | Animation | 16 frames |
| vera_idle_late | Animation | 8 frames |
| vera_talk | Animation | 12 frames |
| vera_remember | Animation | 20 frames |

### CELIA (P2)
| Asset | Type | Variants |
|-------|------|----------|
| celia_projector | Sprite | 1 |
| celia_face | Overlay | 6 emotions |
| celia_reels | Animation | Rotation |
| celia_beam | Effect | Light cone |
| celia_idle | Animation | 8 frames |
| celia_dramatic | Animation | 16 frames |
| celia_filters | Shader | 4 era types |

### PROFESSOR COG (P2)
| Asset | Type | Variants |
|-------|------|----------|
| cog_body | Sprite | 1 |
| cog_chest | Animation | Gear loop |
| cog_expressions | Overlay | 6 emotions |
| cog_idle | Animation | 8 frames |
| cog_think | Animation | 10 frames |
| cog_teach | Animation | 12 frames |
| cog_winddown | Animation | 20 frames |

### SUCRE (P2)
| Asset | Type | Variants |
|-------|------|----------|
| sucre_base | Sprite | Modular |
| sucre_variants | Sprite | 6 flavor types |
| sucre_expressions | Overlay | 6 emotions |
| sucre_idle | Animation | 8 frames |
| sucre_excited | Animation | 12 frames |
| sucre_melt | Animation | 16 frames |
| sucre_transform | Animation | 24 frames |

---

## Environments

### The Lobby (P1)
| Asset | Type | Variants |
|-------|------|----------|
| lobby_bg_floor | Background | 1 |
| lobby_bg_walls | Background | 4 restoration |
| lobby_bg_ceiling | Background | 1 |
| lobby_chandelier | Sprite | 4 restoration |
| lobby_fountain | Sprite | 4 restoration + anim |
| lobby_desk | Sprite | 1 |
| lobby_cabinets | Sprite | Row + player custom |
| lobby_doors_* | Sprite | 7 doors × 4 states |
| lobby_lost_found | Sprite | 2 states |
| lobby_hall_cases | Sprite | 3 |

### Neon Alley (P1)
| Asset | Type | Variants |
|-------|------|----------|
| neon_bg_floor | Background | 4 restoration |
| neon_bg_walls | Background | 4 restoration |
| neon_bg_ceiling | Background | 1 |
| neon_stage | Sprite | 4 restoration |
| neon_tournament_board | Sprite | 4 + animation |
| neon_cabinet_* | Sprite | 3 games × 3 states |
| neon_lounge | Background | 1 |
| neon_lights | Effect | Pulse animation |
| neon_fog | Effect | Particle |

### Pixel Beach (P1)
| Asset | Type | Variants |
|-------|------|----------|
| beach_bg_sky | Background | 2 (day/dusk) |
| beach_bg_ocean | Background | Wave animation |
| beach_bg_sand | Background | 4 restoration |
| beach_shack | Sprite | 4 restoration |
| beach_pier | Sprite | 4 restoration |
| beach_palms | Sprite | 3 variants |
| beach_umbrellas | Sprite | 4 colors |
| beach_sandcastle | Sprite | 5 build stages |
| beach_shells | Sprite | 6 variants |

### Glitch Garden (P2)
| Asset | Type | Variants |
|-------|------|----------|
| glitch_bg_sky | Background | Animated shift |
| glitch_bg_ground | Background | 4 restoration |
| glitch_willow | Sprite | Multi-layer |
| glitch_fountain | Sprite | 4 + animation |
| glitch_gazebo | Sprite | Exterior + interior |
| glitch_roses | Sprite | 5 colors |
| glitch_trees | Sprite | Ghost overlay |
| glitch_boundary | Effect | Static wall |
| glitch_paths | Sprite | Impossible configs |

### Starlight Cinema (P2)
| Asset | Type | Variants |
|-------|------|----------|
| cinema_bg_auditorium | Background | 4 restoration |
| cinema_screen | Sprite | + content overlay |
| cinema_curtains | Animation | Open/close |
| cinema_seats | Sprite | 4 restoration |
| cinema_booth | Sprite | Exterior + interior |
| cinema_lobby | Background | 4 restoration |
| cinema_archives | Background | 1 |
| cinema_posters | Sprite | 8+ variants |

### Clockwork Quarter (P2)
| Asset | Type | Variants |
|-------|------|----------|
| clock_bg_floor | Background | 1 |
| clock_bg_walls | Background | 4 restoration |
| clock_orrery | Sprite | 4 + rotation |
| clock_workshop | Background | 4 restoration |
| clock_engine_door | Sprite | Locked/unlocked |
| clock_gears | Animation | Various sizes |
| clock_pipes | Sprite | 1 |
| clock_steam | Effect | Puff animation |

### Sugar Rush (P2)
| Asset | Type | Variants |
|-------|------|----------|
| sugar_bg_street | Background | 4 restoration |
| sugar_bg_sky | Background | 1 |
| sugar_bakery | Sprite | 4 restoration |
| sugar_fountain | Sprite | 4 states |
| sugar_stage | Sprite | Dark/lit |
| sugar_shops | Sprite | 3 types |
| sugar_lampposts | Sprite | Lollipop |
| sugar_fences | Sprite | Candy cane |

---

## Minigame Assets

### Void Breaker (P1)
| Asset | Count |
|-------|-------|
| Paddle variants | 3 |
| Ball + trail | 1 |
| Brick types | 7 |
| Power-ups | 6 |
| Particle effects | 5 |

### Synth Racer (P1)
| Asset | Count |
|-------|-------|
| Car + variants | 3 |
| Note types | 4 |
| Environment tiles | 10 |
| Effect layers | 5 |

### Pixel Invaders (P1)
| Asset | Count |
|-------|-------|
| Player ship | 1 |
| Enemy types | 5 |
| Boss variants | 3 |
| Projectiles | 6 |
| Effects | 8 |

### Reel Deal (P1)
| Asset | Count |
|-------|-------|
| Rod + bobber | 2 |
| Fish sprites | 50 |
| Bait types | 4 |
| Water effects | 4 |

### Wave Rider (P1)
| Asset | Count |
|-------|-------|
| Surfer poses | 8 |
| Wave segments | 4 |
| Obstacles | 3 |
| Background layers | 3 |

### Shell Shocked (P1)
| Asset | Count |
|-------|-------|
| Shell types | 10 |
| Board variants | 1 |
| Tide animation | 1 |
| Effects | 4 |

### (Additional P2 games follow same pattern)

---

## UI Elements

### Universal (P1)
| Asset | Description |
|-------|-------------|
| ui_token | Token currency icon |
| ui_button_* | Button styles (5) |
| ui_panel_* | Panel backgrounds (3) |
| ui_progress_bar | Generic progress |
| ui_icons_* | System icons (20+) |
| ui_cursor | Custom cursor |

### HUD (P1)
| Asset | Description |
|-------|-------------|
| hud_token_counter | Top corner display |
| hud_restoration | Progress indicator |
| hud_zone_name | Location label |
| hud_menu_button | Menu access |
| hud_notif_badge | Notification pip |

### Menus (P1)
| Asset | Description |
|-------|-------------|
| menu_main_bg | Main menu background |
| menu_pause_bg | Pause overlay |
| menu_settings | Settings panel |
| menu_collection | Collection viewer |

### Dialogue (P1)
| Asset | Description |
|-------|-------------|
| dialogue_box | Text box |
| dialogue_nameplate | Speaker indicator |
| dialogue_advance | Continue indicator |

---

## Effects & Particles

### Universal (P1)
| Effect | Type |
|--------|------|
| fx_token_collect | Particle burst |
| fx_sparkle | Generic sparkle |
| fx_transition | Scene wipe |
| fx_click | Click feedback |
| fx_hover | Hover indicator |

### Zone-Specific (P1-P2)
| Effect | Zone |
|--------|------|
| fx_dust_motes | Lobby |
| fx_neon_bloom | Neon Alley |
| fx_pixel_trail | Pixel Beach |
| fx_glitch_tear | Glitch Garden |
| fx_film_grain | Starlight Cinema |
| fx_steam_puff | Clockwork Quarter |
| fx_sugar_sparkle | Sugar Rush |

---

## Audio Assets (Reference)

See separate audio spec for full list. Visual team should coordinate with:
- UI sound sprites
- Character voice blips
- Ambient loops
- Music stems

---

## Production Estimates

### P1 (MVP)
- Characters: 3
- Environments: 3 zones
- Minigames: 6
- UI: Full set
- Estimated sprites: ~500

### P2 (Full Release)
- Characters: +5
- Environments: +4 zones
- Minigames: +12
- Estimated sprites: ~1500

### P3 (Polish)
- Variants and alternates
- Seasonal content
- User-generated support
- Estimated: Variable
