class Car:
    def __init__(self, make, color, year):
        self.make = make
        self.color = color
        self.year = year

    def crash(self, other_car):
        print(f"{self.color} {self.make} crashed into {other_car.color} {other_car.make}!")

car1 = Car("Toyota", "Grey", 2020)
car2 = Car("BMW", "Black", 2018)
car1.crash(car2)
