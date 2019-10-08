import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """A class to report scoring info"""

    def __init__(self, settings, screen, stats):
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Font settings for scoring information
        self.text_color = (230, 230, 230)
        self.green = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.font2 = pygame.font.SysFont(None, 200)
        self.font3 = pygame.font.SysFont(None, 150)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.prep_title_screen()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw the scores and ships to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.prep_high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.prep_high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.prep_high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how mnay ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width * 1.2
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_title_screen(self):
        title = 'Space'
        subtitle = 'Invaders'
        alien1_points = '500'
        alien2_points = '200'
        alien3_points = '100'
        ufo_points = '???'

        self.title_image = self.font2.render(title, True, self.text_color, self.settings.bg_color)
        self.subtitle_image = self.font3.render(subtitle, True, self.green, self.settings.bg_color)
        self.alien1_points_image = self.font.render(alien1_points, True, self.text_color, self.settings.bg_color)
        self.alien2_points_image = self.font.render(alien2_points, True, self.text_color, self.settings.bg_color)
        self.alien3_points_image = self.font.render(alien3_points, True, self.text_color, self.settings.bg_color)
        self.ufo_points_image = self.font.render(ufo_points, True, self.text_color, self.settings.bg_color)
        self.alien1_image = pygame.image.load('images/alien_1.bmp')
        self.alien2_image = pygame.image.load('images/alien_2.bmp')
        self.alien3_image = pygame.image.load('images/alien_3.bmp')
        self.ufo_image = pygame.image.load('images/ufo.bmp')

        self.title_rect = self.title_image.get_rect()
        self.subtitle_rect = self.subtitle_image.get_rect()
        self.alien1_points_rect = self.alien1_points_image.get_rect()
        self.alien2_points_rect = self.alien2_points_image.get_rect()
        self.alien3_points_rect = self.alien3_points_image.get_rect()
        self.ufo_points_rect = self.ufo_points_image.get_rect()
        self.alien1_rect = self.alien1_image.get_rect()
        self.alien2_rect = self.alien2_image.get_rect()
        self.alien3_rect = self.alien3_image.get_rect()
        self.ufo_rect = self.ufo_image.get_rect()

        self.title_rect.center = (600, 100)
        self.subtitle_rect.center = (600, 220)
        self.alien1_points_rect.center = (500, 320)
        self.alien2_points_rect.center = (500, 400)
        self.alien3_points_rect.center = (500, 480)
        self.ufo_points_rect.center = (700, 450)
        self.alien1_rect.center = (400, 320)
        self.alien2_rect.center = (400, 400)
        self.alien3_rect.center = (400, 480)
        self.ufo_rect.center = (700, 350)

    def show_title_screen(self):
        self.screen.blit(self.title_image, self.title_rect)
        self.screen.blit(self.subtitle_image, self.subtitle_rect)
        self.screen.blit(self.alien1_points_image, self.alien1_points_rect)
        self.screen.blit(self.alien2_points_image, self.alien2_points_rect)
        self.screen.blit(self.alien3_points_image, self.alien3_points_rect)
        self.screen.blit(self.ufo_points_image, self.ufo_points_rect)
        self.screen.blit(self.alien1_image, self.alien1_rect)
        self.screen.blit(self.alien2_image, self.alien2_rect)
        self.screen.blit(self.alien3_image, self.alien3_rect)
        self.screen.blit(self.ufo_image, self.ufo_rect)