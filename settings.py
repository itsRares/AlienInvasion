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
        self.bullet_speed_factor = 15
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1