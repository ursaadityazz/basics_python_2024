#defining my first class:

"""we use class to define our own object. and whenever we would create object , __init__ methid gets called.
according to convention 1st argument of init method lass should be always self"""
class Person:
    def __init__(self,firstname,lastname,age):
        print("init method get called")
        # instance variables
        self.firstname = firstname    
        self.lastname = lastname
        self.age = age

p1 = Person('aditya','kumar',26)
p2 = Person('amiya','kumar',26)
print(p1.firstname)
