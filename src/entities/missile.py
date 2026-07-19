from ursina.vec3 import Vec3
from ursina import Entity, color, time

class Missile(Entity):
    def __init__(self):
        super().__init__(y=12, name="missile")
        self.velocity = Vec3(0, 0, 0)

        self.body = Entity(parent=self, y=.3, name="missile-body")

        self.top_part = Entity(
            name="missile-top-part",
            model="cube",
            color=color.red,
            scale=(1, 1.8, 1),
            position=(0, 0, 0),
            collider="box",
            texture="brick",
            parent=self.body
        )

        self.bot_part = Entity(
            name="missile-bot-part",
            model="cube",
            color=color.blue,
            scale=(1, .6, 1),
            texture="brick",
            collider="box",
            parent=self.body
        )
        self.bot_part.position = self.top_part.position + Vec3(0, -1.2, 0)

        self.fire = Entity(
            name="missile-fire",
            model="cube",
            color=color.orange,
            scale=(1, .6, 1),
            position=(0,-.8,0),
            texture="brick",
            parent=self.bot_part,
            enabled=False
        )

    def control(self, rotation, speed=100):
        speed *= time.dt

        match rotation:
            case "up":    self.rotation_x -= speed
            case "down":  self.rotation_x += speed
            case "left":  self.rotation_z -= speed
            case "right": self.rotation_z += speed
            case _: pass

        self.rotation_x %= 360
        self.rotation_y %= 360
        self.rotation_z %= 360

    def move(self, vector3): self.position+=vector3
    
    def onFire(self): self.fire.enabled=True
    def offFire(self): self.fire.enabled=False
