class Vehicle:
    def __init__(self, carType):
        self.car = carType

    def getCarType(self):
        return self.car

class Automobile(Vehicle):
    def __init__(self, carType, year, make, model, doors, roof):
        Vehicle.__init__(self, carType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def vehicleInput(self):
        print(f"Vehicle Type: {self.car}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of Doors: {self.doors}\nType of Roof: {self.roof}")



carType = input("What is the type of the vehicle?")
year = input("What year is the vehicle?")
make = input("What is the make of the vehicle?")
model = input("What is the model of the vehicle?")
doors = input("Is the vehicle a 2 or 4 door ?")
roof = input("Does the car have a sunroof or solidroof?")

v = Automobile(carType, year, make, model, doors, roof)

v.vehicleInput()