import pygame
import time
import sys
import core

WHITE = (255, 255, 255)
RED = (100, 0, 0)
YELLOW = (255, 255, 0)
DARK_RED = (30, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

MARGIN = 50


class Display:
    def __init__(self, window_size):
        pygame.init()
        self.screen = pygame.display.set_mode(window_size)
        self.scale = window_size[0] - 2 * MARGIN
        self.xoffset = MARGIN
        self.yoffset = window_size[1] / 2
        pygame.display.set_caption("Bee Tunnel Simulation")

    def update(self, data):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        self.screen.fill(BLACK)
        for sensor in data.sensors:
            self.draw_sensor(sensor)
        for bee in data.bees:
            self.draw_bee(bee)
        pygame.display.flip()
        time.sleep(data.dt)

    def draw_bee(self, bee: core.Bee):
        pygame.draw.rect(
            self.screen,
            YELLOW,
            pygame.rect.Rect(
                self.xoffset + self.scale * (bee.position - bee.radius),
                self.yoffset - 15,
                self.scale * 2 * bee.radius,
                30,
            ),
        )

    def draw_sensor(self, sensor: core.Sensor):
        pygame.draw.rect(
            self.screen,
            RED if sensor.triggered else DARK_RED,
            pygame.rect.Rect(
                self.xoffset + self.scale * (sensor.position - sensor.radius),
                self.yoffset - 150,
                self.scale * 2 * sensor.radius,
                300,
            ),
        )


class DummyDisplay:
    def __init__(self, window_size):
        pass

    def update(self, data):
        pass
