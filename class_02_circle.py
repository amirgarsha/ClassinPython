## define circle class, it store radius as variable(attribute) and method to calculate area
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area_calc(self):
        area = round(math.pi * self.radius**2, 2)
        return area
## create an object (instantiation)    
circle_2 = Circle(2)
print(circle_2.area_calc())

circle_3 = Circle(3.5)
print(circle_3.area_calc())

circle_9 = Circle(9)
print(circle_9.area_calc())

## call attribute and methods from class with "dot" 
print(circle_2.radius)
print(circle_3.area_calc())

## assignment attributes with dot
circle_3.radius = 10
print(circle_3.radius)
print(circle_3.area_calc())