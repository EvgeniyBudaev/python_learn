import csv

with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/cars.csv') as file:
  csv_reader = csv.reader(file)
  next(csv_reader) # чтобы не было заголовков таблицы
  for car in csv_reader:
    # print(car) # построчно списки
    print(f'{car[1]} {car[2]} costs {car[4]}') # строки

# ===
# with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/cars.csv') as file:
#   csv_reader = csv.reader(file)
#   data_list = list(csv_reader)
#   for car in csv_reader:
#     print(data_list)


# === ;
with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/cars_EU.csv') as file:
  csv_reader = csv.reader(file, delimiter=";")
  next(csv_reader)
  for car in csv_reader:
    # print(car) # построчно словари
    print(f'{car[1]} {car[2]} is {car[3]}') # строки


    