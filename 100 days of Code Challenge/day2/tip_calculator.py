print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give ? 10, 12, or 15? "))
people = int(input("how many people to split the bill? "))
tip = percent / 100
tip_amount = bill * tip
total_bill = tip_amount + bill
each_pay = total_bill /people

result = round(each_pay, 2)
print(f"Each person sholud pay: ${result}")