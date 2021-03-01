import pickle

class Character():

  def __init__(self, race, armor, damage = 10):
    self.race = race
    self.damage = damage
    self.armor = armor
    self.health = 100

  def hit(self, damage):
    self.health -= damage

  def is_dead(self):
    return self.health == 0 

  # def __getstate__(self):  

  def __setstate__(self, state):
    self.race = state.get('race', 'Elf') # Elf - значение по умолчанию
    self.damage = state.get('damage', 10)
    self.armor = state.get('armor', 20)
    self.health = state.get('health', 100)      

c = Character('Elf')
c.hit(10)
print(c.health) # 90 

with open(r'C:\tmp\game_state.bin', 'w+b') as f:
  pickle.dump(c, f) # dump - преобразует объект в битовое представление

c = None

with open(r'C:\tmp\game_state.bin', 'rb') as f:
  c = pickle.load(f)

print(c.health) # 90 
print(c.__dict__) # {'race': 'Elf', 'damage': 10, 'armor': 20, 'health': 90}
  