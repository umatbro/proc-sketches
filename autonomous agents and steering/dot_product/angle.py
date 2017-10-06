import sys
import pygame
from pygame.math import Vector2
from math import acos, degrees

# setup
pygame.init()

WIDTH = 640
HEIGHT = 480
MAX_FRAMES = 60
LINE_LEN = 140

CENTER = Vector2(WIDTH / 2, HEIGHT / 2)
normal_vector = Vector2(LINE_LEN, 0)
user_vector = Vector2(0, 0)

# create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# create clock
clock = pygame.time.Clock()
total_time = 0

consolas_font = pygame.font.SysFont('Consolas', size=40, bold=True)

# main loop
while True:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
            sys.exit(0)

    total_time += clock.tick(MAX_FRAMES)
    screen.fill((255, 255, 255))

    # mose pos
    mpos = pygame.mouse.get_pos()
    user_vector = mpos - CENTER  # type: Vector2
    user_vector.scale_to_length(LINE_LEN)

    # how to calculate angle between 2 vectors A and B
    # A_x * B_x + A_y + B_y = |A| * |B| * cos(A, B),  so:
    # angle(A, B) = cos^(-1)((A_x * B_x + A_y + B_y)/(|A| * |B| )

    # calculate angle between user_vector and normal_vector
    _cos = (user_vector.x * normal_vector.x + user_vector.y * normal_vector.y) / (user_vector.length() * normal_vector.length())
    angle = acos(_cos)

    # draw normal line
    pygame.draw.line(screen, (0, 0, 0), CENTER, CENTER + normal_vector, 3)
    # draw user angle line
    pygame.draw.line(screen, (0, 0, 0), CENTER, CENTER + user_vector, 3)
    pygame.draw.arc(screen, (0, 0, 0), pygame.Rect(CENTER - (50, 50), (100, 100)), 0, angle)

    # render captions
    radians = consolas_font.render('{} rad'.format(round(angle, 2)), True, (0, 0, 0))
    deg = consolas_font.render('{} deg'.format(round(degrees(angle), 1)), True, (0, 0, 0))
    screen.blit(radians, (WIDTH/10, 3 * HEIGHT/4))
    screen.blit(deg, (WIDTH/10, 3*HEIGHT/4 + 50))
    pygame.display.update()
