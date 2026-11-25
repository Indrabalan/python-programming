
# Match case with

num1 = int(input("Enter first number : \n"))
num2 = int(input("Enter second number : \n"))

operation = input("Enter the operation : \n")

match(operation):
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)            