# Write a function that takes two lists as input and returns a new list that contains the elements that are common to both input lists.

def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elements = set1.intersection(set2)
    return list(common_elements)


list1 = [1,5,4,9]
list2 = [22,5,2,10]
print(find_common_elements(list1, list2))