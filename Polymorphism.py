class Phone:  #Base c;ass / parent class

    def __init__(self,brand_name,model_name,price) :
        self.b_name = brand_name
        self.m_name = model_name
        self._price = max(price,0)
    
    def full_name(self):
        return f"{self.b_name} {self.m_name}"

    def calling(self,mobile_number):
        return f"calling {mobile_number}"
    

    def __str__(self):
        return f"{self.b_name} {self.m_name} and price is {self._price}"
    
    def __repr__(self):
        return f"phone(\'{self.b_name}\' {self.m_name})"
    
    def __len__(self):
        return len(self.full_name())
    
    def __add__(self, other):
        return self._price  + other._price
    
    

    
myphone= Phone('Nokia','1600', 1100)
myphone2= Phone('Samsung','1313', 1100)
# print(myphone.full_name())
# print(myphone) #it will return locaton but if __repr__ method is defined then it will print the name
print(myphone.__str__())
print(myphone.__repr__())
print(myphone.__len__())

total_price = myphone + myphone2  
print(total_price)

"""this will work as we have overloaded a method called __add__"""

#operator overlaoding :
"""when a function is having more than one forms that is called as polymorphism
ex : '+' operator :

when we use + in case of int it returns the sum of 2 numbers 
but when we use + in case of string it concatenates them. 

here + operator is having more than one forms.


"""



