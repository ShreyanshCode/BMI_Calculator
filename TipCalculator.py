print("Welcome to Tip Calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10,12, or 15?"))
no_of_people = int(input("How many people to split the bill?"))
total_tip_value = tip_percentage / 100 * total_bill + total_bill
each_person_share = total_tip_value / no_of_people
final_amount = round(each_person_share, 2)
print(f"Each person should pay: $ {final_amount}")
