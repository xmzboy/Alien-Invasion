import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """Класс рекордов и отображения игровой информации"""
    def __init__(self, ai_game):
        """Инициализация параметров отображения игровой информации"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.ai_game = ai_game
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 64)
        self.prep_images()

    def prep_images(self):
        """Создание всех видов игровой информации"""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Создание информации об очках"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(f'Score: {score_str}', True, self.text_color, self.ai_game.settings.bg_color)
        self.score_image.set_alpha(127)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Создание информации о рекорде"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(f'Record: {high_score_str}', True, self.text_color, self.ai_game.settings.bg_color)
        self.high_score_image.set_alpha(127)
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.high_score_image_rect.top


    def prep_level(self):
        """Создание информации об уровне"""
        level_str = str(f'Level: {self.stats.level}')
        self.level_image = self.font.render(level_str, True, self.text_color,  self.ai_game.settings.bg_color)
        self.level_image.set_alpha(127)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Создание информации об оставшихся жизнях"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_score(self):
        """Проверка на рекорд"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Отображение игровой информации"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.ships.draw(self.screen)