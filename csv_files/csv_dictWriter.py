import csv

with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/students_writer.csv', 'w') as file:
  header_list = ['First name', 'Last name', 'age']
  csv_writer = csv.DictWriter(file, fieldnames=header_list)
  csv_writer.writeheader()
  csv_writer.writerow({
    'First name': 'Jack', 
    'Last name': 'White', 
    'age': 24
    })
  csv_writer.writerow({
    'First name': 'Evgeniy', 
    'Last name': 'Budaev',
     'age': 34
     })

# ===
# чтение
with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/cars.csv') as file:
  csv_reader = csv.DictReader(file)  
  car_list = list(csv_reader)

# запись
with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/cars_dict_writer.csv', 'w') as file: 
  headers_list = ['Make', 'Model']
  csv_writer = csv.DictWriter(file, fieldnames=headers_list)
  csv_writer.writeheader()
  for car in car_list:
    csv_writer.writerow({
      'Make': car['Make'],
      'Model': car['Model']
    })    