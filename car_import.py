from class_test import Car

car1 = Car("ford", "silver", 2013)
car2 = Car("toyota", "grey", 2003)
print(car1.rekt)
print(car2.rekt)
car1.crash(car2)
print(car1.rekt)
print(car2.rekt)
car2.crash(car1)
print(car1.rekt)
print(car2.rekt)
car1.repair()
# car2.repair()
print(car1.rekt)
print(car2.rekt)