import math
class Shape:
    """Базовый класс для геометрических фигур."""
    def area(self):
        raise NotImplementedError("Метод area должен быть переопределён.")
    def perimeter(self):
        raise NotImplementedError("Метод perimeter должен быть переопределён.")
class Rectangle(Shape):
    """Прямоугольник."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
class Circle(Shape):
    """Круг."""
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
def main():
    rectangle = Rectangle(5, 3)
    circle = Circle(4)
    print("Прямоугольник:")
    print(f"Площадь: {rectangle.area()}")
    print(f"Периметр: {rectangle.perimeter()}")
    print("\nКруг:")
    print(f"Площадь: {circle.area():.2f}")
    print(f"Периметр: {circle.perimeter():.2f}")
if __name__ == "__main__":
    main()
