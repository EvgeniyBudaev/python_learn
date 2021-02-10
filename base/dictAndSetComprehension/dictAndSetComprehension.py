# dict comprehension

number_dict = {'first': 1, 'second': 2, 'third': 3}
new_dict = {key: value for key, value in number_dict.items()}

number_list = [1, 2, 3, 0, -5]
number_dict2 = {number: number**2 for number in number_list}
number_dict3 = {number: 'posotive' if number > 0
 else 'negative' if number < 0 else 'zero' for number in number_list}
print('number_dict3 ', number_dict3)

# Set comprehension

number_list = [1, 2, 3, 0, -5]
number_set = {number: number ** 2 for number in number_list}