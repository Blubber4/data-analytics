# A program to calculate income tax according to the 1913 US tax code
#
# @author 
# @assignment CSCI 333 Assignment 1
# @date 7/17/2022
#

while True:
    print("Enter a non-numeric value to end the program")
    income = input("Enter total annual income: ")
    try:
        income = float(income)
    except ValueError:
        break

    tax = 0
    # why a chain of if/elif/else statements ??????
    if income > 500000:
        tax += .06 * (income - 500000)
        income = 250000
    if income > 250000:
        tax += .05 * (income - 250000)
        income = 100000
    if income > 100000:
        tax += .04 * (income - 100000)
        income = 75000
    if income > 75000:
        tax += .03 * (income - 75000)
        income = 50000
    if income > 50000:
        tax += .02 * (income - 50000)
        income = 50000
    if income <= 50000:
        tax += .01 * income

    print("Total taxes owed: ", tax, "\n")
