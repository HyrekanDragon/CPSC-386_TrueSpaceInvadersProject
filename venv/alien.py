import pygame
import random
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        #Load the alien image and set its rect attribute.
        self.images = (pygame.image.load('images/alien_1.bmp'),
                       pygame.image.load('images/alien_1-2.bmp'),
                       pygame.image.load('images/alien_2.bmp'),
                       pygame.image.load('images/alien_2-2.bmp'),
                       pygame.image.load('images/alien_3.bmp'),
                       pygame.image.load('images/alien_3-2.bmp'))
        self.image_index = 0
        self.animation_time = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()

        # Start each new alinet near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alient's exact position
        self.x = float(self.rect.x)

        # Store time to shoot laser
        self.laser_timer = random.randint(1000, 2000)

        # Death sound
        self.alien_hit = pygame.mixer.Sound("sounds/invaderkilled.wav")

        # Alien explosion images
        self.alien_kill_explosion = (pygame.image.load('images/invaderkilled.bmp'),
                                     pygame.image.load('images/invaderkilled_2.bmp'),
                                     pygame.image.load('images/invaderkilled_3.bmp'),
                                     pygame.image.load('images/invaderkilled_4.bmp'),
                                     pygame.image.load('images/invaderkilled_5.bmp'),
                                     pygame.image.load('images/invaderkilled_6.bmp'),)

        self.multiplier = 2


    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return true if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right."""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
        self.update_animation()

    def change_image(self, index):
        if index == 0 or index == 1:
            self.multiplier = 5
        elif index == 2 or index == 3:
            self.multiplier = 2
        else:
            self.multiplier = 1
        self.image_index = index
        self.image = self.images[self.image_index]

    def update_animation(self):
        if self.animation_time == 100:
            if self.image_index == 0:
                self.image_index = 1
            elif self.image_index == 1:
                self.image_index = 0
            elif self.image_index == 2:
                self.image_index = 3
            elif self.image_index == 3:
                self.image_index = 2
            elif self.image_index == 4:
                self.image_index = 5
            else:
                self.image_index = 4
            self.animation_time = 0
        else:
            self.animation_time += 1

        self.image = self.images[self.image_index]

    def shoot_laser(self):
        if self.laser_timer == 0:
            self.laser_timer = random.randint(1000, 2000)
            return True
        else:
            self.laser_timer -= 1
            return  False

    def play_death_sound(self):
        self.alien_hit.play()

    def play_death_animation(self):
        for i in range(2):
            for image in self.alien_kill_explosion:
                image_rect = image.get_rect()
                image_rect.centerx = self.rect.centerx
                image_rect.bottom = self.rect.bottom

                self.screen.blit(image, image_rect)
                pygame.display.flip()