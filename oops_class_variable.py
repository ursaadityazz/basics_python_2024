"""suppose there is a value which we need to use for every method,

so instead of defining it with object we can define it inside the class itself (class_variable)
this will save memory space as well """

class Circle:
    """here lets take an example of circle class , as the value of PI is same for every method"""
    pi= 3.141
    def __init__(self,radious):
        self.r = radious

    def circle_area(self):
        return Circle.pi*(self.r**2)
    
    def Circle_Circumference(self):
        return 2*Circle.pi*self.r
    

c = Circle(20)
print(c.circle_area())
print(c.Circle_Circumference())


class Laptop:

#if there is a sale and there is a constant discount that is applied with every laptop
    discount_percent = 50
    def __init__(self,brand_name,model_name,price):
        self.b_name = brand_name        
        self.m_name = model_name        
        self.price = price        
    # instance mrthods
    def full_name(self):
        return f"{self.b_name} {self.m_name}"

    def is_cheap(self):
        return self.price < 50000
    
    def apply_discount(self):
        off_price = self.price*(self.discount_percent/100)
        new_price = self.price - off_price
        return new_price 



l1 = Laptop("hp","pavilion",72000)
l2 = Laptop("Dell","victus",46000)
# l2.discount_percent = 20
print(l2.__dict__)



print(Laptop.full_name(l2))
print(Laptop.is_cheap(l2))

print(l2.apply_discount())

"""when there is a specific discount on each brand then we cant apply the same discount value in all the laptops.
in that case we will have to define a discount percent while creating the object and when apply discount() function gets called it should
use the value that is given inside the object. >> to do that we have to use self keyword inside the apply discount()


so that it when discount percent is not given in object it will use the class variable"""

