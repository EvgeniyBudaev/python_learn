# Мой вариант
number = int(input('Введите число: '))

for i in range(number + 1):
  if i%2 == 0:
    print(f'{i} is EVEN')
  else:
    print(f'{i} is ODD')

# Вариант №2
limit = int(input('Enter the limit: '))

result = [f'{x} is EVEN' if x%2==0 else f'{x} is ODD' for x in range(number + 1)]
for i in result:
  print(i)
