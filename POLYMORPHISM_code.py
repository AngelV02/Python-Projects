# Python 3.11.2
#
# Author: Angel Dominick Velasco
#
# Purpose: This Python code demonstrates inheritance and polymorphism with a 'Vehicle' parent class and two child classes, 
#           'Car' and 'Motorcycle'.The child classes add some unique attributes and behaviors, 
#           and override a method from the parent class 'Vehicle' to showcase polymorphism. 
#           The code creates instances of the child classes and calls their methods to highlight the differences of them.


#Parent class Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.make} {self.model} is starting its engine,"


#Child class Car
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def start_engine(self):
        return f"{super().start_engine()} with a key."

    def honk(self):
        return f"{self.make} {self.model} is honking its horn!"


#Child class Motorcyle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def start_engine(self):
        return f"{super().start_engine()} with a kick."

    def rev_engine(self):
        return f"{self.make} {self.model} is revving its engine!"


#Create instances of car and motorcyle classes

my_car = Car("Toyota", "Camry", 2022, 4)
my_motorcycle = Motorcycle("Harley Davidson", "Sportster", 2021, 2)

#Prints output to console

print(my_car.start_engine()) # Toyota Camry is starting its engine. with a key.
print(my_car.honk(), "\n") # Toyota Camry is honking its horn!

print(my_motorcycle.start_engine()) # Harley Davidson Sportster is starting its engine. with a kick.
print(my_motorcycle.rev_engine()) # Harley Davidson Sportster is revving its engine!

