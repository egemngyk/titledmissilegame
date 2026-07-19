from ursina.vec3 import Vec3

class Shape:
    def __init__(self, entity, colliderClass):
        self.entity = entity
        self.colliderClass = colliderClass

    def intersects(self, other):
        raise NotImplementedError

class BoxShape(Shape):
    def getBounds(self):
        world_position = self.entity.world_position
        world_scale = self.entity.world_scale
        return (
            world_position - world_scale/2,
            world_position + world_scale/2
        )

    def intersects(self, other):
        minA, maxA = self.getBounds()
        minB, maxB = other.getBounds()
        hit = HitInfo()
        hit.hit = (
            maxA.x >= minB.x and
            maxA.y >= minB.y and
            maxA.z >= minB.z and
            minA.x <= maxB.x and
            minA.y <= maxB.y and
            minA.z <= maxB.z
        )

        if not hit.hit:
            return hit

        depth = {}
        depth["x"] = min(maxA.x - minB.x, maxB.x - minA.x)
        depth["y"] = min(maxA.y - minB.y, maxB.y - minA.y)
        depth["z"] = min(maxA.z - minB.z, maxB.z - minA.z)

        normal = {}
        centerA = self.entity.world_position
        centerB = other.entity.world_position

        if centerA.x > centerB.x: normal["x"] = Vec3(1, 0, 0)
        else: normal["x"] = Vec3(-1, 0, 0)
        if centerA.y > centerB.y: normal["y"] = Vec3(0, 1, 0)
        else: normal["y"] = Vec3(0, -1, 0)
        if centerA.z > centerB.z: normal["z"] = Vec3(0, 0, 1)
        else: normal["z"] = Vec3(0, 0, -1)

        axis = min(depth, key=depth.get)
        hit.depth = depth[axis]
        hit.normal = normal[axis]

        hit.shapeA = self
        hit.shapeB = other

        return hit

class HitInfo:
    def __init__(self):
        self.hit = False

        self.shapeA = None
        self.shapeB = None

        self.normal = None
        self.point = None
        self.depth = 0