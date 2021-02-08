# Мой вариант
numbers = int(input("Введите количество звезд"))
x = 0
star = '*'

while x < numbers:
  print('star:', star)
  x += 1
  star += '*'

# Решение преподавателя
rows = int(input('Enter the number of rows'))

for x in range(rows):
  print('*' * (x + 1))