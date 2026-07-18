from ursina import Ursina, EditorCamera, held_keys, time
from core.game import Game

app = Ursina()
game = Game()

def update(): game.update(held_keys, time.dt)

EditorCamera()

app.run()