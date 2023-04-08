# Write/test a recursive function countdown(n) that prints numbers as it counts down from n to zero, and prints “stop” at the end.
import time
def countdown(n):
    if n == 0:
        print(0)
        time.sleep(0.5)
        print("stop")
        return
    time.sleep(0.5)
    print(n)
    return countdown(n-1)
countdown(10)