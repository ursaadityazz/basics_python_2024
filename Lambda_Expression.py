
#without using Lambds expression
def add (a,b):
    return a+b
#using lambda expression we can write the func in 2 lines

a = lambda a,b :a+b   #lambda (on which parametr process will run) : what is the process to run
print(a(2,3))
#we dont store lambda functions in a variable.

#some more examples :
is_even = lambda a :a%2 ==0
print(is_even(3))
asf = lambda a : "sahi hai" if a[1] == 'S' else "galat"
print(asf('aSda'))

