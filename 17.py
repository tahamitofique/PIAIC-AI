#17 Binary To Decimal Converter

binaryNumber = input("Enter a Binary number ")
binaryNumberList = list(binaryNumber)
defaultValue = 0
actualNumber = str(binaryNumber)



for d in range(len(binaryNumberList)):
    numbers = binaryNumberList.pop()
    if numbers == '1':
        defaultValue = defaultValue + pow(2, d)
print("Decimal Representation of ", actualNumber," is " ,defaultValue)