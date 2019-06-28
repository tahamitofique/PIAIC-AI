#20 Count Alphabets, Numbers and Special Characters  

userInput = input("Please Enter your Own String : ")
alphabets = digits = special = 0
spaces = userInput.count(' ')
for i in range(len(userInput)):
    if(userInput[i].isalpha()):
        alphabets = alphabets + 1
    elif(userInput[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1

specialCharacter = special - spaces
print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", specialCharacter) 
print("Total Number of Spaces in this String :  ", spaces)