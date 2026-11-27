
i =1

while i<=10:
    print(i)
    i+=1



password = "Y2k@123"
enter_pass = input("Enter the password. \n")

while(enter_pass != password):
       enter_pass = input("Wrong password ! Try again and enter password :")

print("Success! you are logged in")


#Reverse number 

num = 12345

print(int(str(num)[::-1]))