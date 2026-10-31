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
        pAngle = (angle + math.pi) % (2 * math.pi)

        correctiveCommand: float = 0

        # pendulum PID
        if angle < math.pi / 2 or angle > math.pi * 2 - (math.pi / 2):
            # upright
            # negative = right
            correctiveCommand += -(pAngle - math.pi) * 1000     # P
            correctiveCommand += -velocity * 100                # I
        else:
            # downright
            # degative = left
            correctiveCommand += (pAngle - math.pi) * 100
            correctiveCommand += velocity * 100

        print()
        #print(1/(now - self.lastUpdate))

        self.lastUpdate = now

        return correctiveCommand