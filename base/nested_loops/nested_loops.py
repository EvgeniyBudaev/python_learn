smile = '\U0001f600'

for number in range(10):
  count = 0
  emoticons = ''
  while count <= number:
    emoticons += smile
    count += 1
  print(emoticons) 

# тоже самое, но короче
for number in range(11):
  print(smile * number)  

count = 1
while count < 11:
  print(smile * count) 
  count += 1
   