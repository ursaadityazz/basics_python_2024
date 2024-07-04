class NameTooShortError(ValueError):
    pass


def Validate(name):
    if len(name) < 8 :
        raise NameTooShortError("name is too short")
    return f"Hello {name}"


"""to create a custom excetion 
> create a class
>inherit the appropriete error
>the exception is ready to use 


why use custom exception ?
> it will increase code readability"""

name = input("Enter your name : ")
print(Validate(name))