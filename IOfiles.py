#to open a file we will use its path:

f= open('File.txt','r')
print(f.read())  #read() is used to read the contents in the file 
"""but once all the contents in file has read it changes the cursor position 
to check the cursor position we will use tell()"""

print(f.tell()) #it will print the current position of cursor in the file 
"""to change the cursor position to anywhere according to the req we will use seek()"""

f.seek(0)  #this will move the cursor to o'th position
print(f.tell()) #>>0 #now we can print the contents again from the beginning.

# print(f.readline()) #readline() is used to print the contents in the file one by one
# for line in range(0,4):
#     print(f.readline(),end= '') #we can even create a loop on readline()

print(f.readable()) #this will return a boolean value if the file is readable or not
# l = f.readlines() #readlines() will append the lines in the file to a list 
# print(l)
# for i in l:
#     print(i, end='')
print(f.name)  #it will return the name of the file .
print(f.closed) #it will return a boolean value to check whether the file is closed or not
f.close() #close () is used to close the file.
print(f.closed) #it will return a boolean value to check whether the file is closed or not



# new = open('Generator.py','r')  #we use "r" to let python know we have to read the file.
# print(new.read())

with open('file.txt') as f:
    data = f.read() 
    print(data)  
    """another way to open file and using this method once the opeation done
    file closes automatically to check we can use closed()"""

print(f.closed)

