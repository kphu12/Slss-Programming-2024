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
SCREEN_SIZE = (WIDTH, HEIGHT)

NUM_COINS = 10

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pg.image.load("./Images/Mario.webp")
    
        self.rect = self.image.get_rect()
    
    def update(self):
        """Updates the loaction of sprite to the mouse cursor"""
        self.rect.centerx = pg.mouse.get_pos()[0]
        self.rect.centery = pg.mouse.get_pos()[1]

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self. image = pg.image.load("./Images/Coin.png")
        
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randrange(0, WIDTH - self.rect.width)
        self.rect.centery = random.randrange(0, HEIGHT - self.rect.height)

class Enemy(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # image -> visual representation
        self.image = pg.image.load("./Images/dvd-logo.png")

        # rect  -> hitbox representation
        # get_rect() -> Rect
        #     [x, y, width, height]
        #     [0, 0, <width of image>, <height of image>]
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

        # Velocity of the Dvd logo set randomly
        self.vel_x = random.choice([-6, -5 -4, -3, 3, 4, 5, 6])
        self.vel_y = random.choice([-6, -5 -4, -3, 3, 4, 5, 6])

    def update(self):
        # Update the location of the DVD log
        self.rect.x += self.vel_x
        self.rect.y +=self.vel_y

        # Bouncef if reaches bottom
        #   if the bottom of the sprite is past the bottom of screen
        #   convert to negative (* -1)
        if self.rect.bottom < 775:
            self.vel_y *= -1
        #Top
        if self.rect.top > 0:
            self.vel_y *= -1
        #Left
        if self.rect.left < 1100:
            self.vel_x *= -1
        #Right
        if self.rect.right > 130:
            self.vel_x *= -1        
    

def start():
    """Environment Setup and Game Loop"""

    pg.init()
    pg.mouse.set_visible(False)


    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    score = 0

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Coin Sprities
    coin_sprites = pg.sprite.Group()

    for _ in range(NUM_COINS):
        coin = Coin()

        all_sprites.add(coin)
        coin_sprites.add(coin)

    # Create a player and store it in a varialbe
    player = Player()

    all_sprites.add(player)

    pg.display.set_caption("Jewel Thief Clone")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        all_sprites.update()

        # Coillision between player and coin_sprites
        # Get a list of ALL coin_sprites that collide
        #      with a player
        # FOr every coin, that colides, print "COLLISION!"
        coins_collided = pg.sprite.spritecollide(
            player,
            coin_sprites,
            True
        )

        for coin in coins_collided:
            # increase the score by 1 
            score += 1

            print(score)

        # if the coin_sprites is empty
        # respawn all the coins
        if len(coin_sprites) <= 0:
                for _ in range(NUM_COINS):
                    coin = Coin()
                    all_sprites.add(coin)
                    coin_sprites.add(coin)

        # --- Draw items
        screen.fill(WHITE)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()