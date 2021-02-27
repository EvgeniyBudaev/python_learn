import sqlite3

conn = sqlite3.connect("students_lite_db.db") # если нету, то создается

cursor = conn.cursor()
cursor.execute('''CREATE TABLE students 
                  (first_name TEXT, last_name TEXT, age INTEGER) ''')

conn.commit()                  

conn.close()