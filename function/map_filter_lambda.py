# Map, Filter, Lambda Expressions
def sum_of_two_numbers(x):
  return x + x

numbers_list = [1,2,3,4,5]

result = map(sum_of_two_numbers, numbers_list)
print('result: ', result) # <map object at 0x7ff9102cb940>

for item in result:
  print(item) # 2 4 6 8 10

for item in map(sum_of_two_numbers, numbers_list):
  print(item)  # 2 4 6 8 10

print(list(map(sum_of_two_numbers, numbers_list))) # [2, 4, 6, 8, 10] 

# ===
def is_a_in_string(string):
  if 'a' in string:
    print("String has 'a'")
    return True
  else:
    print("String has not 'a'")
    return False

string_list = ['hi', 'was', 'name', 'a']

print(list(map(is_a_in_string, string_list))) # [False, True, True, True]

# Filter
def is_number_odd(number):
  return number % 2 == 1

numbers_list = [1,2,3,4,5]

print(list(filter(is_number_odd, numbers_list))) # [1, 3, 5]

for number in filter(is_number_odd, numbers_list):
  print(number) # 1 3 5

# ===
def is_a_in_string2(string):
  if 'a' in string:
    print("String has 'a'")
    return True
  else:
    print("String has not 'a'")
    return False

string_list = ['hi', 'was', 'name', 'a']  

print(list(filter(is_a_in_string2, string_list))) # ['was', 'name', 'a']


# Lambda Expressions

# def cube(number):
#   return number ** 3

lambda number: number ** 3

numbers_list = [1,2,3]  
print(list(map(lambda number: number ** 3, numbers_list))) # [1, 8, 27]

print(list(filter(lambda number: number % 2 == 1, numbers_list))) # [1, 3]

string_list = ['hi', 'my', 'name']
print(list(map(lambda string: string[-1], string_list))) # ['i', 'y', 'e']
print(list(map(lambda string: string[::-1], string_list))) # ['ih', 'ym', 'eman']