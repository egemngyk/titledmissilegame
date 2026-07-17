from ursina import held_keys
# pyrefly: ignore [missing-import]
from world.plot import Plot
# pyrefly: ignore [missing-import]
from entities.missile import Missile

class Game:
    def __init__(self):
        self.plot = Plot()

        self.missile = Missile()
        self.missile.thrust=25

    def update(self):
        if held_keys["space"]:
            self.missile.throttle(self.missile.thrust)
        else:
            self.missile.coast()

        key_map = {"w": "up", "a": "left", "s": "down", "d": "right"}
        for key, rotation in key_map.items():
            if held_keys[key]:
                self.missile.control(rotation)

    def input(self, key):
        pass