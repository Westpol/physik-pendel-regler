import pygame
import pendulumRender
import time

class Pendulum:
    def __init__(self, startAngle: float = 0, startVelocity: float = 0, startPosition: int = 0, cartMass: float = 10, pendulumMass: float = 1, pendulumLenght: float = 400):
        self.angle = startAngle
        self.angularVelocity = startVelocity
        self.position = startPosition
        self.cartMass = cartMass
        self.pendulumMass = pendulumMass
        self.pendulumLength = pendulumLenght
        self.pr = pendulumRender.PendulumRenderer(1500, 1200, self.pendulumLength, 20)

        self.lastUpdate = time.time()

    def update(self):
        now = time.time()

        self.lastUpdate = now

    def render(self, angle: float, cartPos: float | int) -> pygame.Surface:
        return self.pr.render(angle, cartPos)