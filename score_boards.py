import pygame.font

import time

class ScoreBoard:
    """a class to represent a score board"""

    def __init__(self,game,msg,pos):
        """initialize the attributes"""
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.setting = game.setting
        self.font = pygame.font.SysFont(None,self.setting.font_size)
        self.msg = msg
        self.ball = game.ball
        self.render_image(msg,pos)

    def render_image(self,msg,pos):
        """render the image as rectangle"""
        self.image = self.font.render(f"{msg}: 0",True,self.setting.font_color,self.setting.font_size)
        self.rect = self.image.get_rect()
        self.set_position(pos)

    def draw(self):
        """draw the score board"""
        # self.update_score()
        self.screen.blit(self.image,self.rect)

    def set_position(self,pos):
        """Set player position"""
        if pos.lower() == 'top':
            self.rect.top = self.screen_rect.top
        if pos.lower() == 'bottom':
            self.rect.bottom = self.screen_rect.bottom
        if pos.lower() == 'left':
            self.rect.left = self.screen_rect.left + 50
            self.rect.top = self.screen_rect.top + 10
        if pos.lower() == 'right':
            self.rect.right = self.screen_rect.right - 50
            self.rect.top = self.screen_rect.top + 10

    def update_score(self):
        """update scores of players"""
        self.image = self.font.render(f"{self.msg}: {self.setting.player_score}", True,
                                              self.setting.font_color, self.setting.font_size)
