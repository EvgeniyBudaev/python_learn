dict1 = {}
dict2 = {}
print('dict1 == dict2', dict1 == dict2) # True

list1 = []
list2 = []
print('list1 == list2', list1 == list2) # True

tuple1 = ()
tuple2 = ()
print('tuple1 == tuple2', tuple1 == tuple2) # True

print(ord('a')) # Код символа a = 97
print('hi' > 'hello') # True
print(ord('i')) # Код символа i = 105
print(ord('e')) # Код символа e = 101

age = int(input('Введите Ваш возраст '))
print('Доступ разрешен ' + str(age >= 18))

print('A' > 'a') # False A:65 vs a:97
print(ord('A'))