import pygame
from pygame.math import Vector2
from utils import remap


def limit_vector(vector, limit):
    if vector.length() <= limit:
        return vector
    else:
        vector.scale_to_length(limit)
        return vector


class Vehicle:
    def __init__(self, screen, x=0, y=0):
        self.screen = screen
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, -2)
        self.acceleration = Vector2(0, 0)

        self.r = 6
        self.maxspeed = 4
        self.maxforce = 0.3

    @property
    def point(self):
        return Vector2(0, self.r*2) + self.position

    def update(self):
        # update velocity
        self.velocity += self.acceleration
        limit_vector(self.velocity, self.maxspeed)

        # reset acceleration each cycle
        self.acceleration *= 0

        self.position += self.velocity

    def apply_force(self, force):
        self.acceleration += force

    def seek(self, target):
        """
        A method that calculates a steering force towards a target
        steer = desired - velocity
        """
        desired = target - self.position  # type: Vector2

        # scale to maximum speed
        try:
            desired.scale_to_length(self.maxspeed)
        except (ValueError, ZeroDivisionError):
            desired = self.position

        steer = desired - self.velocity
        # steer.limit(self.maxforce)
        limit_vector(steer, self.maxforce)
        self.apply_force(steer)

    def arrive(self, target):
        """
        A method that calculates a steering force towards a target
        STEER = DESIRED - VELOCITY
        """
        desired = target - self.position
        desired_len = desired.length()

        m = remap(desired_len, 0, 50, 0, self.maxspeed)
        try:
            desired.scale_to_length(m)
        except (ValueError, ZeroDivisionError):
            desired = self.position

        steer = desired - self.velocity
        limit_vector(steer, self.maxforce)
        self.apply_force(steer)

    def display(self):
        points = [
            Vector2(0, self.r * 2),
            Vector2(-self.r, -self.r * 2),
            Vector2(self.r, -self.r * 2)
        ]

        theta = self.velocity.angle_to(Vector2(0, 1))

        # rotate points
        points = [p.rotate(theta) for p in points]
        # and move to position
        # points = [Vector2(-p.x, p.y) + self.position for p in points]
        ref = Vector2(1, 0)
        points = [p.reflect(ref) + self.position for p in points]

        pygame.draw.polygon(self.screen, (127, 127, 127), points)
