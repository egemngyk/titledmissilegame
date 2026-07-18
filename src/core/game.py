from world import Plot
from entities import Missile
from physics import PhysicsWorld, RigidBody 

class Game:
    def __init__(self):
        self.physicsWorld = PhysicsWorld()

        self.plot = Plot()
        self.missile = Missile()

        self.missile.physics = RigidBody(self.missile, self.physicsWorld)

        self.key_map = {"w": "up", "a": "left", "s": "down", "d": "right"}

    def update(self, held_keys, dt):
        self.physicsWorld.update(dt)

        if held_keys["space"]: self.missile.onFire()
        else: self.missile.offFire()

        for key, rotation in self.key_map.items():
            if held_keys[key]: self.missile.control(rotation)