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