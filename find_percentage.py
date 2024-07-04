# l1 = input()
# l2 = list(l1.split())
# print(l2)

students = {}
n = int(input("enter n"))
if n >= 2 and n <= 10 :
    for _ in range(n):
        # name = input()
        marks = []
        name, *line = input().split()
        scores = map(float,line)
        for score in scores:
            if 0< score <= 100:
                marks.append(score)
        students[name] = marks

def average(list):
    return sum(list)/len(list)

query_name = input("Enter a name")
if students.__getitem__(query_name):
    result = round(average(students.get(query_name)),2)
    print(result)
    

