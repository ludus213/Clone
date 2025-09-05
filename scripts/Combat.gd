extends Node2D

enum CombatState { PLAYER_TURN, ENEMY_TURN, BATTLE_OVER }

var state = CombatState.PLAYER_TURN

onready var player = $CombatPlayer
onready var enemy = $Enemy

func _ready():
    print("Combat started!")
    player.connect("attacked", self, "_on_Player_attacked")
    enemy.connect("died", self, "_on_Enemy_died")
    next_turn()

func next_turn():
    match state:
        CombatState.PLAYER_TURN:
            print("Player's turn.")
            # In a real game, you would enable player input here.
        CombatState.ENEMY_TURN:
            print("Enemy's turn.")
            enemy.attack(player)
            state = CombatState.PLAYER_TURN
            next_turn()

func _on_Player_attacked():
    if state == CombatState.PLAYER_TURN:
        enemy.take_damage(10)
        state = CombatState.ENEMY_TURN
        next_turn()

func _on_Enemy_died():
    print("Enemy defeated!")
    state = CombatState.BATTLE_OVER
    # In a real game, you would show a victory screen and
    # transition back to the overworld.
    get_tree().change_scene("res://scenes/Main.tscn")
