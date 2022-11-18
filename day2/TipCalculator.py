print("Welcome to Tip calculator:)")
print("Enter the total bill :")
bill= int(input())
print("Enter the number of the person ? to slit")
number=int(input())
print("What percentage of the tip would u like to give ??? 10 , 12 0r 15 ?12")
tip=int(input())
slipt=int(bill/number+(bill*(tip/100)))
print(f"the total slipt per person is {slipt}")


