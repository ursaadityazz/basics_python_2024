# def add(a,b):
#     return a+b

# print(add(2,3)) # but if we pass strings instead of int 
# print(add('2','3'))  #it will concatenate both sstrings 
"""instead of concatenatio we will raise an error called Typeerror"""
# def add(a,b):
#     if type(a) is int and type(b) is int:
#         return a+b
#     else:
#         raise TypeError("you have passed wrong type ")
    

# print(add(2,3))
# print(add('2','3'))  

class Animal:
    def __init__(self,name,breed) :
        self.name = name
        self.breed = breed 

    def sound(self):
        # return "this is the animal sound"
        raise NotImplementedError("you have to define this method in the subclass")
    

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)

    def sound(self):
        return "Bhoo"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)

    def sound(self):
        return "meaw"
    
animal1 = Dog("dog",'pug')
animal2 = Cat("cat",'russian')
# print(animal1.sound()) 
# print(animal2.sound()) #for both cat and dog we are getting the same sound which is illogical 
"""here we will have to raise an error in the parent class that when ever sound() will be called there will be an error

so that Developer will be forced to define a method in subclass to get the appropriete result form each class """
print(animal1.sound()) 
print(animal2.sound())
