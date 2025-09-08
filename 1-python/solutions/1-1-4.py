# Code Challenge 1-1-4¶
'''
Number to Letter grade
Letter grades in a college class are computed as follows:

95 and above is an A
75 and above, but below 95 is a B
50 and above, but below 75 is a C
below 50 is F
Write a program to input the number grade and calculate the letter grade

Re-write to account for "bad" grades > 120 or < 0
'''

grade = float(input("Enter the numeric grade: "))

if grade > 120 or grade < 0:
    print("Invalid grade. Please enter a value between 0 and 120.")
elif grade >= 95:
    print("Letter grade: A")
elif grade >= 75:
    print("Letter grade: B")
elif grade >= 50:
    print("Letter grade: C")
else:
    print("Letter grade: F")