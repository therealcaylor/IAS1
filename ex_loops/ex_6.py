# Write a program to find the largest number in a given list using a while loop.

arrNumbers = [1,2,5,6,4,8]
counter = 0
max = None

while counter<len(arrNumbers):
    if counter == 0:
        max = arrNumbers[counter]
    else:
        if arrNumbers[counter] > max:
            max = arrNumbers[counter]
    counter +=1
print(max)
