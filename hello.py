# a = 1
# b = 2
#
# # a,b,c = 1,2,3
# a=b=c =1
# print (a,b,c)
#
#
# a= 4
# A= "Sally"
# print(a)
# print(A)
#
# x= "pyhton is awesome"
# print (x)
#
# p = "Python "
# q = "is "
# r = "Awesome"
# print(p,q,r)
# print(p+q+r)
#
# # print (b+p) it wont work
# # TypeError: unsupported operand type(s) for +: 'int' and 'str'
#
#
# # q= " awesome"
# def myfunc():
#     global q
#     q = " Cute"
#     print("python is" +q)
#
# myfunc()
# print("python is" + q)
# e= -9j
#
# print (type(e))
#
#
# import random
# print (random.randrange(1,10))
#
# c= "lorem ipsum"
#
# t = "Helo world"
# if "x" not in t :
#     print ("no its not there")
# else :
#     print("no its there")
# # print(t[5:10])
#
# # for y in t:
# #     print("w" in t)
#
#
#
# v = "{172900}"
# print (v[-4:-1])
#
# print("He is called \"Johnny\"")
#
#
# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

#
# thislist = ["apple", "banana", "cherry"]
# thislist.append("cherry")
# print(thislist)

#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


 #insert method adds one elemt to the list
 #extend adds one iterable (list tuple, dict) to the list


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
a =[]
# for x in fruits:
#     if 'n' in x:
#         print("n is there")
#         a.append(x)
a = [x for x in fruits if 'n' in x ]
print(a)

y = [y for y in range(10)]
print(y)


# thislist = [100, 50, 65, 82, 23]
# # thislist.sort(reverse=True)
# thislist.reverse()
# print (len(thislist))\

w = (10,"ram",40,70)
v = list(w)
v[1] = '20'
w = tuple(v)
print(w)



#in sets  ADD method adds the elements
#in sets upaate method adds the iterables
#to remove any element from sets we will use discard() method
#to remove any random element we will use POP() method.
#to clear the sets we will use clear() method.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
#to methods to join the sets
# set3 = set1 | set2
set3 = set1.union(set2)
print(set3)










