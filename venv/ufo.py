import pygame
import random
from pygame.sprite import Sprite

class UFO(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, settings, screen):
        """Initialize the alien and set its starting position."""
        super(UFO, self).__init__()
        self.screen = screen
        self.settings = settings

        #Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Start each new alinet near the top left of the screen
        self.rect.x = settings.screen_width
        self.rect.y = 100

        # Store the alient's exact position
        self.x = float(self.rect.x)

        # Font settings for point information
        self.text_color = (230, 230, 230)
        self.font = pygame.font.SysFont(None, 140)

        # Store time to appear
        self.timer = random.randint(1000, 2000)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return true if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.left >= screen_rect.right:
            return False
        else:
            return True

    def update(self):
        """Move the alien right."""
        self.reset_position()
        if self.check_edges():
            self.x += self.settings.alien_speed_factor * 2
            self.rect.x = self.x

    def reset_position(self):
        if self.timer == 0:
            self.x = 0 - self.rect.width
            self.rect.x = self.x
            self.timer = random.randint(1000, 2000)
        else:
            self.timer -= 1

    def print_point_values(self, points):
        """Turn the score into a rendered image."""
        rounded_points = int(round(points, -1))
        points_str = "{:,}".format(rounded_points)
        points_image = self.font.render(points_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        points_rect = points_image.get_rect()
        points_rect.x = self.rect.x
        points_rect.y = self.rect.y
        points_rect.width = self.rect.width
        points_rect.height = self.rect.height

        for i in range(20):
            self.screen.blit(points_image, points_rect)
            pygame.display.flip()