import sys

sys.set_int_max_str_digits(30000)


def fibonacci_gen():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_num(n):
    fibonacci = fibonacci_gen()
    for _ in range(n - 1):
        next(fibonacci)
    print(f'Число на позиции {n}: {next(fibonacci)}')


fibonacci_num(5)
fibonacci_num(200)
fibonacci_num(1000)
fibonacci_num(100000)
