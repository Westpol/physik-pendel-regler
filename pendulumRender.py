import pygame
import math
import copy

class PendulumRenderer:
    def __init__(self, width: int, height: int, length: int, ballRadius: int):
        self.width = width
        self.height = height
        self.length = length
        self.ballRadius = ballRadius
        self.panel = pygame.Surface((self.width, self.height))

    def render(self, angle: float, cartPos: float | int) -> pygame.Surface:
        self.panel.fill((0, 0, 0))      # reset screen

        cartPos += self.width // 2      # scale arguments to correct values
        angle += math.pi / 2

        x = math.cos(angle) * self.length + cartPos     # calculate pendulum end position
        y = math.sin(angle) * self.length + self.height // 2

        pygame.draw.rect(self.panel, (100, 100, 100), (100, self.height // 2 - 5, self.width - 200, 10))
        pygame.draw.rect(self.panel, (255, 0, 0), (cartPos - 40 // 2, self.height // 2 - 20 // 2, 40, 20), 0)   # draw cart

        pygame.draw.line(self.panel, (255, 255, 255), (cartPos, self.height // 2), (x, y), 2)   # draw pendulum
        pygame.draw.circle(self.panel, (255, 255, 255), (x, y), self.ballRadius)


        return self.panel
