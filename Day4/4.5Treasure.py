print("welcome to tearsure game ")

row1 = ["😊",'😊','😊']
row2 = ["😊",'😊','😊']
row3 = ["😊",'😊','😊']

map = [row1,row2,row3]

print( f"{row1}\n {row2} \n {row3}\n")

print('enter the poistion where you want to [place the treasure')
vertical = int(input("enter the  coulumn"))
horizontal = int(input("enter the row "))
map[horizontal][vertical]='x'
print((map[horizontal][vertical]))
print( f"{row1}\n {row2} \n {row3}\n")




