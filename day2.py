# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.
#
# Example
# mealcost = 100
# tippercent = 15
# taxpercent = 8
#
#
#
# A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. Print the value  123 and return from the function.


import math
import os
import random
import re
import sys


def solve(meal_cost, tip_percent, tax_percent):
    tax_tip = meal_cost* (tip_percent + tax_percent)/100
    total_mealcost = round(meal_cost + tax_tip)
    return total_mealcost



xyz = solve (100, 15, 8)
print(xyz)