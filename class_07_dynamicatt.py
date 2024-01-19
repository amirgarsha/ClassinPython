## dynamically add attributes in class
## with this class we want to store data from database or csv file but we dont know the structrue of data
## define a record
john ={
    "name": "John Danielz",
    "position":"Python Developer",
    "department": "Engineering",
    "Salary" : 80000,
    "hire_date": "2021-02-05",
}
class Record_data:
    """Hold a record of data"""

##create an instance from class recodr_data   
john_record = Record_data()

## add attributes to the instance
for field, value in john.items():
    setattr(john_record, field, value)
    
print(john_record.name)
print(john_record.position)
print(john_record.__dict__)

## another way to add attribute to an instance from a class
class User:
    pass

amir = User()
amir.name = "Amir"
amir.last_name = "Garshasbi"
amir.position = "NOC technician"
amir.salary = 1000

print(amir.name)
print(amir.__dict__)

## add method dynamically
def __init__(self, name, job):
    self.name = name
    self.job = job

User.__init__ = __init__
print(User.__dict__)

Khatereh = User("Khatereh", "HR specialist")
print(Khatereh.__dict__)