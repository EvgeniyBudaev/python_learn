# Обработка ошибки деления на 0
def devide(a, b):
  try:
    return a / b
  except ZeroDivisionError as ex:
    print(f'an error occured: {ex}')
  except:
    print('unknow error occured!')   
    
devide(4, 0)
devide(4, 'text')

# Обработка ошибки. Пример
user_dictionary = {'first_name': 'Evgeniy', 'last_name': 'Budaev'}

def get_dictionary_values(dictionary, key):
  try:
    return dictionary[key]
  except KeyError:
    return None 

print(get_dictionary_values(user_dictionary, 'first_name'))
print(get_dictionary_values(user_dictionary, 'age'))  
print(get_dictionary_values(user_dictionary, 'last_name'))       


# Обработка ошибки чтения файла
file = None
try:
  file = open(r'Z:\tmp\text.txt')
  data = file.read()
except FileNotFoundError as ex:
  print(f'Error has occured. Description: {ex.strerror}')
else:
  print('maybe else') 
finally: 
  print('Finally')
  if file: 
    file.close()

print('Скрипт продолжает работать')

# До тех пор пока пользователь не введет число
def get_int():
  while True:
    try:
      reply = int(input('Введите число: '))
      return reply
    except:
      print('Вы ввели не число. Попробуйте еще раз')
      continue  

# number = get_int()
# print('number: ', number) 


# Выброс исключений
import math

def calc_square(ab, ac, bc):
  if ab <= 0 or ac <= 0 or bc <= 0:
    raise ValueError("One of the sides is less or equal to 0.")
  p = (ab + ac + bc) / 2
  s = math.sqrt(p * (p-ab) * (p-ac) * (p-bc))

  return s

# square = calc_square(10, 10, 10)
# square = calc_square(-2, 8, 8)
# print('Выброс исключений square ', square)

# Кастомные исключения
class InvalidTriangleError(Exception):
  """Raised when a triangle has invalid sides"""

import math

def calc_square2(ab, ac, bc):
  if ab <= 0 or ac <= 0 or bc <= 0:
    raise InvalidTriangleError("One of the sides is less or equal to 0.")
  p = (ab + ac + bc) / 2
  s = math.sqrt(p * (p-ab) * (p-ac) * (p-bc))

  return s

try:
  square = calc_square2(-5, 8, 8)
except InvalidTriangleError as ex:
  print('ex: ', ex)
else:    
  print('squareInElse: ', square)

print('Программа продолжает работать')  
