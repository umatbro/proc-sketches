import pygame
import random
import utils
from math import pi, cos, sin
from pygame.math import Vector2


class FlowField:
    def __init__(self, screen, resolution):
        self.resolution = resolution
        self.screen = screen

        # generate field, with random vectors pointing to the right
        # (angle between Vector(1, 0) being from -pi/4 to pi/4
        self.field = []
        for row in range(self.rows):
            self.field.append([])
            for col in range(self.cols):
                angle = random.uniform(-pi/4, pi/4)
                self.field[row].append(Vector2(cos(angle), sin(angle)))

    @property
    def cols(self):
        return int(self.screen.get_size()[0] / self.resolution)

    @property
    def rows(self):
        return int(self.screen.get_size()[1] / self.resolution)

    def draw_vector(self, vector, start_pos, length=10):
        v2 = Vector2(vector.x, vector.y)
        v2.scale_to_length(length)
        pygame.draw.line(self.screen, (150, 150, 150), start_pos, v2 + start_pos)

    def lookup(self, position: Vector2):
        """
        Look up flow field Vector value at given position

        :param position: Vector2 with x, y coords of considered place
        :return: Vector at that position (copy)
        """

        col = utils.constrain(int(position.x / self.resolution), self.cols - 1)
        row = utils.constrain(int(position.y / self.resolution), self.rows - 1)
        vec = self.field[row][col]
        return Vector2(vec.x, vec.y)

    def display(self):
        """
        Draw every vector
        """
        for row in range(self.rows):
            for col in range(self.cols):
                self.draw_vector(self.field[row][col], Vector2(col * self.resolution, row * self.resolution))