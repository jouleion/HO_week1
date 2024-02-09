# pygame test
# Better Color Circles By Julian van der Sluis
# conversion form processing to python

import random
import pygame
from pygame import gfxdraw


# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 500))
clock = pygame.time.Clock()
running = True
dt = 0

# color variables
color_speed = 1.1

# initialize color values
r = random.randint(50, 255)
g = random.randint(50, 255)
b = random.randint(50, 255)

# initialize color factors
rfac = random.random() * 1.5 + 0.2
gfac = random.random() * 1.5 + 0.2
bfac = random.random() * 1.5 + 0.2

# initialize color direction variables 1 = up, -1 = down
rdir = 1
gdir = 1
bdir = 1

def check_color_direction(color, dir):
    new_dir = dir
    if dir > 0:
        if color > 230:
            new_dir = -1
    else:
        if color < 50:
            new_dir = 1
    return new_dir


def update_color():
    global r, g, b
    global rdir, gdir, bdir

    # update color values, move color direction randomly, control direction of movement
    r += int(rfac * rdir * random.random() * color_speed)
    g += int(gfac * gdir * random.random() * color_speed)
    b += int(bfac * bdir * random.random() * color_speed)

    # limit color direction
    rdir = check_color_direction(r, rdir)
    gdir = check_color_direction(g, gdir)
    bdir = check_color_direction(b, bdir)

    color = pygame.Color(r, g, b)
    return color


def draw_circle():
    # update color
    circle_color = update_color()

    # generate new random position for next circle
    random_position = [random.randint(0, screen.get_width()), random.randint(0, screen.get_height())]

    # generate random radius
    random_radius = random.randint(5, 20)

    # draw each cirlce
    # pygame.draw.circle(screen, circle_color, random_position, random_radius)
    gfxdraw.aacircle(screen, random_position[0], random_position[1], random_radius, circle_color)
    gfxdraw.filled_circle(screen, random_position[0], random_position[1], random_radius, circle_color)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("black")

    # draw multiple cirlces each frame
    for i in range(0, 10):
        draw_circle()

    # show drawn elements on screen
    pygame.display.flip()

    # consistent FPS
    dt = clock.tick(60) / 1000

pygame.quit()