import sys
import pygame
from pygame.sprite import Group
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
    # Make a group to store bullets in.
    bullets = Group()

    # Star the main loop for the game.
    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullet(bullets)
        gf.update_screen(settings, screen, ship, bullets)

run_game()