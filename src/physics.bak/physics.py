from ursina import time
from physics.gravity import Gravity
from physics.drag import Drag

class Physics:
    def __init__(self):
        self.entities = []
        self.gravity = Gravity()
        self.drag = Drag()
    
    def update(self):
        for entity, type in self.entities:
            self.gravity.applyToEntity(entity)
            self.drag.applyToEntity(entity, type) 

    def add(self, entity, type=None):
        self.entities.append((entity, type))