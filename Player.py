import sys
import pygame

resolution = (400, 300)
WHITE = (255, 255, 255)
black = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player:
    def __init__(self, x, y, height, width, color):
        self.x =x
        self.y =y
        self.height=height
        self.width = width
        self.color=color
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self):
        if self.y + self.height < SCREEN_HEIGHT:
            self.y += self.speed