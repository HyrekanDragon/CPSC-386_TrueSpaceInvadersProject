import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, settings, screen, alien):
        """Create a bullet object at the ship's current position"""
        super(Laser, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and the set correct position.
        self.rect = pygame.Rect(0, 0, settings.laser_width, settings.laser_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = settings.laser_color
        self.speed_factor = settings.laser_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal positon of the bullet.
        self.y += self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_laser(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)