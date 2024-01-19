import math
## define name mangling
class circle_mangle:
    def __init__ (self, radius):
        self.__radius = radius
    
    def __area_calc(self):
        return math.pi**2 * self.__radius
    
circle_1 = circle_mangle(3)

print(circle_1.__radius)
# print(circle_1.__radius)
print(circle_1.__area_calc())
