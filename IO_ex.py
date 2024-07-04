with open('salary.txt','r') as rf:
    with open('output.txt','a')as wf:
        for line in rf.readlines(): 
            name,sal = line.split(',')  #split the list with ',' and store them in 2 variables
            wf.write(f"{name}'s salary is : {sal}") #writing to the file.



