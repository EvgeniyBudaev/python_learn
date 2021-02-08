import random

tries = 0
random_number = random.randint(1, 50)
print(f'random_number: {random_number}')
print('Угадайте число от 1 до 50')

while tries < 6:
  guess = int(input('Введите число: '))
  tries += 1

  if guess < random_number:
    print('Маленькое число!')
  if guess > random_number:
    print('Большое число!')
  if guess == random_number:
    print(f'УРА! Вы выиграли! Число попыток {tries}') 
    break

  if guess != random_number and tries == 6:
    print(f'Вы не угадали число! Мое число было: {random_number}')
    break      