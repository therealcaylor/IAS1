# Write a function that takes a string as input and returns True if the string is a palindrome, and False otherwise.


def is_palindrome(stringa: str):
    if len(stringa) <= 1:
        return True
    if stringa[0] != stringa[-1]:
        return False
    s = stringa[1:-1:1]
    is_palindrome(s)

    

print(is_palindrome("aaiaa"))

