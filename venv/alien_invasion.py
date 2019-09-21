import sys
import pygame

from settings import  Settings
from ship import  Ship

def run_game():
    # Intialize pygame, settings, and scree object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.get_display())
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Star the main loop for the game.
    while True:

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(settings.get_bg_color())
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()