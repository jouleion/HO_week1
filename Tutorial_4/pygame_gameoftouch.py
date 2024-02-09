import pygame
import numpy as np
import random

from TSPDecoder import *

# Define constants
ROWS = 27
COLUMNS = 19
THRESHOLD = 75
PIXEL_WIDTH = 10
PIXEL_HEIGHT = 10
PIXEL_MARGIN = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
grid = np.zeros((ROWS, COLUMNS), dtype=int)
for i in range(50):
    # Select a random cell and make it alive
    row, column = random.randint(0, ROWS-1), random.randint(0, COLUMNS-1)
    grid[row][column] = 1

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
            # Calculate the amount of neighbours to the selected cell
            neighbors = np.sum(grid[row - 1:row + 2, column - 1:column + 2]) - grid[row, column]
            # Apply the rules of Conway's Game of Life
            # Cell dies if it has less than 2 or more than 3 neighbours
            if grid[row, column] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[row, column] = 0
            # Cell comes to life if it has 3 neighbours or is touched
            elif (grid[row, column] == 0 and neighbors == 3) or frame[row][column] > THRESHOLD:
                new_grid[row, column] = 1
    # Save the modified grid to the drawing grid
    grid[:,:] = new_grid[:,:]

    # Loop through all grid pixels and draw them
    for row in range(ROWS):
        for column in range(COLUMNS):
            # Check the pixel value and set the correct color (BLACK = Dead, WHITE = Alive)
            if grid[row][column]:
                color = WHITE
            else:
                color = BLACK

            # Draw a rectangle at the pixel location with the correct color
            pygame.draw.rect(
                screen,
                color,
                [
                    PIXEL_MARGIN + ((PIXEL_MARGIN + PIXEL_WIDTH) * column),
                    PIXEL_MARGIN + ((PIXEL_MARGIN + PIXEL_HEIGHT) * row),
                    PIXEL_WIDTH,
                    PIXEL_HEIGHT
                ]
            )

    # Limit the framerate to 30FPS (looks better than 60FPS)
    clock.tick(30)

    # Draw to the display
    pygame.display.flip()