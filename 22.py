#22  Pattern 2 

number=5
random = 1
for i in range(number):
    for j in range(i):
        print (j+1, end="")
    
    print('')

for i in range(5,0,-1):
    for j in range(i):
        print(j+1, end="")
    print('')