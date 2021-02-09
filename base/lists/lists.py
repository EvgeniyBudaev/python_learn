some_list = [1, 4.5, 'Jack']
print('Длинна списка: ',len(some_list))
another_list = some_list[:2] # [1, 4.5]
new_list = some_list + another_list # Объединение списков

# Методы
# Добавление

new_list.append('new element') # добавляем элемент в конец списка. Метод pop удаляет по индексу.
new_list.insert(0, 'start') # добавляем элемент в начало списка

# Удаление
deleted_item = new_list.pop() # удаляем элемент из конца списка
new_list.pop(-1) # удаляем элемент из конца списка
new_list.pop(0) # удаляем элемент из начала списка

deleted_item = new_list.remove(4.5) # Метод remove удаляет по значению.

print(new_list)

# Сортировка
number_list = [45, 12, 3, -45, 22]
letter_list = ['s', 'w', 't', 'a']
number_list.sort() # Метод sort ничего не возвращает x = number_list.sort() В данном случае x будет None
new_number_list = number_list # таким образом мы записали отсортированный список в переменную
letter_list.sort()

print('Сортировка number_list: ', number_list)
print('Сортировка letter_list: ', letter_list)

# В обратном порядке
number_list.reverse()

list = [1, 2, 3, 4, 5]
new_list = list[:3]
print('new_list: ', new_list)
