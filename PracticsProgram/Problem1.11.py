# Reverse number 

num = 123
reverse = 0
#  step : 1
while (num > 0):
   digit = num % 10
   reverse = reverse * 10 + digit
   num = num // 10

print(reverse)  

num2 = 12345
# step : 2
reverse1  = int(str(num2)[::-1])
print(reverse1)


# with loop

num3 = 1234567
reverse = " "
for digit in str(num3):

    reverse = digit + reverse

print(reverse)    

