import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """On behalf of alien"""

    def __init__(self, ai_settings, screen):
        """Initialize aliens"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien image and set it's rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Alien initial position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw aliens at the given position"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """If alien is at the edges, it will return True"""
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True


    def update(self):
        """Make aliens go right or left"""
        self.x+=(self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x=self.x



