from collections import defaultdict

my_dict = defaultdict(object)
my_dict = {1: 'a'}

print(my_dict[2]) # object если нет такого ключа

s = 'Hello'
d = defaultdict(int)
for k in s:
  d[k] += 1
  print(sorted(d.items()))