import random

def decorator(fn):
    def wrapped():
        try:
            return fn()
        except Exception as a:
            print("Error:", a)
    return wrapped

@decorator
def my_func():
    while True:
        if random.randint(0, 5) == 0:
            raise Exception('Random!')
        print('Ok')


my_func()