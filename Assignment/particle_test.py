from particle_system import *
import random
import pygame
import numpy as np
from pygame import gfxdraw

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 500))
clock = pygame.time.Clock()
dt = 0
running = True

# has to be after random library and pygames init
particle_system = ParticleSystem()

# color variables
color_speed = 1.001

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

rows, columns = 27, 19

# Define constants
PIXEL_WIDTH = 36
PIXEL_HEIGHT = 25

pygame.display.set_caption("Particle Test")

# Initialise the PyGame Clock for timing
clock = pygame.time.Clock()

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


def draw_circle(x, y, intensity):
    # update color
    circle_color = update_color()

    # generate new random position for next circle
    # random_position = [random.randint(0, screen.get_width()), random.randint(0, screen.get_height())]

    # generate random radius
    random_radius = random.randint(0, int(intensity/40))

    offset = np.random.normal(0, intensity/6)
    x_scaled = int(PIXEL_HEIGHT * (x+0.5) + int(offset))

    offset = np.random.normal(0, intensity/6)
    y_scaled = int(PIXEL_WIDTH * (y+0.5) + int(offset))

    # draw each cirlce
    # pygame.draw.circle(screen, circle_color, random_position, random_radius)
    gfxdraw.aacircle(screen, y_scaled + random_radius, x_scaled + random_radius, random_radius, circle_color)
    # gfxdraw.filled_circle(screen, y_scaled + random_radius, x_scaled + random_radius, random_radius, circle_color)

while running:
    # Check if the screen is closed and quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            exit()

    # Clear the screen by blacking it out
    gfxdraw.box(screen,(0,0, 700, 700),(0,0,0,10))

    # simulate particles being added where screen is being pressed
    for x in range(20):
        for y in range(20):
            if(random.randint(0, 100) > 98):
                particle_system.add_particle(x * 30, y * 30)

    # update and draw particles
    particle_system.update()
    particle_system.draw(screen)


    # Limit the framerate to 60FPS
    # consistent FPS
    dt = clock.tick(60) / 1000

    # Draw to the display
    pygame.display.flip()