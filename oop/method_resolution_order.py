# Method Resolution Order

#   A
#  / \
# B   C
#  \ /
#   D

class A:
  def some_method(self):
    print('Method of class A')


class B(A):
  @classmethod
  def some_method(cls):
    print('Method of class B')


class C(A):
  def some_method(self):
    print('Method of class C')


class D(B, C):
  pass
  # def some_method(self):
  #   print('Method of class D')


# __mro__, mro(), help()
print(D.__mro__) # цепочка вызовов (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

print(D.mro()) # тот же самый порядок
# help(D)

# some_object = D()
# some_object.some_method()