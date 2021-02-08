# Мой вариант
table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
handle_cards = ["J_D", "3_D"]

table_suites = [x[-1] for x in table_cards]
handle_suites = [i[-1] for i in handle_cards]

suites_in_game = table_suites + handle_suites

flush = False

for suit in 'CHSD':
  if suites_in_game.count(suit) >= 5:
    flush = True

if flush:
  print('Flush!')   
else:
     print('No Flush!') 

 # Решение преподавателя
table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
handle_cards = ["J_D", "3_D"]

table_suites = [x[-1] for x in table_cards]
handle_suites = [i[-1] for i in handle_cards]

suites_in_game = table_suites + handle_suites

flush = any([suites_in_game.count(suit) >= 5 for suit in 'CHSD']) 

if flush:
  print('Flush!')   
else:
     print('No Flush!') 