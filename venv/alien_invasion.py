import sys
import pygame

from settings import  Settings
from ship import  Ship
import game_functions as gf

def run_game():
    # Intialize pygame, settings, and scree object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.get_display())
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(settings, screen)

    # Star the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(settings, screen, ship)

run_game()