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

INSERT INTO students(first_name, last_name, age) VALUES ("Jack", "White", "18");

INSERT INTO employees(first_name, last_name, age) VALUES ("Jacne", "Black", "20");

SELECT * FROM students;
SELECT * FROM employees;

DROP TABLE table_name; 