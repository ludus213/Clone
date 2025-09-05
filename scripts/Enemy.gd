extends KinematicBody2D

onready var animation_player = $AnimationPlayer

signal died

var health = 50

func _ready():
    animation_player.play("idle")

func attack(player):
    print("Enemy attacks!")
    player.take_damage(5)

func take_damage(amount):
    health -= amount
    print("Enemy took %d damage. Health is now %d" % [amount, health])
    if health <= 0:
        emit_signal("died")
        queue_free() # The enemy disappears
