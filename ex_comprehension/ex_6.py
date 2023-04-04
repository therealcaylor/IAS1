# Write a comprehension that computes the list of all pairs of multiplicative factors for a given integer n>0.

n =10 
print([(i, n//i) for i in range(1, n+1) if n % i == 0])