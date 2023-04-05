# Write a program to find the factorial of a given number using a for loop.
n =5
fact = 1
for number in range(n,0,-1):
    fact *=number
print(fact)