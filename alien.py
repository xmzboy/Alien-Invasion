import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс пришельца"""

    def __init__(self, ai_game):
        """Инициализация пришельца и установка начальной позиции"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загрузка изображения пришельца
        self.image = pygame.image.load('images/alienship.png')
        self.rect = self.image.get_rect()

        # Установка позиции пришельца
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def update(self):
        """Перемещение пришельца влево или вправо"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Возвращает True если пришелец у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
