
class Phone:

    def __init__(self,brand_name,model_name,price) :
        self.b_name = brand_name
        self.m_name = model_name
        self._price = max(price,0)  #it should not take negative value so we will be using max()
        # self.specification = f"{brand_name} {model_name} and price is : {price}"

    @property
    def price(self):
        return self._price   #after this method we can retrive the value of price without writing _price
    
    @price.setter           #only after declaring getter() we can define a setter()
    def price(self, new_price):
        self._price = max(new_price,0)

    @property
    def specification(self):
        return f"{self.b_name} {self.m_name} and price is : {self._price}"

    def calling(self,mobile_number):
        return f"calling {mobile_number}"
    
phone1 = Phone("Apple","iphobne 15 plus", 83000)
phone1.price =10000  
print(phone1.price)
print(phone1.specification)
    

    

