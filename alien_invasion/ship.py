import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and it's settings"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and make it closer to a rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Make every new ship at the bottom of central screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Stores decimals in the ship properties
        self.center = float(self.rect.centerx)

        # Move flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """According to move flag, move the ship"""
        # Update ship's center value instead of rect
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect according to self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at the specified position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the spaceship on the screen"""
        self.center=self.screen_rect.centerx