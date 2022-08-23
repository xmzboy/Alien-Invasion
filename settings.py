class Settings:
    """Класс для всех основных настроек игры"""
    def __init__(self):
        """Инициализация настроек"""
        # Настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 0, 80)
        self.bg_intro_color = (16, 20, 88)

        # Настройки корабля
        self.ship_limit = 3

        # Настройки пули
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = (255, 150, 0)
        self.bullets_allowed = 5

        # Настройки пришельцев
        self.fleet_drop_speed = 15

        self.speedup_scale = 1.5
        self.score_scale = 1.5

        self.init_dynamic_settings()

        self.alien_points = 50

    def init_dynamic_settings(self):
        """Настройки изменяемые во время игры"""
        self.ship_speed = 3.5
        self.bullet_speed = 6.0
        self.alien_speed = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличение сложности с ростом уровня"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def init_hard_dynamic_settings(self):
        """Настройки изменяемые во время игры"""
        self.ship_speed = 8.5
        self.bullet_speed = 6.0
        self.alien_speed = 2.0
        self.fleet_direction = 1
