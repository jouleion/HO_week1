# Particle System
# taken from https://www.makeuseof.com/pygame-games-special-effects-particle-systems-visual-enhancements/
# Altered by Julian van der Sluis

import pygame
import random

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)
        self.lifetime = 60

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.lifetime -= 1

    def draw(self, window):
        color = (200, 200, 200)
        position = (int(self.x), int(self.y))
        pygame.draw.circle(window, color, position, 2)

# Particle system class
class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add_particle(self, x, y):
        self.particles.append(Particle(x, y))

    def update(self):
        for particle in self.particles:
            particle.update()

            if particle.lifetime <= 0:
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
                    self.lifetime = 60

                def update(self):
                    self.x += self.dx
                    self.y += self.dy
                    self.lifetime -= 1

                def draw(self, window):
                    color = (200, 200, 200)
                    position = (int(self.x), int(self.y))
                    pygame.draw.circle(window, color, position, 2)
