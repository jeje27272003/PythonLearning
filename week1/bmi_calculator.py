# bmi_calculator.py

print ("Welcome to the BMI calculator!")

while True:
    try:
        height = float(input("Enter your height in meters: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number for height.")


while True:
    try:
        weight = float(input("Enter your weight in kilograms: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number for weight.")

bmi = weight / (height ** 2)
print("Your BMI is: ", round(bmi, 2))

if bmi < 18.5:
    print("You are underweight.")

elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")

elif 25 <= bmi < 29.9:
    print("You are overweight.")

else :
    print("You are obese.")