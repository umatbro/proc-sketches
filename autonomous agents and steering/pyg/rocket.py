import pygame
from pygame.math import Vector2
from math import pi


class Rocket:
    def __init__(self, game):
        self.game = game

        width, height = self.game.screen.get_size()

        self.pos = Vector2((width/2, height/2))
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

    def add_force(self, force_x, force_y):
        self.acc += Vector2(force_x, force_y)

    def tick(self):
        # input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(0, -1)
        if pressed[pygame.K_a]:
            self.add_force(-1, 0)
        if pressed[pygame.K_s]:
            self.add_force(0, 1)
        if pressed[pygame.K_d]:
            self.add_force(1, 0)

        # physics
        fraction = 0.1 * self.vel
        self.vel += self.acc - fraction
        self.pos += self.vel
        self.acc *= 0

        if self.pos.x > self.game.width:
            self.pos.x = 0
        if self.pos.y > self.game.height:
            self.pos.y = 0
        if self.pos.x < 0:
            self.pos.x = self.game.width - 1
        if self.pos.y < 0:
            self.pos.y = self.game.height - 1

    def draw(self):
        # base triangle
        points = [
            Vector2(0, -20),
            Vector2(-10, 10),
            Vector2(10, 10)
        ]

        # rotate points
        angle = self.vel.angle_to(Vector2(0, 1))

        points = [p.rotate(angle) for p in points]

        # calculate final triangle
        points = [Vector2(p.x, -p.y) + self.pos for p in points]

        # draw triangle
        pygame.draw.polygon(self.game.screen, (0, 122, 255), points)
        # rect = pygame.Rect(self.pos.x, self.pos.y, 50, 50)
        # pygame.draw.rect(self.game.screen, (0, 150, 255), rect)

