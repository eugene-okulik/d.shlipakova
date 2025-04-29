def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        final_result = []
        for _ in range(count):
            result = func(*args)
            final_result.append(result)
        return final_result
    return wrapper


def repeat_me_2(num):
    def repeat_me_2_dec(func):
        def wrapper(*args):
            final_result = []
            for _ in range(num):
                result = func(*args)
                final_result.append(result)
            return final_result
        return wrapper
    return repeat_me_2_dec


@repeat_me
def example(*args):
    print(*args)


example('print me', count=4)


@repeat_me_2(2)
def example3(*args):
    return sum(x * 2 for x in args if x > 5)


print(example3(2, 4, 6, 10))
