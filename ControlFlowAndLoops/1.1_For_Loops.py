

for i in range(1,6):
    print(i)


for i in range(1,11):
    print(f"{i} * 5 = {i*5}") 


tableNum = int(input("Enter the table num : \n")) 

tableRange = int(input("Enter ther table range : \n"))


for i in range(1,tableRange+1):
    print(f"{i} * {tableNum} = {i*tableNum}")