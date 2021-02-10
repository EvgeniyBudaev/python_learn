x = 2

while x > 1:
  print(x)
  x = x -1

while x < 10:  
  print(x)
  x = x + 1

# break, continue, pass

my_list = [1, 2, 3]

for item in my_list:
  pass # заглушка, чтобы цикл ничего не делал

# break
for item in my_list:
  if item == 2:
    break
  print(item)

print('Another code')

#continue
for item in my_list:
  if item == 2:
    continue
  print(item)

print('Another code') 