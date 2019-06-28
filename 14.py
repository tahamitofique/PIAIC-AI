#14 Sum of n Positive Number

sumNumber = 0

userNumber =int(input("Enter Number Of n"))
if userNumber >=0:
    total = int(userNumber * (userNumber + 1)/2)
    print(total)
else:
    print(userNumber," is not positive Number")