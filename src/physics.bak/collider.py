from ursina import time
from ursina.vec3 import Vec3


class Collider:
    def __init__(self):
        self.collided_entities = []

    def collides(self, entity, withEntity = None, type=None):
        if [entity, withEntity] not in self.collided_entities:
            if type=="missile":
                self.collided_entities.append([entity.top_part, withEntity])
                self.collided_entities.append([entity.bot_part, withEntity])
            else:
                self.collided_entities.append([entity, withEntity])
    
    def update(self):
        for entity, withEntity in self.collided_entities:
            self.checkCollision(entity, withEntity)
    
    def checkCollision(self, entity, withEntity=None):
        if withEntity is None: hit = entity.intersects()
        else: hit = entity.intersects(withEntity)

        if hit.hit:
            self.onCollision(entity, hit.entity, hit)

    def onCollision(self, entity, withEntity, hit):
        self.resolveCollision(entity, withEntity, hit)

    def resolveCollision(self, entity, other, hit):
        if other.name == "terrain":
            print(entity.name)
            