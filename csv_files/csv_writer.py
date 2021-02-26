import csv

with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/students.csv', 'w') as file:
  csv_writer = csv.writer(file)
  csv_writer.writerow(['First name', 'Last name', 'age'])
  csv_writer.writerow(['Jack', 'White', 24])
  csv_writer.writerow(['Evgeniy', 'Budaev', 34])


# === Прочитали из файла cars.csv и записали выборку в другой файл cars_make_model.csv
with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/cars.csv') as file:
  csv_reader = csv.reader(file)
  next(csv_reader)
  make_model_list = []
  for car in csv_reader:
    make_model = [car[1], car[2]]
    make_model_list.append(make_model)
  print(make_model_list) 


with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/cars_make_model.csv', 'w') as file: 
  csv_writer_cars = csv.writer(file)  
  for row in make_model_list:
    csv_writer_cars.writerow(row)


# тоже самое через вложенность
with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/cars.csv') as file:
  csv_reader = csv.reader(file)
  next(csv_reader)

  with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/cars_make_model.csv', 'w') as file: 
    csv_writer_cars = csv.writer(file)  
    for row in csv_reader:
      csv_writer_cars.writerow([row[1], row[2]])