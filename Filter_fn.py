

numbers = [1,2,3,4,5,6,7,8,9,9]
even_num = list(filter(lambda a:a%2 ==0 , numbers))
print(even_num)

c = [1,2,3,4,5,]
a =list(map( lambda a: a**2 if a%2==0 else a**3 ,c))
# ex : here list 'a' will store all the square values of even_nums and cube values for all the odds.


