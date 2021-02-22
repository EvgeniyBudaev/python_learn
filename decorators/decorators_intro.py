# def simple_func():
#   print('simple')

def decorator_func(original_func):
  def wrap_func():
    print('before')
    original_func()
    print('after') 
  return wrap_func

# decorator_func = decorator_func(simple_func)
# decorator_func()   
@decorator_func
def simple_func():
  print('simple')

simple_func() 

# === С передачей аргументов
def make_compliment(func):
  def wrapper(*args, **kwargs):
    print('Nice to meet you!')
    func(*args, **kwargs)
  return wrapper

@ make_compliment
def say_name(name):
  print('My name is ' + name)

say_name('Evgeniy')       
