import copy

list1 = [1, 2, 3, [4, 5, 6]]

copied_list = list1.copy()
copied_list[3].append(7)
print(list1) # [1, 2, 3, [4, 5, 6, 7]]
print(copied_list) # [1, 2, 3, [4, 5, 6, 7]]


# Поверхностная копия
shallow_copy = copy.copy(list1)
shallow_copy[3].append(8)
print(list1) # [1, 2, 3, [4, 5, 6, 7, 8]]
print(copied_list) # [1, 2, 3, [4, 5, 6, 7, 8]]

# Глубокое копирование
deep_copy = copy.deepcopy(list1)
deep_copy[3].append(9)
print(list1) # [1, 2, 3, [4, 5, 6, 7, 8]]
print(deep_copy) # [1, 2, 3, [4, 5, 6, 7, 8, 9]]


class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __repr__(self):
    return f"Point({self.x}, {self.y})" 


a = Point(1, 2)
b = copy.copy(a)
a.x = 3
print(a) # Point(3, 2)
print(b) # Point(1, 2)


class Line():
  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2

  def __copy__(self): # так работает неглубокое копирование
    cls = self.__class__
    result = cls.__new__(cls)
    result.__dict__.update(self.__dict__)
    return result  

  def __deepcopy__(self, memo): # рекурсивное копирование всех объектов
    cls = self.__class__
    result = cls.__new__(cls)
    memo[id(self)] = result
    for k, v in self.__dict__.items():
      setattr(result, k, copy.deepcopy(v, memo)) 
    return result  

l1 = Line(a, b)
l2 = copy.copy(l1)
l1.p1.x = 4
print(l1.p1) # Point(4, 2)
print(l2.p1) # Point(4, 2) 


l3 = Line(a, b)
l4 = copy.deepcopy(l3)
l3.p1.x = 6
print(l3.p1) # Point(6, 2)
print(l4.p1) # Point(4, 2)


