# Встроенные функции
print('Hello!')
x = set()

# Встроенные методы
my_list = [1, 2, 3]
my_list.append(4) # append() метод добавления

# Создание функций
def print_greeting():
  '''
  Print 'Создали функцию!' text
  :return: None
  '''
  print('Создали функцию!') 

def greeting():
  '''
  DOCSTRING: information about the function
  INPUT: no input...
  OUTPUT: Hello!
  '''
  print('Hello!')   

#  вызов функции
print_greeting()
# описание функции 
# help(print_greeting) 
# help(greeting)

# Функция с аргументами
def print_text_with_name(name = 'Guest'):
  '''
  :param name
  :return: None
  '''
  print(f'Hello {name} !')
print_text_with_name('Jack')  

# Функция с возвращаемым значением
def sum_of_two_numbers(a = 0, b = 0):
  '''
  :param a: the first addend
  :param b: The second addend
  :return: Sum of a and b
  '''
  return a + b
result = sum_of_two_numbers(1, 2)
print('result: ', result)


def is_hello_in_text(text):
  if 'hello' in text.lower():
    return True
  else:
    return False
print(is_hello_in_text('Say Hello everyone'))  

def is_hello_in_text_2(text):
  return 'hello' in text.lower()
print(is_hello_in_text_2('Say Hello everyone')) 

def is_string_in_text(string, text):
  return string in text
print(is_string_in_text('he', 'The apple')) 


def greeting_depends_on_gender(name, gender):
  if gender == 'male':
    print('Hello ' + name + '! You look great!')
    return gender
  elif gender == 'female':
    print(f'Hello {name}! Yoa are so nice!')
    return gender
  else:
    print(f'Нет такого пола!')
    return gender

greeting_depends_on_gender('Jack', 'male')        


def generate_odd_numbers(a = 0, b = 0):
  list_odd_numbers = []
  for number in range(a, b + 1):
    if number % 2 != 0:
      list_odd_numbers.append(number)
  return list_odd_numbers

generate_odd_numbers(1,3)


def get_odd_number_list(a, b):
    number_list = list(range(a, b + 1))
    odd_number_list = [number for number in number_list if number % 2 == 1]
    return odd_number_list

# Математические функции
print(abs(-1)) # 1
print(max(1, 2, 3)) # 3 
print(max([1, 2, 3])) # 3  
print(min([1, 2, 3])) # 1
print(pow(2, 3)) # 8 pow - возведение в степень  
print(round(3.37, 1)) # 3.4 round - округление до целого. 1 - количество знаков после плавающей точки
print(sum([1,2,3])) # 6 sum - принимает list
h = hex(42)
o = oct(42)
b = bin(42)
print(h) # 0x2a
print(o) # 0o52
print(b) # 0b101010

# Функции с итерируемыми объектами
# all
all_true1 = all([True, True, True])
all_true2 = all([True, False, True])
print(all_true1) # True. all - возвращается boolen. Возвращает True, когда все элементы True
print(all_true2) # False.
players = [('Carlsen', 2842), ('Caruana', 2822)]
print(all(rating > 2700 for _, rating in players)) # True Данная запись работает быстрее. До первого False и остановится
print(all([rating > 2700 for _, rating in players])) # True

# any - если бы хотя бы один элемент True
any_true1 = any([True, False, True]) # True
any_true2 = any([False, False, False]) # False
print(any_true1) # True
print(any_true2) # False

# zip - склеивание двух итерируемых объектов. Излишние элементы отсечены
letters = 'abcd'
numbers = (10, 20 ,30)
zipped = zip(letters, numbers)
print(zipped) # <zip object at 0x7ff778090040>
zipped_list = list(zipped)
print(zipped_list) # [('a', 10), ('b', 20), ('c', 30)]

names = ['Carlsen', 'Caruana']
ratings = [2842, 2822]
players = dict(zip(names, ratings))
print(players) # {'Carlsen': 2842, 'Caruana': 2822}

# input - запрос данных от пользователя
reply = input('Введите данные ')
print(reply)

# unicode
code =  ord('a')
print(code) #97
c = chr(code)
print(c) # 'a'

