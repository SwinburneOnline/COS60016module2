def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def my_decorator(func):
    def wrapper_function(*args):
        print("{0} is called with parameters {1}".format(func.__name__, args))
        return func(*args)

    return wrapper_function


@my_decorator
def add(x, y):
    return x + y


@my_decorator
def sub(x, y):
    return x - y


@my_decorator
def mul(x, y):
    return x * y

