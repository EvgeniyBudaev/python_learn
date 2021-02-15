# Inheritance - наследование класса
class Car:
  wheels_number = 4

  def __init__(self, name, color, year):
    self.name = name
    self.color = color
    self.year = year
    print('Car is created')

  def drive(self, city):
    print(self.name + ' is driving to ' + city)

  def change_color(self, new_color):
    self.color = new_color
    print('Color is changed to ', new_color)

# class Truck наследуется от класса Car
class Truck(Car):
  wheels_number = 6

  def __init__(self, name, color, year):
    Car.__init__(self, name, color, year)
    print('Truck is created')

  def drive(self, city):
    print('Truck ' + self.name + ' is driving to ' + city)

  def load_cargo(self, weight):
    print('The cargo is loaded. Weight is ' + str(weight) + ' kg')    


man_truck = Truck('Man', 'red', 2015) # Car is created  Truck is created
man_truck.drive('Moscow') # Truck Man is driving to Moscow. Переопределили метод класса
print(man_truck.wheels_number) # 6 .Переопределили атрибут wheels_number
print(man_truck.color) # red
man_truck.change_color('silver') # Color is changed to  silver 
print(man_truck.color) # silver
man_truck.load_cargo(2000) # The cargo is loaded. Weight is 2000 kg


# Polymorphism
class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    raise NotImplementedError('Class successor must implement this method')


class Dog(Animal):
  def __init__(self, name):
    Animal.__init__(self, name)

  def speak(self):
    print(self.name + ' is saying woof')


class Cat(Animal):
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(self.name + ' is saying meow')

class Fish:
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(self.name + ' is saying nothing')  
 

spike = Dog('Spike')
tom = Cat('Tom')
freddy = Fish('Freddy')

pet_list = [spike, tom, freddy]

for pet in pet_list:
  pet.speak() # Spike is saying woof # Tom is saying meow

def pet_voice(pet):
  pet.speak()

pet_voice(spike) # Spike is saying woof
pet_voice(tom) # Tom is saying meow 
pet_voice(freddy) # Freddy is saying nothing


# === Shape - абстрактный класс
class Shape():
  def __init__(self):
    print('Shape created')

  def draw(self):
    raise NotImplementedError("Can not instantiate an abstract class")

  def area(self):
    raise NotImplementedError("Can not instantiate an abstract class")

  def perimeter(self):
    raise NotImplementedError("Can not instantiate an abstract class")


shape = Shape() # Shape created

class Rectangle(Shape):
  def __init__(self, width, height):
    Shape.__init__(self)

    self.width = width
    self.height = height

    print('Rectangle created')

    # Shape.area(self)

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return 2*(self.width + self.height)  

  def draw(self):
    print(f'Drawing rectangle with width={self.width} and height={self.height}')  


rect = Rectangle(10 ,15) # Shape created \n Rectangle created
print(rect.area()) # 150

# Полиморфизм

for shape in [rect]:
  shape.draw() # Drawing rectangle with width=10 and height=15