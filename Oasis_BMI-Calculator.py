# 1. Begin with getting user input
print("====Welcome to the BMI Calculator====")
weight= float(input("Enter your weight in kg: "))
height= float(input("Enter your hieght in meters: "))

# 2. Formula to calculate BMI 
bmi= weight/ (height**2)

# 3. Result
print(f"\nYour calculated BMI is: {round(bmi, 2)}")

# 4. Use if-else loop to determine health category
if bmi < 18.5:
    print("You are Underweight 📉🥲!")
elif bmi >= 18.5 and bmi <= 24.9: 
    print("You are Healthy ⚖️☺️!")
elif bmi >= 25 and bmi <= 29.9: 
    print("You are overweight 📈😑!")
else:
    print("You are obese ❤️‍🩹🏥")