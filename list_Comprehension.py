#with the help of list comprehension we can create the list in one line:

square = []

for  i in range (1,11):
    square.append(i**2)
print(square)

#using list comprehension:

square2 = [i**2 for i in range(1,11)]
print(square2)

#append the 1st letter of the names in the list using LC :

l1 = ['aditya', 'ankita','swalli']
l2 = [i[0]for i in l1 ]
print(l2)

#reverse the string using Lc :

LIST1 = ['abc','pqr','xyz','mno']
reversed_list = [name[::-1] for name in LIST1]
print(reversed_list)

#lc using if else :
n = list(range (1,11))
even_num = [i for i in n if i%2 ==0]
odd_num = [i for i in n if i%2 !=0]
print(even_num)
print(odd_num)



def str_list(l):
    str_list1 = []
    for i in l:
        if type(i) == int  or type(i) == float:
            str_list1.append(str(i))
    return str_list1

data_list = [True , False , 1,1.0,4]
print(str_list(data_list))

# usinfg LC:

def new_list(l):
    str_list = [str(i) for i in l if type(i)== int or type(i) == float]
    return str_list

data_list = [True , False , 1,1.0,4]
print(new_list(data_list))


# LC using if else
nums = range(1,21)
formated_num = [i*2 if (i%2==0) else -i for i in nums]
print(formated_num)

#LC in LC1;
# o/p = [[1,2,3],[1,2,3],[1,2,3]]
list2 = [[ i for i in range(1,4)] for j in range(3)]
print(list2)

#dictionary comprehension:

# square
squar_Dict = {f"square of {num}" : num**2 for num in range (1,11)}
# print(squar_Dict)
for k,v in squar_Dict.items():
    print(f"{k}: {v}")

# dict comprehension using if else :
value = {i:('even' if  i %2 == 0 else 'odd' )for i in range(1,11)}
print(value)


