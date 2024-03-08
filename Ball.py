import sys
import pygame

resolution = (400, 300)
WHITE = (255, 255, 255)
black = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ball:
    def __init__(self, x, y, xVel=5, yVel=5, rad=10, color=WHITE):
        self.x = x
        self.y = y
        self.xVel = xVel
        self.yVel = yVel
        self.rad = rad
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.rad)

    def update(self, player, scoreboard):
        self.x += self.xVel
        self.y += self.yVel
        if (self.x - self.rad < 0):
            pygame.quit()
            sys.exit()
        if (self.x + self.rad >= SCREEN_WIDTH):
            self.xVel *= -1
        if (self.y - self.rad < 0 or self.y + self.rad >= SCREEN_HEIGHT):
            self.yVel *= -1
        if (self.x + self.rad >= player.x and self.x - self.rad <= player.x + player.width and
                self.y + self.rad >= player.y and self.y - self.rad <= player.y + player.height):
            self.xVel *= -1  # Reverse the ball's horizontal velocity
            scoreboard.incrment_player_score()

    def reset(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2