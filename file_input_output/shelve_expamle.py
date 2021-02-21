import shelve

with shelve.open('shelve_test') as cars:
  cars['opel'] = 'Germany'
  cars['ford'] = 'USA'
  cars['mazda'] = 'Japan'

  print(cars['ford']) # USA
  print(cars['mazda']) # Japan

  del cars['opel']

  for key in cars:
    print('key: ', key)

