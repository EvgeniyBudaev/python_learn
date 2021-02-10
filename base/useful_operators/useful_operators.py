for x in range(1, 10, 3): # 3 - шаг
  print(x)

print(list(range(5))) # [0, 1, 2, 3, 4]

# index
letter_index = 0
my_string = 'Hello'
for letter in my_string:
  print(letter + 'is at index ' + str(letter_index))
  letter_index = letter_index + 1

my_string = 'World'
for item in enumerate(my_string):
  print(item) # (0, 'W') (1, 'o') (2, 'r') (3, 'l') (4, 'd')

for index, letter in enumerate(my_string):
  print(letter + ' is at index ' + str(index)) # W is at index 0 ...

print('a' in 'Jack') # True 

letter_list = ['a', 'b', 'c'] 
print('a' in letter_list) # True 

dict_1 = {1: 'a', 2: 'b'}
print(1 in dict_1) # True 
print('b' in dict_1.values()) # True 

print(min(35, 23, 1))
print(max(35, 23, 1))

math_list = [35, 23, 1]
print(min(math_list))

from random import shuffle # shuffle - перемешать, перетасовать
my_list = [1, 3, 56, 4]
shuffle(my_list)
print(math_list)

from random import randint # случайное целое число
print(randint(1, 3)) # диапозон случайных чисел включительно