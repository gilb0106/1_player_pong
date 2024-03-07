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

    def update(self):
        self.x += self.xVel
        self.y += self.yVel
        if (self.x - self.rad < 0):
            pygame.quit()
            sys.exit()
        if (self.x + self.rad >= SCREEN_WIDTH):
            self.xVel *= -1
        if (self.y - self.rad < 0 or self.y + self.rad >= SCREEN_HEIGHT):
            self.yVel *= -1

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

pygame.init()

pygame.display.set_caption("Square Player")

# Create a player object
player = Player(resolution[0] // 100, resolution[1] // 4, 100, 20, WHITE)

# Create ball object at the center of the screen
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))



# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.move_up()
    if keys[pygame.K_DOWN]:
        player.move_down()

    if (ball.x + ball.rad >= player.x and ball.x - ball.rad <= player.x + player.width and
            ball.y + ball.rad >= player.y and ball.y - ball.rad <= player.y + player.height):
        ball.xVel *= -1  # Reverse the ball's horizontal velocity
        ball.xVel += 1

    ball.update()



    # Clear the screen
    screen.fill(black)

    # Draw the player
    player.draw(screen)

    # Draw the ball
    ball.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

