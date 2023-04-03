# Write a function that takes two strings as input and returns True if the strings are anagrams of each other, and False otherwise.
def is_anagram(str1: str, str2:str):
    reversed1 = "".join(reversed(str1))
    reversed2 = "".join(reversed(str2))
    if reversed1 == str2 and reversed2 == str1:
        return True
    else: return False


print(is_anagram("aabaa","aabaa" ))

