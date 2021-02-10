# for для list
number_list = [1, 2 ,3, 4, 5]
list_numbers_sum = 0

for number in number_list:
  list_numbers_sum = list_numbers_sum + number
print('list_numbers_sum: ', list_numbers_sum)

# for для tuple
tuple_list = [('a', 'b'), ('c', 'd')]
for item in tuple_list:
  print('item: ', item)
for letter1, letter2 in tuple_list:
  print('letter1, letter2 ', letter1, letter2)  

# for для dict

dictionary = {'key1': 'value1', 'key2': 'value2'} 

for item in dictionary:
  print('dict item: ', item) # получили только ключи

for item in dictionary.items():
  print('dict item: ', item) # ('key1': 'value1') ('key2': 'value2')

for key, value in dictionary.items(): # key, value
  print('dict key: ', key)

for item in dictionary.keys(): # keys
  print('dict key ', item)

for item in dictionary.values(): # values
  print('dict value: ', item)

# range

for x in range(2): # диапозон от 0 до 1
  print('x: ', x)  

for _ in range(2): # когда переменная не нужна
  print('Hello')