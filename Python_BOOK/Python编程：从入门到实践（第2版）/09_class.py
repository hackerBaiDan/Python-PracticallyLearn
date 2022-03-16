"""
    class 2022.3.15 hackerBaidan
"""
print("========= class 2022.3.15 hackerBaidan=========")

class Dog:
    """初始化属性"""
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f'{self.name} is now sitting.')
    def roll_over(self):
        print(f"{self.name} rolled over!")
my_dog = Dog("Willie",6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

# 继承
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odomter(self,mileage):
        if mileage >=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")
    def increment_odometer(self,miles):
        self.odometer_reading +=miles
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def fill_gas_tank(self):
        print(f"This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()