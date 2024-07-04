# data = open("File2.txt",'a') #a : append : 
# data.write("what are you learning now ?")   #write() will clear all the content in the file and replace it with given data 
"""a : append function will not clear the contents it will add the given data at the end"""



# with open('File2.txt','r+') as f:
#     f.write("i am learning python now ") #it will clear the contents of the file and add the given data    

"""Using r+ mode you can both read and write to the file
note: unlike 'r' and'w' function it doesn't create the file if its not there inthe path"""

with open('File2.txt','r+',encoding="utf-8") as f:
    f.seek(len(f.read()))
    f.write("\ni am learning python now ") 

with open ('File.txt','r') as r :
    with open('File2.txt','r+')as w:
        w.seek(len(w.read()))
        w.write(r.read())   
        """this will open file.txt and insert all the data from file1 to file 2"""



