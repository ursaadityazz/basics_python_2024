while True: #it will start a infinite loop so that even after getting the error code doesnt stop
    try:
        age  = int(input("Enter your age "))
        
    except ValueError:  #when you know what is the error you are going to get 
        print("maybe you entered something else, Try again ")

    except:
        print("some unexprected error occurred , plese try again")

    else:
        print(f"you have entered {age}")
        break
    finally: #this finally block gets excuted before loop'break'. finally block always gets excuted irrespective of condition satisfies or not 
        print("finally block codes.....") #it is not mandatory to write finally block always



if age < 18:
    print ("you can't watch this movie , you are a kid ")
else:
    print ("you can watch this movie ")


"""according to convention it is not right to write many things in try block.

it is appropriete that we write other things like print statements and conditions in else block """