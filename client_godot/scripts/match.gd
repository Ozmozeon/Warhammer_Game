extends Node2D

const INCH_TO_WORLD := 10.0
const BOARD_WIDTH_IN := 60.0
const BOARD_HEIGHT_IN := 40.0

func _ready() -> void:
	queue_redraw()

func _draw() -> void:
	# Simple 60x40 inch board using 10 world units per inch.
	var rect := Rect2(0, 0, BOARD_WIDTH_IN * INCH_TO_WORLD, BOARD_HEIGHT_IN * INCH_TO_WORLD)
	draw_rect(rect, Color(0.08, 0.08, 0.08), true)
	draw_rect(rect, Color(0.7, 0.7, 0.7), false, 2.0)
