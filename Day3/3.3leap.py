yr = int(input("enter the year for which you want to determone wether its a leap year or not\n\n"))
if yr % 4 == 0:
    if yr % 100 == 0:
        if yr % 400 == 0:
            print("its a leap yr ")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")

year = int(input("enter the year"))
if year % 4 == 0 :
    print("its a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("its a leap year")
else:
    print("its not a leap year")