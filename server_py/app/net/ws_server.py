from __future__ import annotations

import asyncio
import json
from collections.abc import Awaitable, Callable

import websockets
from websockets.server import WebSocketServerProtocol

from .protocol import PROTOCOL_VERSION, make_message

ClientHandler = Callable[[WebSocketServerProtocol, dict], Awaitable[None]]


class WSServer:
    def __init__(self, host: str, port: int, on_message: ClientHandler) -> None:
        self.host = host
        self.port = port
        self.on_message = on_message
        self.connections: set[WebSocketServerProtocol] = set()

    async def _client_loop(self, websocket: WebSocketServerProtocol) -> None:
        self.connections.add(websocket)
        await websocket.send(json.dumps(make_message("hello_ack", protocol_version=PROTOCOL_VERSION)))
        try:
            async for raw in websocket:
                payload = json.loads(raw)
                await self.on_message(websocket, payload)
        finally:
            self.connections.discard(websocket)

    async def run(self) -> None:
        async with websockets.serve(self._client_loop, self.host, self.port):
            await asyncio.Future()

    async def broadcast(self, payload: dict) -> None:
        if not self.connections:
            return
        data = json.dumps(payload)
        await asyncio.gather(*(ws.send(data) for ws in self.connections))
