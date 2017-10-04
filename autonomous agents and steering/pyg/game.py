import sys
import pygame
from rocket import Rocket


class Game:
    def __init__(self, width=640, height=480):
        # config
        self.tps_max = 100.0
        self.width = width
        self.height = height

        # initialization
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player = Rocket(self)

        breaky = False

        while True:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE:
                    breaky = True

            if breaky: break

            self.tps_delta += self.tps_clock.tick(50) / 1000.0
            while self.tps_delta > 1/self.tps_max:
                self.tick()
                self.tps_delta -= 1/self.tps_max

            # drawing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        # checking inputs
        self.player.tick()

    def draw(self):
        mp_x, mp_y = pygame.mouse.get_pos()

        # pygame.draw.rect(self.screen, (100, 0, 200), pygame.Rect(10, 10, 50, 50))
        pygame.draw.circle(self.screen, (110, 110, 110), (mp_x, mp_y), 20)

        self.player.draw()