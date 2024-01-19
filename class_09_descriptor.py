## use desctiptor to avoid repetition 
## if we have some classes and want to check their value not negative 
## can do with property for each class or use descriptor to avoid repetition
import math

class PositiveNumber:
##define descriptor class 
    def __set_name__(self, owner, name):
        self._name = name
        
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    
    def __set__(self, instance, value):
        if not isinstance(value, int|float) or value <= 0:
            raise ValueError("positive number needed")
        instance.__dict__[self._name] = value
    
class Circle:
    radius = PositiveNumber()
    
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return round(math.pi * self.radius **2 , 2)
    
class Square:
    side = PositiveNumber()
    
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return round( self.side **2 , 2)
    
circle_1 = Circle(3)
print(circle_1.calculate_area())

circle_2 = Circle(0)
print(circle_2.calculate_area())

square_1 = Square(5)
print(square_1.calculate_area())

square_2 = Square(-3)
print(square_2.calculate_area())
