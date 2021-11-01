# this is the answer script for euler question 1
import math


def totalSum(start, end):
    nth = math.floor(end/start)
    end = nth * start

    return start * (nth/2) * (1+nth)


value = totalSum(3, 999) + totalSum(5, 999) - totalSum(15, 999)
print(value)


