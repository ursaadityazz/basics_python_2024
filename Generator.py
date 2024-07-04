#
# def num(n):
#     for i in range(1,n+1):
#         yield i  #to create generators we have to use yield keyword
#
# # print(num(10))  #this will return the location of generator
# #as after being used by the for loop nmbers from 1 to 10 has been deleted from the memory.
#
# n =num(10)
# for i in n:
#     print(i)
#
# for i in n:
#     print(i)  # this won't return anything as after its usage it has been deleted from the memory.
#
# print(n)
#
# exercise

def even_nums(n):
    for i in range(1,n+1):
        if i%2 ==0:
            yield i

n = even_nums(10)
for i in n:
    print(i)

