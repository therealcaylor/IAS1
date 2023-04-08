# Write/test a function firstGreater(data, val) that returns the index of the first element of data that is strictly greater than val. If no such element is found, return −1. If the val argument is not passed, it defaults to 0.
from typing import Iterable

def firstGreater(data: Iterable, val: int = 0):
    for i in range(len(data)):
        if data[i] > val:
            return i
    return -1
print(firstGreater([1,2,3,4],10))