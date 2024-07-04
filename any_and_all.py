num1 = [2,4,6,8,10]
num2 = [1,3,5,7,9]

even_t = [True if i %2 ==0 else False for i in num1]
odd_t = [True if i %2 ==0 else False for i in num2]
print(even_t)
print(odd_t)

# [True, True, True, True, True]
# [False, False, False, False, False]

# all function checks if all elements of the list are True

# print(all([True, True, True, True, True])) #--> True if all  elements are true  'False' if one element is False
# print(any([True, True, True, True, True])) #--> True if any element of the list is true

#now checking all numbers in num1 list are even or not using all function

print(all([i%2==0 for i in num1 ]))
print(any([i%2==0 for i in num2 ]))

# example
#run the process if all the elemnts of input are int or float

def sum(*args):
    if all(type(arg) == int or type(arg)==float for arg in args):
        sum =0
        for arg in args:
            sum += arg
        return sum
    else:
        return "invalid input"

print(sum(1,2,3,4,5,6))

