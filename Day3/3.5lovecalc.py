print("Welcomr to the love calculator ")
name1 = input("what is your name ")
name1 = name1.lower()
name2 = input("whats your lover name ")
name2 = name2.lower()

combo = name1+name2
lowerCase = combo.lower()
t=lowerCase.count("t")
r=lowerCase.count("r")
u=lowerCase.count("u")
e=lowerCase.count("e")

true = t+r+u+e

l = lowerCase.count("l")
o = lowerCase.count("o")
v = lowerCase.count("v")

e = lowerCase.count("e")
love = l+o+v+e
true_love = str(love) +str( true)
true_love = int(true_love)
if true_love < 10 or true_love > 90:
    print(f"your Score is {true_love} , you both are like coca and mentos ")
elif true_love >= 40 and true_love < 60:
    print(f"your Score is {true_love}, you all together ")
else:
    print(f"your Score is {true_love}")