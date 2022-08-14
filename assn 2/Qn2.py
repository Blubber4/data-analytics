# A program to calculate the sum of all even numbers between 2 and 100, all squares between 1 and 100,
# sum all odd numbers between given numbers a and b, and the sum of all odd digits of a given number n
#
# @author
# @assignment CSCI 333 Assignment 2
# @date 7/24/2022
#

import math

def isSquare(num):
    sqrt_num = math.sqrt(num)
    if (sqrt_num - int(sqrt_num)) == 0:
        return True
    return False

def isEven(num):
    if num % 2 == 0:
        return True
    return False


# part A
sum_i = 0
for i in range(2, 101):
    if isEven(i):
        sum_i += i
print("Sum of all even numbers 2 - 100: ", sum_i)

# part B
sum_i = 0
for i in range(1, 101):
    if isSquare(i):
        sum_i += i
print("Sum of all squares 1 - 100: ", sum_i)

# part C
a = input("Enter lower bound a: ")
try:
    a = int(a)
except ValueError:
    print("Please enter an integer bound")

b = input("Enter an upper bound b: ")
try:
    b = int(b)
except ValueError:
    print("Please enter an integer bound")

if a > b:
    temp = a
    a = b
    b = temp

sum_i = 0
for i in range(a-1, b+1):
    if not isEven(i):
        sum_i += i
print("Sum of all odd numbers", a, '-', b, ':', sum_i)

# part D
n = input("Enter an integer n: ")
try:
    n_test = int(n)
except ValueError:
    print("Please enter an integer bound")

sum_i = 0
for i in n:
    i = int(i)
    if not isEven(i):
        sum_i += i

print("Sum of all odd digits of n:", sum_i)
