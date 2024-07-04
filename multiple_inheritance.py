class A:
    def class_A_method(self):
        return "this is A simple method"
    def hello(self):
        return "class A hello method"
class B:
    def class_B_method(self):
        return "this is B simple method"
    def hello(self):
        return "class B hello method"
    
class C(B,A):
    pass

instance_C  = C()
print(instance_C.class_A_method()) 
print(instance_C.class_B_method()) 
print(instance_C.hello()) 
"""it will print classs A hello method 
class C(A, B)
 |  Method resolution order:
 |      C
 |      A
 |      B
 |      builtins.object
 
 class C(B, A) as per the inheritance order of parent class methods will be executed
  |  Method resolution order:
 |      C
 |      B
 |      A
 |      builtins.object
"""
help(C)
print(C.mro())  #another way to see MRO (Method resolution order)
print(C.__mro__)