from functools import wraps

def stop_kwargs(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    if kwargs:
      raise ValueError('Keyword arguments are prohibited')
    return func(*args, **kwargs)
  return wrapper

def stop_int_arguments(func):  
    @wraps(func)
    def wrapper(*args, **kwargs):
      for val in args:
        if type(val) == int:
          raise ValueError('integer arguments are prohibited')
      for key, val in kwargs.items():
        if type(val) == int:
          raise ValueError('integer arguments are prohibited')
      return func(*args, **kwargs)
    return wrapper

@stop_kwargs
def print_hello(name):
  print(f'Hello {name}')

# print_hello(name='Jack') # ValueError: Keyword arguments are prohibited
print_hello('Jack')
print_hello(3)      