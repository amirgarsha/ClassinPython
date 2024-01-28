## define static method 
class Three_point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __iter__(self):
        yield from (self.x, self.y, self.z)
    
    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)
    
    @staticmethod
    def show_intro_message(name):
        print (f"Hey {name}, it is your points")
        
    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y},{self.z})"
    
point = Three_point(3,2,9)
print(point)
print(point.from_sequence((4,6,9)))
point.show_intro_message("Amir")