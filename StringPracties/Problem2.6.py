
# Palindrome

String1 = "madam"

text = input("Enter the name like palidrome : \n")

if(text == text[::-1]):
    print(f"{text} is palindrome")
else:
    print(f"{text} is not a palindrom")    