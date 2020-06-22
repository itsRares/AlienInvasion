class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen Settings
        self.screen_width = 999
        self.screen_height = 650
        self.bg_colour = (230,230,230)

        #Ship settings
        self.ship_speed_factor = 15

        #Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3