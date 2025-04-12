# Problem statement
# Take the principal amount, rate of interest, and the time period as input and calculate the Simple Interest.

# Note: Return answer as Floor integer value.

from os import *
from sys import *
from collections import *
from math import *

principal=int(input())
rate=float(input())
time=int(input())

simple_interest=int((principal*rate*time)/100)
print(simple_interest)

