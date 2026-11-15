import pygame
import time
from math import sin, radians

class controlSwitch:
    def __init__(self, x: int, y: int, name: str, state: bool = False, fontSize: int = 25, animationTime: float = 0.2) -> None:
        self.x: int = x
        self.y: int = y

        self.width: int = 100
        self.height: int = 50

        self.name: str = name
        self.state: bool = state    # STATE? STATE?????

        # ============ animation helpers ===============
        self.timeLastSwitch: float = 0
        self.animationTime: float = animationTime


        # ================== switch title ================
        pygame.font.init()
        self.font = pygame.font.SysFont("Ubuntu", fontSize)
        self.title = self.font.render(self.name, False, (255, 255, 255))
        self.totalHeight = self.title.get_height() + 10 + self.height
        self.totalWidth = max(self.title.get_width(), self.width)

        # ================= single panels ================
        self.switchPanel = pygame.Surface((self.width, self.height))
        self.titlePanel = pygame.Surface((self.width, self.height))

        # ================= complete panel ===============
        self.allPanel = pygame.Surface((self.totalWidth, self.totalHeight))

    def checkClick(self, clickPos: tuple[int, int]) -> None:
        # check if click is within render box
        if self.x < clickPos[0] < self.x + self.width and self.y < clickPos[1] < self.y + self.height:
            self.toggleState()

    def renderSwitch(self) -> pygame.Surface:
        self.switchPanel.fill((0, 0, 0))
        pygame.draw.line(self.switchPanel, (100, 100, 100), (10, self.height // 2), (90, self.height // 2), 5)

        # ================= animation calcs =================
        deltaTimeTo180Deg: float = min((time.time() - self.timeLastSwitch) / self.animationTime * 180, 180)
        sineSmooting: float = (sin(radians(deltaTimeTo180Deg - 90)) + 1)  / 2
        xDistance:int = int(sineSmooting * 50)
        if self.state:
            pygame.draw.rect(self.switchPanel, (0, 255, 0), (10 + xDistance, 0, 30, self.height), border_radius=7)
        else:
            pygame.draw.rect(self.switchPanel, (255, 0, 0), (60 - xDistance, 0, 30, self.height), border_radius=7)
        return self.switchPanel

    def renderTitle(self) -> pygame.Surface:
        self.title = self.font.render(self.name, False, (255, 255, 255))
        return self.title

    def renderAll(self) -> pygame.Surface:
        self.allPanel.blit(self.renderSwitch(), (0, 0))
        self.allPanel.blit(self.renderTitle(), (0, self.height))
        return self.allPanel

    def getState(self) -> bool:
        return self.state

    def setState(self, state: bool) -> None:
        self.state = state

    def toggleState(self) -> None:
        self.state = not self.state
        self.timeLastSwitch = time.time()

    def getPos(self) -> tuple[int, int]:
        return (self.x, self.y)