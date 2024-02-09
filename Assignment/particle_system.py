# Particle System
# taken from https://www.makeuseof.com/pygame-games-special-effects-particle-systems-visual-enhancements/
# Altered by Julian van der Sluis and Willem Paternotte

import pygame
import random

class Particle:
    def __init__(self, x, y,init_color):
        self.x = x
        self.y = y
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)
        self.lifetime = 60
        self.color = init_color

    def update(self, update_color):
        self.color = update_color
        self.x += self.dx
        self.y += self.dy
        self.lifetime -= 1

    def draw(self, window):
        position = (int(self.x), int(self.y))
        pygame.draw.circle(window, self.color, position, 2)

    def get_lifetime(self):
        return self.lifetime

# Particle system class
class ParticleSystem:
    def __init__(self):
        self.particles = []

        self.color_speed = 1.001

        self.r = random.randint(50, 255)
        self.g = random.randint(50, 255)
        self.b = random.randint(50, 255)

        self.rfac = random.random() * 1.5 + 0.2
        self.gfac = random.random() * 1.5 + 0.2
        self.bfac = random.random() * 1.5 + 0.2

        self.rdir = 1
        self.gdir = 1
        self.bdir = 1

    def check_color_direction(self, color, dir):
        new_dir = dir
        if dir > 0:
            if color > 230:
                new_dir = -1
        else:
            if color < 50:
                new_dir = 1
        return new_dir

    def update_color(self):

        # update color values, move color direction randomly, control direction of movement
        self.r += int(self.rfac * self.rdir * random.random() * self.color_speed)
        self.g += int(self.gfac * self.gdir * random.random() * self.color_speed)
        self.b += int(self.bfac * self.bdir * random.random() * self.color_speed)

        # limit color direction
        self.rdir = self.check_color_direction(self.r, self.rdir)
        self.gdir = self.check_color_direction(self.g, self.gdir)
        self.bdir = self.check_color_direction(self.b, self.bdir)

        color = pygame.Color(self.r, self.g, self.b)
        return color

    def add_particle(self, x, y):
        self.particles.append(Particle(x, y, self.update_color()))

    def update(self):
        color = self.update_color()
        for particle in self.particles:
            particle.update(color)

            if particle.get_lifetime() <= 0:
                self.particles.remove(particle)

    def draw(self, window):
        for particle in self.particles:
            particle.draw(window)

            # Particle class
            class Particle:
                def __init__(self, x, y):
                    self.x = x
                    self.y = y
                    self.dx = random.uniform(-1, 1)
                    self.dy = random.uniform(-1, 1)
                    self.lifetime = 30

                def update(self):
                    self.x += self.dx
                    self.y += self.dy
                    self.lifetime -= 1

                def draw(self, window):
                    color = (200, 200, 200)
                    position = (int(self.x), int(self.y))
                    pygame.draw.circle(window, color, position, 2)
