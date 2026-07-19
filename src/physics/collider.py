class Collider:
    def __init__(self, entity, world, isTrigger=False, layer=None, mask=None):
        self.entity = entity
        self.world = world

        self.shapes = []

        self.isTrigger = isTrigger
        self.layer = layer
        self.mask = mask

        self.world.addCollider(self)

    def addShape(self, shape):
        self.shapes.append(shape)
        