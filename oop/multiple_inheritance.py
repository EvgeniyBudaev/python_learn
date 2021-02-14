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