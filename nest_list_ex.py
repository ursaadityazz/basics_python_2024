name = []
score = []
n = int(input())
if n >= 2 and n <= 5:
    for i in range(1,n+1):
        a = input()
        b= float(input())
        name.append(a)
        score.append(b)

# print(name)
# print(score)
# students = [name,score]

# making the pair of student and score 
student_score = list(zip(name,score))
list1 =[]
for pair in student_score:
    list1.append (list(pair))


#extarcting the scores
score_values  = [score for name,score in list1]
# print(score_values)

#getting the 2nd lowest score
second_lowest = sorted(set(score_values))[1]
# print(second_lowest)

#getting the names of second lowetst
second_lowest_names = [name for name,score in list1 if score == second_lowest]
# print(second_lowest_names)

# sorting the names in alphabetical order
for name in sorted(second_lowest_names):
    print(name)


