class Swimmable:
  def __init__(self, name):
    print('Method init() of Swimmable')
    self.name = name

  def greeting(self):
    print(f'Hello! My name is {self.name} and I can swim')

  def swim(self):
    print('swim')  


class Walkable:
  def __init__(self, name):
    print('Method init() of Walkable')
    self.name = name

  def greeting(self):
    print(f'Hello! My name is {self.name} and I can walk')

  def walk(self):
    print('walk')   


class Flyable:
  def __init__(self, name):
    print('Method init() of Flyable')
    self.name = name

  def greeting(self):
    print(f'Hello! My name is {self.name} and I can fly')

  def fly(self):
    print('fly')      


class GameCharacter(Swimmable, Walkable, Flyable):
  def __init__(self, name):
    print('Method init() of GameCharacter')
    self.name = name
    Swimmable.__init__(self, name)
    Walkable.__init__(self, name)
    Flyable.__init__(self, name)

  # def greeting(self):
  #   print(f'Hello! My name is {self.name}')       

james = GameCharacter('James') 
james.greeting() # Hello! My name is James and I can swim
# james.swim() # swim
# james.walk() # walk
# james.fly() # fly

# print(isinstance(james, Walkable)) # True. isinstance - является ли объект james объектом класса Walkable

# print(isinstance(james, Flyable)) # True
# print(isinstance(james, Swimmable)) # True
# print(isinstance(james, GameCharacter)) # True
# print(isinstance(james, object)) # True
# print(isinstance(5, object)) # True Любые типы данные являются объектами


# === Множественное наследование
class Animal:
  def die(self):
    print('bye-bye')
    self.health = 0


class Carnivour:
  def hunt(self):
    print('eating')
    self.satiety = 100


class Dog(Animal, Carnivour):
  def bark(self):
    print('woof-woof')


dog = Dog()
dog.bark() # woof-woof
dog.hunt() # eating
dog.die() # bye-bye

# Проблемы с множественным наследованием
class Animal2:
  def set_health(self, health):
    print('set in animal2')


class Carnivour2(Animal2):
  def set_health(self, health): # переопределение метода
    print('set in carnivour2')


class Mammal2(Animal2):
  def set_health(self, health): # переопределение метода
    print('set in mammal2')


class Dog2(Mammal2, Carnivour2):
  pass


dog2 = Dog2()
dog2.set_health(10) # set in mammal2

# ===
class Animal3:
  def set_health(self, health):
    print('set in animal3')


class Carnivour3(Animal3):
  def set_health(self, health): 
    print('set in carnivour3')


class Mammal3(Animal3):
  def set_health(self, health): 
    print('set in mammal3')


class Dog3(Mammal3, Carnivour3):
  def set_health(self, health): 
    Mammal3.set_health(self, health)
    Carnivour3.set_health(self, health)
    Animal3.set_health(self, health)

    print('set in dog3')


dog3 = Dog3()
dog3.set_health(10)  # set in mammal3 \n set in carnivour3 \n  set in animal3 \n set in dog3

# ===
print('=============')

# ===
class Animal4:
  def set_health(self, health):
    print('set in animal4')


class Carnivour4(Animal4):
  def set_health(self, health):
    super().set_health(health)
    # Animal4.set_health(self, health)
    print('set in carnivour4')


class Mammal4(Animal4):
  def set_health(self, health):
    super().set_health(health)
    # Animal4.set_health(self, health) 
    print('set in mammal4')


class Dog4(Mammal4, Carnivour4):
  def set_health(self, health): 
    super().set_health(health)
    # Mammal4.set_health(self, health)
    # Carnivour4.set_health(self, health)

    print('set in dog4')


dog4 = Dog4()
dog4.set_health(10)  