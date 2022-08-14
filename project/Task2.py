# A program to show some functionality of pandas' dataframe type
#
# @author McMillian, Caleb
# @assignment CSCI 333 Project
# @date 8/9/2022
#

import pandas

if __name__ == '__main__':
    temps = {
        "Maxine": [71, 98, 85],
        "James": [67, 89, 77],
        "Amanda": [62, 78, 74]
    }

    # part A
    print("Part A")
    temperatures = pandas.DataFrame(data=temps)
    print(temperatures, '\n')

    # part B
    print("Part B")
    temperatures = pandas.DataFrame(data=temps, index=["Morning", "Afternoon", "Evening"])
    print(temperatures, '\n')

    # part C
    print("part C")
    print(temperatures["Maxine"], '\n')

    # part D
    print("part D")
    print(temperatures.loc["Morning"], '\n')

    # part E
    print("part E")
    print(temperatures.loc[["Morning", "Evening"]], '\n')

    # part F
    print("part F")
    print(temperatures[["Amanda", "Maxine"]], '\n')

    # part G
    print("part G")
    print(temperatures[["Amanda", "Maxine"]].loc[["Morning", "Afternoon"]], '\n')

    # part H
    print("part H")
    print(temperatures.describe(), '\n')

    # part I
    print("part I")
    print(temperatures.T, '\n')

    # part J
    print("part J")
    temperatures = temperatures.sort_index(axis=1)
    print(temperatures)
