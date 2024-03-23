height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = int (weight) / (float(height)**2)

if bmi < 18.5: 
  print(f"Your BMI is {bmi}, you are Underweight")
elif 18.5 < bmi < 25:
  print(f"Your BMI is {bmi}, You have a Normal weight")
elif 25 < bmi < 30:
  print(f"Your BMI is {bmi}, You are Overweight")
elif 30 < bmi < 35:
  print(f"Your BMI is {bmi}, You are Obese")
else:
  print(f"Your BMI is {bmi}, You are clinically Obese")