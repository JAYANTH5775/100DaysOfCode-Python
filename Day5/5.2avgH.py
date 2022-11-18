print("welcome to average height calculator of students")
print("enter the student heights")
student_height = input().split()
sum = 0
for i in  range(0,len(student_height)):
    student_height[i]=int(student_height[i])
    #print("do u want to enter one mor")
print("student height are "+str(student_height))
for i in student_height:
    sum += i
print(sum)
no = int(len(student_height))
avg_height = sum /no
print("average height of the student is "+str(avg_height))