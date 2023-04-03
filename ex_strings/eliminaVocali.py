# Write a function that takes a string as input and returns a new string with all the vowels removed.

def remove_vowels(stringa):
    newStringa = []
    for i in range(len(stringa)):
        if stringa[i] not in "aeiouAEIOU":
            newStringa.append(stringa[i])
    return "".join(newStringa)
print(remove_vowels("christopher caylor" ))
    