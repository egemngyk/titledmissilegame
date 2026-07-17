from ursina import Entity, color

class Missile(Entity):
    def __init__(self):
        super().__init__(
            model="cube",
            color=color.red,
            scale=(1, 2, 1),
            position=(0, 2, 0),
            collider="box",
            texture="brick"
        )

        bot_part = Entity(
            model="cube",
            color=color.blue,
            scale=(1, .6, 1),
            position=(0,-.8,0),
            collider="box",
            texture="brick",
            parent=self
        )