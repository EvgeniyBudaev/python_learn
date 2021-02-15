class Character():
  MAX_SPEED = 100

  def __init__(self, race, damage=10): 
    self.__race = race # private объявление атрибута __race
    self.damage = damage
    self._health = 100 # Видно наследникам. Во внешнем доступе не виден

  def hit(self, damage):
    self._health -= damage


char = Character('Elf')
# char.race     __race стала private
char._Character__race = 'Ork' # изменили
print(char._Character__race) # Ork

# char._health     _health стал protected
char._health = 0 # изменили
