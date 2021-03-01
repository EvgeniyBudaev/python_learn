# Интроспекция - механизм позволяющий анализировать данные об объектах

class Shape:
  pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius


circle = Circle(10)
print(issubclass(Circle, Shape)) # True issubclass - является ли Circle наследником Shape
print(isinstance(circle, Circle)) # True
print(isinstance(circle, Shape)) # True


# === callable а можно ли вызвать ===
print(callable(circle)) # False. Инстанцию класса можно вызвать, если объект реализует метод def __call__()


# === hasattr если определенный атрибут у экземпляра объекта
if hasattr(circle, 'radius'):
  print(getattr(circle, 'radius'))
  setattr(circle, 'radius', 20)
  print(getattr(circle, 'radius'))


# === dir для просмотра атрибутов объекта
print(dir(circle))


# ===
print(Circle.__name__) # Circle
print(type(circle)) # <class '__main__.Circle'>


# === repr отладочная информация
print(repr(circle)) # <__main__.Circle object at 0x0000025308201FD0>
