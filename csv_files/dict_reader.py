import csv

with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/cars.csv') as file:
  csv_reader = csv.DictReader(file)
  for car in csv_reader:
    # print(car) # построчно словари
    print(f'{car["Make"]} {car["Model"]} costs {car["Price"]}') # строки

# === ;
with open('/Users/evgeniybudaev/Documents/CODE/PYTHON/Ilia Fofanov/python_learn/csv_files/cars_EU.csv') as file:
  csv_reader = csv.DictReader(file, delimiter=";")
  for car in csv_reader:
    # print(car) # построчно словари
    print(f'{car["Make"]} {car["Model"]} is {car["Price"]}') # строки