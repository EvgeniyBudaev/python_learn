def ten_percent_of_product(x, y):
  return (x * y) * 0.1
print(ten_percent_of_product(10, 20)) 

# *args
def ten_percent_of_product_with_args(*args):
  print(args) # (10, 20)
  product = 1
  for number in args:
    product = product * number
  return product * 0.1  
print(ten_percent_of_product_with_args(10, 20)) 

def percent_of_product_with_args(percent, *args):
  print(args) # (10, 20)
  product = 1
  for number in args:
    product = product * number
  return product / 100 * percent  
print(percent_of_product_with_args(10, 10, 20)) 

# **kwargs
def func_kwargs(**kwargs):
  print(kwargs) # {'first': 1, 'second': 2}
func_kwargs(first=1, second=2)

def hello_with_kwargs(greeting, **kwargs):
  if 'name' in kwargs:
    print('{}, {}'.format(greeting, kwargs['name']))
  else:
    print(f'{greeting}. What is your name?')  
hello_with_kwargs('Hello', gender='male', age=34, name='Jack')  

def func_with_args_and_kwargs(*args, **kwargs):
  print(args)
  print(kwargs)

# Задачи
def is_cat_here(*args):
    args_in_lower_case = [str(argument).lower() for argument in list(args)]
    if 'cat' in args_in_lower_case:
        return True
    else:
        return False
print(is_cat_here('cat'))

def is_item_here(item, *args):
  args_case = [argument for argument in list(args)]
  if item in args_case:
    return True
  else:
    return False
print(is_item_here(1, 10,5,1)) 

def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is ' + str(my_color) +
              ', but ' + kwargs['color'] + ' is also pretty good!')
    else:
        print('My favorite color is ' + str(my_color) +
              ', what is your favorite color?')