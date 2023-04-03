#Write a function that takes a string as input and returns the number of vowels in the string.

def vowels_counter(stringa):
    vowels = 0
    for i in range(len(stringa)):
        if stringa[i] in "aeiouAEIOU":
            vowels+= 1
    return vowels

print(vowels_counter("ciao"))
