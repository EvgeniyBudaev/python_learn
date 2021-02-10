# Set - Неупорядочная коллекция уникальных элементов 

rainbow_colors = {'red', 'blue', 'orange', 'green'}

# Объявление пустого множества Set
empty_set = set()

number_list = [1, 2, 3, 43] 
text_tuple = ('a', 'b', 'c')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)
print('set_from_list ', set_from_list)
print('set_from_tuple ', set_from_tuple)

# Добавление
set_from_list.add(777)
set_from_tuple.add('hello')

# Удаление
set_from_list.pop() # удаление случайного элемента. Элемент возращается при удалении.
set_from_list.remove(777) # удаление элемента по значению. Элемент не возращается при удалении. Если элемента нет, то будет ошибка при удалении.
set_from_list.discard(43) # Если элемента нет, то не будет ошибки при удалении.
set_from_list.clear() # Полная очистка множества

text = 'This is Python'
set_text = set(text)
print('set_text ', set_text)
print(type(set_text))