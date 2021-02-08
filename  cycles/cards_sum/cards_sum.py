# Мой вариант
current_hand = [2, 3, 4, 10, 'Q', 5] 
total = 0

for x in current_hand:
  if x == 2 or x == 3 or x == 4 or x == 5 or x == 6:
    total += 1 
  elif x == 7 or x == 8 or x == 9:
    total += 0
  elif x == 10 or x == 'J' or x == 'Q' or x == 'K' or x == 'A':
    total += -1  

print(f'total: {total}') 

# Решение преподавателя
cards = {2:1, 3:1, 4:1, 5:1, 6:1, 7:0, 8:0, 9:0, 10: -1, 'J':-1, 'Q':-1, 'K':-1, 'A':-1}

result = sum([cards[x] for x in current_hand])
print(f'result: {result}')