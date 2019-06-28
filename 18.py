#18 Vowel and Consonants Counter 

userInput = input("Enter Text ")
vowels = 0
consonants = 0
for i in userInput:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("Vowels : ",vowels)
print("Consonants : ",consonants)