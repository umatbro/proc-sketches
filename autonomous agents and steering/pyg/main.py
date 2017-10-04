import sys
import pygame
from rocket import Rocket


def remap(x, in_min, in_max, out_min, out_max):
    """
    Map input value (knowing minimum and maximum values that it can take) to another range

    :param x: value to be mapped
    :param in_min: minimum value of input
    :param in_max: maximum value of input
    :param out_min: minimum value of output
    :param out_max: maximum value of output
    :return: changed value
    """
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


pygame.init()

width = 840
height = 600
MAX_FRAMES = 60
screen = pygame.display.set_mode((width, height))

rocket = Rocket(screen)

clock = pygame.time.Clock()
delta = 0.0

frames = 0
breaky = False

while 1337:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit(); sys.exit('1337')
        elif event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
            breaky = True

    if breaky: break
    # ticking
    delta += clock.tick(MAX_FRAMES)/1000

    mp_x, mp_y = pygame.mouse.get_pos()

    color_g = remap(mp_x, 0, width, 0, 255)
    color_b = remap(mp_y, 0, height, 0, 255)
    screen.fill((0, color_g, color_b))

    rocket.tick()
    rocket.draw()
    # pygame.draw.rect(screen, (100, 0, 200), box)
    pygame.draw.circle(screen, (110, 110, 110), (mp_x, mp_y), 20)
    pygame.display.update()

    frames += 1

print('Time: {:.4f} s'.format(delta))
print('Frames: {}'.format(frames))
print('AVG FPS: {:.2f} frames/s'.format(frames/delta))
