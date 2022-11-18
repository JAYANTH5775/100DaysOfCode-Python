print("even sum calculator")
r=int( input("enter the range for which you want to calculate the even sum "))
i=0
sum=0
for i in range(r+1):
    if i%2 == 0:
        sum += i
print("sum is "+str(sum))