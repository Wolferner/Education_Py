from contextlib import contextmanager

def validator(type_):
    def real_decarotor(func):
        def inner (*args):
            for value in args:
                if not isinstance(value, type_):
                    raise ValueError(f'Dolzhen bitj {type_}')
            return func(*args)
        return inner
    return real_decarotor

@contextmanager
def check_con(*arg):
    funkcija = None
    try:
        funkcija = summa(*arg)
        print('Starting...')
        yield funkcija
    except:
        raise
    finally:
        if funkcija:
            print('Zakrito')

#@validator(int)
def summa(*args):
    return sum(args)


if __name__ == '__main__':

    #print(summa(5, 6))
    with check_con(5,6) as f:
        print(f)

