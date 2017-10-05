import sys
import pygame
from flockin_py.vehicle import Vehicle
from flockin_py.flow_field import FlowField

pygame.init()

WIDTH = 640
HEIGHT = 480
MAX_FRAMES = 60

# create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# create clock
clock = pygame.time.Clock()
total_time = 0

vehicle = Vehicle(screen, WIDTH/2, HEIGHT/2)
vehicles = []

# create flow field
flow_field = FlowField(screen, 30)
debug_ff = False

# main loop
while 1337:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
            sys.exit(0)
        elif event.type is pygame.KEYDOWN and event.key is pygame.K_SPACE:
            debug_ff = not debug_ff
        elif event.type is pygame.KEYDOWN and event.key is pygame.K_r:
            flow_field = FlowField(screen, 30)

    total_time += clock.tick(MAX_FRAMES)
    screen.fill((255, 255, 255))

    m_pos = pygame.mouse.get_pos()

    if debug_ff:
        flow_field.display()

    if any(pygame.mouse.get_pressed()):
        vehicles.append(Vehicle(screen, m_pos[0], m_pos[1]))

    for veh in vehicles:
        veh.follow(flow_field)
        veh.update()
        veh.display()

    vehicle.arrive(m_pos)
    vehicle.update()
    vehicle.display()

    pygame.display.update()