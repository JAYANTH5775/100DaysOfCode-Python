import random
people = input("enter everybodies names seperated by comma ")
ppl = people.split(",")
print(ppl)

number = len(ppl)
rand = random.randint(0,number-1)
print(f"{ppl[rand]} should pay the biill")

print(f"{random.choice(ppl)} should treat EveryBody")