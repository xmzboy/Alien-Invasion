class Settings:
    """Класс для всех основных настроек игры"""
    def __init__(self):
        """Инициализация настроек"""
        # Настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (16, 20, 88)

        # Настройки корабля
        self.ship_limit = 3

        # Настройки пули
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = (255, 150, 0)
        self.bullets_allowed = 5

        # Настройки пришельцев
<<<<<<< Updated upstream
        self.fleet_drop_speed = 10

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Настройки изменяемые во время игры"""
        self.ship_speed = 5
        self.bullet_speed = 5
        self.alien_speed = 1
=======
        self.alien_speed = 1
        self.fleet_drop_speed = 15
>>>>>>> Stashed changes
        self.fleet_direction = 1
        self.alien_points = 50

