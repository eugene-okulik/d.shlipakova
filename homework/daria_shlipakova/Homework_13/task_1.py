import os
import datetime

this_file = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(this_file))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(file_path, 'r') as file:
    for line in file:
        date_str = ' '.join(line.split()[1:3])
        text = ' '.join(line.split()[4:])
        python_date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
        if 'на неделю позже' in text:
            result = python_date + datetime.timedelta(days=7)
            print(result)
        elif 'день недели' in text:
            print(python_date.strftime('%A'))
        elif 'дней назад' in text:
            new_date = datetime.datetime.now() - python_date
            print(new_date.days, 'days')
