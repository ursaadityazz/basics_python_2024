
num = [1,2,3,4,5]

def square(a):
    return a**2
# print(square(num))

a = list(map(square,num))  #in map () 1st argument will be the function name and 2nd will be the iterables
print(a)

b = list(map(lambda a:a**3 , num))
print(b)

names = ['aditya','ankitaa']
# c = list(map(lambda names:len(names),names))
c  = map(len,names)
print(c)

for i in c:
    print(i)
for i in c:
    print(i)
    #we can iterate map object only once
    # but if we convert the object to list or tuple we can iterate multiple times :
d = list(map(len,names))


