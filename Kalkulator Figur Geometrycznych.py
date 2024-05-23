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
        # Using Heron's formula to calculate the area of the triangle
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

def main():
    while True:
        print("\nWybierz figurę geometryczną:")
        print("1. Koło")
        print("2. Prostokąt")
        print("3. Trójkąt")
        print("4. Wyjdź")

        choice = input("Wprowadź numer opcji: ")

        if choice == '1':
            radius = float(input("Podaj promień koła: "))
            circle = Circle(radius)
            print(f"Koło: Pole = {circle.area()}, Obwód = {circle.perimeter()}")

        elif choice == '2':
            width = float(input("Podaj szerokość prostokąta: "))
            height = float(input("Podaj wysokość prostokąta: "))
            rectangle = Rectangle(width, height)
            print(f"Prostokąt: Pole = {rectangle.area()}, Obwód = {rectangle.perimeter()}")

        elif choice == '3':
            a = float(input("Podaj długość pierwszego boku trójkąta: "))
            b = float(input("Podaj długość drugiego boku trójkąta: "))
            c = float(input("Podaj długość trzeciego boku trójkąta: "))
            if a + b > c and a + c > b and b + c > a:
                triangle = Triangle(a, b, c)
                print(f"Trójkąt: Pole = {triangle.area()}, Obwód = {triangle.perimeter()}")
            else:
                print("Niepoprawne długości boków trójkąta. Spróbuj ponownie.")

        elif choice == '4':
            print("Koniec programu.")
            break

        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
