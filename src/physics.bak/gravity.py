from ursina import Vec3, time

class Gravity:
    def __init__(self, gravity=9.81):
        self.gravity = gravity

    def applyToEntity(self, entity):
        entity.last_position = entity.position

        if not hasattr(entity, "velocity"):
            entity.velocity = Vec3(0, 0, 0)

        entity.velocity.y -= self.gravity * time.dt
        entity.move(entity.velocity * time.dt)