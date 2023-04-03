# Write a function that takes a string as input and returns the string with all the spaces removed.
def removing_spaces(stringa: str):
    ss = stringa.split(" ")
    return "".join(ss)
    



print(removing_spaces("ciao come stai?"))