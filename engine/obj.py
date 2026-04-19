from engine.vector3 import Vector3

class PhysicsObject: 
    def __init__(self, mass = 0, position = None, velocity = None, force = None): 
        
        self.mass = mass

        if position is None:
            self.position = Vector3()
        else:
            self.position = position

        if velocity is None:
            self.velocity = Vector3()
        else:
            self.velocity = velocity

        if force is None:
            self.force = Vector3()
        else:
            self.force = force

    def addF (self, force):

        self.force = self.force.add(force)

    def acceleration (self):

        a = self.force.divide(self.mass)

        return a
    
    def update (self, dt):

        a = self.acceleration()

        self.velocity = self.velocity.add(a.multiply(dt))

        self.position = self.position.add(self.velocity.multiply(dt)
                                          )
        self.force = Vector3()                                    
