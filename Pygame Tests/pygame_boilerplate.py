# boilerplate for pygame
import random
import pygame
from pygame import gfxdraw

# pygame setup
pygame.init()
screen_size = (600, 400)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()
running = True


def update():
    pass


def draw():
    # Clear the screen by blacking it out
    gfxdraw.box(screen, (0, 0, screen_size[0], screen_size[1]), (0, 0, 0, 10))

    # Draw to the display
    pygame.display.flip()


while running:
    # Check if the screen is closed and quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            exit()
    update()
    draw()

    clock.tick(60)