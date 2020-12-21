import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage ship's bullet"""
    def __init__(self,ai_settings,screen,ship):
        """Creates a bullet object at the ship's location"""
        super(Bullet, self).__init__()
        self.screen=screen

        # Create bullet rectangle, the set the right position
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top  # Bullet position is up to ship position

        # Store the position of bullet
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        """Move upward bullet """
        self.y-=self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        """Draw bullets"""
        pygame.draw.rect(self.screen,self.color,self.rect)