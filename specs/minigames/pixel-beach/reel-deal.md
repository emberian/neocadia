# Minigame Spec: Reel Deal

## Overview

### Telos
Reel Deal is meditation. It's the game you play when you don't want pressure—just the satisfaction of casting, waiting, and occasionally catching something wonderful. It represents Pixel Beach's philosophy: joy doesn't have to be intense.

### Ludos
Cast your line, wait for a bite, time your catch. Simple rhythm, satisfying feedback, collection depth. It's about patience rewarded and the occasional surprise.

---

## Core Loop

1. Select bait (determines possible catches)
2. Cast line (power meter)
3. Wait for bite (watch bobber)
4. React when fish bites (timing window)
5. Reel in with mini-game
6. Add to collection or sell for tokens

**Session Length**: 5-20 minutes typical

---

## Controls

### Mouse (Primary)
- Click + hold + release → Cast (power determines distance)
- Click when bobber dips → Hook fish
- Click rhythm → Reel in (timing-based)

### Keyboard (Alternative)
- Space → Cast / Hook / Reel
- 1-4 → Select bait

---

## Mechanics

### Casting
- Hold to charge (0-100% power)
- Power determines distance (affects fish available)
- Distance zones: Shore (0-30%), Mid (30-70%), Deep (70-100%)

### Waiting
- Bobber floats on water
- Small dips = nothing (false positives)
- Big dip + sound = fish!
- Wait time: 5-30 seconds (randomized)
- Patience bonus: +10% catch chance per 10s waited

### Hooking
- Timing window when fish bites
- Perfect (first 0.3s): Guaranteed catch
- Good (0.3-0.8s): 80% catch
- Late (0.8-1.5s): 50% catch
- Miss (>1.5s): Fish escapes

### Reeling
- Fish has stamina bar
- Click rhythm to reel (beat-based)
- Fish fights back (bar moves backward)
- Perfect rhythm = fast reel
- Stamina depleted = caught

### Bait System
| Bait | Cost | Target Zone | Fish Types | Rarity Boost |
|------|------|-------------|------------|--------------|
| Basic Worm | Free | Shore | Common | None |
| Pixel Grub | 10 | All | Common-Uncommon | +10% |
| Neon Lure | 25 | Mid-Deep | Uncommon-Rare | +25% |
| Golden Hook | 50 | Deep | Rare-Legendary | +50% |

---

## Fish Collection

### Rarity Tiers
| Tier | Catch Rate | Token Value | Collection % |
|------|-----------|-------------|--------------|
| Common | 60% | 5 | 1% per fish |
| Uncommon | 25% | 15 | 2% per fish |
| Rare | 12% | 40 | 3% per fish |
| Legendary | 3% | 100 | 5% per fish |

### Fish Types (50 total)
**Shore Fish (15)**
- Pixel Minnow (Common)
- Byte Bass (Common)
- Data Darter (Common)
- Code Carp (Uncommon)
- Static Sardine (Uncommon)
- Glitch Goldfish (Rare)
- etc.

**Mid Fish (20)**
- Neon Needlefish (Common)
- Cyan Snapper (Common)
- Resolution Ray (Uncommon)
- Refresh Remora (Uncommon)
- Scanline Salmon (Rare)
- Frame Rate Flounder (Rare)
- etc.

**Deep Fish (15)**
- Void Viperfish (Uncommon)
- Polygon Piranha (Rare)
- Shader Shark (Rare)
- Render Whale (Legendary)
- Source Code Squid (Legendary)
- The Forgotten One (Legendary - 0.5%)
- etc.

### Time/Weather Variants
- Some fish only appear at certain times (future feature)
- Weather affects spawn rates
- Special events = special fish

---

## Scoring & Rewards

### Per Catch
- Base tokens from rarity
- Size bonus: ±20% based on size (randomized)
- Perfect hook bonus: +10%
- First catch bonus: +50% (new species)

### Session Bonuses
- Variety: +5 tokens per 5 unique species
- Collection milestone: +50 tokens per tier complete
- Lucky streak: 3+ rare catches = bonus

### Token Conversion
```
tokens = sum(fish_values) + bonuses
```
No cap (encourages long sessions)

---

## Visual Style

### Aesthetic
- Full Pixel Beach integration
- 8-bit water with scanline waves
- Chunky pixel fish
- Warm, relaxing colors

### Pier View
- First-person from end of pier
- Water stretches to horizon
- Bobber visible at cast distance
- Occasional fish shadows

### Fish Designs
- Each fish: unique pixel sprite
- Size variance visible
- Rarity indicated by sparkle/glow
- Legendary fish have special effects

### UI Elements
- Bait selector: Bottom left
- Power meter: Near cast point
- Stamina bar: During reel
- Collection preview: Caught fish splash

---

## Audio

### Music
- Pixel Beach ambient continues
- Softer, more focused during wait
- Excitement build during reel

### Sound Effects
| Event | Sound |
|-------|-------|
| Cast | Whoosh + splash |
| Bobber land | Plop |
| False dip | Soft blip |
| Bite! | Sharp ding |
| Hook success | Satisfying click |
| Reel click | Rhythmic click |
| Fish fight | Splashing |
| Caught | Triumphant chime |
| Missed | Sad blip |
| New species | Special fanfare |

---

## Asset List

### Sprites
| Asset | Description | Variants |
|-------|-------------|----------|
| rd_rod | Fishing rod | 1 |
| rd_bobber | Bobber on water | Still/dip/bite |
| rd_line | Fishing line | Curved path |
| rd_bait_* | Bait icons | 4 types |
| rd_fish_* | All fish sprites | 50 fish |

### Effects
| Asset | Description | Type |
|-------|-------------|------|
| fx_splash | Water splash | Particle |
| fx_ripple | Bobber ripples | Animation |
| fx_catch_burst | Catch celebration | Particle |
| fx_legendary_glow | Rare fish effect | Glow shader |

### UI
| Asset | Description | Notes |
|-------|-------------|-------|
| rd_ui_power | Cast power meter | Charge bar |
| rd_ui_stamina | Reel stamina | Fish HP |
| rd_ui_bait | Bait selector | 4 slots |
| rd_ui_catch_splash | Fish caught display | Center screen |

---

## Implementation Notes

### State Machine
```
states: idle → casting → waiting → bite → hooking → reeling → caught/escaped
```

### Fish Selection
```typescript
function selectFish(zone: Zone, bait: Bait): Fish {
  const available = FISH_TABLE.filter(f =>
    f.zones.includes(zone) &&
    f.minBait <= bait.level
  );
  const weights = available.map(f =>
    f.baseRate * (1 + bait.rarityBoost)
  );
  return weightedRandom(available, weights);
}
```

### Save Data
```typescript
interface ReelDealSave {
  collection: Record<FishId, FishCatchData>;
  total_caught: number;
  legendary_caught: number;
  largest_catch: { fish: FishId, size: number };
}
```
