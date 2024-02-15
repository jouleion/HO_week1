# boilerplate for pygame
import random
import pygame
from pygame import gfxdraw

from paddle import Paddle
from ball import Ball

def update(screen_size):
    paddle.check_collision(ball)

    paddle.update(screen_size)
    ball.update(screen_size)


def draw(screen):
    # Clear the screen by blacking it out
    gfxdraw.box(screen, (0, 0, screen_size[0], screen_size[1]), (0, 0, 0, 15))

    # draw paddle
    paddle.draw(screen)
    ball.draw(screen)

    # Draw to the display
    pygame.display.flip()


# setup
# pygame setup
pygame.init()
screen_size = (400, 200)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()
running = True

paddle = Paddle()
ball = Ball(200, 50, 10, 1)

while running:
    # Check if the screen is closed and quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.set_speed(-1)
            if event.key == pygame.K_RIGHT:
                paddle.set_speed(1)

    update(screen_size)
    draw(screen)

    clock.tick(120)