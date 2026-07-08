from engine.vector3 import Vector3
from engine.obj import PhysicsObject
from engine.world import World

world = World()

obj1 = PhysicsObject(mass=15)

world.add(obj1)

obj1.addF(Vector3(10,10,10))

world.update(1)

print(obj1.position)
print(obj1.velocity)
