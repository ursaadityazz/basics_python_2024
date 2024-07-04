# print square of multiple numbers in a list
# def square (l):
#     square = []
#     for i in l:
#         square.append(i**2)
#     return square
#
# numbers = list(range(1,50))
# print(square(numbers))

#retuen the list in reverse order
# def reverse_list(l):
#     reverse = []
#     for i in range(len(l)):
#         pop_i = l .pop()
#         reverse.append(pop_i)
#     # return reverse[::-1]
#     return reverse
#
# numbers = list(["a","b","c","d"])
# print(reverse_list(numbers))

#return the elements of the list in reverse order
# def reverse_elements(l):
#     reverse = []
#     for i in l:
#         s = i[::-1]
#         reverse.append(s)
#     return reverse
#
# items = list(['abc','xyz','pqr'])
# print(reverse_elements(items))


#filter odd even
# def Odd_Even (l):
#     filtered = []
#     odd = []
#     even = []
#     for i in l:
#         if i%2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     filtered = [even,odd]
#     return filtered
#
# numbers  = list (range(2,10))
# print(Odd_Even(numbers))


#find common between 2 lists
# def common(i,j):
#     common_num = []
#     for x in i:
#         if x in j:
#             common_num.append(x)
#     return common_num
#
# numbers1= list([1,2,3,4])
# numbers2= list([5,2,3,4,7])
# print(common(numbers1,numbers2))

#how many lists present inside the list

def list1(l):
    count = 0
    for i in l:
        if type(i) == list :
            count +=1
    return count

num = list([1,2,3,[4,5],[6,7]])
print(list1(num))



