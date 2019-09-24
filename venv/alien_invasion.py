import sys
import pygame
from pygame.sprite import Group
from settings import  Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import  Ship
from alien import Alien
import game_functions as gf

def run_game():
    # Intialize pygame, settings, and scree object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.get_display())
    pygame.display.set_caption("Alien Invasion")

    # Make the play button.
    play_button = Button(settings, screen, "Play")

    # Create an instance to store game stats and create a scoreboard.
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(settings, screen, ship, aliens)

    # Star the main loop for the game.
    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullet(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()