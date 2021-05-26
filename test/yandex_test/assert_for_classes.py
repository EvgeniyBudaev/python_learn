class Contact:
    def __init__(self, name, year_birth, is_programmer):
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer

    def age_define(self):
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self):
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self):
        return(f'{self.name}, '               
               f'категория: {self.age_define()}, '
               f'статус: {self.programmer_define()}')

    def print_contact(self):
        print(self.show_contact())


mike: Contact = Contact('Михаил Булгаков', 1891, False)

expected_string = 'Михаил Булгаков, категория: Старейшина, статус: Нормальный'

assert mike.show_contact() == expected_string, 'Ошибка в Contact.show_contact()'


#  Задача

test_old_none_programmer = Contact('Пушкин', 1799, False)
expected_programmer_define = 'Нормальный'
print(test_old_none_programmer.programmer_define())
assert test_old_none_programmer.programmer_define() == expected_programmer_define, 'Ошибка в Contact.programmer_define()'

test_old_none_programmer2 = Contact('Пушкин', 1799, True)
expected_programmer_define = 'Программист'
assert test_old_none_programmer2.programmer_define() == expected_programmer_define, 'Ошибка в Contact.programmer_define()'

test_on_age = Contact('Пушкин', 1799, True)
expected_age_define = 'Старейшина'
assert test_on_age.age_define() == expected_age_define, 'Ошибка в Contact.age_define()'

test_on_age2 = Contact('Пушкин', 1965, True)
expected_age_define = 'Олдскул'
assert test_on_age2.age_define() == expected_age_define, 'Ошибка в Contact.age_define()'

test_on_age3 = Contact('Пушкин', 1986, True)
expected_age_define = 'Молодой'
assert test_on_age3.age_define() == expected_age_define, 'Ошибка в Contact.age_define()'

