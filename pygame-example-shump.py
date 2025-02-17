# # Kendrick Phu
# # Pygame
# # May 14, 2024

# pygame-example-shmup.py
# Shoot 'em up

import pygame as pg
import random
NUM_ENEMIES = 10
# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
WIDTH = 720  # Pixels
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./Images/galaga_ship.png")
        self.rect = self.image.get_rect()
    def update(self):
        """Follow the mouse"""
        self.rect.center = pg.mouse.get_pos()
        # keep it at height -200
        if self.rect.top < HEIGHT -200:
            self.rect.top = HEIGHT -200
# TODO: Bullets/lasers
#   - spawn at the player
#   - vertical velocity

class Bullet(pg.sprite.Sprite):
    def __init__(self, player_loc: list):
        """
        Params:
            player_loc: x,y coords of centerx and top
        """
        super().__init__()
        # green rectangle
        self.image = pg.Surface((10, 25))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        # spawn at the player
        self.rect.centerx = player_loc[0]
        self.rect.bottom = player_loc[1]
        # Set initial velocity to some random value
        self.vel_y = random.choice(( -4, -5, -6))
    def update(self):
        self.rect.y += self.vel_y
        
        # Kill the bullet if it leaves the screen
        if self.rect.bottom < 0:
            self.kill()
# TODO: enemies
#   - move left to right to left
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./Images/mario-new.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - 400)
        self.vel_x = random.choice((-6, -5, -4, 4, 5, 6))

    def update(self):
        """Move the goomba and bounce it off the edge of the window"""
        self.rect.x += self.vel_x
       # Bounce
        if self.rect.left < 0:
            self.rect.left = 0  # keep it inside the screen
            self.vel_x = -self.vel_x
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vel_x = -self.vel_x



def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    enemy_sprites = pg.sprite.Group()
    bullet_sprites = pg.sprite.Group()

    # create a Player sprite object
    player = Player()
    all_sprites.add(player)
    for _ in range(NUM_ENEMIES):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
    pg.display.set_caption("<shoot 'em up>")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                bullet = Bullet((player.rect.centerx, player.rect.top))
                all_sprites.add(bullet)
                bullet_sprites.add(bullet)
    
        # --- Update the world state
        all_sprites.update()
        # Detect collision with enemies
        for bullet in bullet_sprites:
            enemies_collided = pg.sprite.spritecollide(bullet, enemy_sprites, True)
            for enemy in enemies_collided:
                bullet.kill()
    
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