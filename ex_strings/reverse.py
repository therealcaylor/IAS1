#Write a function that takes a string as input and returns the string in reverse order.

def reverseHARDWAY(stringa):
    #!using for loop
    #arrChar = []
    #for i in range(len(stringa)-1, -1,-1):#range(start, stop, step)
    #    arrChar.append(stringa[i])
    #return "".join(arrChar)
    
    #!using slicing
    return stringa[::-1]
def reverseEASYWAY(stringa):
    return "".join(reversed(stringa))

print(f"hardway: {reverseHARDWAY('ciao')}")
print(f"easyway: {reverseEASYWAY('ciao')}")
