import numpy as np
from PIL import Image, ImageDraw
from pyxelate import Pyx, Pal
import os
from skimage import io
import random

# PICO-8 Palette Colors
PICO8_BLACK = (0, 0, 0)
PICO8_DARK_BLUE = (29, 43, 83)
PICO8_DARK_PURPLE = (126, 37, 83)
PICO8_DARK_GREEN = (0, 135, 81)
PICO8_BROWN = (171, 82, 54)
PICO8_DARK_GREY = (95, 87, 79)
PICO8_LIGHT_GREY = (194, 195, 199)
PICO8_WHITE = (255, 241, 232)
PICO8_RED = (255, 0, 77)
PICO8_ORANGE = (255, 163, 0)
PICO8_YELLOW = (255, 236, 39)
PICO8_GREEN = (0, 228, 54)
PICO8_BLUE = (41, 173, 255)
PICO8_INDIGO = (131, 118, 156)
PICO8_PINK = (255, 119, 168)
PICO8_PEACH = (255, 204, 170)

def create_player_frame(walk_cycle_frame):
    """Creates a single high-resolution frame of the player character."""
    width, height = 128, 128
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Shading
    draw.rectangle([(40, 48), (88, 96)], fill=PICO8_DARK_BLUE) # Darker shirt

    # Body (Shirt)
    draw.rectangle([(44, 52), (84, 92)], fill=PICO8_BLUE)

    # Head
    draw.ellipse([(44, 12), (84, 52)], fill=PICO8_PEACH)
    # Hair
    draw.arc([(44, 12), (84, 40)], 180, 0, fill=PICO8_BROWN, width=10)
    # Eyes
    draw.point((60, 34), fill=PICO8_BLACK)
    draw.point((72, 34), fill=PICO8_BLACK)

    # Legs (Pants)
    if walk_cycle_frame == 0: # Idle
        draw.rectangle([(48, 92), (60, 116)], fill=PICO8_BROWN)
        draw.rectangle([(68, 92), (80, 116)], fill=PICO8_BROWN)
    elif walk_cycle_frame == 1: # Step 1
        draw.rectangle([(40, 92), (52, 116)], fill=PICO8_BROWN)
        draw.rectangle([(76, 92), (88, 116)], fill=PICO8_BROWN)
    elif walk_cycle_frame == 2: # Idle
        draw.rectangle([(48, 92), (60, 116)], fill=PICO8_BROWN)
        draw.rectangle([(68, 92), (80, 116)], fill=PICO8_BROWN)
    elif walk_cycle_frame == 3: # Step 2
        draw.rectangle([(56, 92), (68, 116)], fill=PICO8_BROWN)
        draw.rectangle([(60, 92), (72, 116)], fill=PICO8_BROWN)

    image_np = np.array(image)
    pixelated_frame = Pyx(height=32, width=25, palette=Pal.PICO_8, dither="none").fit_transform(image_np)
    return Image.fromarray(pixelated_frame)

def generate_player_spritesheet():
    """Generates a player walking spritesheet and saves it."""
    frames = [create_player_frame(i) for i in range(4)]

    spritesheet_width = frames[0].width * 4
    spritesheet_height = frames[0].height
    spritesheet = Image.new("RGBA", (spritesheet_width, spritesheet_height))

    for i, frame in enumerate(frames):
        spritesheet.paste(frame, (i * frame.width, 0))

    output_path = os.path.join("assets", "sprites", "player_walk_spritesheet.png")
    spritesheet.save(output_path)
    print(f"Player spritesheet saved to {output_path}")

def create_enemy_frame(bob_offset):
    """Creates a single frame of the enemy character."""
    width, height = 64, 64
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Body
    draw.ellipse([(12, 16 + bob_offset), (52, 56 + bob_offset)], fill=PICO8_DARK_GREEN)
    draw.ellipse([(16, 20 + bob_offset), (48, 52 + bob_offset)], fill=PICO8_GREEN)

    # Eye
    draw.ellipse([(28, 32 + bob_offset), (36, 40 + bob_offset)], fill=PICO8_WHITE)
    draw.point((32, 36 + bob_offset), fill=PICO8_RED)


    image_np = np.array(image)
    pixelated_frame = Pyx(factor=7, palette=Pal.PICO_8, dither="none").fit_transform(image_np)
    return Image.fromarray(pixelated_frame)

def generate_enemy_spritesheet():
    """Generates an enemy idle spritesheet."""
    frame1 = create_enemy_frame(0)
    frame2 = create_enemy_frame(-2) # Bob up

    spritesheet_width = frame1.width * 2
    spritesheet_height = frame1.height
    spritesheet = Image.new("RGBA", (spritesheet_width, spritesheet_height))

    spritesheet.paste(frame1, (0, 0))
    spritesheet.paste(frame2, (frame1.width, 0))

    output_path = os.path.join("assets", "sprites", "enemy_idle_spritesheet.png")
    spritesheet.save(output_path)
    print(f"Enemy spritesheet saved to {output_path}")

def generate_intro_background():
    """Generates a starry sky background for the intro."""
    width, height = 1024, 600
    image = Image.new("RGB", (width, height), PICO8_DARK_BLUE)
    draw = ImageDraw.Draw(image)

    for _ in range(200):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        draw.point((x, y), fill=PICO8_WHITE)

    output_path = os.path.join("assets", "sprites", "intro_background.png")
    image.save(output_path)
    print(f"Intro background saved to {output_path}")

def generate_main_menu_background():
    """Generates a background for the main menu."""
    width, height = 1024, 600
    image = Image.new("RGB", (width, height), PICO8_BLACK)
    draw = ImageDraw.Draw(image)

    for i in range(0, width, 20):
        draw.line([(i, 0), (i, height)], fill=PICO8_DARK_PURPLE, width=2)
    for i in range(0, height, 20):
        draw.line([(0, i), (width, i)], fill=PICO8_DARK_PURPLE, width=2)

    output_path = os.path.join("assets", "sprites", "main_menu_background.png")
    image.save(output_path)
    print(f"Main menu background saved to {output_path}")

def generate_logo():
    """Generates a logo for the game 'Heart Shatter'."""
    width, height = 400, 200
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Draw a heart
    heart_points = [
        (200, 60), (240, 20), (280, 20), (320, 60),
        (200, 140), (80, 60), (120, 20), (160, 20)
    ]
    draw.polygon(heart_points, fill=PICO8_RED)

    # Draw a crack
    crack_points = [
        (200, 60), (180, 100), (220, 120), (200, 140)
    ]
    draw.line(crack_points, fill=PICO8_BLACK, width=5)

    output_path = os.path.join("assets", "sprites", "logo.png")
    image.save(output_path)
    print(f"Logo saved to {output_path}")

if __name__ == "__main__":
    generate_player_spritesheet()
    generate_enemy_spritesheet()
    generate_intro_background()
    generate_main_menu_background()
    generate_logo()
