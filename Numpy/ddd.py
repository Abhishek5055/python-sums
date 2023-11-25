from abc import ABC, abstractmethod

# Abstract class (Superclass)
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete subclass
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Concrete subclass
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating objects
circle = Circle("Circle", 5)
rectangle = Rectangle("Rectangle", 4, 6)

# Using the objects
print(f"Shape: {circle.name}, Area: {circle.area()}, Perimeter: {circle.perimeter()}")
print(f"Shape: {rectangle.name}, Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
