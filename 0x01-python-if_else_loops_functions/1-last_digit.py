#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
for w in number:
    if w > 5:
        print(F"Last digit of {number} is {w} and is greater than 5")
    elif w < 6 & w > 0:
        print(F"Last digit of {number} is {w} and is less than 6 and not 0")
    else:
        print(F"Last digit of {number} is {w} and is 0")
