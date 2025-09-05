extends KinematicBody2D

signal attacked

export var speed = 300
var health = 100

func _physics_process(delta):
    var velocity = Vector2.ZERO
    if Input.is_action_pressed("ui_right"):
        velocity.x += 1
    if Input.is_action_pressed("ui_left"):
        velocity.x -= 1

    velocity = velocity * speed
    move_and_slide(velocity)

    if Input.is_action_just_pressed("ui_accept"):
        attack()

func attack():
    emit_signal("attacked")

func take_damage(amount):
    health -= amount
    print("Player took %d damage. Health is now %d" % [amount, health])
    if health <= 0:
        print("Player died!")
        get_tree().reload_current_scene() # Restart the battle
