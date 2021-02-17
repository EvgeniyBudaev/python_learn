class Name:
  def __init__(self, first_name, last_name):
    # self.first_name = first_name.lower().capitalize()
    self.first_name = first_name.title() # тоже самое
    self.last_name = last_name.title()
    self.full_name = self.first_name + " " + self.last_name
    self.initials = self.first_name[0] + "." + self.last_name[0]


n = Name('EvgenIY', 'BUdaeV')
print(n.first_name) # Evgeniy
print(n.last_name) # Budaev
print(n.full_name) # Evgeniy Budaev
print(n.initials) # E.B      