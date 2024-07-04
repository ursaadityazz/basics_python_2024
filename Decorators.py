#decorator : it is used to enhance the functionality of a funcrtion

# ex:
from functools import wraps
def decorator_func(func):
    @wraps(func)
    def inside_func(*args,**kwargs):
        '''this is wrapper func'''
        print("this is a awesome func")
        return func(*args,**kwargs)
    return inside_func

#this is an awesome func
def func1():
    print("this is func 1")

f = decorator_func(func1)
f()

#you can write decorator functions by '@'

@decorator_func
def func2(a,b):
    '''this is a add function'''
    return a+b

print(func2(1,2))
print(func2.__doc__)

# '''if we want to give doc string in func2  then its shoowing the wrapper function docstring'''
# to fix the issue we will import @wraps from functools and call it before wrapper function , this will show the proper docstring


#exercise

def print_function_data(func):
    @wraps(func)
    def wrapper_func(*args,**kwargs):
        print(f"you are calling {func.__name__} function")
        print(f"{func.__doc__}")
        return func(*args,**kwargs)
    return wrapper_func


@print_function_data
def add(a,b):
    '''this function adds 2 numbers and returns their sum'''
    return a+b

@print_function_data
def subtract(a,b):
    '''this function subtarcts 2 numbers and returns their value'''
    return a-b


print(add(4,5))
print(subtract(4,5))




