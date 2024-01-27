## special method in class
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
    def __str__(self):
        return f"{self.make},{self.model},{self.color}:({self.year})"
    
    def __repr__(self):
        return(
            f'(make = "{self.make},"'
            f'model = "{self.model},"'
            f'color = "{self.color},"'
            f'year = "{self.year}")'
        )
        
toyota = Car("toyota","Camery",2022,"blue")
print(toyota.__str__())

print(toyota.__repr__())

print(toyota)
repr(toyota)