class GameStats:
    """Класс игровой статистики"""
    def __init__(self, ai_game):
        """Инициализация статистики"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Старт игры в неактивном состоянии
        self.game_active = False

    def reset_stats(self):
        """Сброс статистики"""
        self.ship_left = self.settings.ship_limit
