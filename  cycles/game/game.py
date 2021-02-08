import random

should_continue = True

while should_continue:
  player_choice = input('Player choice: [R/S/P] ').lower()
  if player_choice not in ['r', 's', 'p']:
    print('Incorect input. Try again')
    continue

  gen = {1:'r', 2:'s', 3:'p'}
  comp_choice = gen[random.randint(1,3)]

  print(f'Comp choise = {comp_choice}')

  winning_combinations = [('p', 'r'), ('r', 's'), ('s', 'p')]

  if player_choice == comp_choice:
    print('Ничья')
  elif (player_choice, comp_choice) in winning_combinations:
    print('Вы победили!')
  else:
    print('Победил компьютер')  

  should_continue = input('Want to proceed? [y/n]').lower() == 'y' 