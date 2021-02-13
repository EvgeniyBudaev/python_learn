# dict - словарь

car_prices = {
   'opel': 5000,
   'vaz': 1000,
   'toyota': 6000
   }
  
print('car_prices: ', car_prices)
print('car_prices[opel]: ', car_prices['opel'])

car_prices['vaz'] = 2000

# Удаление
del car_prices['toyota'] # удаление
car_prices.clear() # удаление всех элементов из словаря

simple_dict = {'a': 1, 'b': 2, 'c': 3}
result = simple_dict.pop('a') # result 1 .Удаление по ключу
print(simple_dict) # {'b': 2, 'c': 3}

simple_dict2 = {'a': 1, 'b': 2, 'c': 3}
new_simple_dict = {'f': 10}
new_simple_dict.update(simple_dict2)
print('new_simple_dict ', new_simple_dict) # {'f': 10, 'a': 1, 'b': 2, 'c': 3}

person = {
  'first name': 'Jack',
  'last name': 'Brown',
  'age': 43,
  'hobbies': ['football', 'singing', 'photo'],
  'children': {'son': 'Michael', 'daugter': 'Pamela'}
}

print(person['age'])
print(person['hobbies'][2])
print(person['children']['son'])

# Добавление
person['car'] = 'Mazda'

# Получение ключей и значений
print(person.keys())
print(person.values())
print(person.items())

# Создание словаря из двух списков
list_with_keys = [1, 2]
list_with_values = [3, 4]
data = dict(zip(list_with_keys, list_with_values))
print('data ', data) # {1: 3, 2: 4}