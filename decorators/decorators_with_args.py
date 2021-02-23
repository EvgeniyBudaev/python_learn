from functools import wraps

def check_if_first_arg_is(value):
  def inner_dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      if args and args[0] != value:
        print(f"First argument has to be {value}")
      return func(*args, **kwargs) 
    return wrapper
  return inner_dec

@check_if_first_arg_is('red')
def print_rainbow_colors(*colors):
  print(colors)

print_rainbow_colors('red', 'green', 'blue') # ('red', 'green', 'blue') 

# Приводить к нужному типу аргументы
def enforce(*types):
  def inner_dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      new_args = []
      for a, t in zip(args, types):
        new_args.append(t(a))
      return func(*new_args, **kwargs)
    return wrapper
  return inner_dec

@enforce(str, int)
def print_text_n_times(text, n):
  for number in range(n):
    print(text)

print_text_n_times('Hi!', '2')

# *args - ('Hi!', '2')
# *types - (str, int)
# zip(args, types) - ('Hi!', str) ('3', int)