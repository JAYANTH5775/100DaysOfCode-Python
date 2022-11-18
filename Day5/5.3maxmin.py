student_score = input("enter the student Scores ").split()
for i in range(0,len(student_score)):
    student_score[i] = int(student_score[i])
print(student_score)
min =student_score[0]
max =student_score[0]
for i in range(0,len(student_score)):
    if min > student_score[i]:
        min = student_score
    else:
        min = min
    if max < student_score[i]:
        max=student_score[i]
    else:
        max =max
print("the maximum and minimum of the student score is "+str(min)+" "+str(max))