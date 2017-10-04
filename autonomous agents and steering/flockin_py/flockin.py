import sys
import pygame
from flockin_py.vehicle import Vehicle

pygame.init()

WIDTH = 640
HEIGHT = 480
MAX_FRAMES = 60

# create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# create clock
clock = pygame.time.Clock()

vehicle = Vehicle(screen, WIDTH/2, HEIGHT/2)

# main loop
while 1337:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
            sys.exit(0)

    clock.tick(MAX_FRAMES)
    screen.fill((255, 255, 255))

    vehicle.arrive(pygame.mouse.get_pos())
    vehicle.update()
    vehicle.display()

    pygame.display.update()