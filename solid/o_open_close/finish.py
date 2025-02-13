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

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area_of(self):
        return  self.radius**2 * pi

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area_of(self):
        return self.side ** 2

class AreaCalculator:
    def __init__(self, shapes:list):
        self.shapes = shapes
    
    def total_area(self):
        return sum([item.area_of() for item in self.shapes])

if __name__ == '__main__':

    ar_sh = AreaCalculator(
        [Rect(10, 10), 
         Rect(4, 5), 
         Circle(20), 
         Rect(3, 3), 
         Square(10)]
         )
    area = ar_sh.total_area()
    print(area)