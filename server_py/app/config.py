from dataclasses import dataclass


@dataclass(frozen=True)
class ServerConfig:
    host: str = "0.0.0.0"
    port: int = 8765
    tick_rate_hz: int = 15
