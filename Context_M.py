
class DBConection:

    def __enter__(self):
        print('Conecting ...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Disconecting . . .')

if __name__ == '__main__':

    with DBConection() as conn:
        print('selecting...')