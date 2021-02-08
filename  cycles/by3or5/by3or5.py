# Мой вариант
number = int(input("Введите число: "))
total_sum = 0

for i in range(number + 1):
    if i % 3 == 0 or i % 5 == 0:
             total_sum += i

print(f'Сумма равна: {total_sum}') 

# Решение преподавателя
limit = int(input("Enter the limit: "))

total_sum = sum([x for x in range(limit + 1) if x % 3 == 0 or x % 5 == 0])
print(f'Total = {total_sum}') 