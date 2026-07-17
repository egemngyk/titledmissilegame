from ursina import Ursina, EditorCamera
# pyrefly: ignore [missing-import]
from core.game import Game

app = Ursina()
game = Game()

EditorCamera()

app.run()