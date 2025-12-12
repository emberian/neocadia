# Art Direction

## Overview

Neocadia's visual identity must balance seven distinct zone aesthetics while maintaining a cohesive "arcade that exists between screens" feeling. Every image should feel like a place you'd want to visit.

### Core Principle
*"Beautiful nostalgia, not dated. Stylized, not realistic. Inviting, not intimidating."*

---

## Overall Style

### Medium
- **2D illustrated art** for all environments and characters
- **Vector-based** where possible for scalability
- **Limited texture** (clean reads over gritty detail)
- **Strong silhouettes** for instant readability

### Influences
- Early 2000s Flash game aesthetics (Neopets, Homestar Runner)
- Modern indie games (Hollow Knight's environmental storytelling)
- Synthwave album art (for Neon Alley specifically)
- Studio Ghibli backgrounds (warmth, lived-in detail)
- Classic arcade cabinet art

### What We're NOT
- Realistic/photographic
- Grimdark or gritty
- Overly simple/flat
- Inconsistent between zones

---

## Character Proportions

### Standard
- **3 heads tall** for most characters
- Slightly chibi but not extreme
- Large, expressive features
- Clear silhouettes

### Exceptions
- VERA: More realistic proportions (5 heads), ethereal
- Professor COG: Taller (4 heads), imposing
- PIXEL: Tiny (2 heads worth), cute

### Expression Priority
- Face readable at small sizes
- Emotion conveyed through body language too
- Distinct idle animations per character

---

## Environmental Depth

### Layer Structure
1. **Far Background** - Sky, distant elements (minimal detail)
2. **Mid Background** - Zone structures (moderate detail)
3. **Play Area** - Where interaction happens (full detail)
4. **Foreground** - Occasional overlay elements
5. **UI Layer** - Interface elements

### Parallax
- Gentle parallax scrolling in exploration
- Creates depth without distraction
- 3-4 layers typical

### Scale Reference
- Player avatar: ~80px at 1080p
- NPCs: Similar or larger
- Interactables: Clear, slightly oversized

---

## Lighting Philosophy

### Per-Zone Lighting

| Zone | Light Source | Quality | Shadow |
|------|--------------|---------|--------|
| Lobby | Chandelier, windows | Warm amber | Soft, diffuse |
| Neon Alley | Neon tubes | Electric, stark | Hard, colored |
| Pixel Beach | Sun | Bright, cheerful | Crisp, short |
| Glitch Garden | Ambient/corrupted | Shifting, uncertain | Glitched |
| Starlight Cinema | Projector, spotlights | Dramatic, focused | Deep, theatrical |
| Clockwork Quarter | Oil lamps, brass | Industrial warm | Mechanical |
| Sugar Rush | Candy glow | Bright, saturated | Soft, minimal |

### Time of Day
- Lobby: Always golden hour feel
- Pixel Beach: Option for sunset variant
- Others: Fixed lighting

---

## Animation Principles

### Frame Rates
- **UI/Characters**: 30 FPS
- **Games**: 60 FPS
- **Background loops**: 15-30 FPS (efficiency)

### Character Animation
- Idle: 4-8 frames, subtle loop
- Talk: 4-8 frames, lip-sync optional
- Special: 8-16 frames, more elaborate

### Environmental Animation
- Ambient: Very slow, subtle
- Interactive: Responsive, snappy
- Effects: Smooth, particle-based

### Principles
- Squash and stretch (within style)
- Anticipation before big movements
- Overshooting for energy
- Holds on key poses

---

## Resolution Targets

### Base Resolution
- Designed at **1920×1080**
- Scales down to 1280×720
- Scales up to 4K (vector where possible)

### Asset Sizes
- Characters: 256px height (base)
- Environment tiles: 64px or 128px
- UI elements: Vectorized

### Mobile Consideration
- Touch targets: Min 44px
- Text: Min 14px rendered
- UI scales for portrait/landscape

---

## Image Generation Guidance

When using AI image generation (Google Imagen or similar):

### Prompt Structure
```
[Style keywords], [Subject], [Environment/Context], [Mood/Lighting], [Color notes], [What to avoid]
```

### Example Prompts

**Character**:
```
2D game character illustration, flat colors, clean lines, [character description], standing pose, full body, white background, in the style of modern indie games, colorful, not realistic, not 3D
```

**Environment**:
```
2D game background art, illustrated arcade [zone name], [specific details], [lighting], [palette colors], in the style of hand-painted game backgrounds, detailed but not photorealistic, inviting atmosphere
```

### Style Keywords to Use
- "2D illustrated"
- "Clean vector style"
- "Indie game art"
- "Warm/vibrant colors"
- "Stylized not realistic"
- "Flat shading with soft gradients"

### Keywords to Avoid
- "Realistic"
- "Photographic"
- "3D render"
- "Hyperdetailed"
- "Dark/gritty"

---

## Technical Requirements

### File Formats
- **Raster**: PNG with transparency
- **Vector**: SVG for UI elements
- **Animation**: Sprite sheets or Spine

### Naming Convention
```
[zone]_[category]_[name]_[variant].[ext]
```
Examples:
- `lobby_bg_fountain_restored.png`
- `neon_char_neon_talk_01.png`
- `pixel_fx_wave_spray.png`

### Export Settings
- PNG: 32-bit with alpha
- No compression artifacts
- Power-of-two dimensions where needed

---

## Quality Checklist

Before finalizing any asset:

- [ ] Silhouette reads clearly at 50% size
- [ ] Colors match zone palette
- [ ] Style consistent with existing assets
- [ ] Appropriate level of detail
- [ ] Animation loops cleanly
- [ ] No unintended artifacts
- [ ] Exported at correct resolution
- [ ] Named according to convention
