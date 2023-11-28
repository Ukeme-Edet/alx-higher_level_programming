#!/usr/bin/python3
import random

number = str(random.randint(-10000, 10000))
if int(number[-1]) % 10:
    ans = (
        "and is greater than 5"
        if int(number[-1]) % 10 > 5
        else "and is less than 6 but not 0"
    )
else:
    ans = "and is 0"
print(f"Last digit of {number} is {number[-1]} {ans}")
