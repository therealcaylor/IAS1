# Write a comprehension that produces a list containing all of the numbers from 1 to 1000 that have a digit ‘3’ in them.

print([x for x in range(1000) if "3" in str(x) ])