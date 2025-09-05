import numpy as np
from PIL import Image, ImageDraw
from pyxelate import Pyx, Pal
import os
from skimage import io

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

    # Head
    draw.rectangle([(48, 16), (80, 48)], fill=PICO8_PEACH)
    # Eyes
    draw.rectangle([(56, 32), (60, 36)], fill=PICO8_BLACK)
    draw.rectangle([(72, 32), (76, 36)], fill=PICO8_BLACK)

    # Body (Shirt)
    draw.rectangle([(40, 48), (88, 96)], fill=PICO8_BLUE)

    # Legs (Pants)
    if walk_cycle_frame == 0: # Idle
        draw.rectangle([(48, 96), (60, 120)], fill=PICO8_BROWN)
        draw.rectangle([(68, 96), (80, 120)], fill=PICO8_BROWN)
    elif walk_cycle_frame == 1: # Step 1
        draw.rectangle([(40, 96), (52, 120)], fill=PICO8_BROWN)
        draw.rectangle([(76, 96), (88, 120)], fill=PICO8_BROWN)
    elif walk_cycle_frame == 2: # Idle
        draw.rectangle([(48, 96), (60, 120)], fill=PICO8_BROWN)
        draw.rectangle([(68, 96), (80, 120)], fill=PICO8_BROWN)
    elif walk_cycle_frame == 3: # Step 2
        draw.rectangle([(56, 96), (68, 120)], fill=PICO8_BROWN)
        draw.rectangle([(60, 96), (72, 120)], fill=PICO8_BROWN)

    image_np = np.array(image)
    pixelated_frame = Pyx(height=32, width=32, palette=Pal.PICO_8, dither="none").fit_transform(image_np)
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
    draw.rectangle([(16, 20 + bob_offset), (48, 52 + bob_offset)], fill=PICO8_RED)
    # Eyes
    draw.rectangle([(24, 28 + bob_offset), (30, 34 + bob_offset)], fill=PICO8_WHITE)
    draw.rectangle([(34, 28 + bob_offset), (40, 34 + bob_offset)], fill=PICO8_WHITE)

    image_np = np.array(image)
    pixelated_frame = Pyx(factor=7, palette=Pal.PICO_8, dither="none").fit_transform(image_np)
    return Image.fromarray(pixelated_frame)

def generate_enemy_spritesheet():
    """Generates an enemy idle spritesheet."""
    frame1 = create_enemy_frame(0)
    frame2 = create_enemy_frame(-4) # Bob up

    spritesheet_width = frame1.width * 2
    spritesheet_height = frame1.height
    spritesheet = Image.new("RGBA", (spritesheet_width, spritesheet_height))

    spritesheet.paste(frame1, (0, 0))
    spritesheet.paste(frame2, (frame1.width, 0))

    output_path = os.path.join("assets", "sprites", "enemy_idle_spritesheet.png")
    spritesheet.save(output_path)
    print(f"Enemy spritesheet saved to {output_path}")

if __name__ == "__main__":
    generate_player_spritesheet()
    generate_enemy_spritesheet()
