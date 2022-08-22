class GameStats:
    """Класс игровой статистики"""
    def __init__(self, ai_game):
        """Инициализация статистики"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

        # Старт игры в неактивном состоянии
        self.game_active = False

        # Наилучший результат
        with open('stats/scores.txt') as f:
            self.high_score = int(f.read())

    def reset_stats(self):
        """Сброс статистики"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
