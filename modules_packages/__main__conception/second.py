import first

print('top level in second.py')

first.function1()

if __name__ == '__main__':
  print('second.py is being ru directly')
else:
  print('second.py has been imported')  