from dataclasses import dataclass, field


@dataclass
class RoomState:
    room_code: str
    players: list[str] = field(default_factory=list)
    ready_players: set[str] = field(default_factory=set)
