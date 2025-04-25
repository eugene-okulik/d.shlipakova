import random

bonus = bool(random.getrandbits(1))
money = random.randint(1000, 2000)

while True:
    salary = input('Введите зарплату: ')
    if salary.isdigit() and int(salary) > 0:
        result = int(salary) + money if bonus else int(salary)
        print(f'{salary}, {bonus} - ${result}')
        break
    else:
        print('Введите число больше 0')
