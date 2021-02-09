# tuple - Кортеж. Упорядочный список. Нельзя менять содержимое

tuple_1 = (1, 2, 3, 5.5, 'one')
print('tuple_1[0] ', tuple_1[0])
new_tuple = (tuple_1[0], 'new element', tuple_1[2])
print('new_tuple: ', new_tuple)

# Множественное присваивание
x, y, z = 12, 13, 14
print('x, y, z', x, y, z)
person_tuple = ('John', 'Smith', 1986)
first_name, last_name, age = person_tuple
print('first_name, last_name, age: ', first_name, last_name, age)

# Количество вхождений
t1 = (1, 10, 3, 4, 1, 6)
print('t1.count(1) ', t1.count(1))

# Вычислить index какого-то элемента
print(t1.index(10))