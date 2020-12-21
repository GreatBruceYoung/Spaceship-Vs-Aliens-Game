class GameStats():
    """Track game and statistics related information"""

    def __init__(self,ai_settings):
        """Initialize statistics information"""
        self.ai_settings=ai_settings
        self.reset_stats()

        # Active when the game just started
        self.game_active=True

    def reset_stats(self):
        self.ships_left=self.ai_settings.ship_limit