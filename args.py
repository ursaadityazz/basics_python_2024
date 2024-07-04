# #make flexible operator
# # *operator
#
# def total(a,b):
#     return a +b
#
# total(2,3)  #HERE WE CAN PASS ONLY 2 ARGUMENTS
#
# # IF WE WANT TO PASS MULTPLE ARGS IN A FUNCTION WE HAVE TO USE * OPERATOR:
#
# def all_total(*nums):
#     total = 0
#     for i in nums:
#         total+= i
#     return total
#
# print(all_total(2,3,4,5,6))
# #it will take the numbers  in args as a TUPLE
#
# #args with normal parameter :
# def multiply(num , *args):
#     print(args)
#     multplied = 1
#     for i in args:
#         multplied *= i
#     return multplied
#
# # print(multiply(2,3,4,5,6)) #here 2 won't be the part of the args as we have passed 'num' as a parameter in the function
#         # so it will return the multipication of the rest of the values.
#
# #NOTE : When we pass *args with normal parameters then *args should be passed at the end paramter
# # i,e : def multiply(num , *args):  not like def multiply( *args,num ): as the value of the num will be occupied in the *args tuple.
#
#
# #args as argument :
#
#
# arr = [12,34,5,6]
# print(all_total(*arr)) # when we pass list as args then we have to use * before the list to unpack the values.


def power(num,*args):
    if len(args) == 0:
        return "args is empty"
    else :
        power = [i**num for i in args]
        return power

list1 = []
# list1 = [1,2,3,4]
print(power(2,*list1))


