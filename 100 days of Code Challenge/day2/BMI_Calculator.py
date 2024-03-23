weight_1 = input("What's your Body Mass?: ")
height = input("What's your Body Height?: ")

bmi = int (weight_1) / (float(height)**2)
print("THe Body Mass Index(BMI) is: ", round(bmi))