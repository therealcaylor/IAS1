# Write a function that takes a string as input and returns a list of words in the string, sorted alphabetically.


def sortStringOfWords(stringa:str):
    try:
        innerArr = stringa.split(" ")
    except ValueError as error:
        print(error)
        return
    innerArr.sort()
    return " ".join(innerArr)
print(sortStringOfWords("ciao amici come state ehhh"))