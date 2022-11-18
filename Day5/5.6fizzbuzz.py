print("welcome to the fizz-buzz game \n student need to say fizz-> if divisible by 3 \n buzz ->divisible by 5 \n "
      "fizzbuzz if divisible by both 3 and 5")
i =0
sum =0
for i in range(101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i %3 == 0 :
        print("fizz")
    elif i %5 ==0:
        print("buzzz")
    
    else:
        print(i)