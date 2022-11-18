import random

print("welcome to the cin tosser")
choice = True
while choice:

    coin = random.randint(0,1)
    if coin == 1:
        print("heads")
    if coin == 0:
        print("tails")
    print("do you want to choice coin once more(True or False)")
    choice=input()
    if choice == True:
        continue