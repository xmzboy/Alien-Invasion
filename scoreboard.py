import pygame.font

class Scoreboard:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 72)
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, (0, 0, 0))
        self.score_image.set_alpha(127)
        #self.score_image = pygame.font.Font(None, 100).render(score_str, True, self.text_color, (0,100,100,0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
