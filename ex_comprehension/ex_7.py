# Write a comprehension that creates a list containing common elements between two given lists.

arr1 = [1,2,3,4,5,6]
arr2 = [1,23,77,4,90,6]
print([number for number in arr1 if number in arr2 ])