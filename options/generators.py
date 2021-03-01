import random
import itertools

def randoms(min, max, n):
  for i in range(n):
    yield random.randint(min, max)

for r in randoms(10, 30, 5):
  print(r) 

rand_sequence = randoms(1, 10, 10) 
# по генератору циклом можно пройтись только один раз

seq = list(randoms(1, 10, 5)) # теперь можем циклом проходить сколько угодно раз

# === 
sequence = randoms(1, 10, 10)
five_taken = list(itertools.islice(sequence, 5))
print(five_taken) # [3, 5, 4, 8, 10]

def randoms(min, max):
  while True:
    yield random.randint(min, max)

numbers = randoms(1, 100)
five_numbers = list(itertools.islice(numbers, 5))
print(five_numbers) # [26, 45, 7, 97, 44]  

# Ленивая загрузка из файла
def read_line_by_line(file):
  """Lazy function (generator) to read a file line by line."""
  while True:
    line = file.readline()
    if not line:
      break
    yield line

file = open(f"C:\\temp\\test.txt")
for line in read_line_by_line(file):
  print(line.rstrip())  

# next
rand_seq = randoms(1, 10) 
n = next(rand_seq)
print(n)

# list comprehansion
my_list = [1, 2, 4]
squares = [x**2 for x in my_list]
print(squares )
  