# Write a function that takes a string as input and returns the longest word in the string.

def lonngest_word(arrWords: str):
    longest = None
    try:
        innerArr = arrWords.split(" ")   
    except ValueError as error :
        print(error)
        return
    if len(innerArr) == 1:
        return innerArr[0]
    for i in range(len(innerArr)):
        if i ==0 :
            longest = innerArr[i]
        else:
            if len(innerArr[i]) > len(longest):
                longest = innerArr[i]
    return longest

    
print(lonngest_word("ciao come staui"))