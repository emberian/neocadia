# HUD Specification

## Overview

The HUD (Heads-Up Display) provides persistent interface elements during exploration. It should be unobtrusive but always accessible.

### Design Principles
1. **Minimal intrusion** - Small, corner-positioned
2. **Glanceable info** - Key data at a glance
3. **Zone harmony** - Adapts to zone palette
4. **Expandable** - Quick access to more details

---

## HUD Layout

```
┌─────────────────────────────────────────────────────────────┐
│ [◄ Back] [🏠 Home]                              [⚙️ Menu]   │
│                                                             │
│ [🪙 1,234]              [The Lobby]           [🔔 New!]    │
│                                                             │
│                                                             │
│                                                             │
│                         (Play Area)                         │
│                                                             │
│                                                             │
│                                                             │
│                                                             │
│ [💬 Quest]                                    [Restoration] │
│                                               [████░░ 67%]  │
└─────────────────────────────────────────────────────────────┘
```

---

## HUD Elements

### Top Bar

#### Back Button (Top Left)
- Icon: ◄ arrow
- Position: 16px from top-left
- Action: Return to previous area
- Hidden: At main menu

#### Home Button (Top Left, Adjacent)
- Icon: 🏠 house
- Position: Next to back
- Action: Return to Lobby
- Confirmation: If in game

#### Zone Name (Top Center)
- Text: Current zone name
- Style: Zone-appropriate font color
- Animation: Fade on zone change

#### Menu Button (Top Right)
- Icon: ⚙️ gear or ≡ hamburger
- Position: 16px from top-right
- Action: Open main menu overlay

### Info Strip (Below Top Bar)

#### Token Counter (Left)
- Icon: 🪙 + number
- Shows current balance
- Animation: Count up on earn
- Click: Opens economy detail

#### Notification Badge (Right)
- Icon: 🔔 bell with pip
- Shows when: New content available
- Click: Opens notification list
- Badge count: Number of new items

### Bottom Bar

#### Quest Indicator (Bottom Left)
- Icon: 💬 speech or 📋 clipboard
- Shows: Current active quest step
- Click: Opens quest log
- Pulse: When quest progress made

#### Restoration Meter (Bottom Right)
- Visual: Progress bar
- Shows: Current zone OR overall %
- Click: Toggle zone/overall view
- Style: Fills with luminance color

---

## HUD States

### Normal Exploration
- All elements visible
- Semi-transparent backgrounds
- Full interactivity

### Dialogue Active
- HUD dims (50% opacity)
- Only back button active
- Dialogue box takes focus

### Game Active
- HUD replaced with game UI
- Pause button only
- Zone HUD hidden

### Cutscene Active
- HUD hidden completely
- Skip button available
- Returns after scene

### Menu Open
- HUD dims
- Menu overlay on top
- Click outside closes

---

## Responsive Behavior

### Token Counter
- Animates on change (+/-)
- Shows delta briefly (+50!)
- Returns to total

### Restoration Meter
- Animates on increase
- Glow effect at milestones
- Shake at 100%

### Notification Badge
- Bounces when new notification
- Number increments visibly
- Clears when viewed

---

## Zone Adaptation

### Color Theming
| Zone | HUD Accent Color |
|------|-----------------|
| Lobby | Gold |
| Neon Alley | Pink |
| Pixel Beach | Turquoise |
| Glitch Garden | Magenta |
| Starlight Cinema | Purple |
| Clockwork Quarter | Brass |
| Sugar Rush | Bubblegum |

### Background Adaptation
- HUD backgrounds slightly tinted to zone
- Maintains readability
- Subtle, not distracting

---

## Interaction Feedback

### Hover
- Element brightens
- Optional tooltip after 0.5s delay

### Click
- Brief press animation
- Sound feedback
- Immediate response

### Disabled State
- Grayed out
- No hover effect
- Cursor shows locked

---

## Minimized Mode (Optional)

For players who want less UI:

### Toggle
- Setting in options
- Keyboard shortcut: Tab

### Minimized State
- Only restoration meter visible
- Other elements appear on hover near edges
- Full HUD on any interaction

---

## Mobile Considerations

### Touch Targets
- All elements: Minimum 44px tap area
- Spacing: 8px minimum between elements
- Position: Avoid thumb zones for critical elements

### Portrait Mode
- HUD elements reflow
- Top bar stays top
- Bottom bar stays bottom
- Side bars collapse

---

## Technical Implementation

### Structure
```typescript
interface HUDState {
  visible: boolean;
  opacity: number;
  current_zone: ZoneId | null;
  token_count: number;
  restoration_mode: 'zone' | 'overall';
  notifications: Notification[];
  active_quest: Quest | null;
}
```

### Update Triggers
```typescript
// Token change
onTokenChange(delta: number) {
  animateTokenCounter(delta);
}

// Zone change
onZoneChange(newZone: ZoneId) {
  updateZoneName(newZone);
  updateColorTheme(newZone);
  updateRestoration(newZone);
}

// Notification
onNotification(notif: Notification) {
  incrementBadge();
  bounceIcon();
}
```

### Render Order
1. Game/exploration layer
2. HUD layer (always on top)
3. Menu/dialogue layer (on top of HUD when active)

---

## Accessibility

### High Contrast Mode
- Solid backgrounds instead of transparent
- Increased font weight
- Brighter accent colors

### Large Text Mode
- 125% / 150% / 175% scales
- HUD grows proportionally
- Elements reflow if needed

### Screen Reader
- All elements labeled
- Values announced on change
- Navigation described
