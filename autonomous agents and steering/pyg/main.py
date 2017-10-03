import sys
import pygame


def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


pygame.init()

width = 640
height = 480
MAX_FRAMES = 60
screen = pygame.display.set_mode((width, height))

box = pygame.Rect(10, 10, 50, 50)

clock = pygame.time.Clock()
delta = 0.0

frames = 0
breaky = False

while 1337:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            sys.exit('1337')
        elif event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
            breaky = True

    if breaky: break
    # ticking
    delta += clock.tick(MAX_FRAMES)/1000

    mp_x, mp_y = pygame.mouse.get_pos()

    color_g = remap(mp_x, 0, width, 0, 255)
    color_b = remap(mp_y, 0, height, 0, 255)
    screen.fill((0, color_g, color_b))

    # checking inputs
    if pygame.key.get_pressed()[pygame.K_d]:
        box.x += 1
    if pygame.key.get_pressed()[pygame.K_a]:
        box.x -= 1
    if pygame.key.get_pressed()[pygame.K_s]:
        box.y += 1
    if pygame.key.get_pressed()[pygame.K_w]:
        box.y -= 1

    pygame.draw.rect(screen, (100, 0, 200), box)
    pygame.draw.circle(screen, (110, 110, 110), (mp_x, mp_y), 20)
    pygame.display.flip()

    frames += 1

print('Time: {} s'.format(delta))
print('Frames: {}'.format(frames))
print('AVG FPS: {} frames/s'.format(frames/delta))
