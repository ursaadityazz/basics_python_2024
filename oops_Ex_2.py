# class Person:
#     count_of_instance = 0
#     def __init__(self,f_name,l_name):
#         self.first_name = f_name
#         self.last_name = l_name
#         Person.count_of_instance +=1
    
# p1 = Person("aditya","kumar")
# p1 = Person("amiya","kumar")
# p1 = Person("aliya","kumar")

# print(Person.count_of_instance)


#this progrsm will return the value of insatnce created for Person class.

"""class methods """
class Person:
    count_of_instance = 0
    def __init__(self,f_name,l_name):
        self.first_name = f_name
        self.last_name = l_name
        Person.count_of_instance +=1

    @classmethod
    def instance_counter(cls):
            return f"you have created {cls.count_of_instance} instances of {cls.__name__} class"
    
p1 = Person("aditya","kumar")
p1 = Person("amiya","kumar")
p1 = Person("aliya","kumar")

print(Person.instance_counter())


"""
To show whats inside the object : object_name.__dict__
to print the name of class or to use the name of the class as place holder : cls.__name__

""" 

"""while creating the object if we want to pass a single string"""

class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.b_name = brand_name        
        self.m_name = model_name        
        self.__price = price        # _price : when we use '_' before a variable then it tells the coder to not to change it 
                                    #__price : when we use '__' before variable name then python changes the name of this variable
    # instance mrthods
    def full_name(self):
        return f"{self.b_name} {self.m_name}"
    
    @classmethod
    def from_string(cls,str):
        b_name,m_name,price = str.split(',')
        return cls(b_name,m_name,price)

#there is another method called static method
    @staticmethod
    def static():
        return "hello static method " 

    def is_cheap(self):
        return self.price < 50000
    

    def apply_discount(self,num):
        self.num = num
        off_price = self.price*(num/100)
        new_price = self.price - off_price
        return new_price 



l1 = Laptop("hp","pavilion",72000)
l2 = Laptop("Dell","victus",46000)
l3 = Laptop.from_string("Apple,Macbook,150000")


# print(Laptop.full_name(l3)) #WE CAN WRITE LIKE THIS AS WELL.
# # print(l3.full_name())
# print(Laptop.static())

"""to define static method we will use @staticmethod decorator . static method does not take arguments like self and cls"""
print(l1._Laptop__price) #this is not a private variable 
print(l1.__dict__)

