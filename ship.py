import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс корабля"""

    def __init__(self, ai_game):
        """Инициализация корабля и установка начального положения"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def blitme(self, intro=False):
        """Отрисовка корабля в текущем положении"""
        self.image_intro = pygame.image.load('images/spaceship.png')
        self.intro_rect = self.image_intro.get_rect()
        if intro:
            # Отрисовка корабля на стартовом экране
            self.intro_rect.centerx = self.screen_rect.centerx
            self.intro_rect.top = self.intro_rect.top + 350
            self.screen.blit(self.image_intro, self.intro_rect)
        else:
            self.screen.blit(self.image, self.rect)

    def update(self):
        """Обновление позиции корабля"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def center_ship(self):
        """Центрирование корабля на экране"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
