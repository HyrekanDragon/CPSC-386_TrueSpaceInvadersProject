import sys
import pygame
from pygame.sprite import Group
from settings import  Settings
from ship import  Ship
from alien import Alien
import game_functions as gf

def run_game():
    # Intialize pygame, settings, and scree object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.get_display())
    pygame.display.set_caption("Alien Invasion")

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(settings, screen, ship, aliens)

    # Star the main loop for the game.
    while True:
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullet(settings, screen, ship, aliens, bullets)
        gf.update_aliens(settings, aliens)
        gf.update_screen(settings, screen, ship, aliens, bullets)

run_game()