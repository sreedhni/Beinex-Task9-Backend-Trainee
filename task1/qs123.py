# 3) Add 4 different subclasses for class Shape. - Triangle, Square, Pentagon, Circle. Define constructor for each 
# of them to assign the necessary parameters required for calculating the area. 
# Define the area method for each of the classes. When invoked it Should return the area of the shape by 
# calculating it. 
# Create an object for each of the subclasses and call the area method on the objects. 

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method.")
       

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Pentagon(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 1.72048 * self.side * self.side  
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius  


base_cm=float(input("enter the base size of the trianagle : "))
height_cm=float(input("enter the height size of the trianagle : "))
triangle = Triangle(base_cm,height_cm)
print("Area of Triangle:", triangle.area())

side_cm=float(input("enter the side size of the square : "))
square = Square(side_cm)
print("Area of Square:", square.area())


side_cm=float(input("enter the side size of the pentagon : "))

pentagon = Pentagon(side_cm)
print("Area of Pentagon:", pentagon.area())

radius_cm=float(input("enter the radius of the circle : "))

circle = Circle(radius_cm)
print("Area of Circle:", circle.area())
