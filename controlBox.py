import pygame

class controlBox:
    def __init__(self, x: int, y: int, title: str, defaultValue: float = 0):
        self.x: int = x
        self.y: int = y

        self.title: str = title

        self.value: float = defaultValue


    def checkClicked(self):
        pass