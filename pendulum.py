import pygame
import pendulumRender
import time
import math

class Pendulum:
    def __init__(self, startAngle: float = 0, startVelocity: float = 0, startPosition: int = 0, cartMass: float = 1, pendulumMass: float = 1, pendulumLenght: float = 400):
        self.angle = startAngle
        self.angularVelocity = startVelocity
        self.cartPosition = startPosition
        self.cartVelocity = 0
        self.cartMass = cartMass
        self.pendulumMass = pendulumMass
        self.pendulumLength = pendulumLenght
        self.pr = pendulumRender.PendulumRenderer(1500, 1200, self.pendulumLength, 20)

        self.lastUpdate = time.time()

    def update(self, force: float):
        now = time.time()
        cartAcceleration: float =
        pendulumAcceleration: float =

        # ============== velocity from acceleration =============
        self.cartVelocity += cartAcceleration * (now - self.lastUpdate)
        self.angularVelocity += pendulumAcceleration * (now - self.lastUpdate)

        # ============== position from velocity ====================
        self.cartPosition += self.cartVelocity * (now - self.lastUpdate)
        self.angle += self.angularVelocity * (now - self.lastUpdate)

        self.lastUpdate = now

    def render(self, angle: float, cartPos: float | int) -> pygame.Surface:
        return self.pr.render(self.angle, self.cartPosition)