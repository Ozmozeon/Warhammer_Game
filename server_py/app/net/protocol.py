from __future__ import annotations

from typing import Any


PROTOCOL_VERSION = "1.0.0"


def make_message(msg_type: str, **payload: Any) -> dict[str, Any]:
    return {"type": msg_type, **payload}
