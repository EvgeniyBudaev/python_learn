import sqlite3

conn = sqlite3.connect("students_lite_db.db") # если нету, то создается

cursor = conn.cursor()
cursor.execute('''CREATE TABLE students 
                  (first_name TEXT, last_name TEXT, age INTEGER); ''')

insert_query = "INSERT INTO students VALUES ('Evgeniy', 'Budaev', 34);"                  

cursor.execute('''INSERT INTO students 
                  VALUES ('James', 'Brown', 21); ''')
cursor.execute(insert_query) 


first_name = 'Nikita'
last_name = 'Polyakov'
age  = 45
# плохое решение! SQL injection danger!
# insert_query = f"INSERT INTO students VALUES ('{first_name}', '{last_name}', {age});"

# этот подход более безопасен
insert_query = f"INSERT INTO students VALUES (?, ?, ?);"
cursor.execute(insert_query(first_name, last_name, age))


jane = ('Jane', 'Air', 18)
cursor.execute(insert_query, jane)


students = [
  ('Michail', 'Oreshkin', 20),
  ('Oleg', 'Proshka', 19),
  ('Olya', 'Morozova', 27)
]
# 1 способ
for student in students:
  cursor.execute(insert_query, student)
# 2 способ
cursor.executemany(insert_query, students)  


# Чтение, редактирование и удаление данных при помощи Python
cursor.execute("SELECT * FROM students WHERE first_name IS 'Oleg';")
# 1 спобоб чтения
for row in cursor:
  print(row)
# 2 способ чтения
print(cursor.fetchone()) # одна запись
print(cursor.fetchall()) # извлечь все записи 

# Редактирование
cursor.execute("UPDATE students SET age = 18 WHERE first_name IS 'Oleg';")
data = cursor.fetchall()
cursor.execute("SELECT * FROM students;")
[print(row) for row in data]

# Удаление
cursor.execute("DELEte FROM students WHEre last_name IS 'Morozova";)

conn.commit()                  
conn.close()