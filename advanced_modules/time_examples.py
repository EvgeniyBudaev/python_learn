import time

print(time.gmtime(0)) # 1970 год
print(time.gmtime()) # текущее время
print(time.localtime()) # местное локальное время, для каждой страны свое
print(time.time()) # количество секунд с 1970года

epoch_start_time = time.gmtime(0)
print("Year: ", epoch_start_time[0]) # Year:  1970
print("Year: ", epoch_start_time.tm_year) # Year:  1970
print("Day of week: ", epoch_start_time.tm_wday) # Day of week:  3

# 2 часть
print(time.ctime(time.time())) # Sat Feb 27 18:26:53 2021

print('Text before delay')
time.sleep(1.2)
print('Text after 1.2 seconds')

local_time = time.localtime(time.time())
print(local_time)
print(time.mktime(local_time)) # 1614439940.0
print(time.asctime(local_time)) # Sat Feb 27 18:32:59 2021
print(time.strftime('%X', local_time)) # 18:35:06
print(time.strftime('%x %X', local_time)) # 02/27/21 18:35:43
print(time.strftime('%m/%d/%Y, %H:%M:%S', local_time)) # 02/27/2021, 18:37:29

time_string = '21 December, 2020'
struct_time = time.strptime(time_string, '%d %B, %Y')
print(struct_time)

