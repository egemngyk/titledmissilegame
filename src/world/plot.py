from ursina import texture
from ursina import Entity, color

class Plot(Entity):
    def __init__(self):
        super().__init__(
            model="cube",
            color=color.gray,
            scale=(100, 2, 100),
            position=(0, -2, 0),
            collider="box",
            texture="noise",
            texture_scale=(10, 10)
        )