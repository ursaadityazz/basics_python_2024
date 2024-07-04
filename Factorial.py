fac = 1
def Factorial(n):
    if n==0:
        return 1 
        fac = 1
    else:
        for i in range(1,n+1):
            fac = fac * i
    return fac

def is_strong_num(num):
    sum = 0
    temp = num
    while temp > 0:
        fac =1 
        digit = temp%10 
        for i in range(1,digit+1):
            fac = fac*i
        sum =sum+fac
        temp//10
    return sum == num

number = int(input("Enter a number : "))
if is_strong_num(number):
    print(f"{number} is strong number")
else:
    print(f"{number} is not a strong number")
