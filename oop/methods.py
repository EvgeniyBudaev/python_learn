# Методы - это функции, которые определяются внутри класса
class Car:

  wheels_number = 4

  def __init__(self, name, color, year):
    self.name = name
    self.color = color
    self.year = year

  def drive(self, city):
    print('Car is driving to ' + city)

  def change_color(self, new_color):
    self.color = new_color  

opel_car = Car('Opel Tigra', 'grey', '1999')
opel_car.drive('Moscow')
print(opel_car.wheels_number)
print(opel_car.name)
print(opel_car.color)
print(opel_car.year)

mazda_car = Car('Mazda CX7', 'black', '2021')
mazda_car.change_color('gold')
print(mazda_car.color)

# ===
class Circle:
  pi = 3.14

  def __init__(self, radius = 1):
    self.radius = radius
    self.circle_cumference = 2 * self.pi * self.radius

  def get_area(self):
    return self.pi * (self.radius ** 2)

circle1 = Circle()
print(circle1.get_area())

circle2 = Circle(5)
print(circle2.get_area())
print(circle2.circle_cumference)
