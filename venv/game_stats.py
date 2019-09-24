class GameStats():
    """Track stats for Alien Invasion"""

    def __init__(self, settings):
        """Initialize stats"""
        self.settings = settings
        self.reset_stats()

        # High score shoudl never be reset.
        self.high_score = 0

        # Star Alien Invasion is an active state.
        self.game_active = False

    def reset_stats(self):
        """Intialilze stats that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
