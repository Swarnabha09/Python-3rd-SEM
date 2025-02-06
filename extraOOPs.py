#Question:
""" >Create a class Vehicle with attributes make, model, and year.
    >Define a method display_info() that prints the vehicle's details.
    >Then, create a subclass Car that inherits from Vehicle and adds an attribute fuel_type.
    >Override the display_info() method in the Car class to include fuel_type in the output.

Write the code to:

1. Create an instance of the Car class.
2. Call the display_info() method for the Car instance and print its details.
"""

class Vehicle:
    def __init__(self,a,b,c):
        self.make=a
        self.model=b
        self.year=c
    def display_info(self):
        print("Make:",self.make)
        print("Model:",self.model)
        print("Year:",self.year)

class Car(Vehicle):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.fuel=d
    def display_info(self):
        print("Make:",self.make)
        print("Model:",self.model)
        print("Year:",self.year)
        print("Fuel type:",self.fuel)

v=Car("Toyota","Corolla","2020","Petrol")
v.display_info()
