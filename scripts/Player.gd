extends KinematicBody2D

export var speed = 200

onready var animation_player = $AnimationPlayer
onready var sprite = $Sprite

func _physics_process(delta):
    var velocity = Vector2.ZERO
    if Input.is_action_pressed("ui_right"):
        velocity.x += 1
    if Input.is_action_pressed("ui_left"):
        velocity.x -= 1
    if Input.is_action_pressed("ui_down"):
        velocity.y += 1
    if Input.is_action_pressed("ui_up"):
        velocity.y -= 1

    velocity = velocity.normalized() * speed
    move_and_slide(velocity)

    update_animation(velocity)

func update_animation(velocity):
    if velocity.length() > 0:
        animation_player.play("walk")
    else:
        animation_player.play("idle")

    if velocity.x > 0:
        sprite.flip_h = false
    elif velocity.x < 0:
        sprite.flip_h = true
