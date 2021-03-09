class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return self.base * self.height

class Triangle(Shape):
    def area(self):
        return super().area() / 2




if __name__ == "__main__":
    shape = Shape(5, 8)
    print(shape.area())
    triangle = Triangle(6, 10)
    print(triangle.area())
    