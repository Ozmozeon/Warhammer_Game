# Repository Architecture Baseline

This document tracks the intended base file structure so future work can be added without major repo reshuffles.

## Top-level layout

- `client_godot/` - Godot 4 client
- `server_py/` - Python host-authoritative server
- `shared_data/` - content and rules JSON + schemas
- `docs/` - specifications and technical design docs
- `tools/` - local scripts for validation/dev workflow

## Client layout

- `client_godot/scenes/`
  - `MainMenu.tscn`, `Lobby.tscn`, `Match.tscn`
  - `ui/` (future UI component scenes)
  - `units/` (future unit and effect scenes)
- `client_godot/scripts/`
  - core scene scripts (`main_menu.gd`, `lobby.gd`, `match.gd`)
  - `net/` (future protocol client adapters)
  - `systems/` (future input/render/gameplay client systems)
  - `ui/` (future UI controller scripts)
- `client_godot/assets/`
  - `sprites/`, `fonts/`

## Server layout

- `server_py/app/main.py` - process entrypoint
- `server_py/app/config.py` - runtime config
- `server_py/app/net/` - websocket/protocol transport
- `server_py/app/lobby/` - room/lobby state logic
- `server_py/app/sim/` - rules simulation systems
- `server_py/app/persistence/` - replay/save state support
- `server_py/app/services/` - cross-cutting helpers/registries
- `server_py/tests/` - unit/integration tests

## Docs layout

- `docs/SPEC.md` - product and gameplay spec
- `docs/protocol.md` - network message contracts
- `docs/state_model.md` - host simulation state model
- `docs/M1_TASKS.md` - incremental implementation checklist
