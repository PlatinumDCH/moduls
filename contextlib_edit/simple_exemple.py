import contextlib

# @contextlib.contextmanager
# def meaning_resourse():
#     print('Setting up tp the resourse')
#     yield
#     print('Cleaning up the resourse')

# with meaning_resourse():
#     print('Doing something')


class meaning_resourse(contextlib.contextmanager):
    def __enter__(self):
        print('setting up the resourse')
    
    def __exit__(self, *exc):
        print('cleatning up the resourse')

@meaning_resourse()
def doing_something():
    print('doing something')

doing_something()