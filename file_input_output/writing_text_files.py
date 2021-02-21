# Запись в файл
colors_list = ['red', 'orange', 'yellow', 'green', 'blue']

with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/file_input_output/rainbow_colors.txt', 'w') as rainbow_colors: # w - запись. Если файла не было, то он создается 
  for color in colors_list:
    print(color, file=rainbow_colors)


# Прочитаем информацию у созданного файла
# color_list = [] 
# with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/file_input_output/rainbow_colors.txt', 'r') as rainbow_colors:
#   for color in rainbow_colors:
#     color_list.append(color.strip('\n')) # strip() - обрезает символы

# print(color_list) # ['red', 'orange', 'yellow', 'green', 'blue']


# Добавить в файл
with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/file_input_output/rainbow_colors.txt', 'a') as rainbow_colors:
  print('dark green', file=rainbow_colors)