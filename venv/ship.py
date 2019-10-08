import  pygame
from pygame.sprite import  Sprite

class Ship(Sprite):

    def __init__(self, settings, screen):
        """Intialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.settings = settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom cetner of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal valeu for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Ship desctruction sound
        self.ship_destroyed = pygame.mixer.Sound('sounds/explosion.wav')

        # Ship animation
        self.ship_destroyed_animation = (pygame.image.load('images/explosion.bmp'),
                          pygame.image.load('images/explosion_2.bmp'),
                          pygame.image.load('images/explosion_3.bmp'),
                          pygame.image.load('images/explosion_4.bmp'))

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        # Update rec object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx

    def play_death_sound(self):
        self.ship_destroyed.play()

    def play_death_animation(self):
        for i in range(100):
            for image in self.ship_destroyed_animation:
                image_rect = image.get_rect()
                image_rect.centerx = self.rect.centerx
                image_rect.bottom = self.rect.bottom

                self.screen.blit(image, image_rect)
                pygame.display.flip()