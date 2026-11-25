# Loops in python

# 1.Print Numbers from 1 to 10

for i in range(1,11):
    print(i)

# 2.print even number from 1 to 20   

for i in range(1,21):
    if i % 2 == 0:
        print(i)

# 3.Multiplication table of 5

for i in range(1,11):
#   print("5 * ",i," = ",5*i)
  print(f"5 * {i} = {5 * i}")

# 4.Calculate the sum of numbers from 1 to 10  
sum = 0
for num in range(1,11):
    sum += num
print(sum)
