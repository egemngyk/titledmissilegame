from world import Plot
from entities import Missile
from physics import PhysicsWorld, RigidBody, Collider
from physics.shapes import BoxShape

class Game:
    def __init__(self):
        self.physicsWorld = PhysicsWorld()
        self.physicsWorld.setGravity(0, -2.45, 0)

        self.plot = Plot()
        self.missile = Missile()

        self.missile.physics = RigidBody(self.missile, self.physicsWorld)

        self.missile.collision = Collider(self.missile, self.physicsWorld)
        self.missile.collision.addShape(BoxShape(self.missile.top_part, self.missile.collision))
        self.missile.collision.addShape(BoxShape(self.missile.bot_part, self.missile.collision))

        self.plot.physics = RigidBody(self.plot, self.physicsWorld, isStatic=True)

        self.plot.collision = Collider(self.plot, self.physicsWorld)
        self.plot.collision.addShape(BoxShape(self.plot, self.plot.collision))

        self.key_map = {"w": "up", "a": "left", "s": "down", "d": "right"}

    def update(self, held_keys, dt):
        self.physicsWorld.update(dt)

        if held_keys["space"]: self.missile.onFire()
        else: self.missile.offFire()

        for key, rotation in self.key_map.items():
            if held_keys[key]: self.missile.control(rotation)