class lightweigth:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def multiply(self):
        return self.x * self.y
        
point = lightweigth(4, 6)
print(point.multiply())
print(point.__dict__)