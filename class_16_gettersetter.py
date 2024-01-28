## define instance attribute and use getter and setter
## you have a Person class with a .name instance attribute. You can make .name a 
# non-public attribute and provide getter and setter methods to access and change that attribute:
class person_one:
    def __init__(self, name):
        self.set_name(name)
        
    def get_name(self):
        return self._name 
    
    def set_name(self, value):
        self._name = value
        
amir = person_one("Amir")
print(amir.get_name())
amir.set_name("Amir Garsha")
print(amir.get_name())

# this pattern is less popular in the Python community. 
# it’s completely normal to expose attributes as part of an object’s public API.
#  you ever need to add function-like behavior on top of a public attribute, 
# then you can turn it into a property instead of breaking the API by replacing the attribute with a method.

class Person_two:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        self._name = value.upper()
        
khatereh = Person_two("khatereh")
print(khatereh.name)

khatereh.name = "khatereh abazari"
print(khatereh.name)

