# Protocol (Draft)

## Transport
- WebSocket JSON messages.

## Message envelope
```json
{ "type": "message_name", "...": "payload" }
```

## Implemented
- `hello_ack`
- `state_delta`
- `phase_changed`
- `pong`

## Planned
- `join_room`, `lobby_state`, `submit_roster`, `roster_validation_failed`, `match_start`, `match_end`
