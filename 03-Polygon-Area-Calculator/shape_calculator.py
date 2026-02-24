"""
Project 3: Polygon Area Calculator
Part of the freeCodeCamp "Python Certification" (Python v9)

Key Features:
- Class Inheritance: Demonstrates the 'Is-A' relationship by subclassing Rectangle into Square.
- Method Overriding: Customizing behavior for Square while reusing Rectangle's geometric logic.
- Geometric Algorithms: Calculates area, perimeter, diagonal, and shape nesting.
- String Representation & Visualization: Custom __str__ methods and ASCII art generation for shapes.
"""

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width
        return self.width

    def set_height(self,height):
        self.height = height
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        result_get_picture = ""
        for i in range(self.height):
            result_width = ""
            for j in range(self.width):
                result_width += "*"
            result_get_picture += result_width + "\n"

        return result_get_picture

    def get_amount_inside(self,obj_shape):
        area_self = self.get_area()
        area_obj_shape = obj_shape.get_area()
        multiplier = area_self / area_obj_shape
        return int(multiplier)


class Square(Rectangle):
    def __init__(self,side_length):
        super().__init__(side_length,side_length)
    def set_width(self,side_length):
        self.width = side_length
        self.height = side_length
    def set_height(self,side_length):
        self.height = side_length
        self.width = side_length
    def set_side(self,side_length):
        self.width = side_length
        self.height = side_length

    def __str__(self):
        return f"Square(side={self.width})"




rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
