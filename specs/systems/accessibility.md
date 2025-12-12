# Accessibility System

## Overview

Neocadia should be playable by everyone. Accessibility isn't an afterthought—it's a core design principle. Every player deserves to experience the arcade.

### Guiding Principles
1. **Options, not compromises** - Accessibility settings enhance, never subtract
2. **Clear defaults, easy changes** - Work out of the box, customize when needed
3. **Multiple input methods** - Mouse, keyboard, and touch all supported
4. **No penalty for using assists** - Full game, full achievements, full experience

---

## Accessibility Settings

### Location
- Settings > Accessibility (dedicated section)
- Also prompted on first launch (optional quick setup)

### Visual Settings

| Setting | Options | Default | Description |
|---------|---------|---------|-------------|
| **Text Size** | Normal / Large / Extra Large | Normal | Scales all UI text (125% / 150%) |
| **High Contrast** | On / Off | Off | Solid backgrounds, bolder colors |
| **Colorblind Mode** | None / Deuteranopia / Protanopia / Tritanopia | None | Adjusts palette for color vision |
| **Reduce Motion** | On / Off | Off | Minimizes animations, removes particles |
| **Screen Shake** | On / Off | On | Disables camera shake effects |
| **Flash Effects** | On / Off | On | Reduces/removes flashing |
| **UI Opacity** | 50-100% | 80% | Transparency of HUD elements |
| **Hotspot Highlights** | Auto / Always / Off | Auto | Visibility of clickable areas |

### Audio Settings

| Setting | Options | Default | Description |
|---------|---------|---------|-------------|
| **Master Volume** | 0-100 | 100 | Overall audio level |
| **Music Volume** | 0-100 | 80 | Background music |
| **SFX Volume** | 0-100 | 100 | Sound effects |
| **Voice Volume** | 0-100 | 100 | Character dialogue (future) |
| **Audio Cues** | On / Off | On | Sound indicators for visual events |
| **Mute When Unfocused** | On / Off | On | Silence when tabbed away |

### Gameplay Settings

| Setting | Options | Default | Description |
|---------|---------|---------|-------------|
| **Auto-Fire** | On / Off | Off | Automatic shooting in action games |
| **Extended Timers** | Off / +50% / +100% | Off | More time for timed events |
| **Simplified Controls** | On / Off | Off | One-button mode where possible |
| **Tutorial Mode** | On / Off | On | In-game guidance (can toggle) |
| **Pause in Menus** | On / Off | On | Game pauses when menu open |
| **Skip Animations** | On / Off | Off | Faster transitions |

### Input Settings

| Setting | Options | Default | Description |
|---------|---------|---------|-------------|
| **Primary Input** | Mouse / Keyboard / Touch | Auto-detect | Preferred control method |
| **Mouse Sensitivity** | 0.5-2.0× | 1.0× | Cursor speed |
| **Click Assistance** | Off / Sticky / Magnetic | Off | Helps with precise clicking |
| **Key Repeat Delay** | 100-500ms | 200ms | Delay before key repeats |
| **Hold Duration** | 100-500ms | 200ms | Required time for "hold" actions |

---

## Visual Accessibility Details

### High Contrast Mode

**What changes**:
- HUD backgrounds: Transparent → Solid dark
- Text: Soft glow → Bold outline
- Buttons: Gradient → Solid colors with borders
- Interactive elements: Subtle glow → Strong outline

**Zone palettes in high contrast**:
| Zone | Standard | High Contrast |
|------|----------|---------------|
| Lobby | Warm gold | Bright yellow on black |
| Neon Alley | Soft neon | Bold magenta/cyan |
| Pixel Beach | Soft pastels | Strong blue/yellow |
| Glitch Garden | Shifting colors | Stable magenta/green |
| Starlight Cinema | Deep purples | Purple/gold borders |
| Clockwork Quarter | Warm brass | Orange/brown outlines |
| Sugar Rush | Soft pinks | Bright pink/white |

### Colorblind Modes

**Deuteranopia (red-green, most common)**:
- Red → Orange/yellow
- Green → Blue/cyan
- Enemy indicators use shape + color

**Protanopia (red-blind)**:
- Similar to deuteranopia adjustments
- Enhanced brightness for former-red elements

**Tritanopia (blue-yellow)**:
- Blue → Cyan/green
- Yellow → Pink/magenta

**Universal design rule**: Never rely on color alone. All important information has shape, icon, or text backup.

### Reduce Motion Mode

**What changes**:
- Scene transitions: Animated → Instant fade
- Particle effects: Full → Minimal or none
- Character animations: Full → Key frames only
- Background animations: Moving → Static
- Screen shake: Disabled
- Bobbing/floating: Disabled

**What stays**:
- Essential gameplay feedback
- Progress indicators
- UI state changes (still visible, just faster)

### Text Scaling

**Normal (100%)**:
- Body: 14px
- Headers: 18-24px
- HUD: 12-14px

**Large (125%)**:
- Body: 17px
- Headers: 22-30px
- HUD: 15-17px
- UI reflows as needed

**Extra Large (150%)**:
- Body: 21px
- Headers: 27-36px
- HUD: 18-21px
- Some UI elements simplify to fit

---

## Audio Accessibility Details

### Audio Cues

Visual events that get audio equivalents:
| Visual Event | Audio Cue |
|--------------|-----------|
| Hotspot available | Soft chime when cursor nears |
| New notification | Bell tone |
| Quest progress | Rising note |
| Token earned | Coin clink |
| Error/invalid action | Low buzz |
| Timer warning | Ticking accelerates |
| Success | Triumphant chord |
| Failure | Descending tones |

### Subtitles & Captions

