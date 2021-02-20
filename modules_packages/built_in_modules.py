import random
# from random import randint

x = random.randint(1, 10)
print(x)

from random import shuffle as shuffle_my_list
my_list = [1, 2, 3]
shuffle_my_list(my_list) # перемешиваем
print(my_list)