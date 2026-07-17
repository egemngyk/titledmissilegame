from ursina import Ursina, EditorCamera
# pyrefly: ignore [missing-import]
from core.game import Game

app = Ursina()
game = Game()

def update(): game.update()

def input(key): game.input(key)

EditorCamera()

app.run()