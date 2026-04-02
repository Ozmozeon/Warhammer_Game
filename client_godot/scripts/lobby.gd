extends Control

func _ready() -> void:
	$VBoxContainer/BackButton.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/MainMenu.tscn"))
	$VBoxContainer/StartMatchButton.pressed.connect(_on_start_match_pressed)

func _on_start_match_pressed() -> void:
	get_tree().change_scene_to_file("res://scenes/Match.tscn")
