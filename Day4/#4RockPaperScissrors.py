import random

paper = '''  
 
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''




rock =''' 
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''



scissors = '''
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
choice = True
while choice:
    print("welcome t0 the Rock paper scissors game ")
    ip = int(input("enter the chioce you want to pick up 0 -> rock , 1 -> paper 2->scissors \n\n"))

    rg = random.randint(0, 2)
    if ip >= 3 or ip < 0:
        print("you typed a invalid number")
    elif ip == 0 and rg == 2:
        print("you  wins :) ")

    elif rg > ip:
        print("you lose")
    elif ip > rg:
        print("you win ")
    elif rg == ip:
        print("its a draw")
    elif rg == 0 and ip == 2:
        print("you lose ")
    cont = [rock, paper, scissors]

    print("user choice")
    print(cont[ip])
    cc = cont[rg]
    print("computer choice")
    print(cc)
    print("would y like to play one more rouns or stop (Y or N)")
    chc=input()
    if chc == "N":
        break
