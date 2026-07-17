from ursina import Entity, color

class Plot(Entity):
    def __init__(self):
        super().__init__(
            model="cube",
            color=color.gray,
            scale=(10, 1, 10),
            position=(0, 0, 0),
            collider="box",
            texture="noise"
        )