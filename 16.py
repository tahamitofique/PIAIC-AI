#16 Decimal To Binary Converter

decimalNumber = int(input("Enter a decimal number "))
finalDecimalNumber = decimalNumber

# to store binary numbers in list
array=[]

while(decimalNumber>0):
    digit=decimalNumber%2
    array.append(digit)
    decimalNumber=decimalNumber//2
    
    # Converting integer list to string list
    s = [str(i) for i in array] 
      
    # Join list items using join() 
    res = int("".join(s))     
array.reverse()

print("Binary Representation of ", finalDecimalNumber," is ",res,end=" ")