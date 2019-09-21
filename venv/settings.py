class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

    def get_display(self):
        return self.screen_width, self.screen_height

    def get_bg_color(self):
        return self.bg_color