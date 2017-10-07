"""
ref: https://www.youtube.com/watch?v=KWoJgHFYWxY
src paper: http://algorithmicbotany.org/papers/abop/abop-ch4.pdf
"""
import sys
import pygame
from math import sqrt, cos, sin, radians

pygame.init()

WIDTH = 640
HEIGHT = 480
MAX_FRAMES = 60

# create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0, 0, 0))

# create clock
clock = pygame.time.Clock()
total_time = 0

# variable to keep track of dots
n = 0
c = 6

# main loop
while 1337:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
            sys.exit(0)

    total_time += clock.tick(MAX_FRAMES)
    # screen.fill((0, 0, 0))

    # m_pos = pygame.mouse.get_pos()

    angle = n * 137.5
    angle_rad = radians(angle)
    r = c * sqrt(n)

    x = r * cos(angle_rad) + WIDTH/2
    y = r * sin(angle_rad) + HEIGHT/2
    x = int(x); y = int(y)

    pygame.draw.circle(screen, (0, 0, 0), (x, y), 10)
    pygame.draw.circle(screen, (r % 255, 255 - angle % 256, 0), (x, y), 8)
    pygame.display.update()

    n += 1