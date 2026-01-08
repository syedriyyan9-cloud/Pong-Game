import random

import pygame

import sys

from player import Player

from settings import Settings

from ball import Ball

import random

class Pong:
    """a class to represent pong game"""

    def __init__(self):
        """initialize game attributes"""
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        self.setting = Settings()
        self.player1 = Player(self,'Player 1','left')
        self.player2 = Player(self,'Player 2','right')
        self.ball = Ball(self)
        self.clock = pygame.time.Clock()

    def check_events(self):
        """check for game events"""
        for event in pygame.event.get():
            self._key_down_events(event)
            self._key_up_events(event)

    def _key_down_events(self,event):
        """check for key presses"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_w:
                self.player1.move_up = True
            if event.key == pygame.K_s:
                self.player1.move_down = True
            if event.key == pygame.K_UP:
                self.player2.move_up = True
            if event.key == pygame.K_DOWN:
                self.player2.move_down = True

    def _key_up_events(self,event):
        """check for key release"""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.player1.move_up = False
            if event.key == pygame.K_s:
                self.player1.move_down = False
            if event.key == pygame.K_UP:
                self.player2.move_up = False
            if event.key == pygame.K_DOWN:
                self.player2.move_down = False

    def update_screen(self):
        """update the screen"""
        self.check_events()
        # self.screen.fill(random.choice(self.setting.list_of_colors)) #comment in to make the bg color keep on changing
        self.screen.fill(self.setting.color_white)
        self.player1.draw()
        self.player2.draw()
        self.ball.draw()
        pygame.display.flip()

    def run(self):
        """Keep the game running"""
        while True:
            self.clock.tick(60)
            self.update_screen()
            self.player1.move_player()
            self.player2.move_player()
            self.ball.update_position()
            pygame.mouse.set_visible(False)

if __name__ == '__main__':
    pong = Pong()
    pong.run()