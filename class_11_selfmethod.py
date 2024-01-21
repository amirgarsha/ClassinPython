## creating class with method use self
class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200
        
    def start(self):
        print ("car starts")
        self.started = True
    
    def stop(self):
        print("car stopped")
        self.started = False
    
    def accelerate(self, value):
        if self.started == False:
            print("please start the car")
            return
        elif self.speed + value <= self.max_speed:
            self.speed = self.speed + value
        elif self.speed + value > self.max_speed:
            self.speed = self.max_speed
        print(f"Acceleration is {self.speed} km/h ....")
    
    def brake(self, value):
        if self.started == False:
            print("start Car first")
            return
        elif self.speed - value > 0:
            self.speed = self.speed - value
        elif self.speed -value < 0:
            self.speed = 0
            self.started = False
        print(f"Acceleration is {self.speed} km/h ....")

peykan = Car("iran_khodro","Peykan",1965, "red")

peykan.start()
peykan.accelerate(60)
peykan.accelerate(150)
peykan.brake(100)
peykan.brake(70)
peykan.accelerate(20)
peykan.brake(120)
peykan.accelerate(10)
print(peykan.started)
print(peykan.model)
        
        
    