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

        if angle < math.pi / 2 or angle > math.pi * 2 - (math.pi / 2):
            print("upright")
        else:
            print("downright")

        #print(angle)
        #print(1/(now - self.lastUpdate))

        self.lastUpdate = now

        return 0