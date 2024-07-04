
#sytax errors: 

# def func();  #instead of ':' if i use ';' it will throw me syntax error
#     pass
# SyntaxError: expected ':'
# IndentationError
""" if we pass wrong count of spaces inside the function we will get indentation error"""
# def func():
# print("")
# IndentationError: expected an indented block after function definition on line 9

#name error:
"""when we try to access something which is not defined we will get Name error"""
# print(name)
# NameError: name 'name' is not defined
# TypeError:
# when we try to perform wrong operations on wrong type :
# print (5 + "ram")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# index error:
# l =[1,2,3,4]
# print(l[5])
# IndentationError: expected an indented block after function definition on line 9

# ValueError:
# s= 'abc'
# print(int(s))
# ValueError: invalid literal for int() with base 10: 'abc'

# AttributeError
# l =[1,2,3,4]
# l.push(45)\
# AttributeError: 'list' object has no attribute 'push'
