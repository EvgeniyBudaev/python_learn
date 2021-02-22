# Generators are iterators
# Генераторы могут быть созданы с помощью функций генераторов
# Генераторы могут быть созданы с помощью generator expressions(выражений)

def count_up_to(x):
  count = 0
  while count <= x:
    yield count
    count += 1

for number in count_up_to(4):
  print(number) # 0...4