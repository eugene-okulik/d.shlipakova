def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)
        return [func(*args, **kwargs) for _ in range(count)]
    return wrapper


def repeat_me_2(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(num)]
        return wrapper
    return decorator


@repeat_me
def example(*args):
    print(*args)


example('print me', count=4)


@repeat_me_2(2)
def example3(*args, **kwargs):
    return args, kwargs


print(example3(1, 3, 4, kwarg=5))
