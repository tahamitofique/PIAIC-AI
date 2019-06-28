#19 Palindrome tester 

userInput = input("Enter Text :")
palindrome = userInput[::-1]
if userInput == palindrome:
    print("Text " , userInput," is Palindrome")
else:
    print("Text " , userInput," is not Palindrome")