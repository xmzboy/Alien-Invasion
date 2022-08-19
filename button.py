import pygame.font


class Button:
    """Класс кнопки"""
    def __init__(self, ai_game, msg, color, shift=0):
        """Инициализация кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if not shift:
            self.rect.center = self.screen_rect.center
        else:
            self.rect.center = (960, 640)

        self._prep_msg(msg, shift)

    def _prep_msg(self, msg, shift):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        if not shift:
            self.msg_image_rect.center = self.rect.center
        else:
            self.msg_image_rect.center = (960, 640)

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
