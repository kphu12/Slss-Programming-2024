# New and improved Pygame
# Create snowflakes falling
# Kendrick Phu
# May 2, 2024

import pygame as pg
import random

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280  # Pixels
HEIGHT = 720
radius = 50 
SCREEN_SIZE = (WIDTH, HEIGHT)


class Snowflake(pg.sprite.Sprite):
    # create the constructor
    #   image, rect
    def __init__(self, size:int):
        # Superclass constructor
        super().__init__()
        # Creating a "blank" image
        self.image = pg.Surface([size, size])

        # Draw a circle on the "blank image"
        pg.draw.circle(
            self.image,
            WHITE,
            (size // 2, size // 2), # draw in the middle of the "blank image"
            size // 2
        )

        self.rect = self.image.get_rect()
        # Spawn this in the middle of screen

        #Initial Coords, Chooses random x coords
        self.rect.centerx = random.randrange(0, WIDTH + 1)
        self.rect.centery = random.randrange(0, HEIGHT + 1)
        

        # Velocity of the snowfall set randomly
        self.vel_y = random.choice([3, 4, 5, 6])

    def update(self):
        # Update the location of the snowflake log
        self.rect.y += self.vel_y
        if self.rect.y > HEIGHT:
            self.rect.y = -10


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Create more snow
    for _ in range (100):
        all_sprites.add(Snowflake(10))

    pg.display.set_caption("Snow Falling")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()