#7 Check If number is Even Or Odd
num = int(input("Enter Number: "))
mod = num % 2
if mod > 0:
    print(num,"is Odd")
else:
    print(num,"is Even")