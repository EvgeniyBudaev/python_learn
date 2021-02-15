# Классы
class MyFirstClass:
  pass

object_of_my_class = MyFirstClass()
print(type(object_of_my_class)) # <class '__main__.MyFirstClass'>

# ===
class Character():
  def __init__(self, race, damage=10, armor=20): # определение конструктора. self - ссылка на экземпляр класса
    self.race = race
    self.damage = damage
    self.armor = armor


unit = Character('Elf', damage=20)
print('race: ', unit.race) # race:  Elf
print('damage: ', unit.damage) # damage:  20