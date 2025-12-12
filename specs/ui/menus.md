# Menu Specifications

## Overview

Menus in Neocadia should feel like part of the arcade—not jarring system interfaces, but extensions of the world.

---

## Main Menu (Title Screen)

### Layout
```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│                                                          │
│                    N E O C A D I A                       │
│               The Arcade Between Screens                 │
│                                                          │
│                                                          │
│                   [ Continue ]                           │
│                   [ New Game ]                           │
│                   [ Settings ]                           │
│                   [ Credits  ]                           │
│                                                          │
│                                                          │
│              Press any key to start                      │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Background
- Animated Neocadia vista
- Soft particle effects
- Zone colors shifting in background

### Options
| Button | Action |
|--------|--------|
| Continue | Load save, enter Lobby |
| New Game | Start fresh (confirm if save exists) |
| Settings | Open settings menu |
| Credits | Show credits scroll |

### First Time
- Only "New Game" available
- Tutorial flag set

---

## Pause Menu

### Trigger
- ESC key
- Menu button in HUD
- Not available during: cutscenes, transitions

### Layout
```
┌─────────────────────────────────────────┐
│                                         │
│              ║ PAUSED ║                 │
│                                         │
│              [ Resume  ]                │
│              [ Settings ]               │
│              [ How to Play ]            │
│              [ Quit to Menu ]           │
│                                         │
│         Press ESC to resume             │
│                                         │
└─────────────────────────────────────────┘
```

### Behavior
- Game state frozen
- Audio muted or lowered
- Background dimmed but visible
- Quick resume on ESC

---

## Settings Menu

### Categories
1. Audio
2. Display
3. Gameplay
4. Accessibility
5. Account (cloud save)

### Audio Settings
| Setting | Type | Range |
|---------|------|-------|
| Master Volume | Slider | 0-100 |
| Music Volume | Slider | 0-100 |
| SFX Volume | Slider | 0-100 |
| Mute When Unfocused | Toggle | On/Off |

### Display Settings
| Setting | Type | Options |
|---------|------|---------|
| Resolution | Dropdown | Auto, 720p, 1080p, 1440p, 4K |
| Fullscreen | Toggle | On/Off |
| Quality | Dropdown | Low, Medium, High |
| Show FPS | Toggle | On/Off |

### Gameplay Settings
| Setting | Type | Default |
|---------|------|---------|
| Auto-Fire | Toggle | Off |
| Show Tutorials | Toggle | On |
| Screen Shake | Toggle | On |
| Skip Animations | Toggle | Off |

### Accessibility Settings
| Setting | Type | Options |
|---------|------|---------|
| Colorblind Mode | Dropdown | None, Deuteranopia, Protanopia, Tritanopia |
| Reduce Motion | Toggle | Off |
| High Contrast | Toggle | Off |
| Text Size | Dropdown | Normal, Large, Extra Large |

---

## Game End Screen

### After Minigame Completion
```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│                   GAME COMPLETE!                         │
│                                                          │
│                  Score: 12,450                           │
│                  ★ Personal Best! ★                      │
│                                                          │
│             ┌─────────────────────┐                      │
│             │  Tokens Earned: 47  │                      │
│             └─────────────────────┘                      │
│                                                          │
│              [ Play Again ]   [ Exit ]                   │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Elements
- Final score (animated count-up)
- Personal best indicator (if achieved)
- Tokens earned (animated)
- Leaderboard position (if applicable)
- Play Again / Exit options

---

## Dialogue Box

