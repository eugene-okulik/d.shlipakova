def finish_me(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('finished')
        return result
    return wrapper


@finish_me
def example(*args, **kwargs):
    if args:
        print(*args)
    else:
        print(kwargs)


example('print me')
example('one', 'two', 'three')
example(One=1)
