## create managed attribute with property
## in a class we want to validate value of a attribute
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
## @propert decorator to change existing attribute to property
# getter return the circle radius and store it in non public attribute         
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if not isinstance(value, int|float) or value <= 0:
            raise ValueError("positive number expected")
        self._radius = value
    
    def calculate_area(self):
        return round(math.pi * self._radius**2, 2)

circle_1 = Circle(2)
print(circle_1.calculate_area())

circle_2 = Circle(11)
print(circle_2.calculate_area())

##wrong circle
circle_3 = Circle(-9)
print(circle_3.calculate_area())
