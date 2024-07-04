
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

        

phone1  = Phone("Apple", "iphone 15 plus",800000)
smartphone1  = Smartphone("Apple", "iphone 15 plus",700000,"8gb","128gb")

print(phone1.full_name())
print(smartphone1.full_name() + f" & price is {smartphone1._price}" )

""" we can use all the attributes and methods of the parent class by using inheritance """