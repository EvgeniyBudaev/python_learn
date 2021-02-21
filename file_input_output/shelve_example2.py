import shelve

with shelve.open('shelve_test') as cars:
# cars =  shelve.open('shelve_test'):
  cars['opel'] = 'Germany'
  cars['ford'] = 'USA'
  cars['mazda'] = 'Japan'

while True:
  key = input('Please enter a car name')
  if key == 'quit':
    break
  country = cars.get(key, 'We do not have a ' + key)
  print(country)

# ===  
while True:
  key = input('Please enter a car name')
  if key == 'quit':
    break
  if key in cars:
    country = cars[key]
    print(country)
  else:
    print('We do not have a ' + key)

 # === сортировка
  ordered_keys_list = list(cars.keys())
  ordered_keys_list.sort()

  # for key in cars:
  #   print(key + ' ' + cars[key]) 
  
  # for key in ordered_keys_list:
  #   print(key + ' ' + cars[key])   

  for value in cars.values():
    print(value)
  print(cars.values())

  for key in cars.keys():
    print(key)
  print(cars.keys()) 

  for item in cars.items():
    print(item)
  print(cars.items())   
  
