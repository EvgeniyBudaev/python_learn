class MyStack:

  def __init__(self):
    self.array = []

  def push(self, item):
    self.array.append(item)

  def pop(self):
    popped_item = self.array.pop()
    return popped_item

  def peek(self):  # peek возвращает последний элемент, но не удаляет его
    return self.__current()

  def __current(self):
    return self.array[self.count()-1]

  def count(self):
    return len(self.array)

  def __iter__(self):
    self.index = self.count()-1
    return self

  def __next__(self):
    if self.index < 0:
      raise StopIteration()
    result = self.array[self.index]
    self.index -= 1
    return result  


stack = MyStack()
stack.push(11)
stack.push(12)   
stack.push(13) 
print(stack.peek()) # 13
print(stack.count()) # 3

for i in stack:
  print(i) # 13 12 11