age = 34
print('Jack is ' + str(34) + ' years old.')

name = 'Jack'
age = 34
name_and_age = "My name is {0}. I'm {1} years old.".format(name, age)
name_and_age = "My name is {}. I'm {} years old.".format(name, age)
name_and_age = "My name is {name}. I'm {age} years old.".format(name = 'Alisa', age = '20')
print(name_and_age)
name_and_age = f"My name is {name}. I'm {age} years old."
print('Версия python 3.6: ', name_and_age)

float_result = 1000 / 7
print('float_result: ', float_result)
print('The result is {0:1.3f}'.format(float_result))


print('''
 {0:15.4f} {1:15.4f} {2:15.4f} {3:15.4f} 
 {4:15.4f} {5:15.4f} {6:15.4f} {7:15.4f}
'''.format(34.2344, 1234.23,1.45778, 345.232352,
           1.45778, 345.232352, 34.2344, 1234.23))