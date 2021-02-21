import shelve

university = shelve.open('university_file')

university['schedules'] = {
    'monday_schedule': ['Math', 'English', 'System programming', 'Python'],
    'tuesday_schedule': ['English', 'HTML', 'Python', 'Football'],
    'wednesday_schedule': ['Phisics', 'English', 'Python'],
    'thursday_schedule': ['Math', 'Chemistry', 'Java'],
    'friday_schedule': ['Running', 'Math', 'Python']
}

university['tutors']: {
  "Math": ['Jack White', 'Jim Black'],
  "Python": ['YouRa Allakhverdov', 'Jane Smith']
}

print(university['schedules']['wednesday_schedule']) # ['Phisics', 'English', 'Python']

university.close()

# university = {
#   'schedules': {
#     'monday_schedule': ['Math', 'English', 'System programming', 'Python'],
#     'tuesday_schedule': ['English', 'HTML', 'Python', 'Football'],
#     'wednesday_schedule': ['Phisics', 'English', 'Python'],
#     'thursday_schedule': ['Math', 'Chemistry', 'Java'],
#     'friday_schedule': ['Running', 'Math', 'Python']
#   },
#   'tutors': {
#     "Math": ['Jack White', 'Jim Black'],
#     "Python": ['YouRa Allakhverdov', 'Jane Smith']
#   }
# }

# print(university['schedules']['wednesday_schedule'])

