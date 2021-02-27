CREATE TABLE students (
  first_name TEXT,
  last_name TEXT,
  age INTEGER
);

CREATE TABLE employees (
  first_name TEXT,
  last_name TEXT,
  age INTEGER
);

-- Create
INSERT INTO students(first_name, last_name, age) VALUES ("Jack", "White", "18");
INSERT INTO employees(first_name, last_name, age) VALUES ("Jane", "Black", "20");

-- Read
SELECT * FROM students;
SELECT first_name FROM students;
SELECT * FROM employees;
SELECT first_name FROM students WHERE first_name = "Jack";
SELECT first_name FROM students WHERE first_name IS "Jack";
SELECT last_name FROM students WHERE last_name IS NOT "White";
SELECT last_name, age FROM students WHERE last_name IS NOT "White" AND age IS NOT 17;
SELECT last_name, age FROM students WHERE age < 18;
SELECT first_name FROM students WHERE first_name LIKE "Ja%";
SELECT * FROM students WHERE first_name LIKE "%ck" OR last_name LIKE "%ck";
SELECT * FROM students WHERE first_name LIKE "%an%"

-- Delete
DROP TABLE table_name; 