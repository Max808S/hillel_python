from statistics import mean

students = (
    ('Max', 25, 'Odessa', 7.1),
    ('Ivan', 23, 'Kiev', 8.2),
    ('Danilo', 25, 'Mariupol', 5.1),
    ('Misha', 24, 'Kiev', 7.0),
    ('Anya', 21, 'Odessa', 6.7),
    ('Maria', 19, 'Moscow', 9.9),
    ('Oleg', 22, 'Lvov', 8.6),
)

rate_list = []

#  Добавил в новый список имена и оценки с заданого кортежа
for i in range(len(students)):
    rate_list.append(students[i][0::3])

#  Из списка в кортеж
rate_tuple = tuple(rate_list)
#  Из кортежа в словарь
rate_dict = dict((name, rate) for (name, rate) in rate_tuple)

print(f'Creating a dictionary with names and rate from tuple ({type(rate_dict)}): '
      f'\n{rate_dict}')

#  Средняя оценка
avg = mean(rate_dict[k] for k in rate_dict)
#  Получение учеников с оценкой выше среднего
final_dict = dict((name, rate) for name, rate in rate_dict.items() if rate >= avg)

print('Students', ', '.join(final_dict.keys()), 'are studying well this half year!')
