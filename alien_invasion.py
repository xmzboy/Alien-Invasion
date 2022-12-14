import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Главный класс игры"""
    def __init__(self):
        """Инициализация игры и игровых ресурсов"""
        pygame.init()
        self.settings = Settings()

        # Настройки экрана
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        # Картинка на фон
        # self.bg = pygame.image.load("images/bg.jpg")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.button = Button(self, "Play", (0, 200, 0))
        self.hard_button = Button(self, "Hard Mode", (200, 20, 0), 90)

        self.intro = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def run_game(self):
        """Главный цикл игры"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Проверка событий"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                with open('stats/scores.txt', 'w') as f:
                    f.write(str(self.stats.high_score))
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button_events()

    def _check_keydown_events(self, event):
        """Проверка события нажатия кнопки"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_RETURN:
            self._check_play_button_events(flag=True)

    def _check_keyup_events(self, event):
        """Проверка события отпускания кнопки"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button_events(self, flag=False):
        """Нажатие на кнопку начала игры"""
        mouse_pos = pygame.mouse.get_pos()
        if self.button.rect.collidepoint(mouse_pos) or flag:
            self.settings.init_dynamic_settings()
            self._start_game()
        if self.hard_button.rect.collidepoint(mouse_pos):
            self.settings.init_hard_dynamic_settings()
            self._start_game()

    def _start_game(self):
        """Запуск игры"""
        if not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Стрельба"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Обновление экрана"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        self.sb.show_score()
        if not self.stats.game_active:
            self.intro.fill(self.settings.bg_intro_color)
            self.ship.blitme(intro=True)
            self.button.draw_button()
            self.hard_button.draw_button()
        pygame.display.flip()

    def _create_fleet(self):
        """Создание флота пришельцев"""
        alien = Alien(self)
        available_space_y = (self.settings.screen_height - (3 * alien.rect.height) - self.ship.rect.height)
        available_space_x = self.settings.screen_width - (2 * alien.rect.width)
        number_aliens_x = available_space_x // (2 * alien.rect.width)
        number_rows = available_space_y // (2 * alien.rect.height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Создание одного пришельца"""
        alien = Alien(self)
        alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number + 40
        self.aliens.add(alien)

    def _update_aliens(self):
        """Обновление положения пришельцев на экране"""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _update_bullets(self):
        """Обновление положения пуль на экране"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Проверка столкновения пули с пришельцем"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
           self.start_new_level()

    def start_new_level(self):
        """Начало нового уровня"""
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()
        self.stats.level += 1
        self.sb.prep_level()

    def _check_fleet_edges(self):
        """Проверка касания пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """Изменение направления движения флота"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Обработка удара по кораблю"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Проверка достижения конца экрана пришельцем"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
