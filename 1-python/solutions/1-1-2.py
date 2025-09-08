# Code Challenge 1-1-2
'''
Let' write a program to divide up the check among diners in a party.

Write a program to input the amount of a restaurant check, tip %, and number of diners

The program should output the total amount with tip, and the amount each diner owes.
'''

check_amount = float(input("Enter the restaurant check amount: $"))
tip_percent = float(input("Enter tip percentage (e.g., 15 for 15%): "))
num_diners = int(input("Enter number of diners: "))


tip_amount = check_amount * (tip_percent / 100)
total_with_tip = check_amount + tip_amount
amount_per_person = total_with_tip / num_diners

print(f"Check amount: ${check_amount:.2f}")
print(f"Tip amount ({tip_percent}%): ${tip_amount:.2f}")
print(f"Total with tip: ${total_with_tip:.2f}")
print(f"Each diner owes: ${amount_per_person:.2f}")