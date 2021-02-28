class Character():

  _instance = None

  def __new__(cls):
    if not cls._instance:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    self.race = 'Elf'


c = Character()
d = Character()
d.race = 'Ork'
print('C: ', c.race) # Ork
print('D: ', d.race) # Ork