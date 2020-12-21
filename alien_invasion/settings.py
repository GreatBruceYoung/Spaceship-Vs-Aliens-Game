class Settings():
    """Storage all settings"""

    def __init__(self):
        """Initialize the game settings"""
        # Screen settings

        # Set the size of game screen
        self.screen_width = 800
        self.screen_height = 600

        # Set the color of background
        self.bg_color = (230, 230, 230)

        # Speed of ship
        self.ship_speed_factor = 1.5
        self.ship_limit=3 # The number of ship you can possess

        # Set of bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5  # Restrict the number of bullets

        # Set of aliens
        self.alien_speed_factor=1
        self.fleet_drop_speed=5
        # if fleet_direction equals 1, it represents go right; -1, go left
        self.fleet_direction=1
