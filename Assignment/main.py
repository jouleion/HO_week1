# interactive visualisation for the TSP
# made by Julian van der Sluis and Willem Paternotte
#hello 4
from Tutorial_4.TSPDecoder import *
from particle_system import *

import random
import pygame
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
TSP = TSPDecoder(rows=rows, columns=columns)

# Define constants
PIXEL_WIDTH = 36
PIXEL_HEIGHT = 25
PIXEL_MARGIN = 0
BLACK = (0, 0, 0)

# Initialise the PyGame screen according to resolution
pygame.init()
WINDOW_SIZE = [
    columns * PIXEL_WIDTH + columns,
    rows * PIXEL_HEIGHT + rows
]

screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Haptic Skin visualiser")

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
    x_scaled = PIXEL_WIDTH * x + int(offset)

    offset = np.random.normal(0, intensity/6)
    y_scaled = PIXEL_HEIGHT * y + int(offset)

    # draw each cirlce
    # pygame.draw.circle(screen, circle_color, random_position, random_radius)
    gfxdraw.aacircle(screen, y_scaled + random_radius, x_scaled + random_radius, random_radius, circle_color)
    # gfxdraw.filled_circle(screen, y_scaled + random_radius, x_scaled + random_radius, random_radius, circle_color)


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
                for i in range(random.randint(1,int(pixel/10))):
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



    # Limit the framerate to 60FPS
    # consistent FPS
    dt = clock.tick(60) / 1000

    # Draw to the display
    pygame.display.flip()

