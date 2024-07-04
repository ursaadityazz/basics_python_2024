#
user_id = ('user1','user2')
names = ('aditya','ankita')

user_names = tuple(zip(user_id,names))
user_names2 = dict(zip(user_id,names))

# you can convert it into  a dictionary as well (make sure there should be euqal number of values in the interables.
print(user_names)
print(user_names2)


# we can also split a zip object in to 2 lists ex:
# l1 = [1,2,3,4,5]
# l2= [6,7,8,9,10]
#
# l = list(zip(l1,l2))
# print(l)
#
# l1 = [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
# # to split l1 we in  2 tuples we will use *
#
# new_list = list(zip(*l1))
# print(new_list)
# # if we want 2 separate lists we will use list unpacking
# l,l2 = new_list
# print(list(l))
# print(list(l2))

l1 = [1,2,3,4,5]
l2= [6,7,8,9,10]

#we will zip l1 and l2 and store the gretest one from the pair in to  a new_list
new_list = []
n = zip(l1,l2)
for pair in n:
    new_list.append(max(pair))

print(new_list)

# exercise :
# list =[1,2,3],[2,3,4],[4,5,6]

# def average (*args):
#     avg = []
#     for pair in zip(*args):
#         avg.append(sum(pair)/len(pair))
#     return avg
#
# print(average([1,2,3],[2,3,4],[4,5,6]))

average_finder = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder([1,2,3],[2,3,4],[4,5,6]))


