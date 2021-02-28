from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import locale

d1 = date(2021, 2, 28)
print(d1)
print(d1.year)
print(d1.month)
print(d1.day)

t1 = time(23, 10, 59)
print(t1) # 23:10:59
print(t1.hour) # 23
print(t1.minute) # 10
print(t1.second) # 59

print(date.today()) # 2021-02-28

now = datetime.now()
print(now) # 2021-02-28 18:51:13.682646
print(now.year) # 2021

dt1 = datetime.strptime("30/08/2018", "%d/%m/%Y")
dt2 = datetime.strptime("29/03/2018 10:40", "%d/%m/%Y %H:%M")
print(dt1) # 2018-08-30 00:00:00
print(dt2) # 2018-03-29 10:40:00

print(now.strftime('%Y-%m-%d (%a)')) # 2021-02-28 (Sun)
locale.setlocale(locale.LC_ALL, "")
