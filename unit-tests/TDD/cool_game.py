# TDD - Test Drven Development
def greet(name, isEnemy):
  if isEnemy:
    return f'Hello {name}! I will kill you, bastard!'
  else:
    return f'Hello {name}! How are you?' 

def eat_burgers(number):
  if number > 3:
    return f'Oh! I overate!'
  else:
    return f'Mmm! That was excelent!' 

def can_fly(name):
  if name == 'Batman':
   return True
  else:
    return False

def greet2(name, isEnemy):
  if not isinstance(isEnemy, bool):
    raise ValueError('isEnemy must be a boolean type')
  if isEnemy:
    return f'Hello {name}! I will kill you'
  else:
    return f'hello {name}! How are you?'           