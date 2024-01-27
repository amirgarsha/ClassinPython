## user iter protocol
class  Three_point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

#when it is not iterable we get error that object is not iterable
# print(list(Three_point(12,23,4)))

class Three_point_iter:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __iter__(self):
        yield from (self.x, self.y, self.z)

print(list(Three_point_iter(23,10,11)))