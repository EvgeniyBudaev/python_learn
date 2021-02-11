# Вложенные списки

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(len(nested_list)) # длинна 3
print(len(nested_list[0])) # длинна первого списка равна 3

for inner_list in nested_list:
  print(inner_list)

for inner_list in nested_list:
  for number in inner_list:
   print(number) # получили все элементы

result = [number for number in inner_list for inner_list in nested_list]  
print(result) 
[[print(number) for number in inner_list] for inner_list in nested_list]  