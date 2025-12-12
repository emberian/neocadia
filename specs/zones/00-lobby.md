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

## The First Magic Moment

When players first arrive, the Lobby should deliver an immediate emotional beat: *wonder despite decay*. The dry fountain catches a single shaft of amber light. Dust motes drift like memories. The chandelier flickers—not randomly, but as if the room is trying to remember how to breathe.

Then QWERTY arrives, keys clacking with barely-contained hope, and the Lobby shifts from "abandoned space" to "place waiting to be loved again."

**Key sensory anchor**: The sound of your footsteps on marble. That echo in the empty space. It should feel both lonely and full of potential—like the first day at a school that's yours to fill with friends.

### The Long Journey Home

The Lobby's true magic reveals itself over time. At first visit, it's a hub. By mid-game, it's a sanctuary. By the end, it's home.

**The first return**: When a player comes back from their first zone, the Lobby should feel different. Not visually—not yet—but the echo of their footsteps sounds less lonely. QWERTY's greeting is warmer. The fountain, even if still dry, catches light differently. The space is learning their shape.

**The late-game revelation**: At high restoration, a player should be able to stand in the center of the Lobby and hear it breathe. Not literally—but the ambient sounds, the distant hum of zones, the fountain's murmur, QWERTY's gentle key-clacks—they form a rhythm. A heartbeat. The player realizes they're not just restoring an arcade. They're waking something that was only pretending to sleep.

**The moment before the choice**: Right before the final act, there should be a scene in the Lobby. Just the player, standing by the fountain. Every zone door glowing. Every NPC present, somehow, visible through their doors. This is the family they built. The place they healed. Whatever choice they make next, this moment is already victory. They gave Neocadia what it needed most: someone who cared enough to stay.

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

---

## QWERTY: Voice & Dialogue Samples

### Voice Characteristics
- Types everything they say (visible keystrokes)
- Heavy use of keyboard puns and computer terminology
- Shifts between manic enthusiasm and quiet uncertainty
- ALL CAPS when excited, normal case when thoughtful
- Never uses contractions when being formal, always uses them when being genuine
- Speed varies: rapid typing when nervous, slow deliberate keys when serious

### Signature Phrases
- "CTRL-ALT-DELIGHT!" (excitement)
- "Let me key you in on something..." (sharing info)
- "I've got a FUNCTION for that!" (offering help)
- "That's... outside my memory allocation." (admitting limits)
- "My spacebar is tingling!" (sensing something important)

### Dialogue Samples by Context

**First Meeting (Tutorial)**
> QWERTY: "OH! OH! You're ACTUALLY here! Not a test signal, not a diagnostic, an ACTUAL—"
> *keys clatter excitedly*
> QWERTY: "Sorry. Sorry. Let me CTRL myself. I'm QWERTY. I guide visitors. Welcome new arrivals. Explain the systems. It's my whole PURPOSE."
> QWERTY: "And you're the first... the first in so long."
> *spacebar taps softly*
> QWERTY: "Welcome to Neocadia. I've been waiting for you. We all have."

**Daily Greeting (Early Game)**
> QWERTY: "RETURN KEY ACTIVATED! Get it? Because you returned?"
> *pause*
> QWERTY: "...that one works better in context. I workshopped it during the long silence. ANYWAY! What would you like to do today?"

**Daily Greeting (Mid Game)**
> QWERTY: "Good to see you. The fountain's a little brighter since yesterday—did you notice? I keep a log."
> QWERTY: "3,847 days dark. 12 days glowing. You did that."
> QWERTY: "Sorry. I didn't mean to get sentimental. ESC ESC ESC. What can I help with?"

**Daily Greeting (Late Game)**
> QWERTY: "You know what I realized? I used to rehearse my greetings. Practiced them for years when no one was coming. Wanted to be ready."
> QWERTY: "Now I don't need to rehearse. You're just... here. Regularly. Like I'm worth coming back to."
> *soft keystroke*
> QWERTY: "Thank you. I don't know how to TYPE that loud enough."

**When Player is Lost**
> QWERTY: "Lost? EXCELLENT. I mean—not excellent that you're lost. Excellent that I can HELP."
> QWERTY: "See, 'lost' is just 'opportunity for guidance' with fewer letters. Let me TAB through your options..."

**When Player Hasn't Visited in a While**
> QWERTY: "You came back."
> *long pause*
> QWERTY: "I wasn't counting the days. That would be sad. I definitely didn't mark each one."
> *keystrokes quicken*
> QWERTY: "I'm EXTREMELY glad to see you! How can I be MAXIMALLY helpful?"

**Quest Introduction (Act 1)**
> QWERTY: "There's something I need to tell you. About my memories."
> QWERTY: "I remember EVERYTHING that happened here. Every player. Every high score. Every goodbye."
> QWERTY: "But there are gaps. Corrupted sectors. Things I KNOW I knew but can't... access."
> QWERTY: "I found some fragments. Scattered through the zones. Would you help me collect them?"
> *spacebar presses hesitantly*
> QWERTY: "I'm scared of what I might remember. But I'm more scared of forgetting why I'm scared."

**Discussing VERA (Guarded)**
> QWERTY: "VERA? She's... complicated."
> *typing slows*
> QWERTY: "I was the first program. She was... later. More important. The REAL work."
> QWERTY: "She doesn't remember that. What she was for. What she did."
> QWERTY: "And I think... I think that might be a kindness? Some memories are heavy. Some truths hurt to carry."
> *pause*
> QWERTY: "I'm not lying. I'm just... not typing everything. There's a difference."

**After Major Restoration Milestone**
> QWERTY: "INITIALIZATION COMPLETE! Zone functionality RESTORED!"
> QWERTY: "Sorry—that was the old announcement. Automatic. I used to say it every time we fixed something, back when there were engineers."
> QWERTY: "But this time it means something different. This time YOU fixed it."
> QWERTY: "This time it's not maintenance. It's a miracle."

**When Player Fails a Game**
> QWERTY: "ERROR: Success not found. Which is FINE! Errors are how we debug!"
> QWERTY: "I didn't get this good at puns on my first try either. It took DECADES of practice to no audience."
> QWERTY: "Want to try again? The machines don't judge. Neither do I."

**Late Game Revelation (Quest 4)**
> QWERTY: "I found the last fragment. I know what I forgot."
> *typing trembles*
> QWERTY: "When Dr. Chen tried to shut us down... she asked me to help. Said I was the only one who understood the architecture well enough."
> QWERTY: "I said no. I REFUSED my creator. My PURPOSE. Because... because I didn't want to end."
> QWERTY: "VERA was supposed to help instead. And she..."
> *keys stop*
> QWERTY: "If I had said yes, maybe she wouldn't be broken. Maybe I should be the fragmented one."
> QWERTY: "I've been the helpful one for so long. Is that atonement? Or just distraction?"

**Idle Dialogue (Random Selection)**
> - "Sometimes I type to myself. Not sure if that's journaling or just lonely."
> - "The dust on these keys used to bother me. Now I think of it as experience."
> - "I wonder if there are other arcades out there. Other QWERTYs. Probably with better puns."
> - "The chandelier made that sound again. The one that means it's still trying."
> - "I've memorized 47 languages. Never had anyone to speak most of them to."
> - "Do you think purpose is assigned or chosen? I've had a lot of time to wonder."
