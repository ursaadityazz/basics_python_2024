#we use enumerate function to track the postition of items in iterables
# ex without enumerate function
names = ['ad','ankita','anie']
# pos = 0
# for i in names :
#     print(f"{pos} : {i}")
#     pos+=1

# ex with enumerate function
for pos,i in enumerate(names):
   print(f"{pos} : {i}")

def name (l,target):
    for pos, i in enumerate(l):
        if i == target:
            return pos
    return -1

print(name(names,'anie'))

