import pygame

class controlSwitch:
    def __init__(self, x: int, y: int, name: str, state: bool = False) -> None:
        self.x: int = x
        self.y: int = y

        self.width: int = 100
        self.height: int = 50

        self.name: str = name
        self.state: bool = state    # STATE? STATE?????

        # ================== switch title ================
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
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
            self.state = not self.state

    def renderSwitch(self) -> pygame.Surface:
        self.switchPanel.fill((0, 0, 0))
        pygame.draw.line(self.switchPanel, (100, 100, 100), (10, self.height // 2), (90, self.height // 2), 5)
        if self.state:
            pygame.draw.rect(self.switchPanel, (0, 255, 0), (60, 0, 30, self.height))
        else:
            pygame.draw.rect(self.switchPanel, (255, 0, 0), (10, 0, 30, self.height))
        return self.switchPanel

    def renderTitle(self) -> pygame.Surface:
        self.title = self.font.render(self.name, True, (255, 255, 255))
        return self.title

    def renderAll(self) -> pygame.Surface:
        self.allPanel.blit(self.renderSwitch(), (0, 0))
        self.allPanel.blit(self.renderTitle(), (0, self.height))
        return self.allPanel

    def getState(self) -> bool:
        return self.state

    def setState(self, state: bool) -> None:
        self.state = state

    def getPos(self) -> tuple[int, int]:
        return (self.x, self.y)