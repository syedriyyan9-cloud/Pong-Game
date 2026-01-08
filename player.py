import pygame.font

class Player:
    """a class to represent a player"""

    def __init__(self,game,msg,pos):
        """initialize game attributes"""
        pygame.init()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.setting = game.setting
        self.font = pygame.font.SysFont(None, self.setting.player_text_size)
        self.rect = pygame.Rect(0,0,1,1)
        self.move_up = False
        self.move_down = False
        self.player(msg,pos)

    def player(self,msg,pos):
        """render a player"""
        self.image = self.font.render(msg, True, self.setting.player_text_size,self.setting.player_bg_color)
        self.image_rect = self.image.get_rect()
        self.y = float(self.image_rect.y)
        self.set_player_position(pos)

    def set_player_position(self,pos):
        """set player position"""
        if pos.lower() == 'top':
            self.rect.top = self.screen_rect.top
            self.image_rect.top = self.rect.top

        if pos.lower() == 'bottom':
            self.rect.bottom = self.screen_rect.bottom
            self.image_rect.bottom = self.rect.bottom

        if pos.lower() == 'left':
            self.rect.left = self.screen_rect.left
            self.image_rect.left = self.rect.left
            self.image = pygame.transform.rotate(self.image, 270)

        if pos.lower() == 'right':
            self.rect.right = self.screen_rect.right + 100
            self.image_rect.right = self.rect.right
            self.image = pygame.transform.rotate(self.image, 90)


    def draw(self):
        """draw the player"""
        self.screen.blit(self.image,self.image_rect)

    def move_player(self):
        """Move the player position"""
        if self.move_up and self.image_rect.top > self.screen_rect.top:
            self.y -= self.setting.player_speed
        if self.move_down and self.image_rect.bottom < self.screen_rect.bottom-90:
            self.y += self.setting.player_speed

        self.image_rect.y = self.y

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