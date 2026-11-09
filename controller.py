import math
import time

import pendulum

class Controller:
    def __init__(self, pendulum: pendulum.Pendulum):
        self.pendulum = pendulum
        self.lastUpdate = time.time()

    def update(self) -> float:
        now = time.time()
        dt = now - self.lastUpdate

        # skip calculation if dt is 0
        if dt == 0:
            self.lastUpdate = now
            return 0

        angle = self.pendulum.getAngle()
        velocity = self.pendulum.getVelocity()
        cartPos = self.pendulum.getCartPos()
        cartVelocity = self.pendulum.getCartVelocity()
        pAngle = (angle + math.pi) % (2 * math.pi)
        angleSetpoint = math.pi

        correctiveCommand: float = 0

        # cart PID

        angleSetpoint += cartPos * 0.1
        angleSetpoint += (cartVelocity * 0.3) * (min(abs(cartPos * 0.1), 0.9) + 0.2)  # D and D relax
        angleSetpoint += cartPos * 0.02

        angleSetpoint = min(max(angleSetpoint, math.pi - math.pi / 8), math.pi + math.pi / 8)

        # pendulum PID
        if angle < math.pi / 2 or angle > math.pi * 2 - (math.pi / 2):
            # upright
            # negative = right
            correctiveCommand += -(pAngle - angleSetpoint) * 1000     # P
            correctiveCommand += -velocity * 100                # D
        else:
            # downright
            # negative = left
            correctiveCommand += (pAngle - angleSetpoint) * 100
            correctiveCommand += velocity * 100

        #print(correctiveCommand)
        #print(1/(now - self.lastUpdate))

        self.lastUpdate = now

        return correctiveCommand

    def unpause(self):
        self.lastUpdate = time.time()