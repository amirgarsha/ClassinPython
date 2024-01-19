## define different types of attributes in class
##define class attribute
class attribute_class:
    
    num_instances = 0
    def __init__(self):
        attribute_class.num_instances += 1

## print attribute class in different way
print(attribute_class.num_instances)
attribute_class()
print(attribute_class.num_instances)
attribute_class()
print(attribute_class.num_instances)
attribute_class()
attribute_class()
print(attribute_class().num_instances)

class attribute_class:
    
    num_instances = 0
    def __init__(self):
        self.num_instances += 1

## print attribute class in different way
print(attribute_class.num_instances)
attribute_class()
print(attribute_class.num_instances)
attribute_class()
print(attribute_class.num_instances)
attribute_class()
attribute_class()
print(attribute_class().num_instances)

##instance attribute
class car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0
        self.max_speed = 200

toyota_camry = car("Toyota", "Camry", 2022, "Red")
print(toyota_camry.make)
print(toyota_camry.year)
print(toyota_camry.max_speed)

ford_mustang = car("Ford", "Mustang", 2023, "Black")        
print(ford_mustang.make)
print(ford_mustang.year)
print(ford_mustang.max_speed)

##can not access from class
print(car.make)