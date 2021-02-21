# __name__ = '__main__'
print(__name__) # __main__ по умолчанию присваивается

def function1():
  print('function1() from first.py')

print('top level in first.py')

if __name__ == '__main__':
  print('first.py is being ru directly')
else:
  print('first.py has been imported')  