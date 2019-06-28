#15 Digit sum of a Number

number =int(input("Enter a Number"))

sumnum = str(number)

lst = list(sumnum)


totalDigits = ' + '.join(sumnum)

print(totalDigits)

total = 0
while number>0:
    digit = number%10
    total = total+digit
    number = number//10
print("Sum Of ", totalDigits, " is ", total)