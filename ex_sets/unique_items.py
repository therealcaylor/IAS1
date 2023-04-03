# Write a function that takes a list as input and returns a new list that contains only the unique elements from the input list.


def unique_values(list: list):
    return set(list)

list1 =  [11,2,30,4,1,2,3,4]
print(unique_values(list1))