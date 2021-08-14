# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20 , print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.
import os
import math
import random
import re
import sys
def num_even_odd(N =(int(input("Please enter your integer value here: ")))):
    a = ['Weird', 'Not Weird']
    if N % 2 != 0:
        print(a[0])
    elif (N in range(2, 6)):
        print(a[1])
    elif (N in range(6, 21)):
        print(a[0])
    elif N>20:
        print(a[1])

xyz = num_even_odd()
#print(xyz)
