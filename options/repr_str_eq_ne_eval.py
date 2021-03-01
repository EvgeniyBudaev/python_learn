from datetime import datetime

lst = [1, 2, 3]
print(repr(lst)) # '[1, 2, 3]'
print(lst) # [1, 2, 3]

eval(repr(lst)) == lst # True
# eval - исполняет строчку как код

dt = datetime.now()
print(repr(dt)) # datetime.datetime(2021, 3, 1, 5, 27, 12, 611300)
print(dt) # str 2021-03-01 05:27:25.229039
print(str(dt)) # 2021-03-01 05:27:25.229039


class Character():

  def __init__(self, race, damage = 100):
    self.race = race
    self.damage = damage

  def __repr__(self):
    return f"Character('{self.race}', {self.damage}"

  def __str__(self):
    return f"{self.race} with damage = {self.damage}"

  def __eq__(self, other):
    if isinstance(other, Character):
      return self.race == other.race and self.damage == other.damage 
    return False   


c = Character('Elf')
print(c) # Elf with damage = 100
# d = eval(repr(c))
# print(type(d))
# print(c == d) # False       


# Equal

  # def __eq__(self, other):
  #   if isinstance(other, Character):
  #     return self.race == other.race and self.damage == other.damage 

# print(c == d) # True    

