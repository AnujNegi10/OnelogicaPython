class Car():
    def __init__(self,windows,doors,engine):
        self.window = windows
        self.doors = doors
        self.engine = engine
    
    def __str__(self):
        return "object has been initialized"
        
    def drive(self):
        print("the person drive car")
        
my_car = Car(5,4,"petrol")
# print(dir(my_car))
print(my_car)
    
        