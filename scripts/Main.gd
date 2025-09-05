extends Node2D

const DialogueBox = preload("res://scenes/DialogueBox.tscn")

func _on_DialogueTrigger_body_entered(body):
    if body.name == "Player":
        var dialogue_box = DialogueBox.instance()
        add_child(dialogue_box)
        dialogue_box.start_dialogue([
            "Hello, player!",
            "This is a test of the dialogue system.",
            "I hope you like it.",
            "You can use BBCode to make text [b]bold[/b] or [i]italic[/i].",
            "You can also make it [color=red]red[/color] or [color=green]green[/color].",
            "Or even... [shake rate=5 level=10]shaky[/shake]!"
        ])
        # To prevent the dialogue from triggering again immediately,
        # we can disable the trigger area.
        $DialogueTrigger.get_node("CollisionShape2D").set_deferred("disabled", true)

func _on_CombatTrigger_body_entered(body):
    if body.name == "Player":
        get_tree().change_scene("res://scenes/Combat.tscn")
