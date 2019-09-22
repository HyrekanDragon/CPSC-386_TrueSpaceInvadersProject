class GameStats():
    """Track stats for Alien Invasion"""

    def __init__(self, settings):
        """Initialize stats"""
        self.settings = settings
        self.reset_stats()

        # Star Alien Invasion is an active state.
        self.game_active = True

    def reset_stats(self):
        """Intialilze stats that can change during the game."""
        self.ships_left = self.settings.ship_limit
