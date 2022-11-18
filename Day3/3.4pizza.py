print("hey!!! Welcome to pizza Python shop ")
size = input("what size of pizza you want to order (S/L/M?)\n\n")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else :
    bill = 0
add_pepperoni = input("do you want ot add pepperoni to it(Y/N)\n\n")
if add_pepperoni == "Y" and size == "M":
    bill+=2
if add_pepperoni == "Y" and size == "M" or size == "L":
     bill+=3
extra_chess = input("do you want to add some more extra chess to it\n\n\n ")
if extra_chess == 'Y':
    bill+=1


print("the total bill is "+str(bill))