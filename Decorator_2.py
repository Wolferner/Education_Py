
def logger(func):
    def wrapper(a, b):
        print(f'{func.__name__} started')
        result = func(a, b)
        print(f'{func.__name__} Finished')
        return result
    return wrapper

@logger
def summa(a, b):
    return a + b


if __name__ == '__main__':

    # function = logger(summa)
    # print(function(2, 3))

    #print((logger(summa)(2, 3)))

    #summa = logger(summa)  # Это происходит, когда мы пользуемся Декоратором
    #print(summa(2, 3))  # Сдесь уже идет работа с переменной и враппером

    print(summa(2, 3))