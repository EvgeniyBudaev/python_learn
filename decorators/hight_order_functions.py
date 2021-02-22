# Higher order functions, which accept another functions as arguments
def product(n, func):
  result = 1
  for number in range(1, n):
    result *= func(number)
  return result

def square(x):
  return x * x

print(product(3, square)) # 4     


# Using nested functions. Вложенные функции
from random import choice

def colorize(thing):
  def get_color():
    colors = ('red', 'green', 'yellow')
    color = choice(colors)
    return color

  result = get_color() + ' ' + thing 
  return result 


print(colorize('apple')) 


# Возвращается функция
from random import choice

def make_color():
  def get_color():
    colors = ('red', 'green', 'yellow')
    color = choice(colors)
    return color

  return get_color  


my_color = make_color()
print(my_color())


#  Из внутренней функции получить доступ к агрументам внешней функции
from random import choice

def colorize2(thing):
  def get_color():
    colors = ('red', 'green', 'yellow')
    color = choice(colors)
    return color + ' ' + thing 

  return get_color


print(colorize2('apple')()) 