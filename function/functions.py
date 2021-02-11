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

#  вызов функции
print_greeting()
# описание функции 
# help(print_greeting) 

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

