import random

import pygame

import sys

from player import Player

from settings import Settings

from ball import Ball

import random

from score_boards import ScoreBoard

class Pong:
    """a class to represent pong game"""

    def __init__(self):
        """initialize game attributes"""
        pygame.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_height = self.screen_rect.height
        self.setting = Settings()
        self.player1 = Player(self,'Player 1','left')
        self.player2 = Player(self,'Player 2','right')
        self.ball = Ball(self)
        self.clock = pygame.time.Clock()
        self.p1_score_board = ScoreBoard(self,"P1 Score","left")
        self.p2_score_board = ScoreBoard(self,"P2 Score","right")

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
        self.p1_score_board.draw()
        self.p2_score_board.draw()
        pygame.display.flip()

    def detect_collision(self):
        """Detect collisions with the ball"""
        collision_player_1 = pygame.sprite.collide_rect(self.ball,self.player1)
        collision_player_2 = pygame.sprite.collide_rect(self.ball,self.player2)
        self.direction_change_on_collision(collision_player_2,collision_player_1)

    def direction_change_on_collision(self,collision_player_1,collision_player_2):
        """Change the direction of the ball"""
        if collision_player_1 or collision_player_2:
            self.setting.ball_direction_x *= -1

    def update_score(self):
        """update the score"""
        if self.ball.rect.right > self.screen_rect.right:
            self.setting.player1_score += 1
            self.setting.player_score += self.setting.player1_score
            self.p1_score_board.update_score()
        if self.ball.rect.left < self.screen_rect.left:
            self.setting.player2_score += 1
            self.setting.player_score += self.setting.player2_score
            self.p2_score_board.update_score()

    def run(self):
        """Keep the game running"""
        while True:
            self.clock.tick(60)
            self.update_screen()
            self.player1.move_player()
            self.player2.move_player()
            self.ball.update_position()
            self.detect_collision()
            self.update_score()
            pygame.mouse.set_visible(False)

if __name__ == '__main__':
    pong = Pong()
    pong.run()