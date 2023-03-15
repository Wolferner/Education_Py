squares = (e*e for e in range(0,11,2))


def squares_2():
    print("Genertor working...")
    for e in range(0,11,2):
        yield e*e  # По этому интерпритатор понимает что это генератор


def pause():
    print('Working...')
    while True:  # Бесконечный цикл
        print(a)
        yield a  # После применения он останавливается здесь - пауза


a = 10
if __name__ == '__main__':

    gen_3 = pause()
    print(gen_3)
    print(next(gen_3))

    gen = squares_2()
    gen_2 = squares_2()

    print(gen)
    for i in gen:
        print(i)

    print('------------------------')

    print(gen_2)
    for i in gen_2:
        print(i)
