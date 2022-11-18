print("welcom to the rooler coaster \n")
height = int (input("whats your height\n "))

if height >= 120:
    print("yes , you can take your RollerCoaster ride\n")
    age = int(input("enter yr age\n "))
    if age < 12:
        bill = 5
        print("please pay $5\n")
    elif age <= 18:
        bill = 12
        print("please pay $12\n")
    elif age >= 45 and age <=55:
        print("Every thing is going Good , Have  a free ride")
        bill = 0

    else:
        bill = 20
        print("please pay $20 \n")
    img = input("Do youwant to take images while in roolercoaster")
    if img.lower() == "Yes".lower():
    #add 3 more ruppees
        bill = bill+3
        print("total bill is "+str(bill))
    else:
         print("total bill is "+str(bill))

else:
    print("you cannot take the roller coaster ride\n")