from requests import get
number_courses = input('number courses = ')
time_study = input('time study = ')
print(get(f'http://127.0.0.1:5000/api1', json={'number_courses': number_courses, 'time_study': time_study}).json())
