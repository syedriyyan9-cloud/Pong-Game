import pygame

class Ball:
    """a class to represent a ball"""

    def __init__(self,game):
        """initialize the attributes of ball"""
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.screen_width = game.screen_width
        self.screen_height = game.screen_height
        self.setting = game.setting
        self.x_axis = game.screen_width//2
        self.y_axis = game.screen_height//2
        self.pos = (self.x_axis,self.y_axis)

    def draw(self):
        """draw the ball onto the screen"""
        pygame.draw.circle(self.screen,self.setting.ball_color,self.pos,self.setting.ball_radius)

    def update_position(self):
        """update the position of the ball"""
        self._check_y_direction()
        self._check_x_direction()
        self.pos = (self.x_axis,self.y_axis)

    def _check_y_direction(self):
        """Check y-axis direction for the ball"""
        if self.y_axis > self.screen_rect.top or self.y_axis < self.screen_rect.bottom:
            self.y_axis -= self.setting.ball_speed * -self.setting.ball_direction_y
            if self.y_axis < self.screen_rect.top:
                self.setting.ball_direction_y *= -1
            elif self.y_axis > self.screen_rect.bottom:
                self.setting.ball_direction_y *= -1

    def _check_x_direction(self):
        """Check x-axis direction for the ball"""
        if self.x_axis > self.screen_rect.left or self.x_axis < self.screen_rect.right:
            self.x_axis += self.setting.ball_speed * self.setting.ball_direction_x
            # this login would be useful when detecting for collisions
            if self.x_axis < self.screen_rect.left:
                self.setting.ball_direction_x *= -1
            elif self.x_axis > self.screen_rect.right:
                self.setting.ball_direction_x *= -1