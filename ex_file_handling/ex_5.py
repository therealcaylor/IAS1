# Write a program that reads a text file and creates a new file with the same contents, but with all the vowels replaced with asterisks.

def replace_with_asterisks(stringa:str):
    arr_str = []
    for i in list(stringa):
        if i in "aeiouAEIOU":
            arr_str.append("*")
        else: arr_str.append(i)
    return "".join(arr_str)

def reading_and_creating(file_name):
    file = open(file_name)
    lines = file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i] = (replace_with_asterisks(lines[i]))
    print(lines)
    file1 = open("test_test.txt","w")
    file1.writelines(lines)
    file1.close()
    return
    

reading_and_creating("test.txt")