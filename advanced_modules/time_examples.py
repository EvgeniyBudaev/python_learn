import time

print(time.gmtime(0)) # 1970 год
print(time.gmtime()) # текущее время
print(time.localtime()) # местное локальное время, для каждой страны свое
print(time.time()) # количество секунд с 1970года

epoch_start_time = time.gmtime(0)
print("Year: ", epoch_start_time[0]) # Year:  1970
print("Year: ", epoch_start_time.tm_year) # Year:  1970
print("Day of week: ", epoch_start_time.tm_wday) # Day of week:  3