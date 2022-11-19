import random
t=True
def function():
    a= random.randint(0,10)
    if a>4:
        print("hello world !!!")
    else:
        print("good day")
while(t==True):
        function()
        t=False
        if t == False:
            break