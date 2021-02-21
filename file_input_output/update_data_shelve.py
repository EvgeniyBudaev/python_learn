import shelve

monday_schedule = ['Math', 'English', 'System programming', 'Python']
tuesday_schedule = ['English', 'HTML', 'Python', 'Football']
wednesday_schedule = ['Phisics', 'English', 'Python']
thursday_schedule = ['Math', 'Chemistry', 'Java']
friday_schedule = ['Running', 'Math', 'Python']

# with shelve.open('schedules', writeback=True) as schedules: # writeback=True добавили для 2-го способа
with shelve.open('schedules') as schedules:
  schedules['monday_schedule'] = monday_schedule
  schedules['tuesday_schedule'] = tuesday_schedule
  schedules['wednesday_schedule'] = wednesday_schedule
  schedules['thursday_schedule'] = thursday_schedule
  schedules['friday_schedule'] = friday_schedule

  # добавление
  # schedules['tuesday_schedule'].append('Swimming') # добавляет в копию а не в файл
  # 1-способ добавления
  temp_list = schedules['tuesday_schedule']
  temp_list.append('Swimming')
  schedules['tuesday_schedule'] = temp_list
  # 2-способ добавления
  schedules['tuesday_schedule'].append('Geometry') # не лучший способ

  for key in schedules:
    print(key, schedules[key])  
