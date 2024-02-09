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

def update():
    # Clear the screen by blacking it out
    gfxdraw.box(screen, (0, 0, 700, 700), (0, 0, 0, 10))

    # simulate particles being added where screen is being pressed
    for x in range(20):
        for y in range(20):
            if (random.randint(0, 100) > 98):
                particle_system.add_particle(x * 30, y * 30)

    # update and draw particles
    particle_system.update()


def draw():
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

    # Get the frame
    grid = TSP.readFrame()

    # Clear the screen by blacking it out
    gfxdraw.box(screen,  (0,0,WINDOW_SIZE[0],WINDOW_SIZE[1]),(0,0,0,10)  )

    # Loop through all pixels in the frame
    for row in range(rows):
        for column in range(columns):
            # Get the pixel value and set the gray value accordingly
            pixel = grid[row][column]

            # color = (pixel, pixel, pixel)

            # draw circles
            if(pixel > 40):
                for i in range(random.randint(1,int(pixel/40))):
                    draw_circle(row, column, pixel)

            # Draw the pixel on the screen
            """pygame.draw.rect(
                screen,
                color,
                [
                    PIXEL_MARGIN + ((PIXEL_MARGIN + PIXEL_WIDTH) * column),
                    PIXEL_MARGIN + ((PIXEL_MARGIN + PIXEL_HEIGHT) * row),
                    PIXEL_WIDTH,
                    PIXEL_HEIGHT
                ]
            )"""

    particle_system.add_particle(50, 50)
    particle_system.update()
    particle_system.draw(screen)

    # Limit the framerate to 60FPS
    # consistent FPS
    dt = clock.tick(60) / 1000

    # Draw to the display
    pygame.display.flip()

