class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.b_name = brand_name        
        self.m_name = model_name        
        self.price = price        
    # instance mrthods
    def full_name(self):
        return f"{self.b_name} {self.m_name}"

    def is_cheap(self):
        return self.price < 50000
    
    def apply_discount(self,num):
        self.num = num
        off_price = self.price*(num/100)
        new_price = self.price - off_price
        return new_price 



l1 = Laptop("hp","pavilion",72000)
l2 = Laptop("Dell","victus",46000)

print(Laptop.full_name(l1))
print(Laptop.is_cheap(l1))
print(l1.apply_discount(40))


"""here full_name() methods and is_cheap methods are the instance methods of laptop class

like pop(), append(),remove() are the instance methods of List class"""

