from ursina.vec3 import Vec3
from ursina import Entity, color, time

class Missile(Entity):
    def __init__(self):
        super().__init__(y=1.2)

        self.body = Entity(parent=self, y=.3)

        self.top_part = Entity(
            model="cube",
            color=color.red,
            scale=(1, 1.8, 1),
            position=(0, 0, 0),
            collider="box",
            texture="brick",
            parent=self.body
        )

        self.bot_part = Entity(
            model="cube",
            color=color.blue,
            scale=(1, .6, 1),
            collider="box",
            texture="brick",
            parent=self.body
        )
        self.bot_part.position = self.top_part.position + Vec3(0, -1.2, 0)

        self.fire = Entity(
            model="cube",
            color=color.orange,
            scale=(1, .6, 1),
            position=(0,-.8,0),
            collider=None,
            texture="brick",
            parent=self.bot_part,
            enabled=False
        )

    def throttle(self, thrust):
        thrust = thrust*.01

        self.position+=self.up*thrust
        
        
        self.fire.enabled=True

    def coast(self):
        self.fire.enabled=False

    def control(self, rotation):
        speed = 100 * time.dt

        if rotation == "up":
            self.rotation_x -= speed
        elif rotation == "down":
            self.rotation_x += speed
        elif rotation == "left": 
            self.rotation_z -= speed
        elif rotation == "right":
            self.rotation_z += speed

        if self.rotation_x >= 360: self.rotation_x = 0
        if self.rotation_y >= 360: self.rotation_y = 0
        if self.rotation_z >= 360: self.rotation_z = 0
        if self.rotation_x <= -360: self.rotation_x = 0
        if self.rotation_y <= -360: self.rotation_y = 0
        if self.rotation_z <= -360: self.rotation_z = 0