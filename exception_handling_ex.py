def divide(a,b):
    # if b == 0:
    #     raise ValueError("Value of b can t be zero")
    return a/b


while True:
    try:
        a = int(input("Enter an integer value for A : "))
    except ValueError:
        print("you eterred something else , try again")
    except :
        print("unexpected error")
    else:
        break

while True:
        try :
            b = int(input("Enter integer value for B : "))
            if b ==0:
                raise ValueError("Value of b can t be zero")
        except:
            print("Enterred Value of b is Invalid")
        
        else:
            break



print(divide(a,b))

# while True:
#     try:
#         print(divide(a,b))
#     except ZeroDivisionError :
#         print("value of B is invalid")
#     else:    
#         break

    
# while True:
#     try:
#         a,b=map(int,input("enter two number separated by comma : ").split(","))
#         div=a/b
#     except ValueError:
#         print("you entered string instead of number")
#     except ZeroDivisionError:
#         print("dividend should not be zero")
#     except:
#         print("error..")
#     else:
#         print(f"the division is {div}")
#         break
#     finally:
#         print("finally block......")