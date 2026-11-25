# check password 

password = "YZKI123@RKI"

user_password = input("Enter the password : \n")

while (password != user_password):
    user_password = input("Wrong password! Try agin and Enter correct password : \n")

print("Success! you are logged in")
