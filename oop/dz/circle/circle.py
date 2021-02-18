import math

class Circle:
  def __init__(self, r=0):
    self.r = r

  def get_area(self):
    return math.pi * self.r ** 2

  def get_perimeter(self):
    return 2*math.pi * self.r 


circle = Circle(10)
print(circle.get_area()) # 314.1592653589793
print(circle.get_perimeter())  # 62.83185307179586