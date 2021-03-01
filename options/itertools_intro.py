import itertools 

even_numbres = [x for x in range(10) if x % 2 ==0]
print(even_numbres) # память выделяется под все сгенерируемые объекты # [0, 2, 4, 6, 8]

# ленивое исполнение
even_numbers = itertools.count(0, 2)
print(list(next(even_numbers) for _ in range(5))) # [0, 2, 4, 6, 8]
print(list(zip(itertools.count(), ['a', 'b', 'c']))) # [(0, 'a'), (1, 'b'), (2, 'c')]
def print_iterable(iterable, end = None):
  for x in iterable:
    if end:
      print(x, end = end)
    else:
      print(x) 

ones = itertools.repeat(1, 5)       
print_iterable(ones, ' ') # 1 1 1 1 1


# ===
print(list(map(pow, range(10), itertools.repeat(2)))) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
for _ in itertools.repeat(None, 100000): # это работает быстрее чем range
  pass

for _ in range(100000):
  pass


# === cycle ===
pos_neg_ones = itertools.cycle([1, -1])
print(list(next(pos_neg_ones) for _ in range(10))) # [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
letters = itertools.cycle(['A', 'B', 'C'])
print(list(next(letters) for _ in range(10))) # ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']


# === accumulate ===
print(list(itertools.accumulate([1, 2, 3, 4, 5]))) # [1, 3, 6, 10, 15]
print(list(itertools.accumulate(['A', 'B', 'C', 'D']))) # ['A', 'AB', 'ABC', 'ABCD']


# === chain ===
print(list(itertools.chain('ABC', 'DEF'))) # ['A', 'B', 'C', 'D', 'E', 'F']
print(list(itertools.chain.from_iterable(['ABC', 'DEF']))) # ['A', 'B', 'C', 'D', 'E', 'F']
print(list(itertools.chain([1,2,3], [4,5,6], [7,8,9]))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# === dropwhile, takewhile ===
print(list(itertools.dropwhile(lambda x: x<3, [1,2,3,4,5]))) # [3, 4, 5]
print(list(itertools.takewhile(lambda x: x<3, [1,2,3,4,5]))) # [1, 2]


# === filterfalse ===
print(list(itertools.filterfalse(lambda x: x%2==0, range(10)))) # [1, 3, 5, 7, 9]


# === tee ===
iterable1, iterable2 = itertools.tee([1,2,3], 2)
print_iterable(iterable1, ' ') # 1 2 3
print("\niterable is exausted") # iterable is exausted
print_iterable(iterable2, ' ') # 1 2 3


# === zip ===
names = ['Carlsen', 'Caruana', 'Mamedyarov', 'Ding', 'Giri']
ratings = [2842, 2822, 2801, 2792, 2780]
for name, rating in zip(names, ratings):
  print(f"{name}:{rating}")
#  Carlsen:2842
#  Caruana:2822
#  Mamedyarov:2801
#  Ding:2792
#  Giri:2780  

print(list(zip(names, ratings))) # [('Carlsen', 2842), ('Caruana', 2822), ('Mamedyarov', 2801), ('Ding', 2792), ('Giri', 2780)]
print(dict(zip(names, ratings))) # {'Carlsen': 2842, 'Caruana': 2822, 'Mamedyarov': 2801, 'Ding': 2792, 'Giri': 2780}


# === zip_longest ===
names2 = ['Carlsen', 'Caruana', 'Mamedyarov', 'Ding', 'Giri', 'Kramnik']
ratings2 = [2842, 2822, 2801, 2792, 2780]
players = dict(itertools.zip_longest(names2, ratings2))
print(players) # {'Carlsen': 2842, 'Caruana': 2822, 'Mamedyarov': 2801, 'Ding': 2792, 'Giri': 2780, 'Kramnik': None}
players2 = dict(itertools.zip_longest(names2, ratings2, fillvalue = 0))
print(players2) # {'Carlsen': 2842, 'Caruana': 2822, 'Mamedyarov': 2801, 'Ding': 2792, 'Giri': 2780, 'Kramnik': 0}


# === groopby ===
lst = [1, 1, 1, 2, 2 ,2, 3, 3]
for key, grp in itertools.groupby(sorted(lst)):
  print('{}:{}'.format(key, list(grp)))
# 1:[1, 1, 1]
# 2:[2, 2, 2]
# 3:[3, 3]

forecast = [
  {'humidity': 20, 'temperature': 78, 'wind': 7},
  {'humidity': 50, 'temperature': 61, 'wind': 10},
  {'humidity': 20, 'temperature': 84, 'wind': 19}
]
 
def group_sorted(iterable, key = None):
  return itertools.groupby(sorted(iterable, key=key), key=key)

grouped_data = group_sorted(forecast, key=lambda x: x['humidity'])  
for key, grp in grouped_data: 
  print('{}:{}'.format(key, list(grp)))
# 20:[{'humidity': 20, 'temperature': 78, 'wind': 7}], {'humidity': 20, 'temperature': 84, 'wind': 19}]
# 50:[{'humidity': 50, 'temperature': 61, 'wind': 10}] 


# === islice === 
odd_numbers = itertools.count(0, 2)
print([x for x in range(20) if x%2 != 0]) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(list(itertools.islice(odd_numbers, 2, 10, 2))) # [4, 8, 12, 16] срезаем с шагом
print(list(itertools.islice(odd_numbers, 4))) # [20, 22, 24, 26] срезаем по количеству


# === permutations количество возможных комбинаций ===
pin = [7, 5, 2, 8]
print(list(itertools.permutations(pin)))


# === product ===
ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'C', 'S']
koloda = list(itertools.product(ranks, suits))
print(koloda) # [('6', 'H'), ('6', 'D'), ('6', 'C'), ('6', 'S'), ('7', 'H'), ('7', 'D'), ('7', 'C'), ('7', 'S'), ('8', 'H'), ('8', 'D'), ('8', 'C'), ('8', 'S'), ('9', 'H'), ('9', 'D'), ('9', 'C'), ('9', 'S'), ('10', 'H'), ('10', 'D'), ('10', 'C'), ('10', 'S'), ('J', 'H'), ('J', 'D'), ('J', 'C'), ('J', 'S'), ('Q', 'H'), ('Q', 'D'), ('Q', 'C'), ('Q', 'S'), ('K', 'H'), ('K', 'D'), ('K', 'C'), ('K', 'S'), ('A', 'H'), ('A', 'D'), ('A', 'C'), ('A', 'S')]


# === combinations ===
print(list(itertools.combinations(koloda, 2)))

print(list(itertools.combinations('ABCD', 2))) # [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]