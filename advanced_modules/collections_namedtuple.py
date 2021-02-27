from collections import namedtuple

jake = ('Jake', 'Smith', 19, 'male')
jim = ('Jim', 'Blade', 23, 'male')
jane = ('Jane', 'Morrison', 20, 'female')
print(jake[0]) # Jake

Person = namedtuple("Person", "name surname age gender")
jake = Person(name='Jake', surname='Smith', age=19, gender='male')
jane = Person(name='Jane', surname='Morrison', age=20, gender='female')
print(jake[0]) # Jake
print(jake.name) # Jake более читаемый вариант
jane = jane._replace(surname='Budaeva') # заменили фамилию