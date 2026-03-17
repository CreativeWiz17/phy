import math

class Vector3:
    def __init__ (self, x=0, y=0, z=0):

        self.x = x
        self.y = y
        self.z = z


    def add (self, other):

        newx = self.x + other.x
        newy = self.y + other.y 
        newz = self.z + other.z

        return Vector3(newx, newy, newz)

    def subtract (self, other):

        newx = self.x - other.x
        newy = self.y - other.y
        newz = self.z - other.z

        return Vector3(newx, newy, newz)
    
    def multiply (self, mult):

        newx = self.x * mult
        newy = self.y * mult
        newz = self.z * mult

        return Vector3(newx, newy, newz)
    
    def divide (self, div):
        
        if div == 0:
            raise ValueError("Cannot divide by zero")
        
        newx = self.x / div
        newy = self.y / div
        newz = self.z / div

        return Vector3(newx, newy, newz)
    
    def magnitude (self):

        mag = math.sqrt((self.x)**2 + (self.y)**2 + (self.z)**2)

        return mag
    
    def normalize (self):

        mag = self.magnitude()

        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        
        norm = self.divide(mag)

        return norm
    
    