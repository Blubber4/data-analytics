# A program to calculate the minimum number of coins required for a given amount of change
#
# @author 
# @assignment CSCI 333 Assignment 1
# @date 7/17/2022
#

def remainingCoins(total_cents, coin_value):
    max_coins = total_cents // coin_value
    remaining_cents = total_cents % coin_value
    return remaining_cents, max_coins


while True:
    print("Enter a non-integer value to end the program")
    cents = input("Enter number of cents: ")
    try:
        cents = int(cents)
    except ValueError:
        break

    cents, quarters = remainingCoins(cents, 25)
    cents, dimes = remainingCoins(cents, 10)
    cents, nickels = remainingCoins(cents, 5)
    cents, pennies = remainingCoins(cents, 1)

    print("Pennies: ", pennies)
    print("Nickles: ", nickels)
    print("Dimes: ", dimes)
    print("Quarters: ", quarters, "\n")
