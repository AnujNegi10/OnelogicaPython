class Car:
    total_cars =0
    def __init__(self,userbrand,usermodel,price=121):
        
        # ! now brand is private can only be accessed by methods:Encapsulation
        
        self.__brand = userbrand
        self.__model = usermodel
        self.price = price
        Car.total_cars +=1
        
        # out of the two the one that is called afterwards is given as the value
        # self.price = 1000
    #! getter method 
    def get_brand(self):
        return self.__brand + " !"
    
    #! setter method 
    def set_brand(self,brand):
        if isinstance(brand,str) and len(brand)>0:
            self.__brand =brand
        else:
            raise ValueError("Brand must be a non empty string")    
    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod # this is a type of decorator
    def general():
        return "car are a means of object"
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self,value):
        if isinstance(value,str) and len(value)>0:
            self.__model = value
        else:
            raise ValueError("invalid")
        

#! Inheritence   
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "electric car"
    
safari = Car("Tata","Safari")
safariev = ElectricCar("Tata","safariev","75KW")
print(safariev.fuel_type())
print(safari.fuel_type())  

# print(Car.fuel_type()) will give error as not a static method
# my_EV = ElectricCar("tesla","model x","85KW")
# print(my_EV.model)        
# print(my_EV.fullname()+"\n") 
# print(my_EV.fullname()) 
# print(my_EV.get_brand())  

# my_EV.set_brand("newtesla")
# print(my_EV.get_brand())

# print(safari.general())
# print(my_EV.general())
# print(Car.general())
# print(Car.total_cars)


anujcar = Car("toyota","supra")
anujcar.model = "huricane"
print(anujcar.model)





# print("\n")
# my_car = Car("alto","suzuki","1")
# my_car2=Car("toyota","corolla")

# print(my_car.brand)
# print(type(my_car.price))
# print(my_car2.brand)
# print(type(my_car2.price))

# my_new_car = Car("tata","safari")
# # my_new_car = Car()
# print(my_new_car.model)
# print(my_new_car.fullname())

class Battery:
    def battery_info(self):
        return "this is battery"
class Engine:
    def engine_info(self):
        return "this is engine info"

class ElectricCarTwo(Battery,Engine,Car):
    pass

mynewtesla = ElectricCarTwo("tesla","model s")
print(mynewtesla.engine_info())
print(mynewtesla.battery_info())