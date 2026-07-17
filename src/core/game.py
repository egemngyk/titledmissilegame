# pyrefly: ignore [missing-import]
from world.plot import Plot
# pyrefly: ignore [missing-import]
from entities.missile import Missile

class Game:
    def __init__(self):
        self.plot = Plot()
        self.missile = Missile()