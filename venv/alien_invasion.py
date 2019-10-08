import sys
import pygame
from pygame.sprite import Group
from settings import  Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import  Ship
from alien import Alien
from high_score import  Highscores
import game_functions as gf

def run_game():
    # Intialize pygame, settings, and scree object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.get_display())
    pygame.display.set_caption("Alien Invasion")
    # Make the play button.
    play_button = Button(settings, screen, "Play", (600, 600))
    hs_button = Button(settings, screen, "Highscores", (600, 670))
    back_button = Button(settings, screen, "Back", (600, 720))

    # Create an instance to store game stats and create a scoreboard.
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    hs = Highscores(settings, screen)

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(settings, screen)
    lasers = Group()
    bullets = Group()
    aliens = Group()
    ufos = Group()

    # Create the fleet of aliens.
    gf.create_fleet(settings, screen, ship, aliens, ufos)

    # Initialize Music
    # Music taken from https://bitmidi.com/space-invaders-do-the-freak-mid
    # Sprites and sound effects taken from https://www.classicgaming.cc/classics/space-invaders/sounds
    pygame.mixer.music.load('music/Space Invaders - Do The Freak.mid')
    pygame.mixer.music.play(-1, 0.0)

    # Star the main loop for the game.
    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, ufos, bullets, lasers, hs, hs_button, back_button)

        if stats.game_active:
            ship.update()
            gf.update_bullet(settings, screen, stats, sb, ship, aliens, ufos, bullets, lasers)
            gf.update_laser(settings, screen, stats, sb, ship, aliens, ufos, bullets, lasers, hs)
            gf.update_aliens(settings, screen, stats, sb, ship, aliens, ufos, bullets, lasers, hs)

        gf.update_screen(settings, screen, stats, sb, ship, aliens, ufos, bullets, lasers, play_button, hs_button, back_button, hs)

run_game()