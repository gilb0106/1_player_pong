import sys
import pygame
import Player
import Ball

resolution = (400, 300)
WHITE = (255, 255, 255)
black = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

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

