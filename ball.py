import pygame

import random

class Ball:
    """a class to represent a ball"""

    def __init__(self,game):
        """initialize the attributes of ball"""
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.screen_width = game.screen_width
        self.screen_height = game.screen_height
        self.setting = game.setting
        # self.x_axis = game.screen_width//2
        # self.y_axis = game.screen_height//2
        # self.pos = (self.x_axis,self.y_axis)
        self.rect = pygame.Rect(0,0,self.setting.ball_radius,self.setting.ball_radius)
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """draw the ball onto the screen"""
        # pygame.draw.circle(self.screen,self.setting.color_red,self.pos,self.setting.ball_radius)
        # comment the next line of code in to make the color of ball change with every iteration
        # pygame.draw.rect(self.screen,random.choice(self.setting.list_of_colors),self.rect)
        pygame.draw.rect(self.screen,self.setting.ball_color,self.rect)

    def update_position(self):
        """update the position of the ball"""
        self._check_y_direction()
        self._check_x_direction()
        # self.pos = (self.x_axis,self.y_axis)

    def _check_y_direction(self):
        """Check y-axis direction for the ball"""
        if self.rect.top > 0 or self.rect.bottom < self.screen_rect.bottom:
            self.y -= self.setting.ball_speed * -self.setting.ball_direction_y
            if self.y < 0:
                self.setting.ball_direction_y *= -1
            elif self.y > self.screen_rect.bottom:
                self.setting.ball_direction_y *= -1
        self.rect.y = self.y

    def _check_x_direction(self):
        """Check x-axis direction for the ball"""
        if self.rect.left > self.screen_rect.left or self.rect.right < self.screen_rect.right:
            self.x += self.setting.ball_speed * self.setting.ball_direction_x
            # remove this logic when setting up score boards
            if self.x < self.screen_rect.left:
                self.setting.ball_direction_x *= -1
            elif self.x > self.screen_rect.right:
                self.setting.ball_direction_x *= -1
        self.rect.x = self.x