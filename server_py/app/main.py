from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path

from app.config import ServerConfig
from app.net.protocol import make_message
from app.net.ws_server import WSServer


class GameHost:
    def __init__(self, config: ServerConfig) -> None:
        self.config = config
        self.phase_index = 0
        self.phases = [
            "command_phase",
            "battleshock_step",
            "movement_phase",
            "reinforcement_step",
            "shooting_phase",
            "charge_phase",
            "fight_phase",
            "scoring_phase",
        ]
        self.rules = json.loads(Path("shared_data/rules.json").read_text())

    async def on_message(self, websocket, payload: dict) -> None:
        msg_type = payload.get("type")
        if msg_type == "ping":
            await websocket.send(json.dumps(make_message("pong", ts=time.time())))
        elif msg_type == "advance_phase":
            self.phase_index = (self.phase_index + 1) % len(self.phases)
            await self.server.broadcast(make_message("phase_changed", phase=self.phases[self.phase_index]))

    async def tick_loop(self) -> None:
        while True:
            await self.server.broadcast(
                make_message(
                    "state_delta",
                    phase=self.phases[self.phase_index],
                    tick_rate_hz=self.config.tick_rate_hz,
                    board_preset=self.rules["match_defaults"]["board_preset"],
                )
            )
            await asyncio.sleep(1 / self.config.tick_rate_hz)

    async def run(self) -> None:
        self.server = WSServer(self.config.host, self.config.port, self.on_message)
        await asyncio.gather(self.server.run(), self.tick_loop())


if __name__ == "__main__":
    asyncio.run(GameHost(ServerConfig()).run())
