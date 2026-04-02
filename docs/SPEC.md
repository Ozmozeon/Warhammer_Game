# Warhost Tactics – Product Specification (v1, Updated)

## 1. Product Overview

### 1.1 Vision
A simplified, real-time, multiplayer tactical game inspired by tabletop 40k-style play, designed for private games with friends.

### 1.2 Core Goals
- Real-time multiplayer for 2–6 players.
- One player hosts (host-authoritative simulation).
- Basic 2D top-down view.
- Pre-game army builder with points validation.
- Units support variable squad size, loadout/wargear options, and leader attachments.
- Army + detachment selection applies global buffs and unlocks stratagems.

### 1.3 Non-Goals (v1)
- Full official rules parity.
- Dedicated cloud backend mandatory for play.
- Advanced anti-cheat beyond host authority.
- 3D graphics.

## 2. Technology Stack

### 2.1 Chosen Stack
- Client/UI: Godot 4.x
- Host simulation server: Python 3.12+ (asyncio + websockets)
- Content definitions: JSON (+ JSON Schema validation)

### 2.2 Networking
- Host-authoritative over WebSocket (TCP).
- LAN + direct-IP/WAN support (manual port forwarding in v1).

## 3. Game Flow

1. Main Menu
2. Host/Join Lobby
3. Army Builder (required before ready)
4. Ready Check
5. Match Start
6. Real-time Gameplay
7. End Screen + Post-match stats
8. Return to lobby/rematch

## 4. Pre-Game Army Builder (New Required System)

Each player must submit a legal roster before match start.

### 4.1 Required selections
- Choose **Army/Faction**
- Choose **Detachment** (must be compatible with Army)
- Add units up to points cap
- Configure each unit:
  - squad size (legal min/max)
  - wargear/loadout
  - leader attachment (if eligible)

### 4.2 Points system
- Match has configurable points cap.
- Unit points come from:
  - size-based points bands (e.g., 5 models = 80, 10 models = 160), and/or
  - optional wargear/upgrade costs.
- Builder displays running total and blocks over-cap lists.

### 4.3 Validation (must pass before ready)
- Army/detachment compatibility
- Unit count limits
- Squad size constraints
- Composition role constraints
- Wargear legality
- Leader attachment legality
- Points cap compliance

## 5. Datasheet Model Requirements

Each `UnitDefinition` must include:

- Unit metadata (`id`, `name`, `faction`, keywords)
- Statline(s) for model roles
- Allowed squad size range (1–20 supported globally)
- Composition rules (e.g., 1 sergeant + 4–9 troopers)
- Points rules by squad size
- Default wargear
- Wargear replacement options with constraints
- Ability list
- Leader-join eligibility (for non-leader squads)
- Leader flag (for characters/leaders)

## 6. Wargear / Loadout Rules

### 6.1 Option types
- Model-specific replacement
- Role-specific replacement
- Quantity-limited upgrades
- Ratio-limited upgrades (e.g., 1 per 5 models)
- Mutually exclusive sets

### 6.2 Builder behavior
- Show only legal options for current squad configuration.
- Illegal combinations are blocked.
- Loadout changes update points and validations live.

## 7. Leader Attachment Rules

- Leaders can join eligible squads.
- Eligibility based on explicit rule mapping.
- Attached groups share rules/keywords per attachment definition.
- In-match targeting treats attached set according to rule config (combined or layered effects).

### 7.1 v1 simplification
- Attachments are fixed once match begins (no mid-match detach unless explicitly scripted later).

## 8. Army and Detachment System

### 8.1 Army (Faction Layer)
Provides:
- Army-wide keyword bundle
- Baseline faction rule package

### 8.2 Detachment (Sub-faction Layer)
Provides:
- Additional buffs/modifier rules
- Stratagem catalog available in-match
- Optional list-building restrictions

## 9. Stratagem System

### 9.1 Source
- Stratagems come from selected detachment.

### 9.2 Usage constraints
- Timing window (phase/trigger)
- Target legality
- Resource cost (CP)
- Usage limits (once/phase, once/turn, etc.)

### 9.3 v1 CP model
- Start with fixed CP pool.
- Spend CP on stratagem use.
- Optional per-turn CP gain (config-driven).

## 10. Real-Time Match Systems

### 10.1 Simulation authority
- Host is sole authority for movement, combat, scoring, and stratagem resolution.

### 10.2 Tick model
- Fixed tick (default 15 Hz).
- Commands validated/applied on tick boundary.
- Delta snapshots every tick + periodic full snapshot.

### 10.3 Core v1 actions
- Move
- Attack
- Use stratagem
- (Optional) use unit ability

## 11. Win Conditions

Primary v1 mode:
- Objective control scoring over time.
- Win by score cap or highest score at timer end.
- Tie-breakers configurable (e.g., elimination, objectives held).

## 12. UI/UX Requirements

### 12.1 Required screens
- Main Menu
- Host/Join
- Lobby
- Army Builder
- Match HUD
- End Screen

### 12.2 Army Builder UI
- Army selector
- Detachment selector
- Unit list
- Per-unit loadout editor
- Leader attachment controls
- Points breakdown and validation errors

### 12.3 In-match UI
- Score/timer
- CP display
- Stratagem panel
- Selected unit info
- Event feed
- Network/ping indicator

## 13. Data Architecture

### 13.1 Content files
- `armies.json`
- `detachments.json`
- `units.json`
- `stratagems.json`
- `maps.json`
- `rules.json`
- `content_manifest.json`

### 13.2 Runtime roster files
- `roster_player_X.json` (pre-match locked roster)

## 14. Validation & Testing

### 14.1 Content validation
- JSON Schema validation for all content assets.
- Cross-reference checks (IDs, compatibility links).

### 14.2 Gameplay tests
- Unit tests: movement/combat/stratagem constraints.
- Builder tests: legal/illegal roster cases.
- Deterministic replay tests for host sim.

### 14.3 Multiplayer tests
- 2-player smoke test.
- 4-player stability.
- 6-player stress.
- Disconnect/reconnect behavior.

## 15. Milestones

### M1 (Vertical Slice)
- 2 players, 1 map
- Army builder with points + squad size + wargear basics
- 1 army, 1 detachment
- Move/attack/objective loop
- 1–2 stratagems

### M2
- Leader attachments
- Expanded unit pool
- Better UI polish
- Reconnect flow

### M3
- 6-player optimization and balancing
- Expanded content set
- Playtest release candidate