### Layout
```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│    ┌────────────────────────────────────────────────┐    │
│    │                                                │    │
│    │  [Character Portrait]                          │    │
│    │                                                │    │
│    │  ┌──────────────────────────────────────────┐  │    │
│    │  │ Character Name                           │  │    │
│    │  │                                          │  │    │
│    │  │ "This is the dialogue text that appears  │  │    │
│    │  │  letter by letter, creating the feel of  │  │    │
│    │  │  the character speaking..."              │  │    │
│    │  │                                          │  │    │
│    │  │                              [▼ Continue] │  │    │
│    │  └──────────────────────────────────────────┘  │    │
│    │                                                │    │
│    └────────────────────────────────────────────────┘    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Behavior
- Text appears letter-by-letter (typewriter)
- Click to: Speed up → Complete → Continue
- Character portrait animates with speech
- Name box colored by character

### Choice Dialogue
```
│  │ "What do you want to do?"              │  │
│  │                                        │  │
│  │    > Help the character                │  │
│  │      Ask more questions                │  │
│  │      Leave                             │  │
```

---

## Collection Viewer

### Grid Layout
```
┌──────────────────────────────────────────────────────────┐
│  Fish Collection                    [12/50 collected]    │
│──────────────────────────────────────────────────────────│
│                                                          │
│  [🐟] [🐟] [??] [??] [??] [🐟] [??] [🐟] [??] [??]      │
│  [??] [🐟] [??] [??] [🐟] [??] [??] [??] [??] [??]      │
│  [??] [??] [??] [??] [??] [??] [??] [🐟] [??] [??]      │
│  [🐟] [??] [🐟] [??] [??] [🐟] [??] [??] [??] [??]      │
│  [🐟] [??] [??] [??] [??] [??] [??] [??] [??] [🐟]      │
│                                                          │
│──────────────────────────────────────────────────────────│
│  Selected: Pixel Minnow                                  │
│  "A common fish that pixelates when startled..."         │
│                                                          │
│                           [Close]                        │
└──────────────────────────────────────────────────────────┘
```

### Features
- Grid of items (collected shown, others silhouette)
- Click item for details
- Progress counter
- Sorting/filtering options
- Zone-themed border

---

## Quest Log

### Layout
```
┌──────────────────────────────────────────────────────────┐
│  Quest Log                                               │
│──────────────────────────────────────────────────────────│
│                                                          │
│  Active Quests                                           │
│  ─────────────                                           │
│  ▸ SYSTEM RESTORE (QWERTY)          Progress: 3/5       │
│    Current: Find lost keyboard keys                      │
│                                                          │
│  ▸ THE GREAT SANDCASTLE (PIXEL)     Progress: 2/5       │
│    Current: Gather pixel sand                            │
│                                                          │
│  ─────────────                                           │
│  Main Story                                              │
│  ─────────────                                           │
│  ▸ Act 1: Awakening                 Progress: 75%        │
│    Next: Restore the Token Fountain                      │
│                                                          │
│                           [Close]                        │
└──────────────────────────────────────────────────────────┘
```

---

## Confirmation Dialogs

### Standard Confirm
```
┌───────────────────────────────────┐
│                                   │
│   Are you sure you want to        │
│   quit to the main menu?          │
│                                   │
│   Progress will be saved.         │
│                                   │
│     [ Cancel ]   [ Confirm ]      │
│                                   │
└───────────────────────────────────┘
```

### Destructive Confirm
```
┌───────────────────────────────────┐
│                                   │
│   ⚠️ Start New Game?              │
│                                   │
│   This will DELETE your           │
│   existing save data.             │
│                                   │
│     [ Cancel ]   [ DELETE ]       │
│                                   │
└───────────────────────────────────┘
```

---

## Loading Screens

### Quick Load (< 2s)
- Simple "Loading..." text
- Zone-themed background

### Standard Load (2-5s)
```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│                    [Loading...]                          │
│               ████████████░░░░░░░░                       │
│                                                          │
│      "Every game played is a vote for joy."              │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Features
- Progress bar
- Tips/quotes rotate
- Zone preview image
- Never stays if load complete

---

## Common UI Components

### Buttons
- Primary: Zone accent color, rounded
- Secondary: Outlined, transparent
- Destructive: Red accent

### Sliders
- Track: Dark, subtle
- Thumb: Zone accent
- Fill: Gradient to accent

### Toggles
- Off: Gray, left
- On: Accent color, right
- Animation: Smooth slide

### Dropdowns
- Collapsed: Shows selection
- Expanded: Options below
- Hover: Highlight

### Progress Bars
- Background: Dark
- Fill: Luminance gold
- Animated: Shine effect

---

## Responsive Scaling

### Breakpoints
| Width | Layout |
|-------|--------|
| < 768px | Mobile layout |
| 768-1024px | Tablet layout |
| > 1024px | Desktop layout |

### Mobile Adaptations
- Larger buttons
- Single-column menus
- Bottom navigation
- Swipe gestures
