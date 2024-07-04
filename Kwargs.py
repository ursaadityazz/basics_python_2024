# # **kwargs : keyword arguments
# def func (**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k} : {v}")
#
# # func(name = 'aditya',name2= 'ankita')
# #kwargs take the paramter as dictionary input
#
# f = {'name' : 'aditya','name2': 'ankita'}  #passing dict as an argument
# func(**f) #use ** to unpack the argummet

#parameters order to define in a function:
# order
# 1.normal parameter
# 2.*args
# 3. default parameter
# 4.**kwargs
#
# def func(name,*args,age ='25',**kwargs):
#     print(name)
#     print(args)
#     print(age)
#     print(kwargs)
#
# func('ad',1,2,3,4,a=1,b=2)


def func(l ,**kwargs):
    if kwargs.get('reverse') == True:   #get() is used to get the keys of the dict.
        list = [i[::-1].title() for i in l] #title() method will capitalize the first letter of the string.
        print(list)
    else :
        list = [i.title() for i in l]
        print(list)

l = ['aditya','ankita',]
func(l , reverse=True)


