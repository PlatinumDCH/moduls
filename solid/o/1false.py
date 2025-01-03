from math import pi

class React:
    def __init__(self, width, height):
        self.width
        self.heigt

class Circle:
    def __init__(self, radius: float):
        self.rdius = radius
    
class AreaCaculation:
    def __init__(self, shapes:list[React]):
        pass

    def total_area(self) -> float:
        sum = 0
        for el in self.shapes:
            if isinstance(el, React):
                sum += el.width * el.height
            if isinstance(el, Circle):
                sum += el.radius**2 * pi
        return sum
    
    