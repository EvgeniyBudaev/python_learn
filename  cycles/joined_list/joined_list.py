# Мой вариант
first_lst = [1, 2, 3, 4, 5]
second_lst = [11, 16, 13, 18, 17, 19]

joined_list = []

for i in first_lst:
  if i % 2 != 0:
    joined_list.append(i)

for j in second_lst:
  if j % 2 == 0:
    joined_list.append(j)

print('joined_list: ', joined_list)

# Решение преподавателя
first_lst = [1, 2, 3, 4, 5]
second_lst = [11, 16, 13, 18, 17, 19]

unit_list = []

odds = [x for x in first_lst if x % 2 != 0]
evens = [x for x in second_lst if x % 2 == 0]

unit_list = odds + evens
print(f'unit_list: {unit_list}')