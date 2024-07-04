#passing  a funtion as an argument

def square (a):
    return a**2

l = [1,2,3,4]
# print(list(map(square,l))) @ writing this inside a function

def my_map(func,l):
    list =[]
    for i in l:
        list.append(func(i))
    return list

print(my_map(square,l))
print(my_map(lambda a : a**3,l))

# function returning function:

def outer_func():
    def inner_func():
        print("this is inner func")
    return inner_func
v= outer_func()


# example:
def to_the_power(x): #x =3
    def cal_power(n): #n =2
        return n**x  #2**3
    return cal_power

cube = to_the_power(3)
four = to_the_power(4)
print(cube(5))
print(four(2))