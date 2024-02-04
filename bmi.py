height=input("Enter your height in m\n")
weight=input("Enter your weight in kg\n")
bmi=round(float(weight)/(float(height)**2),2)
if bmi<=18.5:
    print(f"BMI of a person is: {bmi},Underweight")
elif bmi<=25:
    print(f"BMI of a person is: {bmi},Normal weight")
elif bmi<=30:
    print(f"BMI of a person is: {bmi},Overweight")
elif bmi<35:
    print(f"BMI of a person is: {bmi},Obese")
else:
    print(f"BMI of a person is: {bmi},Clinically Obese")
