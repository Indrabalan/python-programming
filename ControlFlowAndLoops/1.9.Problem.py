#Loops

for i in range(1,11):
    print(i)


#Mutiplication Table 

table_num = int(input("Enter table num : \n"))
table_range = int(input("Enter table range : \n"))

for i in range(1,table_range+1):
    print(f"{i} * {table_num} = {i*table_num}")


# sum number 1 to 100
sum = 0
for i in range(1,101):
   sum += i
print(sum)


# print pattern

for i in range(1,6):
    print("*"*i)



for i in range(6,1,-1):
    print("*"*i)
