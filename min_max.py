
names = ['adirtya', 'ankita','biswaj']

# def length(items):
#     return len(items)
# print(max(names , key = length))
#this is toom lengthy lets try using lambda fuction:
print(max(names , key = lambda item : len(item)))

students = [
     {'name' : 'aditya','score' : 78} ,
     {'name' : 'ankita','score' : 79} ,
     {'name': 'ram', 'score': 98}
 ]

print(max(students , key = lambda item : item.get('score'))['name'])



