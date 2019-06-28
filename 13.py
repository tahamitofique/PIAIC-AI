#13 BMI Calculator

userHeight = float(input("Enter Your Height in Cm"))
userWeight = float(input("Enter Your Weight in kg"))

heightInMeters = userHeight * 0.01


totalBmi = userWeight / (heightInMeters * heightInMeters)



print(totalBmi)