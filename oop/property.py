class Character():
  MAX_SPEED = 100

  def __init__(self, race, damage=10): 
    self.__race = race # private объявление атрибута __race
    self.damage = damage
    self._health = 100 # Видно наследникам. Во внешнем доступе не виден
    self._current_speed = 20

  def hit(self, damage):
    self._health -= damage

  @property # Свойства класса. Видно на чтение без запись во внешнем доступе
  def health(self):   
    return self._health

  @property
  def race(self):
    return self.__race 

  @property
  def current_speed(self):
    return self._current_speed

  @current_speed.setter
  def current_speed(self, current_speed):
    if current_speed < 0:
      self._current_speed = 0
    elif current_speed > 0:
      self._current_speed = 100
    else:
      self._current_speed = current_speed       
  


char = Character('Elf')
print('race: ', char.race) # race:  Elf
print('health: ', char.health) # health:  100
# char.health = 10 # Не можем изменить. Работает только на чтение

print('Текущая скорость: ', char.current_speed) # 20
char.current_speed = 50 # чтение и запись
print('Текущая скорость: ', char.current_speed) # 50
