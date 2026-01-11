import pygame.font

class Player:
    """a class to represent a player"""

    def __init__(self,game,msg,pos):
        """initialize game attributes"""
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.setting = game.setting
        self.font = pygame.font.SysFont(None, self.setting.player_text_size)
        self.move_up = False
        self.move_down = False
        self.player(msg,pos)

    def player(self,msg,pos):
        """render a player"""
        self.image = self.font.render(msg, True, self.setting.player_text_size,self.setting.player_bg_color)
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.player_width = self.rect.width
        self.player_height = self.rect.height
        self.rect.centery = self.screen_rect.centery
        self.y = float(self.rect.y)
        self.set_position(pos)

    def draw(self):
        """draw the player"""
        self.screen.blit(self.image,self.rect)

    def move_player(self):
        """Move the player position"""
        if self.move_up and self.rect.top > self.screen_rect.top:
            self.y -= self.setting.player_speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.player_speed

        self.rect.y = self.y

    def set_position(self,pos):
        """Set player position"""
        if pos.lower() == 'top':
            self.rect.top = self.screen_rect.top
        if pos.lower() == 'bottom':
            self.rect.bottom = self.screen_rect.bottom
        if pos.lower() == 'left':
            self.rect.left = self.screen_rect.left
        if pos.lower() == 'right':
            self.rect.right = self.screen_rect.right