from abc import ABC
from abc import abstractmethod
import math

class Shape(ABC):
  def __init__(self):
    super().__init__()

  @abstractmethod # наследник такие методы обязан переопределить
  def draw(self):
    pass 

  @abstractmethod 
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    #pass
    print('calc perimeter')

  def drag(self):
    print('Basic dragging functionality')


# s = Shape() нельзя создать экземпляр класса


class Triangle(Shape):
  
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def draw(self):
    print(f'Drawing triangle with sides={self.a}, {self.b}, {self.c}') 

  def area(self):
    s = (self.a + self.b + self.c) / 2
    return math.sqrt(s*(s - self.a) * (s - self.b) * (self.c))

  def perimeter(self):
    super().perimeter()
    return self.a + self.b + self.c

  def drag(self):
    super().drag()
    print('Additional actions')


t = Triangle(10, 10, 10)              
print('perimeter: ', t.perimeter()) # calc perimeter \n 30

print(t.drag()) # Basic dragging functionality \n Additional actions
