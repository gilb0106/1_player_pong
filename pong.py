import sys
import pygame
from Ball import Ball
from Player import Player
from scoreBoard import ScoreBoard

resolution = (400, 300)
WHITE = (255, 255, 255)
black = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
pygame.display.set_caption("Square Player")

# Create a player object
player = Player(resolution[0] // 100, resolution[1] // 4, 100, 20, WHITE)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# Create ball object at the center of the screen
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
scoreboard = ScoreBoard(30, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT)

# Game loop
running = True
game_over = False
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
    ball.update(player, scoreboard)

    # Clear the screen
    screen.fill(black)

    # Draw the player
    player.draw(screen)
    scoreboard.draw(screen)
    # Draw the ball
    ball.draw(screen)

    if ball.x - ball.rad <= 0:
        game_over = True  # Set game over flag

    # Display "Game Over" message
    if game_over:
        game_over_font = pygame.font.Font(None, 50)
        game_over_text = game_over_font.render("Game Over", True, WHITE)
        game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, game_over_text_rect)



    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.time.delay(10000)
pygame.quit()
sys.exit()