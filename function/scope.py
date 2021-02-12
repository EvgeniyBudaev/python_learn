# Local Scope
pi = 'Внешняя переменная'

def print_pi():
  pi = 'Внутрення переменная'
  print(pi) # Внутренняя переменная

print_pi() # Внутренняя переменная
print(pi) #Внешняя переменная

# Enclosed Scope
pi = 'global pi variable'

def outer():
  pi = 'outer pi variable'
  def inner():
    # pi = 'inner pi variable'
    # global pi
    nonlocal pi
    pi = 'new value'
    print(pi)
  inner()
  print(pi) # 'outer pi variable' => 'new value'

outer() 
print(pi) # global pi variable