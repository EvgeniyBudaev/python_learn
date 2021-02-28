from datetime import date

today = date.today()
print(today) # 2021-02-28
print(today.year) # 2021
print(today.month) # 2
print(today.day) # 28

date_1 = date(2021, 2, 28)
date_2 = date(2020, 2, 28)
diff = date_1 - date_2
print(diff) # 366 days, 0:00:00


# расчет кол-ва дней до дня рождения
current_day = date.today()
my_birthday = date(current_day.year, 11, 17)
if my_birthday < today:
  my_birthday = my_birthday.replace(year=today.year + 1) # replace заменяет
print('my_birthday: ', my_birthday) # 2021-11-17
days_until_birthday = my_birthday - today
print('You will clebrate your birthday in', days_until_birthday.days, ' days') 
# You will clebrate your birthday in 262  days


today = date.today()
week_day = today.weekday()
print('week_day ', week_day) # 6
week_day = today.isoweekday()
print('week_day: ', week_day) # 7
