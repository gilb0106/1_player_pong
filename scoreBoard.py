import sys
import pygame

class ScoreBoard:
    def __init__(self, fontsize, color, screen_width, screen_height):
        self.color = color
        self.fontsize = fontsize
        self.player_score = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font(None, fontsize)

    def incrment_player_score(self):
        self.player_score += 1
    def draw(self, surface):
        player_text = self.font.render(f"Player: {self.player_score}", True, self.color)
        surface.blit(player_text, (10, 10))





