extends CanvasLayer

signal dialogue_finished

var dialogue_lines = []
var current_line_index = 0

onready var text_label = $Panel/RichTextLabel
onready var timer = $Timer

func _ready():
    set_process_input(false)
    text_label.bbcode_enabled = true
    text_label.text = ""

func start_dialogue(lines):
    dialogue_lines = lines
    current_line_index = 0
    show_current_line()
    set_process_input(true)
    show()

func _input(event):
    if event.is_action_pressed("ui_accept"):
        if text_label.percent_visible < 1:
            text_label.percent_visible = 1
        else:
            current_line_index += 1
            if current_line_index < dialogue_lines.size():
                show_current_line()
            else:
                set_process_input(false)
                hide()
                emit_signal("dialogue_finished")

func show_current_line():
    text_label.bbcode_text = dialogue_lines[current_line_index]
    text_label.percent_visible = 0
    # A short wait time for the timer will make the text appear character by character.
    # I'll set it to 0.05 seconds, which is a reasonable speed.
    timer.set_wait_time(0.05)
    timer.start()

func _on_Timer_timeout():
    text_label.percent_visible += 0.05
    if text_label.percent_visible < 1:
        timer.start()
