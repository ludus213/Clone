extends Control

func _on_NewGameButton_pressed():
    get_tree().change_scene("res://scenes/Intro.tscn")

func _on_SettingsButton_pressed():
    print("Settings button pressed")
    # I will implement the settings menu later.

func _on_QuitButton_pressed():
    get_tree().quit()
