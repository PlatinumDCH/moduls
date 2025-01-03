from math import pi

class Shape:
    def area_of(self):
        raise NotImplementedError
    
class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of(self):
        return self.width * self.height

class Square:
    def __init__(self, side):
        self.side = side
    
    def area_of(self):
        return self.side ** 2


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area_of(self):
        return self.radius ** 2 * pi

class AreaCalculator:
    def __init__(self, shapes: list[Shape]):
        self.shapes = shapes
    
    def total_area(self)->float:
        return sum(
            [shape.area_of() for shape in self.shapes]
            )
    