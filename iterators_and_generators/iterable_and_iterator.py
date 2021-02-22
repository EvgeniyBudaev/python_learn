# Iterate - перебор
# Iterable - объект, элементы которого можно перебирать
number_list = [1, 2, 3, 4, 5]

for number in number_list:
  print('number: ', number)

# Iterators
number_list_iterator = iter(number_list)  
print('number_list_iterator: ', number_list_iterator) # <list_iterator object at 0x7f81e8039a30>
print(number_list_iterator.__next__()) # 1
print(next(number_list_iterator)) # 2

# Как устроен цикл for
def my_for_loop(iterable):
  iterator = iter(iterable)

  while True:
    try:
      print(iterator.__next__())
    except StopIteration:
      break

my_for_loop('hello')    


