# # def odd_even(num1):
# #     return num1 % 2 == 0
# #
# # print(odd_even(80))
# #
#
#
# def greater_num(num1, num2):
#     if num1 < num2:
#         return "num2 is greater"
#     else:
#         return "num1 is greater"
#
# a = int(input("enter 1st num : "))
# b = int(input("enter 2nd num : "))
#
# print(greater_num(a,b))
#

# def is_pallindrome(str):
#     if str == str[::-1]:
#         return "This is a pallindrome"
#     else :
#         return "its not"
#
# print(is_pallindrome(str(input("Enter the word : "))))

# def Febonacci (num):
#     a= 0
#     j = 2
#     total = 0 #1
#     for i in range(i,num-2):
#         total = i+j
#         i = total
#         j = i + total
#         return j
#
# print(Febonacci(22))

def func(a,b):
    '''this function takes 2 argument as input '''
    return a+b

# print(func.__doc__) #to show the docstring of the function
# print(len.__doc__)
# print(sum.__doc__)