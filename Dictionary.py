# nums =  tuple (range(2,30))
# nums = str(nums)
# print(nums)

# user = { 'name': 'Adi' , 'age': 25}
user =  dict(name = "aditya", age = 26)
print(user['name'])

# inserting data into the dict
user_info = {}
user_info['name'] = 'Adi'
user_info['name2'] = 'ankita'
print(user_info)

#check if the key is present in dict
if 'name' in user_info:
    print ("present")
else:
    print ("not present")

#check if the value is present in dict
if 'ankita' in user_info.values():
    print ("present")
else:
    print ("not present")

# looping through the dict
for i in user_info.items():
    print(i)
    print(type(i))

for key,value in user_info.items():
    print(f"key is {key} and value is {value}")

more_info = {'hobbies':'coding'}
user_info.update(more_info)
print(user_info)

# fromkeys :
# when you want to insert same value to all the keys from the dict we will use fromkeys() method
a ={}
a = dict.fromkeys(['a','b'],'Adi')
print(a)

# get () method:
# when we try to access a value from the dict using its key but thayt key is not present in the dict so it will throw error
#  to handle that error we will use get() method

print(a['a']) #it wll print 'Adi
print(a.get('ac')) #this will print None
print(a.get('ac' , 'this key is not there ')) # if we want to print somehing else other than 'None'

# find cube of all numbers up to any given number in Key value format
# def cube_finder(n):
#     cube = {}
#     for i in range (1,n+1):
#         cube[i] = i**3
#     return cube
#
# num = int(input("enter a number : "))
# print(cube_finder(num))


# word counter:
# def word_counter(s):
#     count = {}
#     for char in s:
#         count[char] = s.count(char)
#     return count
#
# print(word_counter("adityat"))


# Take users input and store it in a dictionary .

users = {}
name = input ("Enter your name : ")
age = input ("Enter your age : ")
mob = int(input ("Enter your mob : "))
hobbies = input("Enter your hobbies separated by ',' : ").split(',')


users['name'] = name
users['age'] = age
users['mob'] = mob
users['hobbies'] = hobbies

print(users)
