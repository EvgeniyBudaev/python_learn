# List Comprehension
text = 'hello'
letter_list = [letter for letter in text]
print(letter_list)

number_list = [number for number in range(0, 10)]
print(number_list)

num_list = [6,43, -7, -10, 1]
num_list = [num for num in num_list if num > 0]
print(num_list)

# Из исходного списка greetings = ['hello', 'hi', 'hey', 'hola'] создаем новый список содержащий, вторую букву из каждой строки исходного списка. Выводим новый список на печать.
greetings = ['hello', 'hi', 'hey', 'hola']
new_greetings = [letter[1] for letter in greetings]
print(new_greetings)

arr_greetings = []
for letter in greetings:
  arr_greetings.append(letter[1])
print(arr_greetings)  

# Из исходного списка digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] создаем новый список, содержащий нечетные числа исходного списка. Выводим новый список на печать.
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_digits = [number for number in digits if number % 2 != 0]
print(new_digits)

odd_list = []
for num in digits:
  if num % 2 != 0:
    odd_list.append(num)
print(odd_list)    