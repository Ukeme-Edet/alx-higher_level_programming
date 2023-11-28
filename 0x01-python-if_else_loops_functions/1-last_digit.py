#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lasd_d = abs(number) % 10
if lasd_d:
    ans = "is greater than 5" if lasd_d > 5 else "is less than 6 and not 0"
else:
    ans = "and is 0"
print(f"The last digit of {number} is {lasd_d} {ans}")
