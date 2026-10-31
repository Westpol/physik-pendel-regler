import math
import time

import pendulum

class Controller:
    def __init__(self, pendulum: pendulum.Pendulum):
        self.pendulum = pendulum
        self.lastUpdate = time.time()

    def update(self) -> float:
        now = time.time()

        angle = self.pendulum.getAngle()
        velocity = self.pendulum.getVelocity()
        cartPos = self.pendulum.getCartPos()
        cartVelocity = self.pendulum.getCartVelocity()
        pAngle = (angle + math.pi) % (2 * math.pi)
        angleSetpoint = math.pi

        correctiveCommand: float = 0

        # cart PID

        angleSetpoint += cartPos * 0.1
        angleSetpoint += (cartVelocity * 0.5) * min(abs(cartPos * 0.1), 1)
        angleSetpoint += cartPos * 0.02

        angleSetpoint = min(max(angleSetpoint, math.pi - math.pi / 8), math.pi + math.pi / 8)

        # pendulum PID
        if angle < math.pi / 2 or angle > math.pi * 2 - (math.pi / 2):
            # upright
            # negative = right
            correctiveCommand += -(pAngle - angleSetpoint) * 1000     # P
            correctiveCommand += -velocity * 100                # I
        else:
            # downright
            # degative = left
            correctiveCommand += (pAngle - angleSetpoint) * 100
            correctiveCommand += velocity * 100

        print()
        #print(1/(now - self.lastUpdate))

        self.lastUpdate = now

        return correctiveCommand