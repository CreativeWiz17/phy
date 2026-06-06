from engine.vector3 import Vector3
from engine.obj import PhysicsObject

obj1 = PhysicsObject(mass = 15) # new object

print(obj1.position) # Object starts at origin
print(obj1.velocity) # Object also at rest
print(obj1.acceleration()) # acceleration method called and again 0

obj1.addF(Vector3(10,10,10)) # addF method called and a force of 10 added on every axis

print(obj1.force) #printing out the force
print(obj1.acceleration()) #printing out the accelration, which is a = f/m

obj1.update(1)  
print(obj1.position) # new position of the object after 1 second
print(obj1.velocity) # new velocity of the object after 1 second

print(obj1.force) # new force, should go back to 0 obv

