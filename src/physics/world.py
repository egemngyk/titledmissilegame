from ursina.vec3 import Vec3

class PhysicsWorld:
    def __init__(self):
        self.gravity=Vec3(0, -9.81, 0)

        self.bodies = []
        self.collision_components = []

        self.contacts = []

    def addBody(self, body):
        if body not in self.bodies:
            self.bodies.append(body)

    def removeBody(self, body):
        if body in self.bodies:
            self.bodies.remove(body)

    def addCollider(self, collider):
        if collider not in self.collision_components:
            self.collision_components.append(collider)

    def removeCollider(self, collider):
        if collider in self.collision_components:
            self.collision_components.remove(collider)

    def setGravity(self, x=0, y=-9.81, z=0):
        self.gravity = Vec3(x, y, z)

    def update(self, dt):
        self.applyForces(dt)
        self.detectCollisions()
        self.resolveCollisions()


    def applyForces(self, dt):
        for body in self.bodies:
            if body.isStatic: continue

            if body.useGravity:
                body.addForce(self.gravity * body.mass)

            self.integrate(body, dt)
            body.clearForces()

    def integrate(self, body, dt):
        acceleration = body.force / body.mass
        body.velocity += acceleration * dt
        body.entity.position += body.velocity * dt
        
    def detectCollisions(self):
        self.contacts.clear()

        for i in range(len(self.collision_components)):
            for j in range(i+1, len(self.collision_components)):
                colliderA = self.collision_components[i]
                colliderB = self.collision_components[j]

                for shapeA in colliderA.shapes:
                    for shapeB in colliderB.shapes:
                        hit = shapeA.intersects(shapeB)

                        if hit.hit:
                            self.contacts.append(hit)

    def resolveCollisions(self):
        for contact in self.contacts:
            bodyA = contact.shapeA.colliderClass.entity.physics
            bodyB = contact.shapeB.colliderClass.entity.physics

            if bodyA.isStatic and bodyB.isStatic: continue

            elif bodyA.isStatic:
                bodyB.entity.position -= contact.normal * contact.depth
                if contact.normal.y != 0:
                    bodyB.velocity.y = 0
                
            elif bodyB.isStatic:
                bodyA.entity.position += contact.normal * contact.depth
                if contact.normal.y != 0:
                    bodyA.velocity.y = 0

            else:
                offset = contact.normal * (contact.depth / 2.0)

                bodyA.entity.position -= offset
                bodyB.entity.position += offset

                if contact.normal.y != 0:
                    bodyB.velocity.y = 0
                    bodyA.velocity.y = 0
                
                if contact.normal.x != 0:
                    bodyA.velocity.x = 0
                    bodyB.velocity.x = 0
                
                if contact.normal.z != 0:
                    bodyA.velocity.z = 0
                    bodyB.velocity.z = 0
                    
            print("bodyA y: ", bodyA.entity.world_position)
            print("bodyB y: ", bodyB.entity.world_position)

            print("depth: ", contact.depth)