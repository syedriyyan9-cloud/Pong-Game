import random

class Settings:
    """a class to hold game settings"""
    def __init__(self):
        """settings for the game"""
        self.player_text_size = 48
        self.player_speed = 20
        self.player_text_color = (255,255,255)
        self.player_bg_color = (200,200,200)

        self.font_size = 48
        self.font_color = (255,0,0)

        self.ball_speed = 10
        self.ball_radius = 10
        self.ball_color = (255,0,0)
        self.ball_direction_y = random.choice([1,-1])
        self.ball_direction_x = random.choice([1,-1])

        self.color_white = (255,255,255)
        self.color_black = (0,0,0)
        self.color_red = (255,0,0)
        self.color_green = (0,255,0)
        self.color_blue = (0,0,255)
        self.list_of_colors_ball = [self.color_black, self.color_red, self.color_green, self.color_blue]
        self.list_of_colors_player = [self.color_red, self.color_green, self.color_blue]

