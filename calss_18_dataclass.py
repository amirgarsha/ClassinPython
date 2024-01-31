## data class
from dataclasses import dataclass

@dataclass
class ThreeDpoint:
    x : int 
    y : int 
    z : int 
    
    @classmethod
    def from_sequence(cls, value):
        return cls(*value)
    
    @staticmethod
    def show_intro_message(name):
        print(f"Hey {name}! it is your points")

#Python’s @dataclass decorator to turn the regular class into a data class.
# Instead of defining an .__init__() method, you list the instance attributes with their corresponding types.
        
points = ThreeDpoint(2,3,5)
points.show_intro_message("Amir")

print(points.from_sequence(([2,4,7])).__str__())
print(points.__str__())


