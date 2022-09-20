#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
else:
    last = number % 10
print("Last digit of {} is {} and is ".format(number, last), end="")
if last < 6:
    print("less than 6 and not 0")
elif last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
