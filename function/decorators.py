from timeit import default_timer as timer
import math
import time

def hello_world():
  def internal():
    print('Hello, World!')
  return internal

variables = hello_world()
variables() # Hello, World!

# ===
def say_somethings(func):
  func()

def hello_python():
  print('hello, Python!')

say_somethings(hello_python) # hello, Python!  

# Декораторы
def log_decorator(func):
  def wrap():
    print(f'Calling func {func}')
    func()
    print(f'Func {func} finished its work')
  return wrap

def hello():
  print('hello')

wrapped_by_logger = log_decorator(hello)
wrapped_by_logger()

# ==
@log_decorator
def hello_decorator():
  print('hello, decorator!')

hello_decorator() 

# Декоратор для измерения скорости работы функции
def measure_time(func):
  def inner(*args, **kwargs):
    start = timer()
    func(*args, **kwargs)
    end = timer()
    print(f'Function {func.__name__} took {end-start} for execution')
  return inner  

@measure_time
def factorial(num):
  time.sleep(3)
  print(math.factorial(num))

factorial(100)