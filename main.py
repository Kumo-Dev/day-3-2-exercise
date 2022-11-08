# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


bmi = round(weight / (height * height))

if bmi > 35:
  print(f"Your BMI is {bmi}, you are clinically obese")
elif bmi > 30:
  print(f"Your BMI is {bmi}, you are obese")
elif bmi > 25:
  print(f"Your BMI is {bmi}, you are overweight")
elif bmi > 18.5:
  print(f"Your BMI is {bmi}, you normal weight")
else:
  print(f"Your BMI is {bmi}, you are underweight")

