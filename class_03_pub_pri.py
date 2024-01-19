## define public and non_public attributes
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self._width = width
        
    def area_calc(self):
        area = self._width * self.length
        return(area)
    
## create object (instantiation)
rect_1 = rectangle(3, 2)
rect_2 = rectangle(5,9)

## both non public and public attribute are accessible from outside
print(rect_2.length)
print(rect_2._width)

#print area of object
print(rect_1.area_calc())
print(rect_2.area_calc())