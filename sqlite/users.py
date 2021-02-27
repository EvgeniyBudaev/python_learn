import sqlite3
conn = sqlite3.connect("users.db")

# create_query = "CREATE TABLE users (user_name TEXT, USER_password TEXT);"

users = [
  ('jack123', 'root'),
  ('jane123', 'adm')
]

insert_query = "INSERT INTO users VALUES (?, ?);"
user_name = input('Input your username')
user_password = input('Input your password')

select_query = f"SELECT 8 from users WHERE user_name = ? AND user_password = ?"

cursor = conn.cursor()
# cursor.execute(create_query) # при создании таблицы
# cursor.executemany(insert_query, users)
cursor.execute(select_query, (user_name, user_password))
data = cursor.fetchone()
if (data):
  print("You are loggeed in!")
else:
  print("Please try again!")  

conn.commit()
conn.close()