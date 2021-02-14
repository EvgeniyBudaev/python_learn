class Gamer:

  active_gamers = 0

  @classmethod
  def get_active_gamers(cls):
    return Gamer.active_gamers

  @classmethod
  def gamer_from_string(cls, data_string):
    nickname, age, level, points = data_string.split(',')
    return cls(nickname, age, level, points)


  def __init__(self, nickname, age, level, points):
    self.nickname = nickname
    self.age = age
    self.level = level
    self.points = points
    Gamer.active_gamers += 1 # увеличиваем на одного игрока при создании класса

  def logout(self): 
    Gamer.active_gamers -= 1 # Выход игрока из игры 

  def get_nickname(self):
    return self.nickname

  def get_age(self):
    return self.age

  def get_level(self):
    return self.level

  def get_points(self):
    return self.points

  def is_adult(self):
    return self.age >= 18 

  def get_adult_level_permission(self):
    if self.is_adult():
      print('Вы можете перейти на взрослый уровень')
    else:
      print('Вы не можете перейти на следующий уровень')  

print('Количество игроков до инициализации: ', Gamer.active_gamers)

gamer_1 = Gamer('hell_boy', 23, 5, 13)
gamer_2 = Gamer('harry_potter', 13, 7, 34)

print(gamer_1.get_age())
gamer_1.get_adult_level_permission()
print(gamer_2.get_age())
gamer_2.get_adult_level_permission()

print('Количество игроков после инициализации: ', Gamer.active_gamers)

gamer_1.logout()
print('Количество игроков после выхода одного из них: ', Gamer.active_gamers)

print(Gamer.get_active_gamers()) # 1

jack = Gamer.gamer_from_string('jack, 24, 5, 12')
print(jack.get_age()) #24
print(Gamer.get_active_gamers()) # 2

# ===
my_dict = dict.fromkeys((1, 2, 3), ('apple')) # {1: 'apple', 2: 'apple', 3: 'apple'}
print('my_dict: ', my_dict)

