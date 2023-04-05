# 1- Write a program to square each element in a given list using map function.

import math

def square(number:int):
    return number**2

print(list(map(square,[1,2,3,4,5])))
