class Phone:  #Base c;ass / parent class

    def __init__(self,brand_name,model_name,price) :
        self.b_name = brand_name
        self.m_name = model_name
        self._price = max(price,0)
    
    def full_name(self):
        return f"{self.b_name} {self.m_name}"

    def calling(self,mobile_number):
        return f"calling {mobile_number}"
    

class Smartphone(Phone):  #derived class / child class
        
        def __init__(self,brand_name,model_name,price,ram,rom):
            #There are 2 ways to define parent methods in child class
            # Phone.__init__(self,brand_name,model_name,price) #method 1
            super().__init__(brand_name,model_name,price)
            self.ram = ram
            self.rom = rom
        
        def full_name(self):
             return f"{self.b_name} {self.m_name} and ram is {self.ram}"

        
class FlagsipPhone(Smartphone): #this will inherit all the methods of smartphone class as well as phone class.
     def __init__(self, brand_name, model_name, price, ram, rom,front_cam):
          super().__init__(brand_name, model_name, price, ram, rom)
          self.front_cam = front_cam

"""we can achice multilevel Inheritance in Python"""

phone1  = Phone("Apple", "iphone 15 plus",800000)
smartphone1  = Smartphone("Apple", "iphone 15 plus",700000,"8gb","128gb")
flagship = FlagsipPhone("Apple", "iphone 15 plus",700000,"8gb","128gb","16 MP")
print(flagship.full_name())

# print(phone1.full_name())
# print(smartphone1.full_name() + f" & price is {smartphone1._price}" )
# help(Smartphone) # help() function is used to check the order of exection of objects which is MRO(Method resolution order)

"""Method Overriding : 
creating a method which is there in parent class but with some modification
as Per MRO child class will be executed first so the overridden method will be executed
"""


"""Some builtin Functions
isinstnce() : this is used to chcek whether the object is of this class or not 
issubclass() : this is used to check the parent child relationship 
for ex: Smartphone class is a child / derived class of phone or not 
"""

print(isinstance(smartphone1,Smartphone))  #TRUE
print(isinstance(smartphone1,Phone))  #True (as smartphone class is inheriting all  the properties of Phone)
print(issubclass(FlagsipPhone,Smartphone))  #true
print(issubclass(FlagsipPhone,Phone))  #true


