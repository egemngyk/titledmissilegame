from ursina.vec3 import Vec3

class RigidBody:
    def __init__(self, entity, world, mass=1, useGravity=True, isStatic=False):
        self.entity = entity
        self.world = world

        self.mass = mass
        self.useGravity = useGravity
        self.isStatic = isStatic

        self.velocity = Vec3(0, 0, 0)
        self.force = Vec3(0, 0, 0)

        self.world.addBody(self)

    def addForce(self, force):
        self.force += force

    def addImpulse(self, impulse):
        pass

    def clearForces(self):
        pass

    def setVelocity(self, velocity):
        pass

    def stop(self):
        pass

