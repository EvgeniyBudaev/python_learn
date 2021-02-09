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