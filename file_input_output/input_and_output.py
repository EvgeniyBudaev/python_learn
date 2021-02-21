# input('Input something') # ввод
# print('Output something') # вывод

# Чтение файла

lorem_ipsum_text = open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/file_input_output/sample.txt', 'r') # r можно не указывать. По умолчанию 'чтение'

for line in lorem_ipsum_text:
  print(line, end='')

lorem_ipsum_text.close()

# с условием выводим только те строки где есть слово mary
lorem_ipsum_text2 = open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/file_input_output/sample.txt', 'r')

for line in lorem_ipsum_text2:
  if 'mary' in line.lower():
    print(line, end='')

lorem_ipsum_text2.close()

# оператор with - не нужно уже закрывать файл
with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/file_input_output/sample.txt', 'r') as lorem_ipsum_text3:
  for line in lorem_ipsum_text3:
    if 'mary' in line.lower():
      print(line, end='')

# readline() читает одну строку
with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/file_input_output/sample.txt', 'r') as lorem_ipsum_text4:
  line = lorem_ipsum_text4.readline()
  while line:
    print(line, end='')
    line = lorem_ipsum_text4.readline()

# readlines() читает все строки. Читает содержимое всего файла и помещает в список
with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/file_input_output/sample.txt', 'r') as lorem_ipsum_text5:
  lines = lorem_ipsum_text5.readlines()
print(lines)

for line in lines[::-1]: # ::-1 распечатать в обратном порядке
  print(line, end='')

# read - читает весь файл и весь файл помещается в одну строку
with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/file_input_output/sample.txt', 'r') as lorem_ipsum_text6: 
  lines = lorem_ipsum_text6.read() 

# read() и readlines() не использовать для больших файлов. 
# Для больших файлов лучше использовать readline(), чтобы не перезагружать память компьютера


