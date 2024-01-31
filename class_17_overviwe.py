##class will represent an employee of a given company and will implement 
# attributes and methods to manage some related tasks like keeping 
# track of personal information and computing the employee’s age:
from datetime import datetime


class employee:
    #class attribute : it is common for all employee
    company_name = "Mobile Communication of Iran"
    
    ##define initializer
    def __init__(self, name, birth_date):
        ##define two public instance
        self.name = name
        self.birth_date = birth_date
        
        # want to turn .birth_date into a property to 
        # automatically convert the input date in ISO format to a datetime object:
        
    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = datetime.fromisoformat(value)
        
        
        # want to write a regular instance method to compute the employee’s age from their birth date:
    
    def compute_age(self):
        
        today = datetime.today()
        age = today.year - self.birth_date.year
        birthday = datetime(
            today.year,
            self.birth_date.month,
            self.birth_date.day
            )
        if today < birthday:
            age -= 1
        return age
    
        #you’ll often build instances of Employee from dictionaries containing the data of your employees. 
        # You can add a convenient class method to quickly build objects that way:
    @classmethod
    def fromdict(cls, data_dict):
        return cls(**data_dict)
        #you’ll add suitable .__str__() and .__repr__() special methods to 
        # make your class friendly to users and developers, respectively:
    
    def __str__(self):
        return f"{self.name} is {self.compute_age()} years old"
    
    def __repr__(self):
        return(
            f"{type(self).__name__}("
            f"name = '{self.name}',"
            f"birth_date = '{self.birth_date.strftime('%Y-%m-%d')}')"
        )
        #The .__str__() method returns a string describing the current employee in 
        # a user-friendly manner. Similarly, the .__repr__() method returns a 
        # string that will allow you to re-create the current object, which is great from 
        # a developer’s perspective.
    
Amir = employee("amir Garshasbi","1986-07-18")
print(Amir)
print(Amir.company_name)
print(Amir.__repr__())
print(Amir.compute_age())
    
jane_data = {"name": "Jane Doe", "birth_date": "2001-05-15"}
Jane = employee.fromdict(jane_data)
print(Jane)
print(Jane.compute_age())
    