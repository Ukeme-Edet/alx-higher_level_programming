#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numberc = -number if number < 0 else number
if numberc % 10:
    ans = "and is greater than 5" if numberc % 10 > 5 else "and is less than 6 but not 0"
else:
    ans = "and is 0"
print(f"Last digit of {number} is {numberc % 10} {ans}")
