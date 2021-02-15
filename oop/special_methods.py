# Special (magic) methods __method_name__
class Person:
  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

  def __str__(self):
    return self.first_name + ' ' + self.last_name

  def __len__(self):
    return self.age

  def __del__(self):
    print('Person object with name ' + self.first_name + ' is deleted from memory')

  def __add__(self, other):
    return self.age + other.age        


jack = Person('Jack', "White", 45)
jane = Person('Jane', 'Air', 40)
print(jack) # репрезентация Jack White

print(len([1, 2, 3, 4, 5])) # 5
print(len(jack)) # 45
# del (jack) # Person object with name Jack is deleted from memory

print(jack + jane) # 85 складываем возраст