import math

class ShapeCalculator:
    def area(self, a, b=None):
        if b is None:
            return math.pi * a * a  # Circle
        else:
            return a * b  # Rectangle

calc = ShapeCalculator()
print("Circle area:", calc.area(5))
print("Rectangle area:", calc.area(4, 6))
