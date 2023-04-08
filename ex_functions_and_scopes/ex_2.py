# Write/test a function threshold(vals, goal) where vals is a sequence of numbers and goal is a positive number. The function returns the smallest integer n such that the sum of the first n numbers in vals is >= goal. If the goal is unachievable, the function returns 0.
from typing import Iterable 
def threshold(vals: Iterable, goal: int):
    somma = 0
    count = 0
    for number in vals:
        somma +=number
        count +=1
        if somma>= goal:
            return  count
    return 0

print(threshold([1,2,3,4,5,6], 4))

