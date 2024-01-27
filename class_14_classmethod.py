## define classmethod 
class Threepoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __iter__(self):
        yield from (self.x , self.y, self.z)
    
    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)
    
    def __repr__(self):
        return f"{type(self).__name__}({self.x},{self.y},{self.z})"
    
print(Threepoint.from_sequence((3,2,1)))

point = Threepoint(4,2,6)
print(point.from_sequence((3,7,1)))
print(repr(point))
