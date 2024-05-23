import math

class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def perimeter(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

# Example usage:
circle = Circle(5)
print(f"Circle: Area = {circle.area()}, Perimeter = {circle.perimeter()}")

rectangle = Rectangle(4, 7)
print(f"Rectangle: Area = {rectangle.area()}, Perimeter = {rectangle.perimeter()}")

triangle = Triangle(3, 4, 5)
print(f"Triangle: Area = {triangle.area()}, Perimeter = {triangle.perimeter()}")
