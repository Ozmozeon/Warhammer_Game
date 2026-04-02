extends Control

func _ready() -> void:
	$VBoxContainer/HostButton.pressed.connect(_on_host_pressed)
	$VBoxContainer/JoinButton.pressed.connect(_on_join_pressed)
	$VBoxContainer/QuitButton.pressed.connect(func(): get_tree().quit())

func _on_host_pressed() -> void:
	# Host bootstrap is handled by Python server process externally for now.
	get_tree().change_scene_to_file("res://scenes/Lobby.tscn")

func _on_join_pressed() -> void:
	# TODO: prompt host IP/port.
	get_tree().change_scene_to_file("res://scenes/Lobby.tscn")
