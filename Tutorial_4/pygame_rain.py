import pygame
import numpy as np
import random

from TSPDecoder import *

# Define constants
ROWS = 27
COLUMNS = 19
THRESHOLD = 10
WIDTH = ROWS * 10
HEIGHT = 250
DROP_WIDTH = 2
BLACK = (0, 0, 0)
BLUE = (156, 226, 242)
WHITE = (255, 255, 255)

# Initialise the PyGame screen according to resolution
pygame.init()
WINDOW_SIZE = [
    WIDTH,
    HEIGHT
]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Rain example")

# Initialise the PyGame Clock for timing
clock = pygame.time.Clock()

# Initialise the Haptic Skin
TSP = TSPDecoder(rows=ROWS, columns=COLUMNS)


# Class for a single drop in the rain
class Drop:
    # Initialise the drop at random on the screen
    def __init__(self):
        self.x = random.randint(0, WIDTH - DROP_WIDTH)
        self.y = random.randint(0, HEIGHT)

    def update(self, allowed_rows):
        self.y += random.randint(6, 8)

        # If the drop has reached the bottom of the screen, respawn it at the top randomly
        if self.y > HEIGHT:
            # Select an allowed row at random
            row = random.choice(allowed_rows)
            self.x = (row * WIDTH / ROWS) + random.randint(0, int(WIDTH / ROWS))
            self.y = random.randint(-100, -5)

    # Draw the drop as a rounded rectangle
    def draw(self):
        pygame.draw.ellipse(
            screen,
            BLUE,
            [
                self.x,
                self.y,
                DROP_WIDTH,
                10
            ]
        )


# Create drops array
drops = list()

# Make the drops
for i in range(250):
    drops.append(Drop())

# Define the allowed respawn rows
allowed_rows = list()

# Game loop
while TSP.available():
    # Check if the screen is closed and quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Get the frame
    grid = TSP.readFrame()

    # Clear the screen by blacking it out
    screen.fill(BLACK)

    # Check the Left-most row and deteremine the allowed respawn rows
    for row in range(ROWS):
        pixel = grid[row][0]

        # If a touch is detected, remove the row from the allowed rows
        if pixel < THRESHOLD:
            if row not in allowed_rows:
                allowed_rows.append(row)
        else:
            if row in allowed_rows:
                allowed_rows.remove(row)

    print(allowed_rows)

    # Visualise the blocking by drawing rectangles where the touch is detected
    pygame.draw.rect(screen, WHITE, [0, 0, WIDTH, 5])
    for row in allowed_rows:
        pygame.draw.rect(screen, BLACK, [(row * WIDTH / ROWS), 0, WIDTH / ROWS, 5])

    # Loop through all drops, update and draw them on the screen
    for drop in drops:
        drop.update(allowed_rows)
        drop.draw()

    # Limit the framerate to 60FPS
    clock.tick(60)

    # Draw to the display
    pygame.display.flip()
