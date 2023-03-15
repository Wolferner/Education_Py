
def typed(type_):
    def real_decorator(func):
        def inner(*args):
            for value in args:
                if not isinstance(value, type_):
                    raise ValueError(f'Value must be {type_}')
            return func(*args)
        return inner
    return real_decorator



@typed(int)
def calculate(*args):
    return sum(args)

@typed(str)
def stringer(a,b):
    return a+b


if __name__ == '__main__':

    #calculate = typed_int(calculate)

    print(calculate(1, 2, 3))
    print(stringer('maks','roma'))