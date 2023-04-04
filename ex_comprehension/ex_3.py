# Write a comprehension that takes a list of integers and makes a new one containing only its even elements.
import random
random_integers = [random.randint(1, 1000) for _ in range(100)]
print([x for x in random_integers if x % 2 == 0]) 
