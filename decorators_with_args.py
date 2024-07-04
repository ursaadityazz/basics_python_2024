from functools import wraps


def only_int_allow(func):
    @wraps(func)
    def wrapper_func(*args,**kwargs):
        data_type =[type(arg)==int for arg in args]
        if all(data_type):
            print(func.__doc__)
            return func(*args,**kwargs)
        else:
             return "invalid arguments"
    return wrapper_func


@only_int_allow
def add_all(*args):
    '''this func will return the sum of all numbers'''
    total = 0
    for i in args:
        total+=i
    return total

print(add_all(1,2,3))

#if we have to do operations on multple data types then we have create multple decorators, that will be lengthy so to minmize the length we will use
# decorators with arguments
def only_data_type_allow(data_type):
    def decorator(func):
        @wraps(func)
        def wrapper_func( *args, **kwargs):
            data_types =[type(arg)== data_type for arg in args]
            if all(data_types):
                print(func.__doc__)
                return func(*args,**kwargs)
            else:
                 return "invalid arguments"
        return wrapper_func
    return decorator

only_data_type_allow(str)
def str_join(*args):
    str = ''
    for arg in args:
        str = str+arg
    return str

@only_data_type_allow(dict)
def dict_keys(**kwargs):
    new_dict = {k for k in kwargs.keys()}
    return new_dict

print(str_join('aditya ', '+ ankita'))
print(dict_keys(first_name='aditya',last_name = 'kumar',age = '26'))


