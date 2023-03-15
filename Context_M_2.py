from contextlib import contextmanager
class Resource:
    def __init__(self):
        self.opened = False

    def __del__(self):
        if self.opened:
            print('Memory leak detected!')

    def open(self, *args):
        print(f'Resource is opened! {args}')
        self.opened = True

    def action(self):
        print('Working...')

    def close(self):
        print('Closing ...')
        self.opened = False

@contextmanager
def open_resource(*args):
    resource =None
    try:
        resource = Resource()
        resource.open(args)  # Надо открыть и передать значения в open
        yield resource
    except:
        raise
    finally:
        if resource:
            resource.close()

class ResourceWorker():
    def __init__(self, *args):
        self.args = args
        self.resource = None

    def __enter__(self):
        self.resource = Resource()
        self.resource.open(*self.args)
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resource:
            self.resource.close()

if __name__ == '__main__':
    with open_resource(1, 2 ,3) as res:
        res.action()

    with ResourceWorker(4, 5, 6) as res_2:
        res_2.action()
