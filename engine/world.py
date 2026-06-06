from vector3 import Vector3

class World: 

    def __init__(self):

        self.objects = []
        self.gravity = Vector3(0, -9.80665, 0)

    def add(self, obj):

        self.objects.append(obj)

    def update(self, dt):

        for obj in self.objects:

            gravity_force = self.gravity.multiply(obj.mass)
            obj.addF(gravity_force)

            obj.update(dt)

      