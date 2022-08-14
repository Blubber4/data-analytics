# A program to calculate squares < a number n, positive numbers divisible by 10 < n, and powers of two < n
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

def isPowTwo(num):
    flag = False
    num_binstr = str(bin(num))
    for j in num_binstr:
        if j == '1':
            if flag:
                return False
            flag = True
    return flag


while True:
    print("Enter a non-integer value to end the program")
    n = input("Input a number: ")
    try:
        n = int(n)
    except ValueError:
        break

    # part A
    print("Squares:", end=' ')
    i = 0
    while i < n:
        if isSquare(i):
            print(i, end=' ')
        i += 1

    # part B
    print("\nDivisible by 10:", end=' ')
    i = 1
    while i < n:
        if i % 10 == 0:
            print(i, end=' ')
        i += 1

    # part C
    print("\nPowers of 2:", end=' ')
    i = 0
    while i < n:
        if isPowTwo(i):
            print(i, end=' ')
        i += 1
    print('\n')
