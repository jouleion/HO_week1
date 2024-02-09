import pygame
import numpy as np
import random

from TSPDecoder import *

# Define constants
ROWS = 27
COLUMNS = 19
THRESHOLD = 50
PIXEL_WIDTH = 10
PIXEL_HEIGHT = 10
PIXEL_MARGIN = 5
BLACK = (0, 0, 0)
PSYCH_COLORS = [
    (253,0,255),
    (253,255,0),
    (0,255,56),
    (0,249,255),
    (60,0,255),
    (252, 0, 25)
]

# Initialise the PyGame screen according to resolution
pygame.init()
WINDOW_SIZE = [
    COLUMNS*PIXEL_WIDTH+COLUMNS*PIXEL_MARGIN+2*PIXEL_MARGIN,
    ROWS*PIXEL_HEIGHT+ROWS*PIXEL_MARGIN+2*PIXEL_MARGIN
]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Game of Touch example")

# Initialise the PyGame Clock for timing
clock = pygame.time.Clock()

# Initialise the Haptic Skin
TSP = TSPDecoder(rows=ROWS, columns=COLUMNS)

# Create the game grid and fill it randomly at the start
grid = np.zeros((ROWS, COLUMNS, 3), dtype=int)

# Game loop
while TSP.available():
    # Check if the screen is closed and quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Get the frame
    frame = TSP.readFrame()

    # Clear the screen by blacking it out
    screen.fill(BLACK)

    # Update the grid
    new_grid = grid.copy()
    # Loop through the whole grid
    for row in range(ROWS):
        for column in range(COLUMNS):
            # New pixel is made if cell is touched, with a random color
            if frame[row][column] > THRESHOLD:
                new_grid[row, column] = random.choice(PSYCH_COLORS)
            # Colors get faded and cell is moved at random
            else:
                color = grid[row][column]
                new_row = (row + random.randint(-1, 1)) % ROWS
                new_column = (column + random.randint(-1, 1)) % COLUMNS

                # New values are stored in the new grid
                new_grid[new_row, new_column] = [
                    color[0]-10 if (color[0] > 10) else 0,
                    color[1]-10 if (color[1] > 10) else 0,
                    color[2]-10 if (color[2] > 10) else 0,
                ]

    # Save the modified grid to the drawing grid
    grid[:,:] = new_grid[:,:]

    # Loop through all grid pixels and draw them
    for row in range(ROWS):
        for column in range(COLUMNS):
            # Draw a rectangle at the pixel location with the correct color
            pygame.draw.rect(
                screen,
                (grid[row][column][0], grid[row][column][1], grid[row][column][2]),
                [
                    PIXEL_MARGIN + ((PIXEL_MARGIN + PIXEL_WIDTH) * column),
                    PIXEL_MARGIN + ((PIXEL_MARGIN + PIXEL_HEIGHT) * row),
                    PIXEL_WIDTH,
                    PIXEL_HEIGHT
                ]
            )

    # Limit the framerate to 60FPS
    clock.tick(60)

    # Draw to the display
    pygame.display.flip()