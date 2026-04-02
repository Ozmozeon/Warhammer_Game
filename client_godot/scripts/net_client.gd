extends Node

signal connected_to_server
signal disconnected_from_server
signal message_received(payload)

var _ws := WebSocketPeer.new()
var _connected := false

func connect_to_server(url: String) -> int:
	var err := _ws.connect_to_url(url)
	if err != OK:
		return err
	set_process(true)
	return OK

func send_json(payload: Dictionary) -> void:
	if _ws.get_ready_state() == WebSocketPeer.STATE_OPEN:
		_ws.send_text(JSON.stringify(payload))

func _process(_delta: float) -> void:
	_ws.poll()
	var state := _ws.get_ready_state()
	if state == WebSocketPeer.STATE_OPEN and not _connected:
		_connected = true
		emit_signal("connected_to_server")
	elif state == WebSocketPeer.STATE_CLOSED and _connected:
		_connected = false
		emit_signal("disconnected_from_server")
		set_process(false)
		return

	while _ws.get_available_packet_count() > 0:
		var text := _ws.get_packet().get_string_from_utf8()
		var parsed := JSON.parse_string(text)
		if typeof(parsed) == TYPE_DICTIONARY:
			emit_signal("message_received", parsed)
