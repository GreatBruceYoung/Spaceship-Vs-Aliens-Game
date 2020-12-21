import pygame
from pygame.sprite import Group
from ship import Ship
from settings import Settings
from game_stats import GameStats
import game_functions as gf


def run_game():
    """Initialize the game"""
    pygame.init()  # Initialize the screen
    ai_settings = Settings()  # Create a object
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # Size of game screen
    pygame.display.set_caption("Alien Invasion")  # Set the title of game

    # Create a space ship, a bullet group and a alien group
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens=Group()

    # Create aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # Create information statistics
    stats=GameStats(ai_settings)

    # Begin the main circulation
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        gf.update_screen(ai_settings, screen, ship, aliens,bullets)  # Update screen


run_game()