All dialogue has text display (default: ON).

Caption options:
- **Speaker labels**: "QWERTY: Hello!"
- **Background sounds**: [Keys clacking]
- **Music cues**: [Tense music begins]
- **Caption size**: Scales with text size setting

---

## Input Accessibility Details

### Keyboard Navigation

Full keyboard control is possible throughout the game:

**Universal Keys**:
| Key | Action |
|-----|--------|
| Tab | Cycle through interactive elements |
| Enter/Space | Activate focused element |
| Escape | Back/Close/Pause |
| Arrow keys | Navigate within menus |
| H | Open help |
| M | Toggle mute |
| F11 | Toggle fullscreen |

**Minigame Keys**:
Each minigame has documented keyboard alternatives (see individual specs).

### Click Assistance

**Sticky Clicking**:
- Click to select, click again to confirm
- Reduces need for precision
- Helpful for motor difficulties

**Magnetic Targeting**:
- Cursor "snaps" slightly toward clickable elements
- Subtle assistance, doesn't override player intent
- Adjustable strength

### One-Button Mode (Simplified Controls)

For players who need minimal input:
- Single button/click performs context-appropriate action
- Timing requirements extended
- Multi-input sequences replaced with single inputs
- Full gameplay possible, just streamlined

---

## Per-Game Accessibility

### Action Games (Neon Alley)

| Assist | Effect |
|--------|--------|
| Auto-fire | Player shoots automatically |
| Extended timing | More time to react |
| Wider hitboxes | Easier dodging |
| Invincibility frames | Brief immunity after hit |

### Puzzle Games (Clockwork Quarter, Glitch Garden)

| Assist | Effect |
|--------|--------|
| Unlimited time | No time pressure |
| Hint system | On-demand suggestions |
| Undo moves | Take back mistakes |
| Solution preview | See target state |

### Relaxed Games (Pixel Beach)

| Assist | Effect |
|--------|--------|
| Extended windows | More time to react |
| Simplified reeling | One-click fishing |
| Guaranteed catches | No failure state |

### Trivia/Narrative (Starlight Cinema)

| Assist | Effect |
|--------|--------|
| Extended timer | More reading time |
| Extra lives | More chances |
| Hint elimination | Remove wrong answers |

---

## Screen Reader Support

### ARIA Implementation

All interactive elements include:
- `aria-label`: Descriptive name
- `aria-describedby`: Detailed description when needed
- `aria-live`: Announcements for state changes
- `role`: Proper element identification

### Navigation Announcements

Screen readers hear:
- Current location: "The Lobby. Token Fountain, Registry Desk, Hall of Champions, 6 Zone Doors"
- Focus changes: "Token Fountain, sparkle available"
- State changes: "Tokens: 1,234. Increased by 50"
- Actions: "Door to Pixel Beach. Press Enter to travel"

### Game Compatibility

| Game Type | Screen Reader Experience |
|-----------|-------------------------|
| Exploration | Full audio description of areas |
| Dialogue | Complete text access |
| Trivia | Questions read aloud |
| Action | Limited (primarily visual) |
| Puzzle | Depends on puzzle type |

**Honest limitation**: Some minigames are inherently visual. We provide audio cues where possible but acknowledge limits.

---

## Testing & Compliance

### Testing Checklist

- [ ] All features keyboard-accessible
- [ ] All text scales properly
- [ ] Colorblind modes tested with simulators
- [ ] Screen reader tested with NVDA/VoiceOver
- [ ] No flashing >3Hz (seizure safety)
- [ ] All audio has visual alternative
- [ ] All visual feedback has audio alternative
- [ ] Touch targets minimum 44px
- [ ] Focus indicators visible
- [ ] Motion can be disabled

### WCAG 2.1 Targets

**Level AA compliance** for all UI elements:
- 4.5:1 contrast ratio for normal text
- 3:1 for large text and UI components
- Focus visible
- Resize to 200% without loss
- Consistent navigation
- Error identification

---

## Implementation Notes

### Settings Persistence
```typescript
interface AccessibilitySettings {
  visual: {
    text_size: 'normal' | 'large' | 'extra_large';
    high_contrast: boolean;
    colorblind_mode: ColorblindMode | null;
    reduce_motion: boolean;
    screen_shake: boolean;
    flash_effects: boolean;
    ui_opacity: number;
    hotspot_highlights: 'auto' | 'always' | 'off';
  };
  audio: {
    master_volume: number;
    music_volume: number;
    sfx_volume: number;
    audio_cues: boolean;
    mute_unfocused: boolean;
  };
  gameplay: {
    auto_fire: boolean;
    extended_timers: 'off' | '50' | '100';
    simplified_controls: boolean;
    tutorials_enabled: boolean;
  };
  input: {
    primary_input: 'mouse' | 'keyboard' | 'touch' | 'auto';
    mouse_sensitivity: number;
    click_assistance: 'off' | 'sticky' | 'magnetic';
    key_repeat_delay: number;
    hold_duration: number;
  };
}
```

### CSS Custom Properties

Accessibility-affected values use CSS variables:
```css
:root {
  --text-scale: 1;
  --motion-reduce: 0;
  --contrast-boost: 0;
  --ui-opacity: 0.8;
}

.high-contrast {
  --contrast-boost: 1;
  --ui-opacity: 1;
}

.reduce-motion {
  --motion-reduce: 1;
}
```

### Testing Tools

- Color contrast: Stark / Colour Contrast Analyser
- Colorblind simulation: Sim Daltonism / Color Oracle
- Screen reader: NVDA (Windows) / VoiceOver (Mac)
- Keyboard testing: Unplug mouse, use Tab
- Motion sensitivity: User testing with vestibular disorders
