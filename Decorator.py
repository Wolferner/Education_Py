
def validate(func):  # Чтобы не копировать код делают валидатор отдельно, Декоратор
    def wrapper(*args):
        for value in args:
            if type(value) not in (int, float):
                raise ValueError('Values should be int or float')
        return func(*args)
    return wrapper


@validate  # Применение Декоратора - Валидатора
def add_values(*args):
    return sum(args)


def sub_values(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):  # Валидатор
        raise ValueError('Values should be int or float')
    return a - b


if __name__ == '__main__':

    print(add_values(5, 3, 6, 7))
