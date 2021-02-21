def to_inches(cm):
  return cm * 0.393701

def to_miles(km):
  return km*0.621371

def to_fahrenheit(celsius):
  return (celsius*9/5)+32 

if __name__=='__main__':
  print('Call a converting func that you want') # эта ветка выполниться если скрипт был запущен напрямую без импорта файла 
else:  
  print('Was imported (not executed directly)') # эта ветка выполниться если наш файл был заимпортирован