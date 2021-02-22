def get_number_from_range():
  for number in range(10):
    yield number

counter = get_number_from_range()
print(next(counter)) # 0   

counter1 = (number for number in range(10))
print(next(counter1)) # 0

print([number for number in range(10)]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]