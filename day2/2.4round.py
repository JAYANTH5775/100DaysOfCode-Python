print(round(35/4,2))
print(35//6)

result=242
check=True
while check:
    result /= 2
    print("result is : "+str(result))
    print("would u like to divide one more time ")
    check=input("enter True or False")
    if check == False:
            break

