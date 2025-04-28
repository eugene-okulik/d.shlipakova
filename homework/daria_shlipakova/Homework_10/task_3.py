import operator


def count_for_me(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second != 0:
            operation = '/'
        else:
            print('Cannot divide by zero')
            return None
        return func(first, second, operation)
    return wrapper


@count_for_me
def calc(first, second, operation):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    return operations[operation](first, second)


while True:
    first_number = input('Enter first number: ')
    second_number = input('Enter second number: ')

    if first_number.lstrip('-').isdigit() and second_number.lstrip('-').isdigit():
        result = calc(int(first_number), int(second_number))

        if result is not None:
            print(result)
        break
    else:
        print('Enter digits')
