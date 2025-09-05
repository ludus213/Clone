extends Control

onready var label = $Label
onready var timer = $Timer

var story_text = [
    "In a world where magic and technology intertwine...",
    "Two factions, the Arcane and the Machinists, lived in a fragile peace.",
    "But the balance was shattered when a powerful artifact, the Chronos Crystal, was stolen.",
    "Now, a young hero must embark on a journey to recover the crystal and restore harmony to the world.",
    "This is your story."
]
var current_line = 0

func _ready():
    label.text = ""
    timer.start()

func _on_Timer_timeout():
    if current_line < story_text.size():
        label.text = story_text[current_line]
        current_line += 1
        timer.start()
    else:
        get_tree().change_scene("res://scenes/MainMenu.tscn")
