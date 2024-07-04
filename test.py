# # #check number is strong or not

# # number = int(input("enter a number"))
# # sum = 0
# # temp = number 
# # while temp > 0:
# #     fac =1 
# #     digit = temp%10 
# #     for i in range(1,digit+1):
# #         fac = fac*i
# #     sum =sum+fac
# #     temp//10


# # if sum == number:
# #     print("the number is strong ")
# # else: 
# #     print("the number is  not a strong number ")




# def Factorial(n):
#     if n==0:
#         return 1 
#         fac = 1
#     else:
#         fac =1
#         for i in range(1,n+1):
#             fac = fac * i
#     return fac

# print(Factorial(10))

sum = []

l =[[1,2,3],[3,4,5,6]]
l1= 0
for i in l:
    for j in i:
        l1 = l1 + j
    sum.append(l1)
      
print(sum)