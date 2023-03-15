


def names():
    all_names = []

    def inner(name:str) -> list:
        all_names.append(name)
        return all_names

    return inner

if __name__ == '__main__':

    students =  names()
    print(students('Vasja'))
    print(students('Oleg'))
    print(students('Nikita'))