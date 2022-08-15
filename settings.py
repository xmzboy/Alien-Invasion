class Settings:
    def __init__(self):
        # Настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (16, 20, 88)

        # Настройки корабля
        self.ship_speed = 5
        self.ship_limit = 3

        # Настройки пули
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = (255, 50, 0)
        self.bullets_allowed = 5

        # Настройки пришельцев
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

