# A program to generate 1000 random numbers, and keep a count of how many are even vs odd
#
# @author
# @assignment CSCI 333 Assignment 2
# @date 7/24/2022
#

import random

def getRandom(a, b):
    if a > b:
        temp = a
        a = b
        b = temp

    return random.randint(a, b)

def isEven(num):
    if num % 2 == 0:
        return True
    return False


min_bound = 1
max_bound = 1000
even_count = 0
odd_count = 0
for i in range(1000):
    n = getRandom(min_bound, max_bound)
    if isEven(n):
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers generated:", even_count)
print("Number of odd numbers generated:", odd_count)
