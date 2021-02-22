# Infinity process

def create_patterns():
  max_patterns_number = 100
  patterns = ('First pattern', 'Second pattern', 'Third pattern')
  i = 0 
  result_list = []
  while len(result_list) < max_patterns_number:
    if i >= len(patterns):
      i = 0
    result_list.append(patterns[i])
    i += 1
  return result_list 

print(create_patterns())

# Прии помощи генератора
def get_current_pattern():
  patterns = ('First pattern', 'Second pattern', 'Third pattern')
  i = 0
  while True:
    if i >= len(patterns):
      i = 0
    yield patterns[i]
    i += 1

current_pattern =  get_current_pattern()
print(current_pattern.__next__()) # First pattern
print(current_pattern.__next__()) # Second pattern    
print(current_pattern.__next__()) # Third pattern   
print(current_pattern.__next__()) # First pattern         