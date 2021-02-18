ДЗ-3: Парсинг сотрудника

Создать класс Employee, который принимает имя, фамилию и зарплату в качестве аргументов при конструировании.

Класс должен поддерживать:
атрибут first_name, возвращающий имя
атрибут last_name, возвращающий фамилию
атрибут salary, возвращающий зарплату
функцию from_string, которая принимает имя, фамилию и зарплату в формате 'first_name-last_name-salary', парсит строку и возвращает экземпляр Employee

Примеры
emp1 = Employee('Mary', 'Sue', 6000)
emp2 = Employee.from_string('John-Smith-55000')

emp1.first_name -> 'Mary'
emp1.salary -> 6000
emp2.first_name -> 'John'
emp2.salary -> 55000