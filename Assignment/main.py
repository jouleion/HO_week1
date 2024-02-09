# interactive visualisation for the TSP
# made by Julian van der Sluis and Willem Paternotte
#hello 4
from Tutorial_4.TSPDecoder import *
from particle_system import *

import random
import pygame
from pygame import gfxdraw

#setup touch sensitive pad
rows, columns = 27, 19
TSP = TSPDecoder(rows=rows, columns=columns)

# Define constants
PIXEL_WIDTH = 36
PIXEL_HEIGHT = 25
BLACK = (0, 0, 0)

# Initialise the PyGame screen according to resolution
WINDOW_SIZE = [
    columns * PIXEL_WIDTH + columns,
    rows * PIXEL_HEIGHT + rows
]

# pygame setup
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TSP visualizer")
clock = pygame.time.Clock()
dt = 0
running = True

# init particle system
particle_system = ParticleSystem()
SPAWN_THRESHOLD = 30


def update():
    # Get the frame
    grid = TSP.readFrame()

    # Loop through all pixels in the frame
    for row in range(rows):
        for column in range(columns):
            # Get the pixel value and set the gray value accordingly
            pixel = grid[row][column]

            # spawn particles
            if (pixel > SPAWN_THRESHOLD):
                if(random.randint(0, 100) > 90):
                    particle_system.add_particle(column * PIXEL_WIDTH, row * PIXEL_HEIGHT)
    # update particles
    particle_system.update()


def draw():
    # Clear the screen by blacking it out
    gfxdraw.box(screen, (0, 0, WINDOW_SIZE[0], WINDOW_SIZE[1]), (0, 0, 0, 10))

    # draw particles
    particle_system.draw(screen)

    # Draw to the display
    pygame.display.flip()


while TSP.available and running:
    # Check if the screen is closed and quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            exit()
    update()
    draw()

    # consistent 60 fps
    dt = clock.tick(60) / 1000