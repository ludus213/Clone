extends Control

onready var label = $Label

var story_text = [
    "In a world where magic and technology intertwine...",
    "Two factions, the Arcane and the Machinists, lived in a fragile peace.",
    "But the balance was shattered when a powerful artifact, the Chronos Crystal, was stolen.",
    "Now, a young hero must embark on a journey to recover the crystal and restore harmony to the world.",
    "This is your story."
]
var current_line = 0

func _ready():
    show_next_line()

func _unhandled_input(event):
    if event.is_action_pressed("ui_accept"):
        show_next_line()

func show_next_line():
    if current_line < story_text.size():
        label.text = story_text[current_line]
        current_line += 1
    else:
        get_tree().change_scene("res://scenes/MainMenu.tscn")
