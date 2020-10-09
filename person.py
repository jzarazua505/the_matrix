class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def birthday(self):
        self.age += 1

class Student(Person):
    def __init__(self, first_name, last_name, age, major):
        super().__init__(first_name, last_name, age)
        self.major = major

    def __str__(self):
        return f"{self.major} Major {super().__str__()}"

pers1 = Person("Julian", "Zarazua", 20)
stud1 = Student("Julian", "Zarazua", 20, "Computer Science")
stud2 = Student("Manuel", "Zamora", 25, "Math")
print(pers1)
print(stud1)
test = [1, 2, 3]
print(test)
