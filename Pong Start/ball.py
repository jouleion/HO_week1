import math
import random
import pygame
import numpy
from pygame import gfxdraw


class Ball:
    """
    A class for a circular object with a position and a speed
    """
    position = numpy.array([300, 300])
    velocity = numpy.array([0, 0])
    max_speed = 5

    def __init__(self, new_x, new_y, radius, team):
        self.radius = radius
        self.diameter = 2 * self.radius
        self.mass = math.pi*(radius**2)
        self.team = team

        # set color dependent on team
        if team == 0:
            self.color = (100, 100, 255)
        else:
            self.color = (255, 100, 100)

        self.position = numpy.array([float(new_x), float(new_y)])
        self.velocity = 5 * numpy.array([random.uniform(-1, 1), random.uniform(-1, 1)])

    def update(self, screen_size):
        # get speed
        if(numpy.sqrt(self.velocity.dot(self.velocity)) != self.max_speed):
            self.velocity = self.max_speed * self.velocity / (numpy.linalg.norm(self.velocity) + 1e-16)
        self.position += self.velocity

        if self.position[0] < self.radius and self.velocity[0] < 0:
            self.velocity[0] = -self.velocity[0] * random.uniform(0.8, 1.2)

        if self.position[1] < self.radius and self.velocity[1] < 0:
            self.velocity[1] = -self.velocity[1] * random.uniform(0.8, 1.2)

        if self.position[0] > screen_size[0] - self.radius and self.velocity[0] > 0:
            self.velocity[0] = -self.velocity[0] * random.uniform(0.8, 1.2)

        if self.position[1] > screen_size[1] - self.radius and self.velocity[1] > 0:
            self.velocity[1] = -self.velocity[1] * random.uniform(0.5, 1)

    def draw(self, screen):
        # draw anit aliased circle
        gfxdraw.aacircle(screen, int(self.position[0]), int(self.position[1]), int(self.radius), self.color)
        gfxdraw.filled_circle(screen, int(self.position[0]), int(self.position[1]), int(self.radius), self.color)

    def __del__(self):
        pass

    def identify(self):
        pass

    def __eq__(self, other):
        return self.team == other.team
