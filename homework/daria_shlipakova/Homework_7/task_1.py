import random

magic_number = random.randint(1, 20)
attempts = 0

while attempts < 5:
    client_number = input('Угадайте число от 1 до 20: ')
    if client_number.isnumeric() and 0 < int(client_number) < 21:
        attempts += 1
        if int(client_number) == magic_number:
            print('Поздравляю! Вы угадали!')
            break
        elif attempts < 5:
            print('Попробуйте снова')
        else:
            print('Вы проиграли')
    else:
        print('Введите число от 1 до 20')
