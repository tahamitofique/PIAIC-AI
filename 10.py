#10 Calculate Interest
p = float(input("Please enter principal amount: "))
r = float(input("Please Enter Rate of interest in %: "))
t = float(input("Enter number of years for investment: "))
#a = p* (1 + r/100)**2
a = p* (pow((1 + r*100 / 100), t))
print(a)