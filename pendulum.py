import pygame
import pendulumRender
import time
import math

class Pendulum:
    def __init__(self, startAngle: float = 0, startVelocity: float = 0, startPosition: int = 0, cartMass: float = 5, pendulumMass: float = 1, pendulumLenght: int = 400):
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
        dt = now - self.lastUpdate

        # skip calculation if dt is 0
        if dt == 0:
            self.lastUpdate = now
            return

        sin_theta = math.sin(self.angle)
        cos_theta = math.cos(self.angle)

        M = self.cartMass
        m = self.pendulumMass
        L = self.pendulumLength / 400   # 400 pixel per meter
        g = 9.81

        denominator = M + m * sin_theta ** 2

        cartAcceleration = (force - m * L * self.angularVelocity ** 2 * sin_theta + m * g * sin_theta * cos_theta) / denominator

        pendulumAcceleration = (force * cos_theta - m * L * self.angularVelocity ** 2 * sin_theta * cos_theta + (M + m) * g * sin_theta) / (L * denominator)

        # ============== velocity from acceleration =============
        self.cartVelocity += cartAcceleration * dt
        self.angularVelocity += pendulumAcceleration * dt

        # ============== position from velocity ====================
        self.cartPosition += self.cartVelocity * dt
        self.angle += self.angularVelocity * dt

        self.lastUpdate = now

    def render(self) -> pygame.Surface:
        BASE_SCALING = 400
        MAX_SCALING = 600
        MIN_SCALING = 50

        maxDistance = (self.pr.width - 200) / 2     # Maximum visible distance in pixels

        distance = abs(self.cartPosition) * BASE_SCALING    # Distance the cart travels in pixels at the default scale

        scaling = BASE_SCALING

        if distance > maxDistance:      # Only zoom out when the cart reaches the end of the rail
            scaling = BASE_SCALING * (maxDistance / distance)

        scaling = min(max(scaling, MIN_SCALING), MAX_SCALING)

        return self.pr.render(self.angle, self.cartPosition * scaling, int(scaling))

    def unpause(self):
        self.lastUpdate = time.time()

    def getAngle(self) -> float:
        return self.angle % (2 * math.pi)

    def getVelocity(self) -> float:
        return self.angularVelocity

    def getCartPos(self) -> float:
        return self.cartPosition

    def getCartVelocity(self) -> float:
        return self.cartVelocity