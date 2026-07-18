from ursina.vec3 import Vec3

class PhysicsWorld:
    def __init__(self):
        self.gravity=Vec3(0, -9.8, 0)
        self.bodies = []

    def addBody(self, body):
        if body not in self.bodies:
            self.bodies.append(body)

    def removeBody(self, body):
        if body in self.bodies:
            self.bodies.remove(body)

    def update(self, dt):
        for body in self.bodies:
            pass