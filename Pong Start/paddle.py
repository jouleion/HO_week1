import numpy
import pygame
from pygame import gfxdraw


class Paddle:
    width = 150
    height = 15
    radius = 50
    mass = 100

    def __init__(self):
        self.position = numpy.array([200, 150])
        self.velocity = numpy.array([0, 0])

    def update(self, screen_size):
        self.velocity[1] = 0
        self.position += self.velocity

        if self.position[0] > screen_size[0] - self.width / 2:
            self.position[0] = screen_size[0] - self.width / 2
        elif self.position[0] < 0 + self.width / 2:
            self.position[0] = self.width / 2

    def get_circle_rect_distance(self, circle_position, rectangle_position):
        circle_x = circle_position[0]
        circle_y = circle_position[1]

        rectangle_x = rectangle_position[0]
        rectangle_y = rectangle_position[1]

        half_width = self.width / 2
        half_heigth = self.height / 2

        # init test variables
        test_x = 0
        test_y = 0
        x_in_paddle = False
        y_in_paddle = False

        # which edge is closest?
        if (circle_x < rectangle_x - half_width):
            # left edge
            test_x = rectangle_x - half_width

        elif (circle_x > rectangle_x + half_width):
            # right edge
            test_x = rectangle_x + half_width
        else:
            x_in_paddle = True

        if (circle_y < rectangle_y - half_heigth):
            # top edge
            test_y = rectangle_y - half_heigth

        elif (circle_y > rectangle_y + half_heigth):
            # bottom edge
            test_y = rectangle_y + half_heigth
        else:
            y_in_paddle = True

        if(x_in_paddle and y_in_paddle):
            return -1

        dist_x = circle_x - test_x
        dist_y = circle_y - test_y

        # return distance
        return numpy.sqrt(dist_x ** 2 + dist_y ** 2)

    def check_collision(self, other):
        # rectangle circle collision
        distance_now = self.get_circle_rect_distance(other.position, self.position)
        distance_next = self.get_circle_rect_distance(other.position + other.velocity, self.position + self.velocity)

        if(distance_now == -1 or distance_next == -1):
            print("Ball in paddle")

        # check if ball is colliding in the next frame, but not this frame, then update velociy of ball
        if distance_now > other.radius > distance_next:
            print("Touching")

            # calculate bounce with impulse
            d_vel = self.velocity - other.velocity
            d_pos = self.position - other.position
            numerator = d_vel[0] * d_pos[0] + d_vel[1] * d_pos[1]
            denominator = d_pos[0] ** 2 + d_pos[1] ** 2

            # mass calculation
            mass_fraction_self = (2 * other.mass) / (self.mass + other.mass)
            mass_fraction_other = (2 * self.mass) / (self.mass + other.mass)

            # calulate fraction for the bounce
            fraction = numerator / denominator

            # set calculate own and others velocity in x and y axis
            # new_dx1 = self.velocity[0] - mass_fraction_self * fraction * d_pos[0]
            # new_dy1 = self.velocity[1] - mass_fraction_self * fraction * d_pos[1]
            new_dx2 = other.velocity[0] - mass_fraction_other * fraction * (-d_pos[0])
            new_dy2 = other.velocity[1] - mass_fraction_other * fraction * (-d_pos[1])

            # only set the velocity when all is calculated
            # do not set own velocity as the paddle is clamped
            # self.velocity[0] = new_dx1 * 0.95
            # self.velocity[1] = new_dy1 * 0.95
            other.velocity[0] = new_dx2
            other.velocity[1] = new_dy2

    def draw(self, screen):

        gfxdraw.box(
            screen,
            (
                self.position[0] - int(self.width / 2),
                self.position[1] - int(self.height / 2),
                self.width,
                self.height
            ),
            (255, 255, 255)
        )

    def set_speed(self, direction):
        self.velocity[0] = direction * 10


"""
Cirlce cirlce collision

    # get distance between paddle and ball
    distance_vector = self.position - other.position
    distance = numpy.sqrt(distance_vector.dot(distance_vector))

    # calculate next distance after one step considering velocity
    next_distance_vector = self.position + self.velocity - (other.position + other.velocity)
    next_distance = numpy.sqrt(next_distance_vector.dot(next_distance_vector))

    # minimal distance between objects
    collision_distance = self.radius + other.radius

    # if not touching now, but touching in the next frame
    if (distance > collision_distance) and (next_distance < collision_distance):
"""