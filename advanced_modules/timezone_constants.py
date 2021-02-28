import time

print('UTC time: ' + time.strftime('%Y/%m/%d %H:%M:%S', time.gmtime()))
# UTC time: 2021/02/28 04:37:00
print('Local time: ' + time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
# Local time: 2021/02/28 07:37:00


print(time.altzone/60/60) # deprecated -3.0
print(time.daylight) # deprecated 1
print(time.timezone/60/60) # deprecated -3.0
print(time.tzname) # ('MSK', 'MSK')  второй параметр нужно проверять на наличие
print(time.tzname[0]) # MSK
if time.daylight != 0:
  print(time.tzname[1])

# лучше использовать
print(time.localtime().tm_zone)
print(time.localtime().tm_gmtoff) # 10800   