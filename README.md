# Warhost Tactics (Prototype Scaffold)

## What this adds
- `client_godot/`: minimal Godot 4 project with MainMenu, Lobby, and Match scenes.
- `server_py/`: minimal Python host-authoritative websocket server scaffold.
- `shared_data/`: data + schema files for armies, units, detachments, maps, rules, and stratagems.
- `tools/validate_content.py`: JSON and optional schema validation script.

## Run server
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r server_py/requirements.txt
python server_py/app/main.py
```

## Run content validation
```bash
python tools/validate_content.py
```

## Open client
Open `client_godot/project.godot` in Godot 4.x and press Play.
