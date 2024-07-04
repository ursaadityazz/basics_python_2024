import time
from functools import wraps


# returning the time taken to execute the function
def calculate_time(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        t1 = time.time()
        print(f"executing {func.__name__}")
        res = func(*args, **kwargs)
        t2 = time.time()
        t = t2 - t1
        print(f"this function took {t}s of time")
        print(f"{func.__doc__}")
        return res

    return wrapper_func


@calculate_time
def func(a):
    '''this is a square function'''
    return a ** 5


print(func(1000909))

